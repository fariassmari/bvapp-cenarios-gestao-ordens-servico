'''
UC005 - Visualizar detalhes da OS e consultar a conta associada

Objetivo: Permitir que o usuário consulte os detalhes de uma Ordem de Serviço, a conta associada e seus pagamentos.

Requisitos relacionados:
- Detalhes da OS: 23509, 23510, 23511, 23512 e 23513.
- Formatação e informações opcionais: 34143, 34144 e 34145.
- Conta e pagamentos: 34151, 34152, 34153, 34154, 34155 e 34156.
- Carregamento e retorno à listagem: 34157 e 34158.

Ator:
- Usuário autenticado com as permissões SERVICO_LISTAR, SERVICO_VISUALIZAR e CONTA_VISUALIZAR.

Autoria:
- Mariana Farias de Brito.

Pré-condições:
- Existem serviço S01 e prestador P01 cadastrados e não removidos.
- O serviço S01 possui periodicidade igual a zero.
- O usuário solicitante e o prestador possuem dados conhecidos para permitir a conferência das informações exibidas.
- Existe uma OS não removida, identificada como OS_REFERENCIA, com identificador conhecido, status "Aberta" e os dados planejados. Essa OS não possui conta vinculada.
- Para as alternativas financeiras, existe uma OS de preparação com uma única conta cuja elegibilidade foi confirmada.
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
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem e localiza OS_REFERENCIA pelo identificador conhecido.

# O ator seleciona a ação de visualização de OS_REFERENCIA.

# O sistema abre o painel lateral inicialmente na aba "Detalhes".

# O ator verifica que as informações correspondem à OS selecionada:
# - Identificador;
# - Status "Aberta";
# - Nome do serviço S01;
# - Descrição cadastrada;
# - Custo R$ 150,00;
# - Periodicidade "Pontual";
# - Nome e CPF ou CNPJ do prestador P01;
# - Telefone do prestador, quando informado;
# - Nome e e-mail do usuário solicitante;
# - Data de abertura 02/11/2026;
# - Data prevista de conclusão 05/11/2026;
# - Data de conclusão apresentada como "Não informada" ou "-". [RN1]

# O ator acessa a aba "Conta associada".

# O sistema informa "Nenhuma conta associada.", pois OS_REFERENCIA não possui conta vinculada. [A1][A2][A3][A4]

# O ator seleciona "Voltar" ou fecha o painel.

# O sistema encerra a visualização e preserva a página, a busca, os filtros e a ordenação da listagem.


# [A1] - CONSULTAR CONTA ASSOCIADA E PAGAMENTOS
# ---------------------------------------------------------------

# O ator utiliza a OS de preparação que possui uma única conta associada com elegibilidade confirmada. [P1]

# O ator abre a visualização e acessa "Conta associada".

# O sistema apresenta:
# - Nome da conta;
# - Descrição, quando informada;
# - Valor total;
# - Status;
# - Tipo da conta;
# - Data de lançamento;
# - Quantidade de parcelas pagas e quantidade total de parcelas;
# - Informação de recorrência e intervalo, quando aplicável.

# O ator compara os valores exibidos com os dados conhecidos da conta vinculada à OS.

# O sistema apresenta os pagamentos não removidos, informando:
# - Número da parcela;
# - Valor da parcela;
# - Data de vencimento;
# - Situação do pagamento;
# - Data do pagamento, quando registrada;
# - Indicação de comprovante aprovado associado, quando existente.

# O ator verifica que os pagamentos estão ordenados por vencimento crescente e, em caso de empate, pelo número da parcela.

# Para conferir o desempate, a preparação contém as parcelas 1 e 2 com vencimento em 05/11/2026 e a parcela 3 com vencimento em 10/11/2026.

# O resultado esperado é a apresentação das parcelas na ordem 1, 2 e 3, independentemente da ordem de preparação dos registros.

# A consulta da indicação de comprovante não pressupõe uma ação de anexar ou abrir o arquivo dentro da OS. [RN2]


# [A2] - CONTA SEM PAGAMENTOS
# ---------------------------------------------------------------

# O ator abre uma OS de preparação com conta elegível associada, mas sem pagamentos cadastrados.

# O ator acessa "Conta associada".

# O sistema apresenta os dados da conta e informa: "Nenhum pagamento encontrado."


# [A3] - USUÁRIO SEM PERMISSÃO PARA CONSULTAR A CONTA
# ---------------------------------------------------------------

# O ator utiliza uma sessão com SERVICO_VISUALIZAR, mas sem CONTA_VISUALIZAR.

# O ator abre os detalhes da OS.

# O sistema permite consultar os detalhes autorizados da OS, mas bloqueia o acesso aos dados da conta e de seus pagamentos.

# A permissão de visualizar a OS não substitui a permissão necessária para consultar a conta.


# [A4] - CARREGAMENTO E FALHA NA CONSULTA
# ---------------------------------------------------------------

# O ator acessa uma aba do painel lateral.

# Enquanto a consulta estiver em andamento, o sistema apresenta uma indicação de carregamento.

# Caso a consulta falhe, o sistema informa que não foi possível carregar os dados.

# O sistema não apresenta a falha como se não existissem registros.


# [A5] - SERVIÇO COM PERIODICIDADE POSITIVA
# ---------------------------------------------------------------

# O ator consulta uma OS de preparação cujo serviço possui periodicidade de 30 dias.

# O sistema apresenta a recorrência em dias, correspondente ao valor 30, em vez de apresentar "Pontual".


# [RN1] - FORMATAÇÃO E DADOS OPCIONAIS
# ---------------------------------------------------------------

# As datas devem ser apresentadas no formato DD/MM/AAAA.

# Os valores monetários devem ser apresentados em reais, com duas casas decimais.

# A ausência da data de conclusão não deve provocar o preenchimento automático de uma data.

# Informações opcionais devem corresponder aos registros vinculados, sem apresentar valores inventados.


# [RN2] - CONSULTA FINANCEIRA
# ---------------------------------------------------------------

# Os dados financeiros exibidos devem pertencer à conta associada à OS selecionada.

# Somente pagamentos não removidos devem ser apresentados.

# A indicação de comprovante deve corresponder à existência de comprovante aprovado associado ao pagamento.

# Este cenário consulta os detalhes da OS, a conta e seus pagamentos, utilizando registros previamente preparados.


# [RN3] - PRESERVAÇÃO DOS DADOS
# ---------------------------------------------------------------

# A consulta dos detalhes não deve alterar a OS nem a conta.
