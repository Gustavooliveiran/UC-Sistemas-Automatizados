"""Simulador logico da Celula de Separacao e Transferencia (TP11 / P11)."""

from dataclasses import dataclass, asdict
import json


@dataclass
class CelulaState:
    e0_ok: bool = True
    g1_ok: bool = True
    b1: bool = False
    b2: bool = True
    b3: bool = False
    modo_auto: bool = True
    start_cmd: bool = False
    stop_cmd: bool = False
    reset_cmd: bool = False
    manual_y1: bool = False
    manual_y2: bool = False
    run: bool = False
    step_t: bool = False
    step_a: bool = False
    step_r: bool = False
    fault: bool = False
    alarme_code: str = ""
    rede_ok: bool = True
    pecas_count: int = 0
    tempo_etapa_s: float = 0.0
    timeout_preset_s: float = 3.0

    @property
    def safe(self) -> bool:
        return self.e0_ok and self.g1_ok

    @property
    def m1(self) -> bool:
        return self.safe and (not self.fault) and self.run and self.modo_auto and self.step_t and (not self.b1)

    @property
    def y1(self) -> bool:
        if (not self.safe) or self.fault:
            return False
        if self.modo_auto:
            return self.run and self.step_a and (not self.b3) and (not self.y2)
        return self.manual_y1 and (not self.b3) and (not self.manual_y2)

    @property
    def y2(self) -> bool:
        if (not self.safe) or self.fault:
            return False
        if self.modo_auto:
            return self.run and self.step_r and (not self.b2) and (not self.y1)
        return self.manual_y2 and (not self.b2) and (not self.manual_y1)

    def passo(self, dt: float = 0.5) -> dict:
        if self.reset_cmd:
            self.fault = False
            self.alarme_code = ""
            self.tempo_etapa_s = 0.0
            self.reset_cmd = False

        if (not self.e0_ok) or (not self.g1_ok):
            self.run = False
            self.step_t = False
            self.step_a = False
            self.step_r = False
            self.tempo_etapa_s = 0.0
            self.start_cmd = False
            return self.snapshot()

        if self.fault:
            self.run = False
            self.step_t = False
            self.step_a = False
            self.step_r = False
            self.start_cmd = False
            return self.snapshot()

        if self.stop_cmd:
            self.run = False
            self.step_t = False
            self.step_a = False
            self.step_r = False
            self.tempo_etapa_s = 0.0
            self.stop_cmd = False
        elif self.start_cmd and self.safe:
            self.run = True
            if self.modo_auto and not (self.step_t or self.step_a or self.step_r):
                self.step_t = True
                self.tempo_etapa_s = 0.0
            self.start_cmd = False

        if self.run and self.modo_auto:
            if self.step_t:
                if self.b1:
                    self.step_t = False
                    self.step_a = True
                    self.tempo_etapa_s = 0.0
            elif self.step_a:
                if self.b3:
                    self.step_a = False
                    self.step_r = True
                    self.tempo_etapa_s = 0.0
                else:
                    self.tempo_etapa_s += dt
                    if self.tempo_etapa_s >= self.timeout_preset_s:
                        self.fault = True
                        self.alarme_code = "ALM_TIMEOUT_A1"
                        self.run = False
                        self.step_a = False
                        self.tempo_etapa_s = 0.0
            elif self.step_r:
                if self.b2:
                    self.step_r = False
                    self.step_t = True
                    self.b1 = False
                    self.b3 = False
                    self.pecas_count += 1
                    self.tempo_etapa_s = 0.0
                else:
                    self.tempo_etapa_s += dt
                    if self.tempo_etapa_s >= self.timeout_preset_s:
                        self.fault = True
                        self.alarme_code = "ALM_TIMEOUT_R1"
                        self.run = False
                        self.step_r = False
                        self.tempo_etapa_s = 0.0

        return self.snapshot()

    def snapshot(self) -> dict:
        data = asdict(self)
        data["safe"] = self.safe
        data["m1"] = self.m1
        data["y1"] = self.y1
        data["y2"] = self.y2
        return data


def executar_suite_testes() -> list[dict]:
    resultados = []

    # T01: start com condicoes seguras
    s = CelulaState(e0_ok=True, g1_ok=True, modo_auto=True, b2=True, start_cmd=True)
    snap = s.passo()
    resultados.append({
        "id": "T01",
        "aprovado": snap["step_t"] and snap["m1"] and (not snap["y1"]) and (not snap["y2"]),
        "estado": snap
    })

    # T02: B1 durante transporte
    s.b1 = True
    s.b2 = False
    snap = s.passo()
    resultados.append({
        "id": "T02",
        "aprovado": (not snap["m1"]) and (not snap["step_t"]) and snap["step_a"] and snap["y1"],
        "estado": snap
    })

    # T03: G1 abre durante avanco
    s.g1_ok = False
    snap = s.passo()
    resultados.append({
        "id": "T03",
        "aprovado": (not snap["safe"]) and (not snap["run"]) and (not snap["y1"]) and (not snap["m1"]),
        "estado": snap
    })

    # T04: timeout em avanco (B3 nao chega em 3.0s)
    s = CelulaState(e0_ok=True, g1_ok=True, modo_auto=True, b2=True, start_cmd=True)
    s.passo(0.5)
    s.b1 = True
    s.b2 = False
    s.passo(0.5)  # entra em STEP_A
    for _ in range(6):  # 6 * 0.5s = 3.0s
        snap = s.passo(0.5)
    resultados.append({
        "id": "T04",
        "aprovado": snap["fault"] and (snap["alarme_code"] == "ALM_TIMEOUT_A1") and (not snap["y1"]),
        "estado": snap
    })

    # T05: retorno apos falha (reset + novo start)
    s.reset_cmd = True
    snap_reset = s.passo(0.5)
    sem_partida_espontanea = (not snap_reset["fault"]) and (not snap_reset["run"]) and (not snap_reset["m1"])
    # Restabelece os sensores de processo antes de uma nova partida deliberada.
    s.b1 = False
    s.b2 = True
    s.b3 = False
    s.start_cmd = True
    snap_start = s.passo(0.5)
    resultados.append({
        "id": "T05",
        "aprovado": sem_partida_espontanea and snap_start["run"] and snap_start["step_t"] and snap_start["m1"],
        "estado_pos_reset": snap_reset,
        "estado_pos_start": snap_start
    })

    # T06: perda de comunicacao HMI/rede
    s_net = CelulaState(e0_ok=True, g1_ok=True, modo_auto=True, b2=True, start_cmd=True, rede_ok=False)
    snap_net = s_net.passo(0.5)
    resultados.append({
        "id": "T06",
        "aprovado": (not snap_net["rede_ok"]) and snap_net["safe"] and snap_net["run"] and snap_net["m1"],
        "estado": snap_net
    })

    return resultados


if __name__ == "__main__":
    res = executar_suite_testes()
    print(json.dumps(res, indent=2, ensure_ascii=False))
