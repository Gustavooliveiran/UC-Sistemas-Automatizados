# TP09 - Projeto de rede industrial

## Escopo e entregáveis
Célula A com CLP, HMI, duas remotas e três inversores. Célula B com controlador legado Modbus RTU. SCADA na sala de controle, a 120 m, com EMI perto dos motores. Parada tolerável informada no cenário: até 15 min; expansão de quatro nós. Entrega: rede.drawio, rede.pdf, rede.png e enderecamento.xlsx (Nós, Matriz, Testes e Riscos).

## Decisões por trecho
**Controle da célula A:** PROFINET IO, pois as duas remotas e os inversores exigem essa interface. Modbus RTU e “Ethernet comum” não são substitutos nativos para esses dispositivos. Ethernet é tecnologia de rede; sua presença não garante o protocolo de aplicação. A matriz explicita a eliminação por incompatibilidade antes da comparação numérica.

**Supervisão:** fibra entre sala e células evita usar um único segmento de cobre de 120 m e reduz acoplamento eletromagnético no backbone. Dentro das células, cobre industrial com canais limitados a 100 m e encaminhamento afastado de potência. A especificação de fibra, transceptores e orçamento óptico deve ser confirmada com os equipamentos escolhidos.

**Legado:** gateway Modbus TCP/RTU com endereço Ethernet 10.20.40.10 e controlador serial slave 5. O gateway atua como cliente RTU. Proposta inicial: 9600 bit/s, 8E1, timeout 500 ms, uma repetição; parâmetros precisam coincidir no dispositivo e ser validados. Terminação e polarização RS-485 conforme topologia e fabricante.

**Zonas:** três /24 roteados por FW-OT, com ACL permitindo apenas fluxos necessários. SCADA consulta CLP-A por OPC UA (hipótese de suporte) e GW-B por Modbus TCP. Controle PN cíclico permanece local; supervisão não participa de permissivos críticos. Os nomes PN são únicos e seguem os IDs em minúsculas.

## Disponibilidade e testes
Não se afirma cumprimento dos 15 min sem ensaio de substituição/recuperação. Switch, gateway, fonte, fibra e roteador são pontos únicos declarados em Riscos. O modelo é estrela segmentada, sem promessa de redundância automática. A leitura de dados deve marcar comunicação ruim quando perder atualização; dado antigo não vale como normal.

## Extensões
Segundo legado: reservar slave 6 e documentar mapa de registradores com o fabricante; não inventar endereços funcionais. Estimativa para leitura de dez registradores: requisição 8 bytes e resposta 25 bytes, 11 bits por caractere em 8E1 → 37,8 ms de transmissão a 9600 bit/s. Dois intervalos de 3,5 caracteres acrescentam aproximadamente 8,0 ms, além do processamento. Dois escravos exigem cerca de 91,7 ms mais processamento no caso normal. Timeout e repetição de um nó ausente podem ultrapassar 1 s. Separar essa estimativa de medição.

Disponibilidade adicional: para tolerar rompimento de um enlace, propor anel gerenciado compatível, fontes independentes e rotas físicas separadas. Tempo de comutação é requisito a contratar e ensaiar; não deduzir do desenho. Revisão por pares depende de projeto real de outro aluno e não foi simulada como colaboração.

Fonte: Calvetti TP09, slides 52–69. Casos em planilha distinguem inspeção documental de ensaio físico.
