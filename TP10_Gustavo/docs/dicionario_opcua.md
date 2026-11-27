# Dicionário OPC UA

| NodeId | BrowseName | Descrição | DataType | Unidade | AccessLevel/UserAccessLevel | Origem Modbus |
|---|---|---|---|---|---|---|
| `ns=2;s=P101.Cmd` | StartCommand | Comando de partida da bomba | Boolean | – | Write / Write conforme papel | 00001 / FC05 |
| `ns=2;s=P101.Run` | Running | Estado de funcionamento | Boolean | – | Read / Read | 10001 / FC02 |
| `ns=2;s=T101.LevelRaw` | LevelRaw | Leitura bruta de nível | UInt16 | count | Read / Read | 30001 / FC04 |
| `ns=2;s=T101.LevelSP` | LevelSetpoint | Setpoint de nível | Double | % | ReadWrite / ReadWrite autorizado | 40001 / FC03/06 |
| `ns=2;s=T101.Temp` | Temperature | Temperatura medida | Double | °C | Read / Read | 40002–03 / FC03 |

Todos os nós devem incluir StatusCode e SourceTimestamp. Em falha de leitura, marcar qualidade Bad/Uncertain e timestamp coerente; não apresentar indefinidamente um valor antigo como atual. AccessLevel não substitui UserAccessLevel.
