# TP07 - Temporização e contagem

## Atraso obrigatório
START mantido com STOP_OK e EMG_OK habilita TON T1 por 3 s. Antes de PT, Q=0; ao atingir PT, Q=1 e MOTOR_DELAY=1. Interrupção zera ET e Q. Não há selo de START neste exercício. MOTOR_DELAY também recebe permissivos diretamente.

## Extensões
1. PISCA alterna OFF/ON a cada 1 s. Avaliar conclusões dos timers usando o estado anterior e aplicar no máximo uma mudança por varredura. Em seis segundos: OFF [0,1), ON [1,2), OFF [2,3), ON [3,4), OFF [4,5), ON [5,6).
2. CTU acumula uma borda de subida por peça, PV=5. Manter sensor ativo não aumenta CV. LOTE_OK usa CV≥5.
3. RESET_LOTE vence uma borda simultânea. CV=0 e LOTE_OK=0, qualquer que seja CV anterior. O sinal anterior do sensor continua sendo atualizado durante reset.
4. E0 transporta, E1 enche por 2 s e E2 libera. A passagem E1→E2 incrementa quantidade. Uma etapa por vez. Emergência bloqueia ações e exige RESET seguro, sem peça, para reinicializar. A temporização pressupõe vazão constante; não mede volume real.

## Arquivos e reprodução
ladder.txt detalha rungs e ordem de avaliação. modelo_tp07.py gera testes_modelo.csv e traco_temporal.csv a partir do ladder.txt (varredura de 10 ms); são resultados de um modelo computacional auxiliar, não observações do PLC Simulator Online. casos_teste.csv é a verificação a executar no simulador principal. Fonte: Calvetti TP07, slides 60–69. A contingência documental não substitui o programa Ladder executável, conforme slide 67.

## Execução no simulador

TON com PT de 3000 ms e CTU com PV de 5 peças foram executados no PLC Simulator Online. Os testes incluem interrupção, sinal mantido e reset. No T08, as duas entradas foram configuradas antes de iniciar a simulação e foi lido o resultado estabilizado. A intermitência e a sequência livre foram verificadas apenas no modelo computacional ([testes_modelo.csv](testes_modelo.csv) e [traco_temporal.csv](traco_temporal.csv)); a execução delas no simulador segue pendente. O modelo adota como hipótese que, após emergência, a sequência só volta com RESET seguro (sem peça), e que o contador de produção é preservado. Veja a [tabela de testes](casos_teste.csv) e a capturas [TON antes de PT](ton-antes.png), [TON atingido](ton-atingido.png) e [CTU do lote](ctu-lote.png). O link do projeto compartilhado depende de login no simulador.
