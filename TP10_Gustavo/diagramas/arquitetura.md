# Arquitetura integrada (Mermaid)

```mermaid
flowchart LR
 subgraph C[Zona de Controle]
  CLP[CLP / servidor Modbus\nT-101 e P-101]
 end
 subgraph I[Zona de Integração]
  GW[Gateway / servidor OPC UA]
  PUB[Publisher MQTT]
  BR[Broker MQTT]
 end
 subgraph S[Zona de Serviços]
  HMI[HMI]
  HIS[Histórico]
  AL[Serviço de alarmes]
 end
 CLP -- Modbus RTU/TCP\nleitura autorizada --> GW
 GW -- tags / qualidade --> PUB
 PUB -- PUBLISH: tanque101/#\nQoS 1 --> BR
 BR -- SUBSCRIBE autorizado --> HMI
 BR -- SUBSCRIBE autorizado --> HIS
 BR -- SUBSCRIBE autorizado --> AL
```

**Controles:** segmentação e firewall entre zonas, TLS, identidade e ACLs no broker; broker não acessa diretamente o CLP. Os permissivos e intertravamentos ficam no controlador local.
