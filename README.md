# TP11 / P11 — Integração, Startup e Manutenção

**Projeto:** célula didática de separação e transferência — Semana 11  
**Versão do pacote:** v1.0.1

## Conteúdo
- `tabela_io.csv` — endereçamento de entradas, saídas e memórias.
- `casos_teste.csv` — matriz dos testes T01 a T06.
- `celula11_tp11.xlsx` — planilha consolidada (Requisitos, IO, Estados, Testes e MQTT).
- `grafcet_hmi_rede.drawio` — diagrama editável no diagrams.net.
- `ladder_logica.md` — redes Ladder especificadas para transcrição no simulador de CLP.
- `simulador_celula11.py` — simulador executável da sequência, permissivos, falhas e testes.
- `topicos_mqtt.csv` e `evidencias/roteamento_mqtt.csv` — proposta de telemetria MQTT.
- `manutencao_e_backup.md` — diagnóstico, manutenção e recuperação.
- `evidencias/resultados_testes.json` — resultado reproduzível da suíte do simulador.

## Sequência funcional
1. Com E0_OK e G1_OK ativos, um comando START habilita RUN e inicia STEP_T.
2. STEP_T aciona M1 até B1 detectar a peça.
3. B1 encerra STEP_T e inicia STEP_A/Y1.
4. B3 confirma o avanço e inicia STEP_R/Y2.
5. B2 confirma o retorno, incrementa a contagem e reinicia STEP_T.

## Permissivos e intertravamentos
- `SAFE = E0_OK AND G1_OK`: representa somente os permissivos físicos de emergência e proteção.
- `FAULT` é uma condição separada. RUN e todas as saídas exigem `SAFE=1` e `FAULT=0`.
- Y1 e Y2 possuem intertravamento cruzado e não podem ser acionadas simultaneamente.
- RESET limpa a falha, mas não inicia o ciclo. É necessário um novo START deliberado.
- Perda de comunicação não deve comandar atuadores nem substituir a lógica local.

## Como conferir
Com Python 3 instalado, executar dentro desta pasta:

```bash
python simulador_celula11.py
```

O programa imprime os resultados T01–T06 em JSON. A evidência salva em `evidencias/resultados_testes.json` foi gerada por essa execução; nesta versão, os seis casos da simulação lógica passaram.

## Limites do pacote
O simulador Python valida o comportamento lógico modelado. `ladder_logica.md` é a especificação das redes para implementação; não é um projeto nativo compilado de um fabricante específico. O diagrama HMI/rede e os tópicos MQTT são documentação de integração, não uma tela HMI executável nem uma conexão com broker real. Portanto, não se afirma que houve teste em CLP físico, HMI real ou broker MQTT.

Este material é acadêmico e não substitui projeto, validação de segurança ou comissionamento de máquina real (NR-12 e normas aplicáveis).
