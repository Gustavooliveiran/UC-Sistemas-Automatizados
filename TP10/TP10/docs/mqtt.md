# Contrato MQTT

## Tópicos
- `fabrica/linha1/tanque101/temperatura`
- `fabrica/linha1/tanque101/nivel`
- `fabrica/linha1/tanque101/estado`
- `fabrica/linha1/tanque101/alarme`

## Publicação de exemplo
Tópico: `fabrica/linha1/tanque101/temperatura`

```json
{
  "source": "T101",
  "ts": "2026-11-26T20:00:00Z",
  "value": 78.4,
  "unit": "degC",
  "quality": "GOOD",
  "alarm": "HIGH",
  "schemaVersion": 1
}
```

| Campo | Tipo | Obrigatório | Regra |
|---|---|---|---|
| source | string | sim | Identificador do ativo |
| ts | string ISO 8601 | sim | Timestamp UTC de origem |
| value | number | sim | Valor na unidade declarada |
| unit | string | sim | Unidade padronizada |
| quality | string | sim | GOOD, UNCERTAIN ou BAD |
| alarm | string | não | Estado de alarme, quando aplicável |
| schemaVersion | integer | recomendado | Versão do contrato |

## QoS e RETAIN
- QoS 1 para indicadores e alarmes demonstrativos; tratar possíveis duplicatas.
- RETAIN true para estado atual válido; false para eventos transitórios.
- Publisher: PUBLISH somente em `fabrica/linha1/tanque101/#`.
- HMI: assinatura restrita aos tópicos de linha necessários.
- TLS, identidade e ACL são necessários; não inserir credenciais no repositório.
