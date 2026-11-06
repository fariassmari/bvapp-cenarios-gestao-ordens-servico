'''
UC008 - Exportar a listagem de Ordens de Serviço em PDF e CSV

Objetivo: Permitir que o usuário exporte todos os registros correspondentes à consulta, respeitando os filtros aplicados
e os campos definidos para cada formato.

Requisitos relacionados:
- Acesso, seleção de formato e filtros: 23774, 23775, 23776 e 23777.
- Abrangência e conteúdo: 23778.
- Download e mensagem de sucesso: 23779 e 23780.
- Ausência de dados: 23781.
- Nome do arquivo: 23782.
- Autorização: 23783.
- Carregamento e retorno: 23784, 34140 e 34141.
- Formato não suportado: 34142.
- Ação de exportação na listagem: 33788.

Ator:
- Usuário autenticado com a permissão SERVICO_LISTAR.

Autoria:
- Mariana Farias de Brito.

Pré-condições:
- Existem serviço S01 e prestador P01 válidos.
- Existem 12 OS não removidas que correspondem aos filtros planejados, incluindo OS_REFERENCIA com os dados abaixo.
- Existe uma OS de controle que não corresponde aos filtros.
- Existe uma OS removida que corresponde aos demais filtros, para conferir que não será incluída no arquivo.
- Os identificadores dos registros de preparação são conhecidos.
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
- Filtros: serviço S01 e prestador P01.
- Quantidade por página: 10 registros.
- Total esperado na consulta: 12 registros correspondentes.
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem e aplica os filtros de serviço S01 e prestador P01.

# O sistema apresenta 12 registros correspondentes, distribuídos em páginas de 10 registros.

# O ator confere os identificadores esperados nas duas páginas e retorna à primeira página.

# O ator seleciona "Exportar".

# O sistema solicita a seleção do formato.

# O ator seleciona PDF e confirma a exportação.

# O sistema apresenta um modal de carregamento durante a geração.

# Ao concluir, o sistema encerra o carregamento, disponibiliza o arquivo para download e apresenta: "Arquivo gerado com sucesso!"

# O ator confere que o PDF contém os 12 registros da consulta, incluindo os que estavam na segunda página.

# O ator verifica que a OS de controle fora dos filtros não aparece no arquivo.

# O ator verifica que a OS removida também não aparece no arquivo.

# Para cada registro, o ator confere:
# - Identificador da OS;
# - Nome do serviço vinculado;
# - Prestador;
# - Data de abertura;
# - Data prevista de conclusão;
# - Data de conclusão, quando informada;
# - Custo;
# - Status.

# O ator verifica o nome do arquivo no padrão: ordens_servico_AAAAMMDD_HHmmss.pdf. [P1]

# O ator repete a exportação selecionando CSV.

# O sistema apresenta o carregamento e, ao concluir, disponibiliza o arquivo e informa o sucesso.

# O ator confere os mesmos 12 registros e os campos exigidos, acrescentando:
# - Descrição da OS;
# - Nome do solicitante.

# O ator verifica o nome do arquivo no padrão: ordens_servico_AAAAMMDD_HHmmss.csv. [P1]


# [A1] - CONSULTA SEM RESULTADOS
# ---------------------------------------------------------------

# O ator aplica filtros que não correspondem a nenhuma OS.

# O ator solicita a exportação.

# O sistema informa: "Não há dados disponíveis para exportação"

# O sistema encerra o carregamento e não gera o arquivo.


# [A2] - FORMATO NÃO SUPORTADO
# ---------------------------------------------------------------

# É considerada uma solicitação de exportação em formato diferente de PDF ou CSV.

# O sistema rejeita a solicitação e informa que o formato não é suportado.

# O sistema não disponibiliza um arquivo como se a operação tivesse sido concluída com sucesso.


# [A3] - FALHA NA GERAÇÃO
# ---------------------------------------------------------------

# O ator solicita uma exportação válida.

# Durante a geração, ocorre uma falha.

# O sistema encerra o carregamento e informa a falha.

# O sistema não disponibiliza arquivo inválido nem apresenta a mensagem de sucesso.


# [A4] - USUÁRIO SEM AUTORIZAÇÃO
# ---------------------------------------------------------------

# O ator utiliza uma sessão sem SERVICO_LISTAR e solicita a exportação.

# O sistema bloqueia a operação.

# O mesmo bloqueio deve ocorrer quando não houver autenticação.


# [RN1] - ABRANGÊNCIA DA EXPORTAÇÃO
# ---------------------------------------------------------------

# A exportação deve considerar os filtros aplicados à consulta.

# O arquivo deve conter todos os registros correspondentes, independentemente da página exibida.

# Registros fora dos filtros ou removidos não devem ser incluídos.


# [RN2] - CONTEÚDO POR FORMATO
# ---------------------------------------------------------------

# O PDF deve conter os campos definidos no critério 23778.

# O CSV deve conter esses campos e acrescentar a descrição da OS e o nome do solicitante.

# Uma data de conclusão ausente não deve ser preenchida com um valor inventado.


# [RN3] - RETORNO DA OPERAÇÃO
# ---------------------------------------------------------------

# A mensagem de sucesso somente deve ser apresentada após a geração e a disponibilização do arquivo.

# Carregamento, ausência de dados e falha devem ter tratamentos distintos.
