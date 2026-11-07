#!/usr/bin/env python3
"""Modelo computacional auxiliar do TP07 (intermitência e sequência livre).

Segue ladder.txt com varredura de 10 ms. Os resultados NÃO são observações do
PLC Simulator Online: são a verificação do modelo. Uso:

    python3 modelo_tp07.py

Gera testes_modelo.csv e traco_temporal.csv na pasta do script.
"""
import csv
import os

SCAN = 10  # ms por varredura


class TON:
    def __init__(self, pt):
        self.pt, self.et = pt, 0

    def run(self, enable):
        self.et = min(self.et + SCAN, self.pt) if enable else 0
        return self.et >= self.pt


class Pisca:
    """Fase inicia OFF. Captura DONE_OFF/DONE_ON antes de atualizar PISCA."""

    def __init__(self):
        self.pisca = 0
        self.t_off, self.t_on = TON(1000), TON(1000)

    def scan(self, enable):
        done_off = self.t_off.run(enable and not self.pisca)
        done_on = self.t_on.run(enable and self.pisca)
        if not enable:
            self.pisca = 0
        elif done_off:
            self.pisca = 1
        elif done_on:
            self.pisca = 0
        return self.pisca


class Sequencia:
    def __init__(self):
        self.e = [1, 0, 0]  # E0, E1, E2
        self.t_enche = TON(2000)
        self.prod = 0
        self.falha = 0  # exige RESET seguro depois de emergência

    def scan(self, s_pos, emg_ok, reset=0):
        e0, e1, e2 = self.e
        done = self.t_enche.run(e1)
        if not emg_ok:
            self.falha = 1
        if reset and emg_ok and not s_pos:
            self.e, self.falha = [1, 0, 0], 0
            self.t_enche.run(0)
        elif not self.falha:
            t01, t12, t20 = e0 and s_pos, e1 and done, e2 and not s_pos
            if t12:
                self.prod += 1
            self.e = [int(e0 and not t01 or t20), int(e1 and not t12 or t01),
                      int(e2 and not t20 or t12)]
        e0, e1, e2 = self.e
        ok = emg_ok and not self.falha
        return dict(E0=e0, E1=e1, E2=e2, MOTOR=int((e0 or e2) and ok),
                    VALVULA=int(e1 and ok), PROD=self.prod)


def pisca_trace():
    p, rows, ant = Pisca(), [], None
    for t in range(0, 6000, SCAN):
        v = p.scan(1)
        if v != ant:
            rows.append(("PISCA", t / 1000, v))
            ant = v
    return rows


