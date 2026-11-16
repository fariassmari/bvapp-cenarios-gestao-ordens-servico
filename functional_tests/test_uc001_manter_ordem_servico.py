'''
UC001 - Manter Ordem de Serviço

Objetivo:
Permitir que o usuário cadastre, consulte, altere e remova uma Ordem de Serviço.

Requisitos relacionados:
- Cadastro: CAs 23478, 23479, 23482, 23483, 23484, 23486, 23487, 23490, 25415 e 34175.
- Consulta: CAs 23674, 23675 e 23676.
- Edição: CAs 23741, 23742, 23743, 23744, 23745 e 23746.
- Remoção: CAs 23466, 23467, 23468, 23469, 23470, 23471 e 23473.

Ator:
- Técnico

Autoria:
- Mariana Farias de Brito.

Pré-condições:
- Existe um serviço cadastrado e não removido.
- Existe um prestador cadastrado e não removido.
- Para o fluxo completo de remoção, a OS não possui conta vinculada que impeça a operação.

Dados planejados:
- Descrição: Limpeza programada dos painéis do bloco A.
- Serviço: serviço previamente cadastrado.
- Prestador: prestador previamente cadastrado.
- Custo: R$ 150,00.
- Data de abertura: dia seguinte à data de referência do cenário.
- Data prevista: quatro dias após a data de referência.
- Data de conclusão: não informada.

A data de referência deve permanecer a mesma durante o cenário.
O status inicial considera essa data em UTC, conforme CA04 revisado.
'''

# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# 1. O ator acessa a listagem de Ordens de Serviço.

# 2. O sistema apresenta a listagem e disponibiliza a ação "Adicionar", conforme a permissão do ator.

# 3. O ator seleciona "Adicionar".

# 4. O sistema abre o formulário de cadastro de Ordem de Serviço.

# 5. O ator verifica os campos:
# - Descrição da Ordem de Serviço;
# - Serviço;
# - Prestador responsável;
# - Custo;
# - Data de abertura;
# - Data prevista de conclusão;
# - Data de conclusão.
#
# 6. O ator verifica as opções "Salvar" e "Cancelar". [A4]

# 7. O ator seleciona o serviço e o prestador previamente cadastrados.

# 8. O sistema apresenta os nomes selecionados nos respectivos campos.

# 9. O ator preenche a descrição, o custo e as datas com os dados planejados, mantendo a conclusão sem preenchimento.

# 10. O ator seleciona "Salvar".

# 11. O sistema valida os campos conforme [RN1] e [RN2]. [A5]

# 12. O sistema gera o identificador da OS.
# Como a abertura é futura e não há conclusão, o status inicial é "Aberta", conforme [RN3].

# 13. Após confirmar a gravação, o sistema apresenta: "Ordem de Serviço cadastrada com sucesso!"

# 14. O ator consulta a listagem e localiza a OS cadastrada. [A1]

# 15. O ator verifica que o identificador, o serviço, o prestador, o custo e os demais dados correspondem ao cadastro realizado.

# 16. O ator realiza a edição descrita em [A2].

# 17. Após conferir os dados atualizados, o ator realiza a remoção descrita em [A3].


# [A1] - LOCALIZAR A ORDEM DE SERVIÇO
# ---------------------------------------------------------------

# 1. O ator acessa a listagem de Ordens de Serviço.

# 2. O sistema apresenta os registros disponíveis.

# 3. O ator localiza a OS pelo identificador gerado no cadastro, navegando entre as páginas, se necessário.

# 4. O ator verifica que o registro corresponde à OS cadastrada.


# [A2] - EDITAR A ORDEM DE SERVIÇO
# ---------------------------------------------------------------

# 1. O ator executa [A1] e seleciona a ação de edição da OS.

# 2. O sistema abre o formulário com os dados atuais preenchidos.

# 3. O ator altera a descrição para:
# "Limpeza programada dos painéis do bloco B".

