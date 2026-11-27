# Especificação Ladder — TP11 / P11

Este documento descreve as redes a transcrever no PLC Simulator Online. A sintaxe gráfica pode variar entre simuladores; os nomes das tags seguem `tabela_io.csv`.

## Tags principais

- Entradas: `E0_OK`, `G1_OK`, `B1`, `B2`, `B3`, `START`, `STOP`, `RESET`, `AUTO`.
- Memórias: `SAFE`, `RUN`, `STEP_T`, `STEP_A`, `STEP_R`, `FAULT`.
- Saídas: `M1`, `Y1`, `Y2`.
- Temporizadores: `TON_A` e `TON_R`, preset de 3,0 s.

## Redes (ordem de execução)

| Rede | Condição / instrução | Ação |
|---|---|---|
| N01 — permissivo físico | `E0_OK AND G1_OK` | `SAFE` |
| N02 — parada segura | `NOT SAFE` | Reset de `RUN`, `STEP_T`, `STEP_A`, `STEP_R` |
| N03 — parada normal | `STOP` | Reset de `RUN` e das etapas |
| N04 — partida | `SAFE AND NOT FAULT AND START AND NOT STOP` | Set `RUN`; se nenhuma etapa ativa, Set `STEP_T` |
| N05 — transporte | `RUN AND AUTO AND STEP_T AND B1` | Reset `STEP_T`; Set `STEP_A` |
| N06 — avanço confirmado | `RUN AND AUTO AND STEP_A AND B3` | Reset `STEP_A`; Set `STEP_R`; reset `TON_A` |
| N07 — timeout avanço | `RUN AND STEP_A` | Habilita `TON_A`; ao concluir, Set `FAULT`, reset `RUN` e etapas |
| N08 — retorno confirmado | `RUN AND AUTO AND STEP_R AND B2` | Reset `STEP_R`; Set `STEP_T`; incrementar contador de peças; reset `TON_R` |
| N09 — timeout retorno | `RUN AND STEP_R` | Habilita `TON_R`; ao concluir, Set `FAULT`, reset `RUN` e etapas |
| N10 — reset de falha | `RESET AND SAFE` | Reset `FAULT` e temporizadores; não setar RUN |
| N11 — saída M1 | `SAFE AND NOT FAULT AND RUN AND AUTO AND STEP_T AND NOT B1` | `M1` |
| N12 — saída Y1 | `SAFE AND NOT FAULT AND RUN AND AUTO AND STEP_A AND NOT B3 AND NOT Y2` | `Y1` |
| N13 — saída Y2 | `SAFE AND NOT FAULT AND RUN AND AUTO AND STEP_R AND NOT B2 AND NOT Y1` | `Y2` |

## Regras de implementação

1. A prioridade de `NOT SAFE`, STOP e FAULT deve prevalecer sobre a partida e as transições.
2. `SAFE` é exclusivamente `E0_OK AND G1_OK`; não incorporar `NOT FAULT` nessa tag. Usar `NOT FAULT` como permissivo adicional em RUN e saídas.
3. Garantir exclusividade das etapas. Se o simulador permitir, implementar intertravamento para impedir duas etapas simultâneas.
4. RESET apenas reconhece/limpa a falha quando as condições físicas estão restabelecidas. Não deve religar M1 nem válvulas.
5. Após reset, exigir sensores em condição inicial (`B1=0`, `B2=1`, `B3=0`) e um novo pulso START.

**Observação:** esta é uma especificação de lógica, não um arquivo Ladder nativo nem evidência de execução no PLC Simulator Online. A validação executada neste pacote é a simulação Python descrita no README.
