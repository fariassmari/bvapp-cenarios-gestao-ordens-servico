'''
UC004 - Buscar e filtrar Ordens de Serviço

Objetivo:
Permitir que o usuário pesquise, filtre, ordene e navegue pelas Ordens de Serviço, apresentando somente os registros que atendam às condições da consulta.

Requisitos relacionados:
- Busca: CAs 23697, 23698, 23699, 23700 e 33790.
- Filtros: CAs 33791, 33792, 33793, 33794, 33795, 33799, 33800, 33801 e 33802.
- Ordenação: CAs 33796, 33797 e 33798.
- Consulta e autorização: CAs 23674, 23676, 33781 e 33782.
- Paginação: CAs 25697, 25698 e 25699.

Ator:
- Usuário autenticado com SERVICO_LISTAR.

Autoria:
- Mariana Farias de Brito.

Pré-condições:
- Existem serviço S01 e prestador P01 cadastrados e não removidos.
- O serviço S01 está atualmente vinculado ao ativo A01.
- Existem 12 OS não removidas que atendem à combinação de filtros utilizada neste cenário, incluindo OS_REFERENCIA, cujo identificador gerado pelo sistema é conhecido.
- Existem outras OS que não atendem a essa combinação.
- Os identificadores e as datas da massa são conhecidos, permitindo comparar os registros esperados.

Dados planejados:
- Data de referência: 01/11/2026, às 12:00 UTC.
- Descrição de OS_REFERENCIA: Limpeza programada dos painéis do bloco A.
- Serviço: S01.
- Prestador: P01.
- Custo: R$ 150,00.
- Data de abertura: 02/11/2026.
- Data prevista: 05/11/2026.
- Data de conclusão: não informada.
- Status de OS_REFERENCIA: Aberta.
- Filtros combinados: status Aberta, serviço S01, prestador P01, ativo A01, abertura entre 02/11/2026 e 04/11/2026, previsão entre 05/11/2026 e 07/11/2026.
- Quantidade inicial por página: 10 registros.

As 12 OS previamente preparadas atendem aos mesmos filtros.
Essas quantidades são dados de teste, não limites da funcionalidade.
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem de Ordens de Serviço.

# O sistema apresenta os registros disponíveis e o campo de pesquisa.

# O ator informa o identificador conhecido de OS_REFERENCIA no campo de pesquisa.

# O sistema atualiza a listagem, apresentando os registros que correspondem ao termo informado. [A1]

# O ator verifica que OS_REFERENCIA está no resultado.

# O ator limpa o campo de pesquisa.

# O sistema remove a condição textual e apresenta a primeira página dos resultados correspondentes.

# O ator seleciona "Filtrar".

# O sistema apresenta o painel com os filtros:
# - Status;
# - Serviço;
# - Prestador;
# - Ativo vinculado;
# - Data de abertura inicial e final;
# - Data prevista de conclusão inicial e final.

# O ator preenche os filtros com os dados planejados e seleciona "Aplicar filtros". [A2][A3]

# O sistema valida os períodos e combina os filtros conforme [RN1] e [RN2].

# O sistema apresenta a primeira página da consulta, contendo somente as OS que atendem a todos os filtros.

# O ator verifica que o total da consulta é 12 e que OS_REFERENCIA pertence ao conjunto retornado.

# O ator verifica que as OS que não atendem aos filtros não pertencem ao resultado.

# O ator utiliza os cabeçalhos "ID" e "Prevista" para ordenar os registros. [A4]

# O sistema aplica a ordenação antes da paginação e indica a coluna e o sentido utilizados.

# O ator navega para a segunda página. [A5]

# O sistema apresenta os registros correspondentes, mantendo os filtros e a ordenação.

# O ator altera a quantidade de registros por página para 20.

# O sistema retorna à primeira página, preservando os filtros e a ordenação, e apresenta os 12 registros da consulta.

# O ator informa novamente o identificador completo de OS_REFERENCIA no campo de pesquisa.

# O sistema combina a pesquisa com os filtros existentes e apresenta a OS correspondente.

# O ator seleciona "Limpar" no painel de filtros. [A6]

# O sistema remove as restrições do painel, mantendo o termo pesquisado, a ordenação e a quantidade de registros por página.

# O ator verifica que a pesquisa pelo identificador continua aplicada.

# O ator limpa o campo de pesquisa.

# O sistema remove a condição textual e apresenta a primeira página da consulta sem os filtros anteriores.


# [A1] - PESQUISA SEM CORRESPONDÊNCIA
# ---------------------------------------------------------------

# O ator informa um termo que não corresponde a nenhuma OS da massa de teste.

# O sistema aplica a pesquisa junto dos filtros vigentes.

# Como não existem registros correspondentes, o sistema apresenta: "Nenhuma Ordem de Serviço encontrada."

# O ator limpa o campo de pesquisa.

# O sistema remove somente a condição textual, mantendo os filtros e a ordenação selecionados.


# [A2] - INFORMAR SOMENTE UM LIMITE DO PERÍODO
# ---------------------------------------------------------------

# O ator acessa o painel de filtros e informa somente a data inicial de um período.

# O ator seleciona "Aplicar filtros".

# O sistema apresenta registros com a data correspondente maior ou igual à data inicial informada.

# O ator limpa esse período e informa somente a data final.

# O ator seleciona "Aplicar filtros".

# O sistema apresenta registros com a data correspondente menor ou igual à data final informada.

# Os demais filtros preenchidos continuam compondo a consulta.


# [A3] - INFORMAR UM PERÍODO INVÁLIDO
# ---------------------------------------------------------------

# O ator informa uma data inicial posterior à data final no período de abertura ou de previsão.

# O ator seleciona "Aplicar filtros".

# O sistema impede a aplicação do intervalo inválido e apresenta: "A data inicial não pode ser posterior à data final."

# O ator corrige as datas e solicita a aplicação novamente.

# O sistema valida o período e atualiza a consulta.


# [A4] - ALTERNAR A ORDENAÇÃO
# ---------------------------------------------------------------

# O ator seleciona o cabeçalho "ID".

# O sistema ordena os resultados pelo identificador da OS e indica o sentido utilizado.

# O ator seleciona novamente o mesmo cabeçalho.

# O sistema alterna o sentido da ordenação.

# O ator repete a operação no cabeçalho "Prevista".

# O sistema ordena pela Data prevista de conclusão, alternando o sentido ao repetir o clique.

# A busca e os filtros continuam aplicados.

# O ator compara o conjunto completo de resultados, verificando que a ordenação não foi aplicada apenas aos registros da página visível.


# [A5] - NAVEGAR ENTRE AS PÁGINAS
# ---------------------------------------------------------------

# Com 12 registros correspondentes e 10 por página, o ator acessa a segunda página.

# O sistema apresenta os dois registros restantes, mantendo a busca, os filtros e a ordenação.

# O ator retorna à primeira página.

# O sistema apresenta os registros correspondentes à primeira página da mesma consulta.

# O ator aplica ou remove uma busca ou um filtro.

# O sistema retorna à primeira página dos resultados.


# [A6] - LIMPAR OS FILTROS DO PAINEL
# ---------------------------------------------------------------

# O ator mantém um termo de pesquisa aplicado e acessa o painel de filtros.

# O ator seleciona "Limpar".

# O sistema retorna os seletores à opção "Todos", esvazia os campos de período e remove as restrições desses filtros.

# O sistema mantém o termo de pesquisa, a ordenação e a quantidade de registros por página.

# O sistema apresenta a primeira página dos resultados correspondentes à pesquisa que permaneceu aplicada.


# [A7] - CONSULTAR SEM AUTORIZAÇÃO
# ---------------------------------------------------------------

# Um usuário não autenticado ou sem SERVICO_LISTAR tenta solicitar a consulta de Ordens de Serviço.

# O sistema bloqueia a consulta e não apresenta os dados solicitados.


# [A8] - FALHA AO CARREGAR A CONSULTA
# ---------------------------------------------------------------

# O ator solicita a consulta com uma sessão autorizada, mas ocorre uma falha no carregamento dos dados.

# O sistema informa que não foi possível carregar a consulta.

# O sistema distingue essa falha da ausência de resultados, sem apresentá-la como uma consulta válida sem registros.


# [RN1] - COMBINAÇÃO DAS CONDIÇÕES
# ---------------------------------------------------------------

# Os filtros preenchidos e a pesquisa textual devem ser atendidos simultaneamente.

# A opção "Todos" representa ausência de restrição pelo respectivo seletor.

# Selecionar um status no filtro não altera o status de nenhuma Ordem de Serviço.


# [RN2] - FILTROS DE PERÍODO
# ---------------------------------------------------------------

# Quando somente a data inicial estiver preenchida, considerar datas maiores ou iguais a ela.

# Quando somente a data final estiver preenchida, considerar datas menores ou iguais a ela.

# Quando ambos os limites estiverem preenchidos, incluir as datas inicial e final no intervalo.

# A data inicial não pode ser posterior à data final.


# [RN3] - FILTRO POR ATIVO
# ---------------------------------------------------------------

# O filtro por ativo deve apresentar somente as OS cujo serviço esteja atualmente vinculado ao ativo selecionado.


# [RN4] - ORDENAÇÃO E PAGINAÇÃO
# ---------------------------------------------------------------

# A ordenação deve ser aplicada a todos os resultados antes da divisão em páginas.

# Sem ordenação selecionada, utilizar o identificador da OS em ordem crescente.

# Navegar entre páginas deve preservar a busca, os filtros e a ordenação.

# Aplicar ou remover uma busca ou filtro deve retornar à primeira página.

# Alterar a quantidade de registros por página também deve retornar à primeira página.


# [RN5] - TRATAMENTO DA PESQUISA
# ---------------------------------------------------------------

# A pesquisa deve permitir correspondência parcial pelo identificador da OS, sem diferenciar letras maiúsculas e minúsculas.

# Espaços no início e no final do termo devem ser desconsiderados.

# Este cenário utiliza a pesquisa pelo identificador.
# Não define por suposição outros campos pesquisáveis ou um tamanho mínimo de termo ainda não confirmado.


# RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# A consulta apresenta somente os registros que atendem simultaneamente às condições aplicadas.

# As 12 OS previamente preparadas compõem os resultados da consulta filtrada.

# A ordenação e a paginação preservam o conjunto correto de resultados.

# Limpar os filtros não remove a pesquisa textual.

# Uma falha de consulta não é apresentada como ausência de registros.

# A busca, os filtros, a ordenação e a paginação não alteram os registros previamente preparados.