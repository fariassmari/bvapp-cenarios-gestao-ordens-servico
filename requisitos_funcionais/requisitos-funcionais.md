## Módulo 02 - Gestão de Ordens de Serviço

### [RF02001] - Cadastro de ordem de serviço

Cenário relacionado: [UC001 - Manter ordem de serviço](../functional_tests/test_uc001_manter_ordem_servico.py)

Como usuário com a permissão SERVICO_ADICIONAR, gostaria de cadastrar uma ordem de serviço (OS) com as seguintes informações: Descrição, Serviço vinculado, Prestador responsável, Custo, Data de abertura, Data prevista de conclusão e Data de conclusão (opcional). O serviço e o prestador devem ser previamente cadastrados e não removidos. O identificador da OS deve ser gerado automaticamente no formato AAAA-MM-DD-TTT-NNNN (data de abertura, até três primeiras letras do tipo do serviço em maiúsculas e sequência de pelo menos quatro algarismos), sem permitir preenchimento ou alteração manual, e deve ser único. O status inicial deve ser definido automaticamente a partir da data atual em UTC. O custo deve ser numérico e maior que zero. A descrição deve ter pelo menos 10 caracteres, desconsiderando espaços no início e no fim. A Data prevista de conclusão e a Data de conclusão não podem ser anteriores à Data de abertura. Caso a OS seja incluída com sucesso, deve-se registrar o ID da OS, o usuário que fez a inclusão e a data e hora da criação. A gravação deve ser transacional: em caso de falha, nenhum cadastro parcial pode ser mantido e o sistema deve informar o campo ou a regra que impediu a operação, sem exibir mensagem de sucesso.

### [RF02002] - Consulta de ordens de serviço

Cenário relacionado: [UC004 - Consultar, filtrar e exportar](../functional_tests/test_uc004_consultar_filtrar_exportar.py)

Como usuário com a permissão SERVICO_LISTAR, gostaria de consultar a lista de ordens de serviço cadastradas e não removidas, com paginação (página atual, total de registros e seleção da quantidade de itens por página). A navegação entre páginas deve manter busca, filtros e ordenação aplicados. A ordenação padrão é pelo código da OS em ordem crescente. A listagem deve permitir ordenar por ID e por Data prevista de conclusão (crescente ou decrescente), aplicando a ordenação a todos os registros antes da paginação. Falhas de carregamento devem ser distinguidas da ausência de registros ("Nenhuma Ordem de Serviço encontrada."). A partir de cada registro, o sistema deve disponibilizar as ações de visualizar, editar, remover (conforme as permissões SERVICO_VISUALIZAR, SERVICO_EDITAR e SERVICO_EXCLUIR), além de adicionar e exportar. O status de cada OS deve ser exibido em um seletor que permite alterá-lo (ver RF02006).

### [RF02003] - Busca e filtros de ordens de serviço

Cenário relacionado: [UC004 - Consultar, filtrar e exportar](../functional_tests/test_uc004_consultar_filtrar_exportar.py)

Como usuário com a permissão SERVICO_LISTAR, gostaria de buscar ordens de serviço por nome ou código (busca parcial, sem diferenciar maiúsculas/minúsculas e desconsiderando espaços nas extremidades) e filtrá-las por Status (Aberta, Em andamento, Atrasada, Concluída ou Cancelada), por período (data inicial, data final ou ambas) e por Ativo (OS cujo serviço esteja atualmente vinculado ao ativo selecionado). Os critérios são combinados simultaneamente (E lógico). Quando a data inicial for posterior à data final, o sistema deve impedir a aplicação e informar "A data inicial não pode ser posterior à data final.". Ao aplicar ou remover busca ou filtro, o sistema deve retornar à primeira página. O painel de filtros deve ter a ação "Limpar". O filtro não altera o status das OS.

### [RF02004] - Visualização detalhada de ordem de serviço

Cenário relacionado: [UC005 - Detalhes da conta](../functional_tests/test_uc005_detalhes_conta.py) e [UC006 - Ativos associados](../functional_tests/test_uc006_ativos_associados.py)

Como usuário com a permissão SERVICO_VISUALIZAR, gostaria de visualizar os detalhes de uma OS em um painel lateral, iniciando na aba "Detalhes". Quando não houver Data de conclusão, deve ser exibido "Não informada" ou "-", sem preenchimento automático. Quando a periodicidade do serviço vinculado for zero, deve ser exibido "Pontual"; caso contrário, o intervalo de recorrência em dias. O painel deve conter:

- **Aba "Ativos associados"**: ativos do serviço da OS, agrupados por tipo com quantidade por grupo (grupos expansíveis/recolhíveis), exibindo número de série, status e data de entrada em operação (quando informada). Acesso somente com SERVICO_VISUALIZAR e ATIVO_VISUALIZAR. Sem ativos: "Nenhum ativo associado.".
- **Aba "Conta associada"**: conta da OS e seus pagamentos, ordenados por data de vencimento crescente e, em empate, pelo número da parcela. Acesso somente com SERVICO_VISUALIZAR e CONTA_VISUALIZAR. Sem conta: "Nenhuma conta associada."; sem pagamentos: "Nenhum pagamento encontrado.". Caso exista uma nota fiscal ou comprovante de pagamento associado à OS, o sistema deve exibir essa informação nos detalhes da OS.

Falhas no carregamento de uma aba devem ser distinguidas da ausência de registros. Ao fechar ou voltar, a página, a busca, os filtros e a ordenação da listagem devem ser preservados. O painel deve oferecer as ações de exportação individual (SERVICO_VISUALIZAR) e edição (SERVICO_EDITAR).

