# Simulação de roteamento MQTT

| Publicação | Filtro | Corresponde? | Motivo |
|---|---|---|---|
| `fabrica/linha1/tanque101/temperatura` | `fabrica/linha1/+/temperatura` | SIM | `+` corresponde ao único nível tanque101 |
| `fabrica/linha2/tanque101/temperatura` | `fabrica/linha1/+/temperatura` | NÃO | Linha diferente |
| `fabrica/linha1/motor03/estado` | `fabrica/linha1/#` | SIM | `#` aceita os níveis descendentes |
| `fabrica/linha1` | `fabrica/linha1/+` | NÃO | Falta um nível para `+` |

`+` representa exatamente um nível. `#` representa zero ou mais níveis e deve estar no final do filtro.
