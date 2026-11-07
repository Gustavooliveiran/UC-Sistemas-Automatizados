# Fundamentos dos sistemas automatizados

## 1. Sistemas automatizados e aplicações

Um sistema automatizado combina aquisição de informações, regras de decisão e atuação para executar um processo com um objetivo definido. A presença de um motor, isoladamente, não caracteriza automação. É necessário estabelecer quem percebe a situação, quem decide a próxima ação e quem a executa. Em um sistema manual, a pessoa realiza as decisões operacionais. No semiautomático, parte do ciclo depende de intervenção humana. No automático, o controlador executa o ciclo previsto, enquanto a pessoa configura, supervisiona e responde às situações excepcionais.

Uma porta automática exemplifica essa organização: o sensor detecta aproximação, o controlador verifica permissivos e o acionamento movimenta a folha. Sensores de posição confirmam o deslocamento. Uma barreira interrompida durante o fechamento exige parada e reabertura, conforme as hipóteses do projeto. O benefício não se limita à conveniência: a lógica deve considerar quem utiliza a porta, o tempo de passagem e os riscos de aprisionamento.

Na indústria, esteiras transportam e classificam produtos, controladores regulam reservatórios e sistemas supervisórios apresentam estados, tendências e alarmes. Em edifícios, iluminação e climatização ajustam a operação conforme ocupação e demanda. Na agricultura, a irrigação pode depender de umidade e horário. Cada aplicação exige critérios de aceitação próprios: reduzir consumo não autoriza comprometer a função principal do sistema.

## 2. Processos e suas variáveis

Um processo transforma matéria, energia ou informação. Para controlá-lo, é preciso definir sua fronteira e selecionar variáveis que descrevam seu comportamento. A variável controlada é aquela que se deseja manter ou conduzir a uma condição. A variável manipulada é modificada pelo controlador. Perturbações alteram o processo sem constituir o comando principal. O valor de referência, ou setpoint, representa a condição desejada.

Em um reservatório abastecido por bomba, o nível é a variável controlada, o acionamento ou a vazão da bomba é a variável manipulada e o consumo é uma perturbação. O nível medido retorna à lógica. Um controle com dois limites liga a bomba abaixo do nível mínimo e a desliga no máximo. Entre esses limites, conserva a decisão anterior. Essa histerese reduz o chaveamento repetitivo causado por pequenas oscilações da medida. Um sensor alto-alto independente pode fornecer uma condição adicional de bloqueio.

Processos podem ser contínuos, discretos ou híbridos. Temperatura varia continuamente, enquanto a chegada de uma peça representa um evento discreto. Uma linha de envase combina ambas as características: há eventos de posicionamento e mudanças contínuas de nível. A modelagem deve registrar unidades, faixas, condições iniciais e tempos relevantes. Sem isso, a mesma leitura numérica pode receber interpretações incompatíveis.

## 3. Automatização, malhas de controle e software

Automatizar significa atribuir ao sistema técnico uma sequência de percepção, decisão e ação antes realizada integral ou parcialmente por pessoas. O desenvolvimento começa pelo requisito, e não pela escolha da ferramenta. É necessário descrever a condição de partida, as saídas permitidas, as transições, a parada e a recuperação após uma falha. Essas definições podem ser representadas por diagramas funcionais, tabelas-verdade e modelos de estados.

Em malha aberta, o comando não é corrigido a partir da medição do resultado. Acionar uma bomba por um intervalo fixo é um exemplo, quando não existe retorno de nível. Em malha fechada, a medição do processo participa da decisão. Isso permite reagir a perturbações, mas introduz dependência da qualidade do sensor. Um sinal incorreto pode levar a decisões inadequadas; por isso, realimentação e diagnóstico precisam ser projetados conjuntamente.

O controlador lógico programável lê entradas, executa o programa e atualiza saídas em ciclos de varredura. Em Ladder, contatos avaliam condições e bobinas recebem resultados lógicos. Temporizadores verificam duração e contadores acumulam eventos. O programa precisa distinguir um evento novo de um sinal mantido ativo. Caso contrário, uma única peça pode ser contada muitas vezes. A organização das prioridades também importa: uma emergência não pode ser anulada por um ramo de retenção.

