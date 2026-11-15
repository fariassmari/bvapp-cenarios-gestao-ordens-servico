'''
UC002 - Consultar, filtrar e exportar Ordens de Serviço

Objetivo:
Permitir que o usuário pesquise, filtre, ordene e navegue pelas Ordens de Serviço e exporte em PDF ou CSV todos os registros da consulta, apresentando somente os que atendam às condições aplicadas.

Requisitos relacionados:
- Busca: CAs 23697, 23698, 23699, 23700 e 33790.
- Filtros: CAs 33791, 33792, 33793, 33794, 33795, 33799, 33800, 33801 e 33802.
- Ordenação: CAs 33796, 33797 e 33798.
- Consulta e autorização: CAs 23674, 23676, 33781 e 33782.
- Paginação: CAs 25697, 25698 e 25699.
- Exportação (acesso, formato e filtros): CAs 23774, 23775, 23776, 23777 e 33788.
- Exportação (abrangência e conteúdo): CA 23778.
- Exportação (download e mensagem de sucesso): CAs 23779 e 23780.
- Exportação (ausência de dados): CA 23781.
- Exportação (nome do arquivo): CA 23782.
- Exportação (autorização): CA 23783.
- Exportação (carregamento e retorno): CAs 23784, 34140 e 34141.
- Exportação (formato não suportado): CA 34142.

Ator:
- Técnico autenticado com SERVICO_LISTAR.

Autoria:
- Mariana Farias de Brito.

Pré-condições:
- Existem serviço S01 e prestador P01 cadastrados e não removidos.
- O serviço S01 está atualmente vinculado ao ativo A01.
- Existem 12 OS não removidas que atendem à combinação de filtros utilizada neste cenário, incluindo OS_REFERENCIA, cujo identificador gerado pelo sistema é conhecido.
- Existem outras OS que não atendem a essa combinação, incluindo uma OS de controle fora dos filtros.
- Existe uma OS removida que atende aos demais filtros, para conferir que não será incluída na consulta nem no arquivo.
- Os identificadores e as datas da massa são conhecidos, permitindo comparar os registros esperados.
- Os dados são planejados para documentação, sem execução de testes.

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
- Total esperado na consulta: 12 registros correspondentes.

As 12 OS previamente preparadas atendem aos mesmos filtros.
Essas quantidades são dados de teste, não limites da funcionalidade.
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# 1. O ator acessa a listagem de Ordens de Serviço.

# 2. O sistema apresenta os registros disponíveis e o campo de pesquisa.

# 3. O ator informa o identificador conhecido de OS_REFERENCIA no campo de pesquisa.

# 4. O sistema atualiza a listagem, apresentando os registros que correspondem ao termo informado. [A1]

# 5. O ator verifica que OS_REFERENCIA está no resultado.

# 6. O ator limpa o campo de pesquisa.

# 7. O sistema remove a condição textual e apresenta a primeira página dos resultados correspondentes.

# 8. O ator seleciona "Filtrar".

# 9. O sistema apresenta o painel com os filtros:
# - Status;
# - Serviço;
# - Prestador;
# - Ativo vinculado;
# - Data de abertura inicial e final;
# - Data prevista de conclusão inicial e final.

# 10. O ator preenche os filtros com os dados planejados e seleciona "Aplicar filtros". [A2][A3]

# 11. O sistema valida os períodos e combina os filtros conforme [RN1] e [RN2].

# 12. O sistema apresenta a primeira página da consulta, contendo somente as OS que atendem a todos os filtros.

# 13. O ator verifica que o total da consulta é 12 e que OS_REFERENCIA pertence ao conjunto retornado.

# 14. O ator verifica que as OS que não atendem aos filtros não pertencem ao resultado.

# 15. O ator utiliza os cabeçalhos "ID" e "Prevista" para ordenar os registros. [A4]

# 16. O sistema aplica a ordenação antes da paginação e indica a coluna e o sentido utilizados.

# 17. O ator navega para a segunda página. [A5]

# 18. O sistema apresenta os registros correspondentes, mantendo os filtros e a ordenação.

# 19. O ator altera a quantidade de registros por página para 20.

# 20. O sistema retorna à primeira página, preservando os filtros e a ordenação, e apresenta os 12 registros da consulta.

# 21. O ator informa novamente o identificador completo de OS_REFERENCIA no campo de pesquisa.

# 22. O sistema combina a pesquisa com os filtros existentes e apresenta a OS correspondente.

# 23. O ator seleciona "Limpar" no painel de filtros. [A6]

# 24. O sistema remove as restrições do painel, mantendo o termo pesquisado, a ordenação e a quantidade de registros por página.

# 25. O ator verifica que a pesquisa pelo identificador continua aplicada.

# 26. O ator limpa o campo de pesquisa.

# 27. O sistema remove a condição textual e apresenta a primeira página da consulta sem os filtros anteriores.

# 28. O ator aplica novamente os filtros planejados, com 10 registros por página.

# 29. O sistema apresenta 12 registros correspondentes, distribuídos em duas páginas.

# 30. O ator confere os identificadores esperados nas duas páginas e retorna à primeira página.

# 31. O ator seleciona "Exportar". [A7][A10]

# 32. O sistema solicita a seleção do formato.

# 33. O ator seleciona PDF e confirma a exportação. [A8]

# 34. O sistema apresenta um modal de carregamento durante a geração. [A9]

# 35. Ao concluir, o sistema encerra o carregamento, disponibiliza o arquivo para download e apresenta: "Arquivo gerado com sucesso!"

# 36. O ator confere que o PDF contém os 12 registros da consulta, incluindo os que estavam na segunda página.

# 37. O ator verifica que a OS de controle fora dos filtros não aparece no arquivo.

# 38. O ator verifica que a OS removida também não aparece no arquivo.

# 39. Para cada registro, o ator confere:
# - Identificador da OS;
# - Nome do serviço vinculado;
# - Prestador;
# - Data de abertura;
# - Data prevista de conclusão;
# - Data de conclusão, quando informada;
# - Custo;
# - Status.

# 40. O ator verifica o nome do arquivo no padrão: ordens_servico_AAAAMMDD_HHmmss.pdf. [P1]

# 41. O ator repete a exportação selecionando CSV.

# 42. O sistema apresenta o carregamento e, ao concluir, disponibiliza o arquivo e informa o sucesso.

# 43. O ator confere os mesmos 12 registros e os campos exigidos, acrescentando:
# - Descrição da OS;
# - Nome do solicitante.

# 44. O ator verifica o nome do arquivo no padrão: ordens_servico_AAAAMMDD_HHmmss.csv. [P1]


# [A1] - PESQUISA SEM CORRESPONDÊNCIA
# ---------------------------------------------------------------

# 1. O ator informa um termo que não corresponde a nenhuma OS da massa de teste.

# 2. O sistema aplica a pesquisa junto dos filtros vigentes.

# 3. Como não existem registros correspondentes, o sistema apresenta: "Nenhuma Ordem de Serviço encontrada."

# 4. O ator limpa o campo de pesquisa.

# 5. O sistema remove somente a condição textual, mantendo os filtros e a ordenação selecionados.


# [A2] - INFORMAR SOMENTE UM LIMITE DO PERÍODO
# ---------------------------------------------------------------

# 1. O ator acessa o painel de filtros e informa somente a data inicial de um período.

# 2. O ator seleciona "Aplicar filtros".

# 3. O sistema apresenta registros com a data correspondente maior ou igual à data inicial informada.

# 4. O ator limpa esse período e informa somente a data final.

# 5. O ator seleciona "Aplicar filtros".

# 6. O sistema apresenta registros com a data correspondente menor ou igual à data final informada.

# 7. Os demais filtros preenchidos continuam compondo a consulta.


# [A3] - INFORMAR UM PERÍODO INVÁLIDO
# ---------------------------------------------------------------

# 1. O ator informa uma data inicial posterior à data final no período de abertura ou de previsão.

# 2. O ator seleciona "Aplicar filtros".

# 3. O sistema impede a aplicação do intervalo inválido e apresenta: "A data inicial não pode ser posterior à data final."

# 4. O ator corrige as datas e solicita a aplicação novamente.

# 5. O sistema valida o período e atualiza a consulta.


# [A4] - ALTERNAR A ORDENAÇÃO
# ---------------------------------------------------------------

# 1. O ator seleciona o cabeçalho "ID".

# 2. O sistema ordena os resultados pelo identificador da OS e indica o sentido utilizado.

# 3. O ator seleciona novamente o mesmo cabeçalho.

# 4. O sistema alterna o sentido da ordenação.

# 5. O ator repete a operação no cabeçalho "Prevista".

# 6. O sistema ordena pela Data prevista de conclusão, alternando o sentido ao repetir o clique.

# 7. A busca e os filtros continuam aplicados.

# 8. O ator compara o conjunto completo de resultados, verificando que a ordenação não foi aplicada apenas aos registros da página visível.


# [A5] - NAVEGAR ENTRE AS PÁGINAS
# ---------------------------------------------------------------

# 1. Com 12 registros correspondentes e 10 por página, o ator acessa a segunda página.

# 2. O sistema apresenta os dois registros restantes, mantendo a busca, os filtros e a ordenação.

# 3. O ator retorna à primeira página.

# 4. O sistema apresenta os registros correspondentes à primeira página da mesma consulta.

# 5. O ator aplica ou remove uma busca ou um filtro.

# 6. O sistema retorna à primeira página dos resultados.


# [A6] - LIMPAR OS FILTROS DO PAINEL
# ---------------------------------------------------------------

# 1. O ator mantém um termo de pesquisa aplicado e acessa o painel de filtros.

# 2. O ator seleciona "Limpar".

# 3. O sistema retorna os seletores à opção "Todos", esvazia os campos de período e remove as restrições desses filtros.

# 4. O sistema mantém o termo de pesquisa, a ordenação e a quantidade de registros por página.

# 5. O sistema apresenta a primeira página dos resultados correspondentes à pesquisa que permaneceu aplicada.


# [A7] - CONSULTAR OU EXPORTAR SEM AUTORIZAÇÃO
# ---------------------------------------------------------------

# 1. Um usuário não autenticado ou sem SERVICO_LISTAR tenta solicitar a consulta ou a exportação de Ordens de Serviço.

# 2. O sistema bloqueia a operação e não apresenta nem gera os dados solicitados.


# [A8] - FORMATO NÃO SUPORTADO
# ---------------------------------------------------------------

# 1. É considerada uma solicitação de exportação em formato diferente de PDF ou CSV.

# 2. O sistema rejeita a solicitação e informa que o formato não é suportado.

# 3. O sistema não disponibiliza um arquivo como se a operação tivesse sido concluída com sucesso.


# [A9] - FALHA NA GERAÇÃO DO ARQUIVO
# ---------------------------------------------------------------

# 1. O ator solicita uma exportação válida.

# 2. Durante a geração, ocorre uma falha.

# 3. O sistema encerra o carregamento e informa a falha.

# 4. O sistema não disponibiliza arquivo inválido nem apresenta a mensagem de sucesso.


# [A10] - EXPORTAR CONSULTA SEM RESULTADOS
# ---------------------------------------------------------------

# 1. O ator aplica filtros que não correspondem a nenhuma OS.

# 2. O ator solicita a exportação.

# 3. O sistema informa: "Não há dados disponíveis para exportação"

# 4. O sistema encerra o carregamento e não gera o arquivo.


# [A11] - FALHA AO CARREGAR A CONSULTA
# ---------------------------------------------------------------

# 1. O ator solicita a consulta com uma sessão autorizada, mas ocorre uma falha no carregamento dos dados.

# 2. O sistema informa que não foi possível carregar a consulta.

# 3. O sistema distingue essa falha da ausência de resultados, sem apresentá-la como uma consulta válida sem registros.


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


# [RN6] - AUTORIZAÇÃO
# ---------------------------------------------------------------

# A consulta e a exportação exigem usuário autenticado com SERVICO_LISTAR.

# Solicitações sem autenticação ou sem a permissão devem ser bloqueadas.


# [RN7] - ABRANGÊNCIA DA EXPORTAÇÃO
# ---------------------------------------------------------------

# A exportação deve considerar os filtros aplicados à consulta.

# O arquivo deve conter todos os registros correspondentes, independentemente da página exibida.

# Registros fora dos filtros ou removidos não devem ser incluídos.

# Este cenário não define por suposição se o termo pesquisado e a ordenação também são aplicados ao arquivo, pois os critérios de aceitação citam apenas os filtros.


# [RN8] - CONTEÚDO POR FORMATO
# ---------------------------------------------------------------

# O PDF deve conter os campos definidos no critério 23778.

# O CSV deve conter esses campos e acrescentar a descrição da OS e o nome do solicitante.

# Uma data de conclusão ausente não deve ser preenchida com um valor inventado.


# [RN9] - RETORNO DA OPERAÇÃO
# ---------------------------------------------------------------

# A mensagem de sucesso somente deve ser apresentada após a geração e a disponibilização do arquivo.

# Carregamento, ausência de dados e falha devem ter tratamentos distintos.


# RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# A consulta apresenta somente os registros que atendem simultaneamente às condições aplicadas.

# As 12 OS previamente preparadas compõem os resultados da consulta filtrada.

# A ordenação e a paginação preservam o conjunto correto de resultados.

# Limpar os filtros não remove a pesquisa textual.

# O PDF e o CSV contêm todos os 12 registros da consulta, sem a OS de controle e sem a OS removida.

# Os arquivos seguem o padrão de nome e os campos definidos para cada formato.

# Uma falha de consulta ou de geração não é apresentada como ausência de registros nem como sucesso.

# A busca, os filtros, a ordenação, a paginação e a exportação não alteram os registros previamente preparados.