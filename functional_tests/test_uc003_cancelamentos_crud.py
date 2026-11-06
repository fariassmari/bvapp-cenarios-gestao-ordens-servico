'''
UC003 - Cancelar operações de cadastro, edição e remoção de OS

Objetivo:
Permitir que o usuário cancele o cadastro, a edição e a remoção de uma Ordem de Serviço, preservando os dados anteriormente gravados.

Requisitos relacionados:
- Cadastro: CAs 23478, 23484 e 34179.
- Consulta: CAs 23674, 23675 e 23676.
- Edição: CAs 23742, 23745, 23746 e 33806.
- Remoção: CAs 23467, 23468, 23469, 23470 e 23471.

Ator:
- Usuário autenticado com as permissões necessárias para cadastrar, consultar, editar e remover OS.

Autoria:
- Mariana Farias de Brito.

Pré-condições:
- Existe um serviço cadastrado e não removido.
- Existe um prestador cadastrado e não removido.
- A OS utilizada no fluxo principal não possui conta vinculada que impeça sua remoção.
- Os cancelamentos de cadastro e edição ocorrem antes do envio.
- O cancelamento da remoção ocorre antes da confirmação.

Dados planejados:
- Data de referência: 01/11/2026, às 12:00 UTC.
- Descrição do cadastro cancelado: Rascunho de manutenção sem envio.
- Descrição do cadastro confirmado: Limpeza programada dos painéis do bloco A.
- Serviço: serviço previamente cadastrado.
- Prestador: prestador previamente cadastrado.
- Custo inicial: R$ 150,00.
- Data de abertura: 02/11/2026.
- Data prevista: 05/11/2026.
- Data de conclusão: não informada.
- Descrição proposta na edição: Limpeza programada dos painéis do bloco B.
- Custo proposto na edição: R$ 180,00.

O identificador gerado no cadastro confirmado será utilizado
para localizar a mesma OS nas demais operações.
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem de Ordens de Serviço.

# O sistema apresenta a listagem e disponibiliza a ação "Adicionar", conforme a permissão do ator.

# O ator seleciona "Adicionar".

# O sistema abre o formulário de cadastro.

# O ator preenche os campos com os dados planejados, utilizando a descrição "Rascunho de manutenção sem envio".

# Antes de selecionar "Salvar", o ator seleciona "Cancelar". [A1]

# O sistema encerra o formulário sem gravar a OS, conforme [RN1].

# O ator consulta a listagem.

# O sistema apresenta os registros disponíveis.

# O ator verifica que o rascunho cancelado não foi cadastrado.

# O ator seleciona "Adicionar" novamente.

# O sistema abre o formulário de cadastro.

# O ator preenche os campos com os dados válidos, utilizando a descrição: "Limpeza programada dos painéis do bloco A".

# O ator seleciona "Salvar".

# O sistema valida os dados e grava a OS.

# Após confirmar a gravação, o sistema apresenta: "Ordem de Serviço cadastrada com sucesso!"

# O ator consulta a listagem e localiza a OS pelo identificador gerado no cadastro.

# O ator seleciona a ação de edição da OS.

# O sistema abre o formulário com os dados atuais preenchidos.

# O ator altera a descrição para: "Limpeza programada dos painéis do bloco B".

# O ator altera o custo de R$ 150,00 para R$ 180,00.

# Antes de selecionar "Salvar", o ator seleciona "Cancelar". [A2]

# O sistema encerra o formulário e mantém os dados anteriormente gravados, conforme [RN2].

# O ator consulta novamente a OS.

# O sistema apresenta a descrição: "Limpeza programada dos painéis do bloco A", e o custo de R$ 150,00.

# O ator verifica que a edição cancelada não foi gravada.

# O ator abre a edição novamente e realiza as mesmas alterações.

# O ator seleciona "Salvar".

# O sistema valida os dados e confirma a gravação da edição.

# O sistema apresenta: "Ordem de Serviço atualizada com sucesso!"

# O ator consulta novamente a OS.

# O sistema apresenta a descrição: "Limpeza programada dos painéis do bloco B", e o custo de R$ 180,00.

# O ator seleciona a ação de remoção da OS.

# O sistema apresenta um modal identificando a OS e oferecendo as opções "Confirmar" e "Cancelar".

# Antes de confirmar, o ator seleciona "Cancelar". [A3]

# O sistema encerra o modal sem remover a OS, conforme [RN3].

# O ator consulta novamente a listagem.

# O sistema apresenta a OS com o mesmo identificador, a descrição atualizada e o custo de R$ 180,00.

# O ator verifica que a remoção cancelada não alterou o registro.

# O ator solicita a remoção novamente.

# O sistema apresenta o modal de confirmação.

# O ator seleciona "Confirmar".

# O sistema verifica os impedimentos da operação.

# Como não existe conta vinculada que impeça a remoção, o sistema marca a OS como removida, preservando seu registro no banco de dados.

# Após confirmar a gravação, o sistema apresenta: "Ordem de Serviço removida com sucesso!"

# O sistema atualiza a listagem.

# O ator verifica que a OS removida não aparece na consulta de registros disponíveis.


# [A1] - FECHAR O CADASTRO ANTES DO ENVIO
# ---------------------------------------------------------------

# O ator acessa o formulário de cadastro e preenche os dados do rascunho.

# Antes de enviar os dados, o ator fecha o formulário, em vez de selecionar "Cancelar".

# O sistema encerra o formulário sem gravar a OS.

# O ator consulta a listagem e verifica que o rascunho não foi cadastrado.


# [A2] - FECHAR A EDIÇÃO ANTES DO ENVIO
# ---------------------------------------------------------------

# O ator localiza a OS cadastrada e abre sua edição.

# O sistema apresenta os dados atuais preenchidos.

# O ator altera a descrição e o custo.

# Antes de enviar as alterações, o ator fecha o formulário, em vez de selecionar "Cancelar".

# O sistema encerra o formulário sem gravar as alterações.

# O ator consulta novamente a OS.

# O sistema apresenta os valores que estavam gravados antes da abertura da edição.


# [A3] - FECHAR O MODAL DE REMOÇÃO
# ---------------------------------------------------------------

# O ator localiza a OS e solicita sua remoção.

# O sistema apresenta o modal de confirmação.

# Antes de confirmar, o ator fecha o modal, em vez de selecionar "Cancelar".

# O sistema encerra a solicitação sem remover a OS.

# O ator consulta novamente a listagem.

# O sistema apresenta a OS disponível, com o mesmo identificador e os mesmos dados.


# [RN1] - CANCELAMENTO DO CADASTRO
# ---------------------------------------------------------------

# Ao selecionar "Cancelar" ou fechar o formulário antes do envio, o sistema deve encerrá-lo sem gravar a Ordem de Serviço.


# [RN2] - CANCELAMENTO DA EDIÇÃO
# ---------------------------------------------------------------

# Ao selecionar "Cancelar" ou fechar o formulário antes do envio, o sistema deve descartar as alterações do formulário e manter os dados anteriormente gravados.


# [RN3] - CANCELAMENTO DA REMOÇÃO
# ---------------------------------------------------------------

# Ao selecionar "Cancelar" ou fechar o modal antes da confirmação, o sistema deve encerrar a solicitação sem remover a Ordem de Serviço.


# [RN4] - REMOÇÃO CONFIRMADA
# ---------------------------------------------------------------

# A remoção somente deve ocorrer após a confirmação do usuário e a verificação dos impedimentos da operação.

# A remoção deve ser lógica, preservando o registro da OS no banco de dados.


# RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# O cadastro cancelado não gera uma OS gravada.

# A edição cancelada mantém os dados anteriores.

# A remoção cancelada mantém a OS disponível e sem alterações.

# Os mesmos resultados de cancelamento se aplicam
# ao fechamento antes do envio ou da confirmação,
# conforme a operação.

# O cadastro, a consulta, a edição e a remoção confirmados são concluídos no mesmo cenário.

# Após a remoção confirmada, a OS deixa de aparecer na consulta de registros disponíveis.