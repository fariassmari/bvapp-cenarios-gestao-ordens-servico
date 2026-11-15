# Cenários de testes funcionais

Este diretório contém sete cenários documentais do módulo de Gestão de Serviços do BVapp. Os arquivos usam a extensão `.py`, mas descrevem fluxos e regras de negócio em vez de executar testes automatizados.

## Casos contemplados

| Caso de uso | Descrição | Arquivo |
| --- | --- | --- |
| UC001 | Manter Ordem de Serviço | [test_uc001_manter_ordem_servico.py](test_uc001_manter_ordem_servico.py) |
| UC002 | Consultar, filtrar e exportar Ordens de Serviço | [test_uc002_consultar_filtrar_exportar.py](test_uc002_consultar_filtrar_exportar.py) |
| UC003 | Visualizar detalhes da OS e consultar a conta associada | [test_uc003_detalhes_conta.py](test_uc003_detalhes_conta.py) |
| UC004 | Visualizar ativos associados à Ordem de Serviço | [test_uc004_ativos_associados.py](test_uc004_ativos_associados.py) |
| UC005 | Confirmar ou cancelar a alteração de status da OS | [test_uc005_confirmacao_status.py](test_uc005_confirmacao_status.py) |
| UC006 | Exportar o PDF individual de uma Ordem de Serviço | [test_uc006_exportacao_individual.py](test_uc006_exportacao_individual.py) |
| UC007 | Consultar indicadores e acessar listagens pela Gestão rápida | [test_uc007_gestao_rapida.py](test_uc007_gestao_rapida.py) |

## Como ler os cenários

Cada cenário apresenta contexto e pré-condições, seguidos por um fluxo principal `[FP]`, fluxos alternativos `[A1]`, `[A2]` etc. e regras de negócio `[RN1]`, `[RN2]` etc. A numeração dos passos recomeça em 1 em cada fluxo. As referências entre colchetes nos passos apontam para variações ou regras descritas no mesmo arquivo.

Volte ao [README principal](../README.md) para a visão geral do repositório.
