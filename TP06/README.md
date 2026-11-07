# TP06 - Partida, retenção e parada

## Programa
MOTOR := EMG_OK AND STOP_OK AND OL_OK AND (START OR MOTOR_anterior).
RUN := MOTOR. READY := EMG_OK AND STOP_OK AND OL_OK.

START é entrada de solicitação. STOP_OK, EMG_OK e OL_OK são verdadeiros quando saudáveis. MOTOR, RUN e READY iniciam em zero. Os permissivos ficam em série fora do paralelo START/MOTOR; nenhum caminho de selo contorna a parada.

RUN indica comando, não confirmação de rotação. A liberação da falha com START=0 não religa. Se START permanecer pressionado durante a liberação, o circuito básico pode partir: para impedir também essa situação, seria necessário acrescentar reconhecimento de nova borda/rearme. Esse comportamento não é escondido nos testes.

## Implementação
Montar os rungs de ladder.txt no PLC Simulator Online. Executar os casos_teste.csv, incluindo falha com motor previamente ligado. A especificação textual não é formato nativo de importação. Salvar o projeto e incluir link compartilhável após autenticação, se solicitada.

## Reversão adicional
FWD/REV possuem intertravamento cruzado e inibição pelo comando oposto. Se ambos comandos chegam juntos, ambos são bloqueados. A troca de direção exige liberar comandos, parar e emitir nova partida. Contatos e bobinas modelam lógica; em máquina real seriam necessárias proteções e intertravamentos físicos apropriados.

Fonte: Calvetti TP06, slides 60–68.

## Execução no simulador

Sete casos de partida com selo, parada, emergência, sobrecarga e recuperação foram executados no PLC Simulator Online. A reversão foi testada em avanço, recuo e comandos simultâneos. Os [resultados](resultados-reversao.json) registram as duas saídas. Veja a [tabela de testes](casos_teste.csv) e a [captura](ladder-selo.png). O link do projeto compartilhado depende de login no simulador.
