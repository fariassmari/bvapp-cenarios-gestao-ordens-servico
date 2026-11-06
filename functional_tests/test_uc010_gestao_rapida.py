'''
UC010 - Consultar indicadores e acessar listagens pela Gestão rápida

Objetivo: Permitir que o usuário consulte as quantidades de OS por status e, ao selecionar "Ver listagem", seja direcionado
à página específica do status escolhido.

Requisitos relacionados:
- Indicadores e cards: CAs 23734 e 23735.
- Autorização dos indicadores: CA 34046.
- Redirecionamento pelo “Ver listagem”: CA 34047.
- Indicador sem registros: CA 34048.
- Carregamento e falha nos indicadores: CA 34049.
- Listagens de Abertas e Em andamento: CAs 25069, 25070 e 34196.
- Carregamento, ausência de resultados e falha em Abertas e Em andamento: CAs 34202 e 34203.
- Listagem de Concluídas: CAs 25075, 34190 e 34191.
- Carregamento, ausência de resultados e falha em Concluídas: CAs 34194 e 34195.
- Listagem de Atrasadas: CAs 34183, 34184 e 34185.
- Carregamento, ausência de resultados e falha em Atrasadas: CAs 34188 e 34189.

Ator:
- Usuário autenticado com a permissão SERVICO_LISTAR.

Autoria:
- Mariana Farias de Brito.

Pré-condições:
- A preparação contém exatamente 11 OS não removidas em cada status dos indicadores.
- Existem registros removidos para conferir sua exclusão das contagens e das listagens.
- As datas dos registros são conhecidas.
- Os dados são planejados para documentação, sem execução de testes.

Dados planejados:
- Data de referência: 01/11/2026, às 12:00 UTC.
- Contagens iniciais: Abertas 11; Em andamento 11; Concluídas 11; Atrasadas 11.
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a Gestão de Ordens de Serviço.

# O sistema apresenta quatro cards acima da listagem:
# - Abertas: 11;
# - Em andamento: 11;
# - Concluídas: 11;
# - Atrasadas: 11.

# O ator aplica um filtro na listagem geral.

# As quantidades dos cards permanecem gerais, sem serem limitadas pelo filtro ou pela página da listagem.

# O ator seleciona "Ver listagem" no card Abertas.

# O sistema direciona o ator à página específica de OS Abertas.

# A página apresenta um título que identifica as OS Abertas e somente registros não removidos com status "Aberta".

# O ator retorna aos indicadores e seleciona "Ver listagem" no card Em andamento.

# O sistema direciona o ator à página específica de OS Em andamento.

# O ator confere o título e verifica que os registros apresentados são não removidos e possuem status "Em andamento".

# O ator retorna aos indicadores e seleciona "Ver listagem" no card Concluídas.

# O sistema direciona o ator à página específica de OS Concluídas.

# O ator confere o título e verifica que os registros apresentados são não removidos e possuem status "Concluída".

# O ator retorna aos indicadores e seleciona "Ver listagem" no card Atrasadas.

# O sistema direciona o ator à página específica de OS Atrasadas.

# O ator confere o título e verifica que os registros apresentados são não removidos e possuem status "Atrasada".


# [A1] - STATUS SEM REGISTROS
# ---------------------------------------------------------------

# O ator utiliza uma preparação em que um dos status não possui OS não removidas.

# O sistema apresenta zero no card correspondente e mantém a ação "Ver listagem" disponível.

# O ator acessa essa listagem.

# O sistema informa: "Nenhuma Ordem de Serviço encontrada"


# [A2] - CARREGAMENTO E FALHA NOS INDICADORES
# ---------------------------------------------------------------

# Durante a consulta dos indicadores, o sistema apresenta uma indicação de carregamento.

# Se ocorrer uma falha, o sistema informa que não foi possível carregar os indicadores.

# O sistema não apresenta zero como se fosse uma contagem confirmada de registros.


# [A3] - CARREGAMENTO E FALHA NAS LISTAGENS
# ---------------------------------------------------------------

# Durante a consulta de uma listagem por status, o sistema apresenta uma indicação de carregamento.

# Se ocorrer uma falha, o sistema informa que não foi possível carregar os registros.

# O sistema diferencia a falha da ausência de resultados.


# [A4] - USUÁRIO SEM AUTORIZAÇÃO
# ---------------------------------------------------------------

# O ator utiliza uma sessão sem SERVICO_LISTAR e tenta consultar os indicadores ou as listagens por status.

# O sistema bloqueia essas consultas.

# O mesmo bloqueio deve ocorrer sem autenticação.


# [RN1] - CONTAGEM DOS INDICADORES
# ---------------------------------------------------------------

# Cada card deve contar as OS não removidas do respectivo status.

# As contagens devem considerar todos os registros, independentemente da busca, dos filtros e da página da listagem geral.


# [RN2] - NAVEGAÇÃO PELOS CARDS
# ---------------------------------------------------------------

# A ação "Ver listagem" deve abrir a página específica correspondente ao status do card selecionado.

# O clique no card não aplica um filtro à listagem geral nem altera o status de uma Ordem de Serviço.

# A página de destino consulta os registros do respectivo status.


# [RN3] - ESCOPO DO CENÁRIO
# ---------------------------------------------------------------

# Este cenário verifica os indicadores e o redirecionamento para as páginas específicas de cada status.

# Os controles de prazo existentes nas páginas de Abertas e Em andamento pertencem às respectivas listagens.

# Sua aplicação não faz parte do clique nos cards nem do fluxo descrito neste cenário.