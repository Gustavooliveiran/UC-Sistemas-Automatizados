# Diagnostico, Plano de Manutencao e Manifesto de Backup — TP11

## 1. Fluxo de diagnostico orientado a evidencias
1. **Observar:** registrar horario, modo (`MANUAL`/`AUTO`), etapa (`STEP_T`, `STEP_A`, `STEP_R`, `FAULT`), estado de E/S e alarmes.
2. **Conter:** garantir `SAFE` e estado seguro (`M1=0`, `Y1=0`, `Y2=0`) sem mascarar sintomas com reset precoce.
3. **Isolar:** formular hipótese por camada (lógica CLP, modulo de E/S, fiação/bornes, atuador/valvula, rede/HMI).
4. **Testar:** executar verificacao discriminante (ex.: se bobina logica `M1=0`, investigar permissivos/etapa/modo; se logica `=1` e saida fisica `=0`, inspecionar modulo/LED/bornes; se tensao presente sem atuacao, verificar bobina/contator/pressao).
5. **Corrigir e verificar:** aplicar mudanca controlada, repetir o caso de teste e rodar regressao de seguranca e ciclo.

## 2. Plano de manutencao da celula
| Ativo | Modo de falha | Politica | Evidencia / Indicador |
|---|---|---|---|
| Motor M1 / Esteira | Sobrecarga, rolamento, desalinhamento de correia | Preventiva + Preditiva | Corrente do motor, temperatura/vibracao e inspecao mecanica |
| Cilindro A1 | Vazamento de vedacao, atrito, perda de pressao | Preditiva + Preventiva | Tempo de curso (avanco/retorno) e pressao pneumatica |
| Sensores B1, B2, B3 | Desalinhamento, sujeira, cabo rompido | Preventiva + Teste de E/S | Comutacao coerente em campo vs. entrada CLP e contagem de timeouts |
| Valvulas Y1 / Y2 | Travamento de carretel ou bobina aberta | Preventiva + Corretiva planejada | Tempo de resposta e continuidade/tensao na bobina |
| Rede / HMI / Broker | Queda de enlace, dado congelado (`stale`) | Monitoramento + Corretiva | Timestamp, qualidade do dado e registro de eventos |

## 3. Manifesto de backup e rollback (v1.0.0)
- **Baseline:** `TP11 v1.0.0` (2026-11-26)
- **Artefatos incluidos:** `README.md`, `tabela_io.csv`, `casos_teste.csv`, `topicos_mqtt.csv`, `simulador_celula11.py`, `grafcet_hmi_rede.drawio`, `manutencao_e_backup.md`, `celula11_tp11.xlsx` e pasta `evidencias/`.
- **Procedimento de restauracao:** extrair pacote da baseline `v1.0.0`, conferir integridade dos arquivos e enderecos de E/S (`I0.0-I0.4`, `Q0.0-Q0.2`, `M0.0-M0.5`), executar `python simulador_celula11.py` e validar casos `T01` a `T06`.
- **Rollback:** em caso de falha em nova versao, reverter para o commit/pacote da baseline anterior, revalidar `SAFE` (`E0_OK` e `G1_OK`) e registrar o motivo da reversao.
