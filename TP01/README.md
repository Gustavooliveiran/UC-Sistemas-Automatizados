# TP01 - Porta automática

## Objetivo e classificação
Permitir passagem sem contato, interrompendo o fechamento quando a área estiver ocupada. Sistema automático de eventos discretos com realimentação. Usuário: pessoa que acessa o edifício. A fronteira é explicitada em [porta.png](porta.png); fonte [porta.drawio](porta.drawio).

## Comportamento
FECHADA → presença válida → ABRINDO → FC_ABERTA → ABERTA. Após 3 s continuamente sem presença nem obstáculo, FECHANDO → FC_FECHADA → FECHADA. A espera é reiniciada ao detectar ocupação. Durante fechamento, barreira interrompida remove FECHAR antes de comandar ABRIR. Nunca emitir os dois comandos simultaneamente. Sinais contraditórios ou timeout de movimento de 5 s levam a FALHA.

Emergência domina a sequência: motor desenergizado, alarme e retomada bloqueada. Hipótese de projeto: mecanismo permite liberação manual; acessibilidade e evacuação precisam ser avaliadas em projeto físico. RESET só é aceito sem emergência, sinais válidos, área livre e posição conhecida. A liberação da emergência não reinicia o motor sozinha.

## Falhas e limites
Sensor travado: detectar ausência de progressão por timeout; um sensor travado em valor plausível pode exigir redundância. Perda de energia: não há ação elétrica possível; acesso depende da liberação mecânica. Motor sem resposta: retirar comando após timeout e solicitar manutenção. Obstáculo é perturbação, não necessariamente falha de sensor.

Os cenários em casos_teste.csv são verificação documental do modelo, não ensaio de porta física. As saídas representam comandos. Não se presume confirmação de movimento sem fim de curso.

## Exercícios adicionais
**Reservatório:** nível baixo ≤20% liga bomba, nível ≥80% desliga, faixa intermediária conserva estado. Alto-alto ≥90% ou qualidade inválida força bomba=0 e alarme. Consumo é perturbação; nível é realimentação; faixa desejada 20–80%.

**Iluminação:** L = MANUAL_ON ou FALHA_LUZ ou (HORARIO e PRESENCA e ESCURO). Assume-se manter iluminação na falha do sensor para preservar circulação. Casos: noite ocupada →1; noite vazia →0; dia ocupada →0; sensor inválido →1. Manual ON tem prioridade sobre economia, sem dispensar proteções elétricas.

**Proposta própria:** irrigação automática de canteiro. Entradas: umidade, chuva e disponibilidade de água. Processamento: irrigar abaixo do limite inferior, interromper no superior, com chuva ou falta de água. Saída: válvula. Perturbação: evaporação. Falha: leitura inválida desliga válvula e gera alarme. Melhoria: limitar duração de cada ciclo para reduzir desperdício por vazamento. Automação automática híbrida: umidade contínua e válvula discreta.

## Fonte
Calvetti, TP01, slides 56–67, disponível na pasta da disciplina. Abrir .drawio em https://app.diagrams.net/ usando Arquivo > Abrir de > Dispositivo.
