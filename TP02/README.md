# TP02 - Estação de monitoramento

## Montagem e execução
No Wokwi, criar projeto Arduino Uno e substituir sketch.ino e diagram.json pelos arquivos desta pasta. Adicionar as bibliotecas de libraries.txt. Executar e abrir Monitor Serial em 9600 baud. A montagem utiliza D2 para botão com INPUT_PULLUP, D8 para LED em série com 220 ohms, A0 para potenciômetro e D4 para DHT22. Alimentação comum 5 V/GND. Pressionado equivale a LOW.

## Regras
Falha de temperatura tem prioridade; depois ALARME se temperatura ≥40 °C **ou** ADC≥750; ATENÇÃO se temperatura ≥30 °C ou ADC≥400; NORMAL nos demais casos. LED acompanha somente o botão. O gabarito contém uma linha com “e” para o alarme, mas o código, os testes e a seção de prioridades empregam OR: adotada a regra consistente com esses casos. O intervalo de aquisição de temperatura é 2 s. O botão é lido continuamente, evitando resposta atrasada por delay.

## Adicionais
Enviar h no Serial habilita histerese térmica: liga em 40 °C, mantém acima de 37 °C e desliga em 37 °C ou menos. Enviar b retorna à regra básica. Enviar f injeta NaN para testar prioridade da falha e n restaura o sensor. A injeção testa software; não simula eletricamente todos os defeitos do DHT22.

Equivalentes industriais: (1) botão representando presença de peça metálica → sensor indutivo de saída discreta 24 V, alcance definido pela folga e material; (2) potenciômetro representando nível → transmissor de nível 0–100% com 4–20 mA; (3) DHT22 → transmissor de temperatura com elemento adequado à faixa e saída 4–20 mA ou interface digital industrial. Invólucro, temperatura ambiente e compatibilidade química devem ser definidos na seleção real. Detectável: fio aberto com diagnóstico adequado. Não necessariamente detectável: deriva plausível dentro da faixa. Não conectar 24 V diretamente ao Uno.

## Evidências
Os 15 casos de [casos_teste.csv](casos_teste.csv) foram conferidos no [Wokwi](https://wokwi.com/projects/479845101003491329). Os registros seriais documentam a classificação. O teste do botão mostrou [LED aceso ao pressionar](botao-pressionado.png) e [LED apagado ao soltar](botao-solto.png), com o estado do botão registrado em [serial-botao.csv](serial-botao.csv). A simulação não valida ruído, calibração ou segurança funcional.

Fontes: Calvetti, TP02, slides 39–65; https://docs.wokwi.com/parts/wokwi-arduino-uno ; https://docs.wokwi.com/parts/wokwi-dht22 .
