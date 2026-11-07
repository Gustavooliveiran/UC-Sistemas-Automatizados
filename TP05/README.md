# TP05 - Modelagem sequencial

O arquivo grafcet.drawio contém páginas para atividades 23, 24/27, 25 e 26. grafcet.pdf reúne as páginas para leitura. As imagens PNG permitem visualização no GitHub. A atividade obrigatória é o semáforo com E0 vermelho por 8 s, E1 verde por 10 s e E2 amarelo por 3 s. Ciclo nominal de 21 s.

Receptividade só dispara se a etapa precedente estiver ativa. O tempo de cada etapa é reiniciado na sua entrada. O modelo inclui emergência prioritária, que conduz ao vermelho e exige RESET antes da retomada. Isso é hipótese adicional, não controle certificado de tráfego real.

As demais páginas documentam entradas, ações, seleções e condições de falha. O diagrama da esteira usa caixas de estado para legibilidade; as guardas estão nas setas. A seleção A/ B é exclusiva e a convergência aguarda retorno físico. Não há paralelismo de atuadores nesta solução.

casos_teste.csv registra percurso do modelo, sem alegar execução de CLP. Abrir a fonte em diagrams.net e alternar as páginas inferiores. Fonte: Calvetti TP05, slides 58–68.