# 4. O ator altera o custo para R$ 180,00 e mantém
# o serviço, o prestador e as datas anteriores.

# 5. O ator seleciona "Salvar". [A4]

# 6. O sistema valida os dados conforme [RN1] e [RN2]. [A5]

# 7. Após confirmar a gravação, o sistema apresenta: "Ordem de Serviço atualizada com sucesso!"

# 8. O ator consulta novamente a OS.

# 9. O sistema apresenta a nova descrição e o custo de R$ 180,00.

# 10. O ator verifica que os campos não alterados foram preservados e que o identificador da OS permanece o mesmo.


# [A3] - REMOVER A ORDEM DE SERVIÇO
# ---------------------------------------------------------------

# 1. O ator executa [A1] e seleciona a ação de remoção.

# 2. O sistema apresenta um modal de confirmação, identificando a OS e oferecendo "Confirmar" e "Cancelar". [A4]

# 3. O ator seleciona "Confirmar".

# 4. O sistema verifica os impedimentos da operação. [A6]

# 5. Na ausência de impedimentos, o sistema marca a OS como removida, preservando seu registro no banco de dados.

# 6. Após confirmar a gravação, o sistema apresenta: "Ordem de Serviço removida com sucesso!"

# 7. O sistema atualiza a listagem.

# 8. O ator verifica que a OS removida não aparece na consulta de registros disponíveis.


# [A4] - CANCELAR UMA OPERAÇÃO
# ---------------------------------------------------------------

# 1. No cadastro, o ator seleciona "Cancelar" ou fecha
# o formulário antes do envio.

# 2. O sistema encerra o formulário sem cadastrar a OS.

# 3. Na edição, o ator seleciona "Cancelar" ou fecha
# o formulário antes do envio.

# 4. O sistema mantém os dados anteriormente gravados.

# 5. Na remoção, o ator seleciona "Cancelar" ou fecha
# o modal antes da confirmação.

# 6. O sistema mantém a OS disponível e sem remoção.


# [A5] - INFORMAR DADOS INVÁLIDOS
# ---------------------------------------------------------------

# 1. O ator tenta salvar o cadastro ou a edição com um campo obrigatório ausente, descrição insuficiente, custo inválido
# ou datas inconsistentes.

# 2. O sistema rejeita a operação e informa o campo ou a regra que impediu a gravação.

# 3. O sistema não apresenta mensagem de sucesso.

# 4. O ator corrige os dados e solicita a gravação novamente.


# [A6] - REMOÇÃO IMPEDIDA POR CONTA VINCULADA
# ---------------------------------------------------------------

# 1. Nesta variação, a OS possui uma conta vinculada que não está removida nem cancelada.

# 2. O ator solicita e confirma a remoção da OS.

# 3. O sistema bloqueia a remoção e informa o impedimento financeiro.

# 4. O ator consulta novamente a OS e verifica que ela permanece disponível e que seus dados foram preservados.


# [RN1] - PREENCHIMENTO E VALIDAÇÃO DOS CAMPOS
# ---------------------------------------------------------------

# Descrição, serviço, prestador, custo, data de abertura e data prevista são obrigatórios.

# A data de conclusão é opcional.

# A descrição deve conter pelo menos 10 caracteres após desconsiderar espaços nas extremidades.

# O custo deve ser numérico e maior que zero.

# O serviço e o prestador devem existir e não estar removidos.


# [RN2] - CONSISTÊNCIA DAS DATAS
# ---------------------------------------------------------------

# A data prevista não pode ser anterior à data de abertura.

# Quando informada, a data de conclusão não pode ser anterior à data de abertura.


# [RN3] - STATUS INICIAL
# ---------------------------------------------------------------

# Considerando a data atual em UTC, aplicar nesta ordem:
# - Conclusão válida preenchida: Concluída;
# - Sem conclusão e previsão vencida: Atrasada;
# - Sem conclusão, abertura até a data atual e previsão não vencida: Em andamento;
# - Sem conclusão e abertura futura: Aberta.
