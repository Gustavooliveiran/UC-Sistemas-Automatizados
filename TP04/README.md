# TP04 - Lógica combinacional

## Variáveis e expressões
S=solicitação, G=proteção fechada, E=emergência ativa. M=S AND G AND NOT E. O circuito de portas e o rung Ladder devem produzir as oito linhas de tabela_verdade.csv. O arquivo ladder.txt especifica cada rung, mas não é um projeto nativo do simulador.

Incrementos: AND e OR para duas entradas, NOT para uma entrada. Alarme A=E OR NOT G. Ventilação V=D AND G AND NOT F. Divergência de sensores AL_DIV=A XOR B: detecta discordância, sem determinar qual dos dois está errado. Falha comum nos dois pode passar despercebida.

## Arbitragem
Política adotada: bloqueio total quando os dois comandos são simultâneos. MA=CA AND NOT CB AND NOT E. MB=CB AND NOT CA AND NOT E. Assim MA AND MB=0 para todas as entradas. A emergência interrompe ambas as saídas e mantém AL_EMG=E. Não há memória nesta atividade.

## Reprodução
No CircuitVerse, criar entradas S/G/E, inverter E, ligar S/G/NOT E em AND e conectar a saída M. Nomear o circuito Partida_condicionada. Criar circuitos adicionais para cada expressão. No PLC Simulator Online, usar contatos S e G abertos, E negado e bobina M. Rodar as oito linhas e registrar resultados de ambas as ferramentas. Tabelas calculadas não substituem essa comparação observada.

Uma entrada indefinida não pode ser tratada como autorização. O exemplo supõe sinais binários válidos; em aplicação real, diagnóstico adicional deve bloquear a saída. Fonte: Calvetti TP04, slides 49–67.

## Projeto editável e evidências

Abra o [simulador CircuitVerse](https://circuitverse.org/simulator) e importe [logica.cv](logica.cv) em Project → Import Project. O arquivo tem cinco circuitos. As oito combinações do circuito Partida_condicionada foram conferidas no CircuitVerse e no Ladder. A [tabela](tabela_verdade.csv) e as [capturas](evidencias-circuitverse/) registram as entradas e a saída observada. O nome de cada captura corresponde à ordem S, G, E. Os links públicos dos projetos nos simuladores dependem de login.
