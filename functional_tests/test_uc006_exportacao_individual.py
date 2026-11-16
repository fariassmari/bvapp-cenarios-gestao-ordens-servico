'''
UC006 - Exportar o PDF individual de uma Ordem de Serviço

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
- Técnico

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

# 1. O ator localiza OS_REFERENCIA na listagem e abre sua visualização.

# 2. O ator confere o identificador para assegurar que selecionou a OS correta.

# 3. O ator aciona a exportação individual em PDF.

# 4. O sistema abre um modal de carregamento e mantém essa indicação durante a geração.

# 5. Ao concluir, o sistema encerra o carregamento, disponibiliza o PDF para download e apresenta: "Arquivo gerado com sucesso!"

# 6. O ator confere que o PDF contém os dados de OS_REFERENCIA:
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

# 7. O ator verifica que os dados da outra OS de preparação não foram utilizados no lugar dos dados de OS_REFERENCIA.

# 8. Com acesso aos dados dos ativos, o ator confere os ativos não removidos atualmente vinculados ao serviço S01:
# - Tipo;
# - Número de série;
# - Status;
# - Data de entrada em operação, quando informada. [A2]

# 9. Com acesso aos dados da conta, o ator verifica a indicação para OS_REFERENCIA, que não possui conta vinculada:
# "Nenhuma conta associada". [A3][A4]

# 10. O ator confere que o nome do arquivo identifica a OS e contém a data e a hora da geração. [P1]


# [A1] - USUÁRIO SEM AUTORIZAÇÃO PARA EXPORTAR
# ---------------------------------------------------------------

# 1. O ator utiliza uma sessão sem autorização para visualizar a OS e solicita o PDF individual.

# 2. O sistema bloqueia a exportação.

# 3. O mesmo bloqueio deve ocorrer quando não houver autenticação.


# [A2] - PERMISSÃO E AUSÊNCIA DE ATIVOS
# ---------------------------------------------------------------

# 1. O ator utiliza uma sessão autorizada a exportar a OS, mas sem acesso aos dados dos ativos.

# 2. O ator solicita o PDF individual.

# 3. O sistema não inclui informações dos ativos no arquivo.

# 4. Em outra variação, o ator tem acesso aos dados dos ativos, mas o serviço da OS não possui ativos associados.

# 5. O PDF apresenta: "Nenhum ativo associado"


# [A3] - USUÁRIO SEM PERMISSÃO FINANCEIRA
# ---------------------------------------------------------------

# 1. O ator utiliza uma sessão autorizada a exportar a OS, mas sem acesso aos dados da conta.

# 2. O ator solicita o PDF individual de uma OS com conta vinculada.

# 3. O sistema não inclui informações financeiras da conta.

# 4. A permissão de exportar a OS não concede automaticamente acesso aos dados financeiros.


# [A4] - OS COM CONTA ASSOCIADA
# ---------------------------------------------------------------

# 1. O ator utiliza uma OS de preparação com uma única conta cuja elegibilidade foi confirmada. [P2]

# 2. O ator possui autorização para visualizar a OS e os dados da conta e solicita o PDF individual.

# 3. O sistema inclui os dados da mesma conta apresentada na visualização detalhada:
# - Nome;
# - Descrição, quando informada;
# - Valor total;
# - Status;
# - Tipo;
# - Data de lançamento.

# 4. O ator compara os dados do PDF com os dados conhecidos da conta e com a visualização detalhada.


# [A5] - FALHA NA GERAÇÃO DO PDF
# ---------------------------------------------------------------

# 1. O ator solicita a exportação individual.

# 2. Durante a geração, ocorre uma falha.

# 3. O sistema encerra o carregamento e informa que não foi possível gerar o PDF.

# 4. O sistema não disponibiliza arquivo inválido nem apresenta a mensagem de sucesso.


# [RN1] - CORRESPONDÊNCIA DO ARQUIVO
# ---------------------------------------------------------------

# O PDF deve corresponder à OS selecionada.

# A exportação não deve alterar os dados nem gerar um novo identificador para a OS.

# Datas opcionais ausentes não devem receber valores inventados.


# [RN2] - AUTORIZAÇÃO POR SEÇÃO
# ---------------------------------------------------------------

# A exportação individual exige autorização para visualizar a OS.

# A inclusão dos dados de ativos exige também autorização para consultá-los.

# A inclusão dos dados financeiros exige também autorização para consultar a conta.

# A ausência de uma permissão adicional não autoriza a exposição dos dados da seção correspondente.
