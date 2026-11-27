# Casos de teste documental

| ID | Cenário | Resultado esperado | Obtido documental | Conclusão |
|---|---|---|---|---|
| T01 | Ler 40001 com FC03 | SP_NIVEL interpretado com escala 0,1% | Offset 0 e escala registrados no mapa | Aprovado documentalmente |
| T02 | Ler offset inexistente | Exceção de endereço, sem valor válido | Caso de exceção previsto | Aprovado documentalmente |
| T03 | Qualidade OPC UA Bad | Consumidor rejeita o valor | Regra de qualidade documentada | Aprovado documentalmente |
| T04 | Filtro `fabrica/linha1/+/temperatura` | Somente temperaturas da linha 1 | Casos positivos/negativos conferidos | Aprovado documentalmente |
| T05 | Novo assinante com RETAIN | Recebe último estado retido, quando aplicável | Contrato indica estado e timestamp | Aprovado documentalmente |
| T06 | Cliente sem permissão | Operação recusada | ACL restrita documentada | Aprovado documentalmente |

> São inspeções documentais, não testes reais de equipamento, rede, servidor OPC UA ou broker MQTT.
