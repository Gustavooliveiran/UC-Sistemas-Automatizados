# Mapa Modbus – T-101

| Referência | Offset | Área | Função leitura | Escrita | Tipo | Comprimento | Variável | Unidade | Acesso |
|---|---:|---|---|---|---|---:|---|---|---|
| 00001 | 0 | Coil | 01 | 05 | BOOL | 1 bit | P101_CMD | – | RW, conforme autorização |
| 10001 | 0 | Discrete Input | 02 | – | BOOL | 1 bit | P101_RUN | – | R |
| 30001 | 0 | Input Register | 04 | – | UINT16 | 1 | LT101_RAW | count | R |
| 40001 | 0 | Holding Register | 03 | 06 | UINT16 | 1 | SP_NIVEL | 0,1% | RW |
| 40002–40003 | 1–2 | Holding Register | 03 | – | FLOAT32 | 2 | TEMP_REAL | °C | R |

- FC01: ler coils; FC02: ler entradas discretas; FC03: ler holding registers; FC04: ler input registers; FC05: escrever coil; FC06: escrever registro.
- Leitura de `SP_NIVEL` e `TEMP_REAL`: FC03, offset inicial 0, quantidade 3.
- `SP_NIVEL`: aplicar escala 0,1%. `TEMP_REAL`: validar ordem de bytes/palavras com manual do servidor.
- Escrita em `P101_CMD` só quando autorizada e sem contornar intertravamentos e lógica de segurança local.
- Endereço inválido deve produzir exceção de endereço, não um valor presumido.