### [RF02005] - Edição de ordem de serviço

Cenário relacionado: [UC001 - Manter ordem de serviço](../functional_tests/test_uc001_manter_ordem_servico.py)

Como usuário com a permissão SERVICO_EDITAR, gostaria de editar os dados de uma OS já cadastrada, com o formulário aberto com os dados atuais preenchidos e aplicando as mesmas regras de preenchimento do cadastro (RF02001). O identificador não pode ser alterado nem regenerado. Campos não alterados devem preservar seus valores. Caso a edição seja salva com sucesso, deve-se registrar no histórico o usuário que realizou a alteração, a data e hora e os dados alterados. A gravação deve ser transacional (em caso de falha, desfazer a operação e informar que não foi possível salvar). Ao cancelar ou fechar o formulário antes do envio, as alterações devem ser descartadas. Após salvar, listagem e visualização detalhada devem ser atualizadas sem recarregar a página, e o status deve ser recalculado considerando a data atual em UTC.

### [RF02006] - Atualização de status da ordem de serviço

Cenário relacionado: [UC007 - Confirmação de status](../functional_tests/test_uc007_confirmacao_status.py)

Como usuário com a permissão SERVICO_EDITAR, gostaria de alterar o status de uma OS (Aberta, Em andamento, Concluída, Atrasada) diretamente pelo seletor da listagem, respeitando as transições de status permitidas pelo sistema. Ao selecionar um status diferente do atual, o sistema deve exibir um modal de confirmação identificando o status de destino. Ao cancelar ou fechar o modal, o status anterior deve ser mantido e reapresentado no seletor. A conclusão da OS é permitida independentemente da existência de nota fiscal associada. Após a gravação, listagem, visualização detalhada e indicadores devem ser atualizados sem recarregar a página.

### [RF02007] - Remoção de ordem de serviço

Cenário relacionado: [UC003 - Cancelamentos CRUD](../functional_tests/test_uc003_cancelamentos_crud.py)

Como usuário com a permissão SERVICO_EXCLUIR, gostaria de remover uma OS a partir da listagem, mediante modal de confirmação que identifique a OS selecionada. A remoção deve ser lógica (a OS é marcada como removida, preservando o registro no banco de dados). O sistema deve impedir a remoção quando existir ao menos uma conta vinculada à OS que não esteja removida nem cancelada, informando o motivo. Durante o processamento, deve indicar o andamento e impedir envios repetidos. Ao cancelar ou fechar o modal, nenhuma alteração deve ser feita. Após a remoção, a lista deve ser atualizada.

### [RF02008] - Exportação da lista de ordens de serviço

Cenário relacionado: [UC004 - Consultar, filtrar e exportar](../functional_tests/test_uc004_consultar_filtrar_exportar.py)

Como usuário com a permissão SERVICO_LISTAR, gostaria de exportar a lista de OS nos formatos PDF ou CSV, selecionando o formato antes da geração. A exportação deve considerar os filtros e a busca aplicados e conter todas as OS que atendam à consulta, independentemente da página atual. O arquivo deve ser nomeado no padrão `ordens_servico_AAAAMMDD_HHmmss.extensão`. Durante a geração, deve ser exibido um modal de carregamento. Quando não houver registros, o sistema deve informar "Não há dados disponíveis para exportação" e não gerar o arquivo. Formatos diferentes de PDF ou CSV devem ser rejeitados. Em caso de erro, o download de arquivo inválido deve ser impedido.

### [RF02009] - Exportação individual de ordem de serviço

Cenário relacionado: [UC008 - Exportação individual](../functional_tests/test_uc008_exportacao_individual.py)

Como usuário com a permissão SERVICO_VISUALIZAR, gostaria de exportar em PDF uma OS individual a partir da visualização detalhada. O PDF deve incluir informações financeiras somente se o usuário possuir também CONTA_VISUALIZAR, e informações de ativos somente se possuir também ATIVO_VISUALIZAR. Durante a geração, deve ser exibido modal de carregamento e, em caso de falha, nenhum arquivo inválido pode ser disponibilizado.

### [RF02010] - Dashboard de indicadores de ordens de serviço

Como usuário com a permissão SERVICO_LISTAR, gostaria de visualizar, acima da listagem, quatro cards de indicadores: Abertas, Em andamento, Concluídas e Atrasadas. Os cards devem ser atualizados automaticamente após cadastro, edição, alteração de status ou remoção, sem recarregar a página. Status sem registros deve exibir zero. Em caso de falha na consulta, o sistema deve informar o erro, sem exibir zero como resultado confirmado. Cada card deve ter a ação "Ver listagem", que abre a listagem filtrada pelo status:

- **Abertas**: OS não removidas, ordenadas por Data de abertura crescente, com filtro opcional de prazo para início (Data de abertura ≤ data atual + dias selecionados).
- **Em andamento**: OS não removidas, ordenadas por Data prevista de conclusão crescente, com filtro opcional de prazo para vencimento (Data prevista entre a data atual e a data atual + dias selecionados, inclusive).
- **Concluídas**: OS não removidas, ordenadas por Data de conclusão decrescente.
- **Atrasadas**: ordenadas por Data prevista de conclusão crescente.

As listagens devem ser paginadas (ordenação antes da paginação, mantendo status e prazo ao navegar), voltar à primeira página ao alterar prazo ou itens por página, identificar o status no título e considerar a data atual em UTC.