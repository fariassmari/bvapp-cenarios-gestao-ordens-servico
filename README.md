# Cenários de teste — Gestão de Ordens de Serviço do BVApp

## Apresentação

Este repositório contém a documentação dos cenários de teste do módulo de Gestão de Ordens de Serviço do BVApp, elaborada para a disciplina de Verificação, Validação e Testes de Software.

O módulo integra a gestão de serviços de uma cooperativa de energia solar. Os cenários descrevem o comportamento esperado nas operações com Ordens de Serviço (OS), incluindo consultas, alterações, exportações e controle de acesso.

A documentação foi organizada a partir dos requisitos e critérios de aceitação relacionados em cada cenário. Os arquivos registram os fluxos principais, as situações alternativas e as regras de negócio consideradas na especificação.

## Objetivo

Documentar cenários que permitam verificar os principais comportamentos da Gestão de Ordens de Serviço, contemplando:

- Cadastro, consulta, edição e remoção de OS;
- Pesquisa, filtros, ordenação e paginação da listagem;
- Exportação da consulta em PDF e CSV;
- Visualização dos detalhes da OS, da conta associada e dos pagamentos;
- Consulta dos ativos associados ao serviço da OS;
- Confirmação ou cancelamento da alteração de status;
- Exportação individual de uma OS em PDF;
- Indicadores por status e acesso às listagens pela Gestão rápida;
- Permissões de acesso, falhas e restrições das operações.

Cada cenário apresenta ações do ator e respostas esperadas do sistema. Quando uma regra depende de esclarecimento, a pendência é registrada no próprio cenário, sem presumir um comportamento não confirmado.

## Organização dos cenários

Os cenários estão em arquivos individuais, identificados de UC001 a UC007. O UC001 reúne as operações de cadastro, consulta, edição e remoção; os demais detalham funcionalidades e situações complementares.

```text
bvapp-cenarios/
├── README.md
└── functional_tests/
    ├── README.md
    ├── __init__.py
    ├── test_uc001_manter_ordem_servico.py
    ├── test_uc002_consultar_filtrar_exportar.py
    ├── test_uc003_detalhes_conta.py
    ├── test_uc004_ativos_associados.py
    ├── test_uc005_confirmacao_status.py
    ├── test_uc006_exportacao_individual.py
    └── test_uc007_gestao_rapida.py
```

| Caso de uso | Funcionalidade | Arquivo |
| --- | --- | --- |
| UC001 | Manter Ordem de Serviço | [test_uc001_manter_ordem_servico.py](functional_tests/test_uc001_manter_ordem_servico.py) |
| UC002 | Consultar, filtrar e exportar Ordens de Serviço | [test_uc002_consultar_filtrar_exportar.py](functional_tests/test_uc002_consultar_filtrar_exportar.py) |
| UC003 | Visualizar detalhes da OS e consultar a conta associada | [test_uc003_detalhes_conta.py](functional_tests/test_uc003_detalhes_conta.py) |
| UC004 | Visualizar ativos associados à Ordem de Serviço | [test_uc004_ativos_associados.py](functional_tests/test_uc004_ativos_associados.py) |
| UC005 | Confirmar ou cancelar a alteração de status da OS | [test_uc005_confirmacao_status.py](functional_tests/test_uc005_confirmacao_status.py) |
| UC006 | Exportar o PDF individual de uma Ordem de Serviço | [test_uc006_exportacao_individual.py](functional_tests/test_uc006_exportacao_individual.py) |
| UC007 | Consultar indicadores e acessar listagens pela Gestão rápida | [test_uc007_gestao_rapida.py](functional_tests/test_uc007_gestao_rapida.py) |

Consulte também o [README dos cenários funcionais](functional_tests/README.md).

## Estrutura de cada cenário

Sempre que aplicável, cada arquivo apresenta:

- **Identificador e título:** identificação do caso de uso.
- **Autoria e objetivo:** responsável e finalidade do cenário.
- **Requisitos relacionados:** critérios de aceitação associados.
- **Ator e pré-condições:** papel do usuário e condições necessárias para iniciar o fluxo.
- **Dados planejados:** informações usadas para descrever as verificações.
- **Fluxo principal `[FP]`:** sequência esperada de ações e respostas.
- **Fluxos alternativos `[A1]`, `[A2]` etc.:** variações, erros, cancelamentos e restrições.
- **Regras de negócio `[RN1]`, `[RN2]` etc.:** condições que orientam o comportamento esperado.
- **Pendências:** pontos que ainda exigem esclarecimento, quando houver.

Os passos do fluxo principal e de cada fluxo alternativo são numerados separadamente, a partir de 1. Referências entre colchetes relacionam os passos às variações, regras ou pendências descritas no arquivo.

## Situações alternativas contempladas

Além dos fluxos principais, os cenários incluem, conforme a funcionalidade:

- Dados obrigatórios ausentes, valores inválidos e datas inconsistentes;
- Pesquisa ou filtros sem resultados;
- Falha no carregamento de consultas ou na geração de arquivos;
- Usuário sem autenticação ou sem a permissão necessária;
- Cancelamento de cadastro, edição, remoção ou alteração de status;
- Restrição de remoção de OS com conta vinculada;
- Ausência de conta, pagamentos ou ativos associados;
- Tentativa de transição a partir de um status final.

## Rastreabilidade e ferramentas

Os arquivos listam os critérios de aceitação relacionados a cada caso de uso. Essa identificação permite localizar os requisitos contemplados e revisar os cenários quando as regras forem esclarecidas ou alteradas.

- **Python:** extensão usada para organizar os arquivos documentais.
- **Git e GitHub:** versionamento e disponibilização do projeto.

Os arquivos `.py` contêm descrições e comentários estruturados. Eles não são testes automatizados executáveis.

## Escopo da entrega

Esta entrega corresponde à especificação e organização dos cenários de teste. Não inclui a implementação do BVApp, a criação de interfaces, a automação ou a execução dos testes.

## Responsável

- **Autora:** Mariana Farias de Brito
- **Instituição:** Instituto Federal da Paraíba (IFPB)
- **Disciplina:** Verificação, Validação e Testes de Software
- **Atividade:** Mini projeto individual — N3
- **Entrega:** 06/11/2026
