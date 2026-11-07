# TP03 - Sinais, escalonamento e filtragem

## Artefatos
sketch.ino e diagram.json: aquisição de botão, ADC e LED no Wokwi. escalonamento.xlsx: cálculos, inversão, diagnóstico e gráfico. A planilha usa **casos controlados de entrada**, permitidos no gabarito; não são leituras capturadas. Consultar a [versão compartilhada no Google Planilhas](https://docs.google.com/spreadsheets/d/187Cu2bqNWRs2fhchuI5CMyPgcGpsKsUSxsrkj9zEd7Y/edit?usp=sharing).

## Modelo
p=100×ADC/1023; temperatura=p apenas na faixa 0–100 °C; I=4+16×p/100; V=10×p/100. ADC=512 produz 50,0489%, não exatamente 50%. NORMAL<70%; ATENÇÃO de 70 a menos de 85%; PERIGO≥85%. Valores fora de 0–100% são FALHA. No cálculo inverso, I=4+16×T/100 e V=T/10. Corrente fora de 4–20 mA é diagnosticada antes do escalonamento de processo.

Média móvel: janela de cinco leituras com divisão pelo número efetivo de amostras no início. O valor filtrado é diagnóstico; o LED usa o valor bruto escalonado para não atrasar o alarme. A 500 ms por amostra, a janela completa cobre 2 s entre primeira e última observação. O DHT22 permanece no circuito anterior, mas não é usado nesta atividade de escalonamento.

## Testes e limites
Conferir ADC 0, 512 e 1023; fronteiras 69,99/70 e 84,99/85%; falhas -1 e 100,01%; corrente 3,2 e 20,8 mA. Fórmulas e testes numéricos são auditáveis no XLSX. Execução e captura no Wokwi permanecem separadas desses resultados. Na tendência dos casos controlados, 716 ainda está abaixo de 70%, 717 entra em atenção e 870 entra em perigo. A redução posterior demonstra retorno às faixas.

Tabela de E/S: BTN_COMANDO D2/DI; POT_BRUTO A0/AI; LED_ALARME D8/DO. DHT22 D4 transmite dado digital codificado, não saída analógica. Fonte: Calvetti TP03, slides 48–67, e gabarito TP03.
