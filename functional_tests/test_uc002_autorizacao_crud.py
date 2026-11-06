'''
UC002 - Controlar autorização nas quatro operações de OS

Objetivo:
Permitir que as operações de cadastro, consulta, edição e remoção de Ordens de Serviço sejam realizadas somente por usuários
autenticados com as permissões correspondentes.

Requisitos relacionados:
- Cadastro: CA 23490.
- Consulta: CAs 23676 e 33781.
- Ações da listagem: CAs 33783, 33784, 33785 e 33786.
- Edição: CA23741.
- Alteração de status: CA 23753.
- Remoção: CAs 23466 e 23472.

Ator:
- Usuário A: autenticado com SERVICO_ADICIONAR, SERVICO_LISTAR,
  SERVICO_VISUALIZAR, SERVICO_EDITAR e SERVICO_EXCLUIR.
- Usuário B: autenticado, mas sem a permissão específica da operação avaliada.
- Usuário não autenticado.

Autoria:
- Mariana Farias de Brito.

Pré-condições:
- Existe um serviço cadastrado e não removido.
- Existe um prestador cadastrado e não removido.
- A OS utilizada no fluxo principal não possui conta vinculada que impeça sua remoção.
- Nas variações do usuário B, retirar somente a permissão avaliada e manter as demais necessárias ao acesso.
- As tentativas de consulta, edição e remoção sem autorização devem ocorrer enquanto a OS ainda estiver disponível.

Dados planejados:
- Data de referência: 01/11/2026, às 12:00 UTC.
- Descrição: Limpeza programada dos painéis do bloco A.
- Serviço: serviço previamente cadastrado.
- Prestador: prestador previamente cadastrado.
- Custo: R$ 150,00.
- Data de abertura: 02/11/2026.
- Data prevista: 05/11/2026.
- Data de conclusão: não informada.

O identificador gerado no cadastro será utilizado para localizar a mesma OS nas demais operações.
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O usuário A acessa o sistema com uma sessão autenticada.

# O sistema identifica as permissões do usuário conforme [RN1].

# O usuário A acessa a listagem de Ordens de Serviço. [A1][A3]

# O sistema apresenta a listagem e disponibiliza a ação
# "Adicionar", pois o usuário possui SERVICO_ADICIONAR.

# O usuário A seleciona "Adicionar". [A1][A2]

# O sistema apresenta o formulário de cadastro.

# O usuário A preenche os campos com os dados planejados
# e seleciona "Salvar".

# O sistema verifica a autenticação e a permissão
# SERVICO_ADICIONAR, valida os dados e grava a OS.

# O sistema gera o identificador e apresenta o retorno
# de sucesso após confirmar a gravação.

# O usuário A consulta a listagem e localiza a OS
# pelo identificador gerado. [A1][A3]

# O sistema apresenta o registro correspondente à OS cadastrada.

# O usuário A seleciona a ação de visualização. [A1][A4]

# O sistema verifica SERVICO_VISUALIZAR e apresenta os detalhes da OS selecionada.

# O usuário A retorna à listagem e seleciona a ação de edição da OS. [A1][A5]

# O sistema verifica SERVICO_EDITAR e abre o formulário com os dados atuais preenchidos.

# O usuário A altera a descrição para: "Limpeza programada dos painéis do bloco B".

# O usuário A altera o custo para R$ 180,00, mantém os demais campos e seleciona "Salvar".

# O sistema verifica a autorização, valida os dados e confirma a gravação das alterações.

# O usuário A consulta novamente a OS.

# O sistema apresenta a descrição atualizada e o custo de R$ 180,00, preservando os campos não alterados.

# O usuário A seleciona a ação de remoção. [A1][A6]

# O sistema verifica SERVICO_EXCLUIR e apresenta o modal de confirmação da remoção.

# O usuário A seleciona "Confirmar".

# O sistema verifica a autorização e os impedimentos da operação.

# Como a OS não possui conta impeditiva, o sistema realiza a exclusão lógica e apresenta o retorno de sucesso.

# O sistema atualiza a listagem.

# O usuário A verifica que a OS removida não aparece na consulta de registros disponíveis.


# [A1] - SOLICITAR OPERAÇÃO SEM AUTENTICAÇÃO
# ---------------------------------------------------------------

# No ponto correspondente do fluxo principal, o usuário
# não autenticado tenta solicitar cadastro, consulta,
# edição ou remoção de uma OS.

# O sistema verifica que não existe uma sessão autenticada.

# O sistema bloqueia a operação solicitada.

# Para cadastro, nenhuma OS deve ser criada.

# Para consulta, os dados solicitados não devem ser apresentados.

# Para edição ou remoção, os dados e a disponibilidade
# da OS anteriormente gravada devem ser preservados.

# O usuário A retoma o fluxo principal na operação correspondente.


# [A2] - CADASTRAR SEM SERVICO_ADICIONAR
# ---------------------------------------------------------------

# O usuário B está autenticado, mas não possui
# a permissão SERVICO_ADICIONAR.

# O usuário B tenta acessar ou solicitar o cadastro de uma OS.

# O sistema não disponibiliza a ação de cadastro para esse usuário
# e bloqueia solicitações realizadas sem a permissão necessária.

# O usuário A consulta a listagem e verifica que nenhuma OS
# foi criada pela tentativa não autorizada.


# [A3] - CONSULTAR SEM SERVICO_LISTAR
# ---------------------------------------------------------------

# O usuário B está autenticado, mas não possui
# a permissão SERVICO_LISTAR.

# O usuário B tenta acessar ou solicitar a consulta
# da listagem de Ordens de Serviço.

# O sistema bloqueia a consulta e não apresenta os dados
# da listagem solicitada.

# A tentativa não altera os registros existentes.

# Esta restrição se refere à listagem. A autorização para
# visualizar detalhes é verificada separadamente em [A4].


# [A4] - VISUALIZAR SEM SERVICO_VISUALIZAR
# ---------------------------------------------------------------

# O usuário B possui SERVICO_LISTAR, mas não possui
# SERVICO_VISUALIZAR.

# O usuário B acessa a listagem e localiza a OS.

# O sistema não disponibiliza a ação de visualização detalhada
# para esse usuário.

# Se o usuário B solicitar diretamente a visualização,
# o sistema deve bloquear o acesso aos detalhes da OS.

# Os dados da OS permanecem sem alterações.


# [A5] - EDITAR OU ALTERAR STATUS SEM SERVICO_EDITAR
# ---------------------------------------------------------------

# O usuário B possui SERVICO_LISTAR, mas não possui
# SERVICO_EDITAR.

# O usuário B acessa a listagem e localiza a OS.

# O sistema não disponibiliza a ação de edição
# nem permite utilizar a alteração de status.

# Se o usuário B solicitar diretamente uma edição
# ou alteração de status, o sistema bloqueia a operação.

# O usuário A consulta a OS e verifica que a descrição,
# o custo, as datas e o status anteriormente gravados
# foram preservados.


# [A6] - REMOVER SEM SERVICO_EXCLUIR
# ---------------------------------------------------------------

# O usuário B possui SERVICO_LISTAR, mas não possui
# SERVICO_EXCLUIR.

# O usuário B acessa a listagem e localiza a OS.

# O sistema não disponibiliza a ação de remoção
# e impede o acesso ao modal correspondente.

# Se o usuário B solicitar diretamente a remoção,
# o sistema bloqueia a operação.

# O usuário A consulta novamente a listagem e verifica
# que a OS continua disponível e sem alterações.


# [RN1] - AUTENTICAÇÃO E PERMISSÕES
# ---------------------------------------------------------------

# O cadastro exige autenticação e SERVICO_ADICIONAR.

# A consulta da listagem exige autenticação e SERVICO_LISTAR.

# A visualização detalhada exige autenticação
# e SERVICO_VISUALIZAR.

# A edição e a alteração de status exigem autenticação
# e SERVICO_EDITAR.

# A remoção exige autenticação e SERVICO_EXCLUIR.


# [RN2] - INDEPENDÊNCIA DAS PERMISSÕES
# ---------------------------------------------------------------

# A permissão de uma operação não concede automaticamente
# autorização para realizar as demais.

# A autorização deve ser verificada na operação solicitada,
# inclusive quando a solicitação não for iniciada
# por um botão disponível na interface.


# [RN3] - PRESERVAÇÃO DOS DADOS
# ---------------------------------------------------------------

# Uma tentativa de cadastro sem autorização não deve criar OS.

# Uma tentativa de consulta sem autorização não deve
# apresentar os dados solicitados.

# Uma tentativa de edição, alteração de status ou remoção
# sem autorização não deve modificar a OS existente.


# RESULTADOS ESPERADOS
# ---------------------------------------------------------------

# O usuário A conclui o cadastro, a consulta, a edição
# e a remoção da OS com as permissões correspondentes.

# As tentativas sem autenticação ou sem a permissão
# necessária são bloqueadas.

# Nenhuma tentativa não autorizada cria, altera
# ou remove indevidamente uma OS.

# Não são definidos neste cenário códigos HTTP ou mensagens
# literais de acesso negado que não constem dos requisitos.
