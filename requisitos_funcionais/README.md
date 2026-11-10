# Requisitos funcionais

Este diretório reúne a documentação dos requisitos do módulo de Gestão de Ordens de Serviço do BVapp.

## Navegação

- [README principal](../README.md)
- [Cenários de testes](../functional_tests/README.md)
- [Arquivo de requisitos completo](requisitos-funcionais.md)

## Requisitos principais

| Código | Requisito | Cenário |
| --- | --- | --- |
| RF02001 | Cadastro de ordem de serviço | [UC001 - Manter ordem de serviço](../functional_tests/test_uc001_manter_ordem_servico.py) |
| RF02002 | Consulta de ordens de serviço | [UC004 - Consultar, filtrar e exportar](../functional_tests/test_uc004_consultar_filtrar_exportar.py) |
| RF02003 | Busca e filtros de ordens de serviço | [UC004 - Consultar, filtrar e exportar](../functional_tests/test_uc004_consultar_filtrar_exportar.py) |
| RF02004 | Visualização detalhada de ordem de serviço | [UC005 - Detalhes da conta](../functional_tests/test_uc005_detalhes_conta.py) e [UC006 - Ativos associados](../functional_tests/test_uc006_ativos_associados.py) |
| RF02005 | Edição de ordem de serviço | [UC001 - Manter ordem de serviço](../functional_tests/test_uc001_manter_ordem_servico.py) |
| RF02006 | Atualização de status da ordem de serviço | [UC007 - Confirmação de status](../functional_tests/test_uc007_confirmacao_status.py) |
| RF02007 | Remoção de ordem de serviço | [UC003 - Cancelamentos CRUD](../functional_tests/test_uc003_cancelamentos_crud.py) |
| RF02008 | Exportação da lista de ordens de serviço | [UC004 - Consultar, filtrar e exportar](../functional_tests/test_uc004_consultar_filtrar_exportar.py) |
| RF02009 | Exportação individual de ordem de serviço | [UC008 - Exportação individual](../functional_tests/test_uc008_exportacao_individual.py) |

## Fonte

O detalhamento completo está em [requisitos-funcionais.md](requisitos-funcionais.md), que descreve as histórias de usuário e as regras de negócio associadas aos cenários de teste.
