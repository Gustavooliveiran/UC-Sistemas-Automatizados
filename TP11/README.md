# TP11 / P11 — Integracao, Startup e Manutencao

Celula didatica de separacao e transferencia (USJT — Sistemas Automatizados, Semana 11).
Simulacao logica e documental de integracao (E/S, GRAFCET, Ladder, HMI, MQTT), comissionamento, testes, diagnostico e manutencao.

## Estrutura da pasta TP11
- `README.md`: visao geral, premissas, arquitetura e instrucoes de uso.
- `tabela_io.csv`: entradas/saidas fisicas, memorias de controle/etapas e estados seguros.
- `casos_teste.csv`: matriz de testes T01 a T06 com pre-condicoes, estimulos, resultados esperados e evidencias.
- `topicos_mqtt.csv`: topicos, payloads, QoS, retencao e limites de autoridade da celula.
- `simulador_celula11.py`: simulador executavel em Python da logica Ladder/GRAFCET, timeouts, falhas e casos de teste.
- `grafcet_hmi_rede.drawio`: diagrama editavel (diagrams.net) com visoes de GRAFCET, HMI e Rede/MQTT.
- `manutencao_e_backup.md`: diagnostico orientado a evidencias, plano de manutencao (M1, A1, sensores, valvulas, rede) e manifesto de backup/rollback.
- `celula11_tp11.xlsx`: planilha consolidada com abas Requisitos, IO, Estados, Testes e MQTT.
- `evidencias/resultados_testes.json`: registro estruturado da execucao dos casos de teste T01 a T06.
- `evidencias/roteamento_mqtt.csv`: mapeamento de eventos da celula para topicos MQTT e consumidores.

## Premissas e limites
- Simulacao academica/logica: nao substitui validacao de seguranca de maquina real (NR-12 / IEC 60204-1) nem certificacao de campo.
- Condicao de seguranca global `SAFE = E0_OK AND G1_OK` tem prioridade sobre comandos manuais, automaticos e selo de `RUN`.
- `Y1` e `Y2` possuem intertravamento cruzado para nunca energizarem simultaneamente.
- Perda de rede/broker nao aciona atuadores nem remove a seguranca local; o controle local permanece soberano.
