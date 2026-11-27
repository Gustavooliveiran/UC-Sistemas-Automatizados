# TP10 – Sistemas Automatizados | Modbus, OPC UA e MQTT

**Tanque T-101 – integração documental**

Projeto acadêmico de simulação documental: mapa Modbus, dicionário OPC UA, contrato e roteamento MQTT, riscos e casos de teste. Não estabelece comunicação real com equipamentos.

## Estrutura
- `docs/mapa_modbus.md`: mapa de cinco variáveis e funções.
- `docs/dicionario_opcua.md`: cinco nós e metadados.
- `docs/mqtt.md`: tópicos, payload, QoS, retenção e consumidores.
- `docs/roteamento.md`: quatro cenários de filtros.
- `docs/seguranca.md`: riscos e controles.
- `docs/testes.md`: testes T01–T06.
- `diagramas/arquitetura.md`: diagrama Mermaid.
- `planilhas/`: tabelas CSV que podem ser abertas no Excel/Google Planilhas.

## Cenário
O tanque T-101 possui medição de nível e temperatura, uma bomba P-101 e setpoint de nível. Um servidor legado disponibiliza dados Modbus; um gateway documenta e normaliza os dados em OPC UA; um publisher publica indicadores selecionados no broker MQTT. HMI, histórico e serviço de alarmes recebem apenas dados autorizados.

## Artefatos
Consultar os arquivos nas pastas `docs`, `diagramas` e `planilhas`. Identificadores, endereços e dados são didáticos; valide com documentação real antes de qualquer implantação.