def run():
    aqui = os.path.dirname(os.path.abspath(__file__))
    testes, traco = [], []

    # M1: intermitência por 6 s
    # O valor de uma varredura vale no instante em que ela termina (t + SCAN).
    p, amostras, ant = Pisca(), {0: 0}, 0
    traco.append(("PISCA", "0.00", 0))
    for t in range(0, 6000, SCAN):
        v = p.scan(1)
        amostras[t + SCAN] = v
        if v != ant:
            traco.append(("PISCA", f"{(t + SCAN)/1000:.2f}", v))
            ant = v
    esperado = [(0, 0), (1000, 1), (2000, 0), (3000, 1), (4000, 0), (5000, 1)]
    ok = all(amostras[t] == v for t, v in esperado) and \
        all(amostras[t - SCAN] == 1 - v for t, v in esperado[1:])
    testes.append(("M01", "ENABLE=1 por 6 s", "OFF[0,1) ON[1,2) OFF[2,3) ON[3,4) OFF[4,5) ON[5,6)",
                   "transições em " + ", ".join(f"{t/1000:.1f}s" for t, _ in esperado[1:]) if ok else "divergente",
                   "Conferido no modelo" if ok else "FALHOU"))

    # M2: ENABLE cai no meio da fase ON
    p = Pisca()
    for _ in range(150):
        p.scan(1)
    meio = p.pisca
    p.scan(0)
    ok = meio == 1 and p.pisca == 0 and p.t_on.et == 0 and p.t_off.et == 0
    testes.append(("M02", "ENABLE=0 em t=1,5 s (fase ON)", "PISCA=0; timers zerados", f"PISCA={p.pisca}; ET_ON={p.t_on.et}", "Conferido no modelo" if ok else "FALHOU"))

    # M3: reiniciar com ENABLE recomeça em OFF por 1 s
    for _ in range(99):
        p.scan(1)
    antes = p.pisca
    p.scan(1)
    ok = antes == 0 and p.pisca == 1
    testes.append(("M03", "ENABLE=1 de novo", "recomeça OFF e liga após 1 s", f"PISCA=0 até 0,99 s; PISCA=1 em 1,00 s" if ok else "divergente", "Conferido no modelo" if ok else "FALHOU"))

    # Sequência livre
    s, t = Sequencia(), 0
    def passo(ms, s_pos, emg_ok=1, reset=0):
        r = None
        for _ in range(ms // SCAN):
            r = s.scan(s_pos, emg_ok, reset)
        return r

    def reg(id_, acao, esperado, r, cond):
        obt = "; ".join(f"{k}={v}" for k, v in r.items())
        testes.append((id_, acao, esperado, obt, "Conferido no modelo" if cond else "FALHOU"))

    r = passo(SCAN, 0)
    reg("S01", "Estado inicial, sem peça", "E0=1; MOTOR=1; VALVULA=0; PROD=0", r, r["E0"] and r["MOTOR"] and not r["VALVULA"] and r["PROD"] == 0)
    r = passo(SCAN, 1)
    reg("S02", "S_POS=1 em E0", "E1=1; MOTOR=0; VALVULA=1", r, r["E1"] and not r["MOTOR"] and r["VALVULA"])
    r = passo(1900, 1)
    reg("S03", "Enchendo por 1,9 s", "ainda E1; PROD=0", r, r["E1"] and r["PROD"] == 0)
    r = passo(100, 1)
    reg("S04", "T_ENCHE atinge 2 s", "E2=1; MOTOR=1; VALVULA=0; PROD=1", r, r["E2"] and r["MOTOR"] and not r["VALVULA"] and r["PROD"] == 1)
    r = passo(500, 1)
    reg("S05", "Peça ainda em S_POS", "permanece E2; PROD=1", r, r["E2"] and r["PROD"] == 1)
    r = passo(SCAN, 0)
    reg("S06", "S_POS=0 em E2", "E0=1; PROD=1", r, r["E0"] and r["PROD"] == 1)
    passo(SCAN, 1)
    r = passo(500, 1, emg_ok=0)
    reg("S07", "EMG_OK=0 durante E1", "MOTOR=0; VALVULA=0; estado E1 congelado", r, r["E1"] and not r["MOTOR"] and not r["VALVULA"])
    r = passo(3000, 1, emg_ok=0)
    reg("S08", "Emergência por 3 s (> PT)", "sequência bloqueada; PROD=1", r, r["E1"] and r["PROD"] == 1)
    r = passo(SCAN, 1, emg_ok=1)
    reg("S09", "EMG_OK=1 sem RESET", "continua bloqueado: MOTOR=0; VALVULA=0", r, not r["MOTOR"] and not r["VALVULA"] and r["PROD"] == 1)
    r = passo(SCAN, 1, emg_ok=1, reset=1)
    reg("S10", "RESET com peça em S_POS", "recusado: sem ações", r, not r["MOTOR"] and not r["VALVULA"])
    r = passo(SCAN, 0, emg_ok=1, reset=1)
    reg("S11", "RESET seguro sem peça", "E0=1; MOTOR=1; PROD=1 preservado", r, r["E0"] and r["MOTOR"] and r["PROD"] == 1)

    with open(os.path.join(aqui, "testes_modelo.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Ação", "Esperado", "Obtido no modelo", "Situação"])
        w.writerows(testes)
    with open(os.path.join(aqui, "traco_temporal.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Sinal", "Instante (s)", "Valor"])
        w.writerows(traco)
    return testes


if __name__ == "__main__":
    for linha in run():
        print(linha)
