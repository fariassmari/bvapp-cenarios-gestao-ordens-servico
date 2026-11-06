'''
UC007 - Confirmar ou cancelar a alteração de status da OS

Objetivo: Permitir que o usuário altere o status de uma Ordem de Serviço mediante confirmação, respeitando as permissões
e as transições especificadas.

Requisitos relacionados:
- Alteração de status: 23753, 23754, 23755 e 23756.
- Atualização das informações apresentadas: 33810.
- Transições permitidas: 25417.
- Confirmação e cancelamento: 33811 e 33812.
- Disponibilização da alteração na listagem: 33783.
- Conclusão independentemente de nota fiscal: CA 23759.

Ator:
- Usuário autenticado com as permissões SERVICO_LISTAR, SERVICO_VISUALIZAR e SERVICO_EDITAR.

Autoria:
- Mariana Farias de Brito.

Pré-condições:
- Existem serviço S01 e prestador P01 válidos.
- Existe uma OS não removida, identificada como OS_REFERENCIA, com identificador conhecido, status "Aberta" e os dados planejados.
- As variações utilizam registros independentes, preparados no status de origem necessário.
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
- Alteração manual do fluxo principal: Aberta para Em andamento.
'''


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a listagem e localiza OS_REFERENCIA pelo identificador conhecido.

# O ator consulta os detalhes e confere os dados planejados e o status atual "Aberta".

# Na listagem, o ator seleciona "Em andamento" no controle de status de OS_REFERENCIA.

# O sistema apresenta um modal identificando o status de destino, com as ações "Confirmar" e "Cancelar".

# O ator seleciona "Cancelar". [A1]

# O sistema fecha o modal, mantém o status "Aberta" e reapresenta esse valor no seletor.

# O ator seleciona novamente "Em andamento".

# O sistema apresenta o modal de confirmação.

# O ator confere o destino e seleciona "Confirmar".

# O sistema valida a transição e grava o status "Em andamento".

# Após confirmar a gravação, o sistema apresenta: "Status da ordem de serviço atualizado com sucesso!"

# O sistema atualiza o status na listagem, na visualização detalhada quando aberta e nos indicadores afetados,
# sem exigir recarregamento manual.

# O ator consulta OS_REFERENCIA e verifica o status "Em andamento".


# [A1] - FECHAR O MODAL SEM CONFIRMAR
# ---------------------------------------------------------------

# O ator seleciona um status diferente do atual.

# O sistema apresenta o modal de confirmação.

# O ator fecha o modal antes de confirmar.

# O sistema mantém o status anteriormente gravado e reapresenta esse valor no seletor.


# [A2] - USUÁRIO SEM AUTORIZAÇÃO
# ---------------------------------------------------------------

# O ator utiliza uma sessão sem SERVICO_EDITAR e tenta alterar o status da OS.

# O sistema bloqueia a alteração e preserva o status gravado.

# O mesmo bloqueio deve ocorrer em uma solicitação sem autenticação.


# [A3] - CONFERIR AS DEMAIS TRANSIÇÕES DOCUMENTADAS
# ---------------------------------------------------------------

# Para cada variação, o ator utiliza uma OS independente, preparada no status de origem indicado.

# O ator solicita e confirma as seguintes transições:
# - Em andamento para Concluída;
# - Em andamento para Atrasada;
# - Aberta para Cancelada.

# O sistema valida cada transição conforme a matriz documentada, grava a alteração e atualiza as informações apresentadas.

# Os efeitos dessas alterações sobre as datas da OS dependem do esclarecimento registrado em P1.


# [A4] - TENTAR SAIR DE UM STATUS FINAL
# ---------------------------------------------------------------

# O ator utiliza uma OS com status "Concluída" e tenta alterá-lo para outro status.

# O sistema bloqueia a transição e mantém "Concluída".

# O ator repete a tentativa em uma OS com status "Cancelada".

# O sistema bloqueia a transição e mantém "Cancelada".


# [RN1] - CONFIRMAÇÃO DA ALTERAÇÃO
# ---------------------------------------------------------------

# Selecionar um status de destino não deve gravar a alteração.

# A gravação exige confirmação do usuário e validação da transição.

# Cancelar ou fechar o modal antes da confirmação deve preservar o status anteriormente gravado.


# [RN2] - TRANSIÇÕES DOCUMENTADAS
# ---------------------------------------------------------------

# A matriz utilizada especifica:
# - Aberta para Em andamento;
# - Em andamento para Concluída;
# - Em andamento para Atrasada;
# - Aberta para Cancelada.

# A matriz impede a saída dos estados Concluída e Cancelada.

# Não devem ser acrescentadas transições por suposição.


# [RN3] - FILTRO E ALTERAÇÃO DE STATUS
# ---------------------------------------------------------------

# Filtrar a listagem por status apenas modifica a consulta.

# Essa ação não altera o status de nenhuma Ordem de Serviço.
