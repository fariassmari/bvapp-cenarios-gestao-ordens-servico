'''
UC004 - Visualizar ativos associados à Ordem de Serviço

Objetivo: Permitir que o usuário consulte os ativos vinculado ao serviço da OS, agrupados por tipo, com suas quantidades e informações individuais.

Requisitos relacionados:
- Abertura, autorização e correspondência dos detalhes: CAs 23509, 23511, 23512 e 23513.
- Formatação: 34143.
- Ativos associados: 34146, 34147, 34148, 34149 e 34150.
- Carregamento e falha na consulta: 34157.
- Preservação da listagem: 34158.

Ator:
- Técnico autenticado com SERVICO_LISTAR, SERVICO_VISUALIZAR e ATIVO_VISUALIZAR.

Autoria:
- Mariana Farias de Brito.

Pré-condições:
- Existem prestador P01 e serviços S01 e S02 válidos.
- O serviço S01 possui três ativos vinculados: dois do tipo Painel e um do tipo Inversor.
- O serviço S02 não possui ativos vinculados.
- Existem ativos de outro serviço para verificar que eles não são apresentados indevidamente.
- Os ativos utilizados no fluxo principal não estão removidos.
- Existe uma OS não removida, identificada como OS_REFERENCIA, com identificador conhecido e os dados planejados, vinculada ao serviço S01.
- Os dados são planejados para documentação, sem execução de testes.

Dados planejados:
- Data de referência: 01/11/2026, às 12:00 UTC.
- Descrição: "Limpeza programada dos painéis do bloco A".
- Serviço: S01.
- Prestador: P01.
- Custo: R$ 150,00.
- Data de abertura: 02/11/2026.
- Data prevista de conclusão: 05/11/2026.
- Data de conclusão: não informada.
- A01: Painel, série PAINEL-001, status conhecido e entrada em operação em 10/10/2026.
- A02: Painel, série PAINEL-002, status conhecido e entrada em operação não informada.
- A03: Inversor, série INVERSOR-001, status conhecido e entrada em operação em 15/10/2026.
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# 1. O ator localiza OS_REFERENCIA na listagem e seleciona a visualização.

# 2. O sistema abre o painel lateral na aba "Detalhes".

# 3. O ator verifica o identificador da OS e o serviço S01, confirmando que abriu o registro correto.

# 4. O ator seleciona a aba "Ativos associados". [A1][A2][A3]

# 5. O sistema apresenta os ativos vinculados ao serviço S01, agrupados por tipo:
# - Painel: quantidade 2;
# - Inversor: quantidade 1.

# 6. O ator expande o grupo Painel.

# 7. O sistema apresenta A01 e A02, com seus números de série e os respectivos status.

# 8. Para A01, o sistema apresenta a entrada em operação como 10/10/2026.

# 9. Para A02, o sistema não apresenta uma data de entrada em operação que não esteja registrada. [RN2]

# 10. O ator recolhe o grupo Painel.

# 11. O sistema oculta os itens desse grupo, mantendo disponíveis sua identificação e quantidade.

# 12. O ator expande o grupo Inversor.

# 13. O sistema apresenta A03, com número de série INVERSOR-001, status correspondente ao cadastro e entrada em operação em 15/10/2026.

# 14. O ator verifica que os ativos de outros serviços não aparecem nos grupos apresentados. [RN1]

# 15. O ator fecha o painel.

# 16. O sistema preserva a página, a busca, os filtros e a ordenação da listagem.


# [A1] - SERVIÇO SEM ATIVOS ASSOCIADOS
# ---------------------------------------------------------------

# 1. O ator utiliza uma OS de preparação vinculada ao serviço S02, que não possui ativos associados.

# 2. O ator abre a visualização e acessa "Ativos associados".

# 3. O sistema informa: "Nenhum ativo associado."


# [A2] - USUÁRIO SEM PERMISSÃO PARA CONSULTAR ATIVOS
# ---------------------------------------------------------------

# 1. O ator utiliza uma sessão com SERVICO_VISUALIZAR, mas sem ATIVO_VISUALIZAR.

# 2. O ator abre os detalhes da OS e tenta acessar os ativos.

# 3. O sistema bloqueia a consulta dos ativos associados.

# 4. Em outra variação, o ator possui ATIVO_VISUALIZAR, mas não possui SERVICO_VISUALIZAR.

# 5. O sistema também bloqueia a consulta dos ativos dessa OS.

# 6. As duas permissões são necessárias simultaneamente. [RN3]


# [A3] - CARREGAMENTO E FALHA NA CONSULTA
# ---------------------------------------------------------------

# 1. O ator acessa "Ativos associados".

# 2. Enquanto os dados estiverem sendo consultados, o sistema apresenta uma indicação de carregamento.

# 3. Caso a consulta falhe, o sistema informa que não foi possível carregar os dados.

# 4. O sistema não apresenta "Nenhum ativo associado." como resposta a uma falha de carregamento.


# [RN1] - ORIGEM E AGRUPAMENTO DOS ATIVOS
# ---------------------------------------------------------------

# Os ativos apresentados devem estar vinculados ao serviço da Ordem de Serviço selecionada.

# Os ativos devem ser agrupados por tipo, com a quantidade correspondente aos itens de cada grupo.

# Os grupos devem permitir expansão e recolhimento.

# Os dois painéis e o inversor são dados de preparação, sem estabelecer limites de quantidade ou de tipos.


# [RN2] - INFORMAÇÕES INDIVIDUAIS DOS ATIVOS
# ---------------------------------------------------------------

# Para cada ativo, devem ser apresentados o número de série, o status e a data de entrada em operação, quando informada.

# As datas devem seguir o formato DD/MM/AAAA.

# Quando a data não estiver informada, não deve ser inventado um valor nem presumido um marcador obrigatório que não esteja definido no critério.


# [RN3] - AUTORIZAÇÃO
# ---------------------------------------------------------------

# O acesso aos ativos associados exige autenticação e, simultaneamente, SERVICO_VISUALIZAR e ATIVO_VISUALIZAR.


# [RN4] - ESCOPO DAS OPERAÇÕES
# ---------------------------------------------------------------

# Os ativos são dados de preparação deste cenário.

# O fluxo descreve somente a consulta dos ativos associados ao serviço de uma OS previamente preparada, sem alterar a OS, os ativos ou seus vínculos.