## 4. Sensores, transdutores e transmissores

Sensor é o elemento que responde a uma grandeza ou fenômeno de interesse. Transdutor converte uma forma de energia ou sinal em outra. Transmissor condiciona e disponibiliza a informação em uma interface apropriada para o sistema. Os termos podem descrever funções integradas no mesmo equipamento, mas não são automaticamente sinônimos. Um conjunto de medição de temperatura pode reunir elemento sensível, conversão elétrica e transmissão do valor.

A escolha do instrumento depende do mensurando, faixa, ambiente, velocidade e interface. Para detectar objetos metálicos, um sensor indutivo pode ser adequado. Para identificar presença sem contato, outras tecnologias, como fotoelétrica, podem atender melhor dependendo do material e das condições de instalação. Para nível, a tecnologia deve considerar espuma, geometria e propriedades do fluido. Não basta selecionar um componente porque ele aparece em um simulador.

Resolução é a menor variação distinguível na representação. Repetibilidade diz respeito à proximidade entre resultados obtidos em condições repetidas. Essas características não garantem, por si, exatidão. Um sensor pode repetir um valor deslocado do valor de referência. Da mesma forma, uma interface digital não elimina incertezas da medição física.

## 5. Sinais e tratamento da informação

Uma variável física contínua pode ser representada por sinal analógico ou por dados digitais. Um botão fornece um estado discreto. Um potenciômetro fornece uma tensão variável; ao ser amostrada pelo conversor analógico-digital do Arduino Uno, ela é representada por códigos de 0 a 1023. Um DHT22 comunica uma temperatura por protocolo digital, embora a grandeza física temperatura seja contínua.

O escalonamento relaciona a faixa do sinal à faixa de engenharia. Para um código ADC de 0 a 1023, a expressão p = 100 × ADC / 1023 produz o percentual da faixa. Uma representação ideal de 4 a 20 mA pode ser calculada por I = 4 + 16 × p / 100. Nesse exemplo, 4 mA corresponde ao início da faixa, não à ausência de sinal. O diagnóstico deve ocorrer antes de limitar artificialmente os valores: substituir qualquer leitura abaixo de 4 mA por 4 mA esconderia uma possível condição anormal.

Filtros podem suavizar ruído, mas também atrasam a resposta. Uma média móvel de cinco amostras depende das leituras recentes e retarda a indicação de mudanças rápidas. A decisão de filtrar deve considerar os tempos do processo. A apresentação de uma medida deve informar valor, unidade e qualidade; um número antigo apresentado como atual pode induzir o operador ao erro.

## 6. Testes, falhas e conclusão

A validação relaciona cada requisito a entradas e resultados observáveis. Testar apenas uma condição normal é insuficiente. Devem ser avaliados extremos, fronteiras, comandos simultâneos, perda de sinal e retomada após falhas. Uma tabela útil distingue resultado esperado, resultado obtido, ambiente utilizado e situação do teste. Uma previsão teórica não pode ser registrada como observação de um simulador.

Em uma porta, a perda do sensor não deve autorizar fechamento automático. Em um reservatório, uma medida inválida precisa ser diferenciada de nível baixo. Em redes, a perda da supervisão não deveria eliminar uma proteção que depende de resposta local. O estado seguro é definido pelo risco da aplicação e pelas hipóteses físicas; simplesmente desligar tudo nem sempre resolve todos os perigos.

Sistemas automatizados exigem coerência entre processo, medição, lógica e atuação. O software produz consequências físicas por meio dos atuadores. Diagramas, simulações e testes documentados ajudam a verificar essa coerência, mas não demonstram, isoladamente, confiabilidade industrial, calibração ou segurança certificada. A compreensão desses limites é parte do projeto técnico.

## Referências

CALVETTI, Robson. Materiais TP00, TP01, TP02 e TP03 da UC Sistemas Automatizados. Universidade São Judas Tadeu, 2026. Material disponibilizado na pasta da disciplina.

WOKWI. Arduino Uno Reference; DHT22 Reference. Disponível em: https://docs.wokwi.com/parts/wokwi-arduino-uno e https://docs.wokwi.com/parts/wokwi-dht22. Acesso em: 5 nov. 2026.
