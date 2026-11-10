'''
UC009 - Exportar o PDF individual de uma Ordem de Serviço

Objetivo: Permitir que o usuário exporte a OS selecionada, respeitando as permissões para os dados de ativos e da conta.

Requisitos relacionados:
- Disponibilização e autorização: 34164 e 34165.
- Conteúdo do PDF: 34166.
- Download e nome do arquivo: 34167 e 34168.
- Carregamento, sucesso e falha: 34169, 34170 e 34171.
- Autorização e conteúdo financeiro: 34172.
- Autorização dos dados de ativos: 34173.
- Ação no painel de detalhes: 34159.

Ator:
- Usuário autenticado com as permissões SERVICO_LISTAR, SERVICO_VISUALIZAR, ATIVO_VISUALIZAR e CONTA_VISUALIZAR.

Autoria:
- Mariana Farias de Brito.

Pré-condições:
- Existem serviço S01 e prestador P01 válidos.
- O serviço S01 possui ativos atuais, não removidos, cujos dados são conhecidos.
- Existe outra OS com descrição e identificador diferentes, para conferir que o arquivo corresponde à seleção correta.
- Existe uma OS não removida, identificada como OS_REFERENCIA, com identificador conhecido e os dados planejados. Essa OS não possui conta vinculada.
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
- Ativos do serviço: A01, tipo Painel, e A02, tipo Inversor,
  com números de série e status conhecidos.
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator localiza OS_REFERENCIA na listagem e abre sua visualização.

# O ator confere o identificador para assegurar que selecionou a OS correta.

# O ator aciona a exportação individual em PDF.

# O sistema abre um modal de carregamento e mantém essa indicação durante a geração.

# Ao concluir, o sistema encerra o carregamento, disponibiliza o PDF para download e apresenta: "Arquivo gerado com sucesso!"

# O ator confere que o PDF contém os dados de OS_REFERENCIA:
# - Identificador;
# - Status;
# - Nome do serviço;
# - Descrição da OS;
# - Nome do prestador;
# - Nome do solicitante;
# - Custo;
# - Data de abertura;
# - Data prevista de conclusão;
# - Data de conclusão, quando informada.

# O ator verifica que os dados da outra OS de preparação não foram utilizados no lugar dos dados de OS_REFERENCIA.

# Como possui ATIVO_VISUALIZAR, o ator confere os ativos não removidos atualmente vinculados ao serviço S01:
# - Tipo;
# - Número de série;
# - Status;
# - Data de entrada em operação, quando informada. [A2]

# Como possui CONTA_VISUALIZAR e OS_REFERENCIA não possui conta, o ator verifica a indicação:
# "Nenhuma conta associada". [A3][A4]

# O ator confere que o nome do arquivo identifica a OS e contém a data e a hora da geração. [P1]


# [A1] - USUÁRIO SEM AUTORIZAÇÃO PARA EXPORTAR
# ---------------------------------------------------------------

# O ator utiliza uma sessão sem SERVICO_VISUALIZAR e solicita o PDF individual.

# O sistema bloqueia a exportação.

# O mesmo bloqueio deve ocorrer quando não houver autenticação.


# [A2] - PERMISSÃO E AUSÊNCIA DE ATIVOS
# ---------------------------------------------------------------

# O ator utiliza uma sessão com SERVICO_VISUALIZAR, mas sem ATIVO_VISUALIZAR.

# O ator solicita o PDF individual.

# O sistema não inclui informações dos ativos no arquivo.

# Em outra variação, o ator possui ATIVO_VISUALIZAR, mas o serviço da OS não possui ativos associados.

# O PDF apresenta: "Nenhum ativo associado"


# [A3] - USUÁRIO SEM PERMISSÃO FINANCEIRA
# ---------------------------------------------------------------

# O ator utiliza uma sessão com SERVICO_VISUALIZAR, mas sem CONTA_VISUALIZAR.

# O ator solicita o PDF individual de uma OS com conta vinculada.

# O sistema não inclui informações financeiras da conta.

# A permissão de exportar a OS não concede automaticamente acesso aos dados financeiros.


# [A4] - OS COM CONTA ASSOCIADA
# ---------------------------------------------------------------

# O ator utiliza uma OS de preparação com uma única conta cuja elegibilidade foi confirmada. [P2]

# O ator possui SERVICO_VISUALIZAR e CONTA_VISUALIZAR e solicita o PDF individual.

# O sistema inclui os dados da mesma conta apresentada na visualização detalhada:
# - Nome;
# - Descrição, quando informada;
# - Valor total;
# - Status;
# - Tipo;
# - Data de lançamento.

# O ator compara os dados do PDF com os dados conhecidos da conta e com a visualização detalhada.


# [A5] - FALHA NA GERAÇÃO DO PDF
# ---------------------------------------------------------------

# O ator solicita a exportação individual.

# Durante a geração, ocorre uma falha.

# O sistema encerra o carregamento e informa que não foi possível gerar o PDF.

# O sistema não disponibiliza arquivo inválido nem apresenta a mensagem de sucesso.


# [RN1] - CORRESPONDÊNCIA DO ARQUIVO
# ---------------------------------------------------------------

# O PDF deve corresponder à OS selecionada.

# A exportação não deve alterar os dados nem gerar um novo identificador para a OS.

# Datas opcionais ausentes não devem receber valores inventados.


# [RN2] - AUTORIZAÇÃO POR SEÇÃO
# ---------------------------------------------------------------

# A exportação individual exige SERVICO_VISUALIZAR.

# Os dados de ativos exigem também ATIVO_VISUALIZAR.

# Os dados financeiros exigem também CONTA_VISUALIZAR.

# A ausência de uma permissão adicional não autoriza a exposição dos dados da seção correspondente.
