# Segurança – riscos e controles

| Risco | Controle |
|---|---|
| Escrita indevida no comando da bomba | Função mínima, ACL de escrita, identidade e permissivos/intertravamentos locais |
| Assinatura MQTT ampla ou acesso não autorizado | TLS, autenticação, ACL por tópico, menor privilégio e segmentação de zonas |

Arquitetura: broker sem acesso direto ao CLP; fluxos entre zonas definidos e filtrados por firewall.
