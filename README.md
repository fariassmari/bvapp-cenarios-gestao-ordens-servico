# BV App - Cenários de gestão de serviços

## Visão geral

Este repositório reúne a documentação e os cenários funcionais do módulo de Gestão de Serviços do BVapp. A intenção é manter a rastreabilidade entre requisitos, cenários e arquivos de teste, facilitando a leitura e a navegação entre os materiais da entrega.

## Navegação rápida

- [Requisitos funcionais](requisitos_funcionais/requisitos-funcionais.md)
- [README de requisitos](requisitos_funcionais/README.md)
- [Cenários de testes](functional_tests/README.md)

## Estrutura do projeto

```text
bvapp-cenarios/
├── README.md
├── requisitos_funcionais/
│   ├── README.md
│   └── requisitos-funcionais.md
├── functional_tests/
│   ├── README.md
│   ├── test_uc001_manter_ordem_servico.py
│   ├── test_uc002_autorizacao_crud.py
│   ├── test_uc003_cancelamentos_crud.py
│   ├── test_uc004_consultar_filtrar_exportar.py
│   ├── test_uc005_detalhes_conta.py
│   ├── test_uc006_ativos_associados.py
│   ├── test_uc007_confirmacao_status.py
│   ├── test_uc008_exportacao_individual.py
│   └── test_uc009_gestao_rapida.py
└── .git/
```

## Casos de uso e arquivos

| Caso | Objetivo | Arquivo |
| --- | --- | --- |
| UC001 | Manter ordem de serviço | [test_uc001_manter_ordem_servico.py](functional_tests/test_uc001_manter_ordem_servico.py) |
| UC002 | Autorização CRUD | [test_uc002_autorizacao_crud.py](functional_tests/test_uc002_autorizacao_crud.py) |
| UC003 | Cancelamentos CRUD | [test_uc003_cancelamentos_crud.py](functional_tests/test_uc003_cancelamentos_crud.py) |
| UC004 | Consultar, filtrar e exportar | [test_uc004_consultar_filtrar_exportar.py](functional_tests/test_uc004_consultar_filtrar_exportar.py) |
| UC005 | Detalhes da conta | [test_uc005_detalhes_conta.py](functional_tests/test_uc005_detalhes_conta.py) |
| UC006 | Ativos associados | [test_uc006_ativos_associados.py](functional_tests/test_uc006_ativos_associados.py) |
| UC007 | Confirmação de status | [test_uc007_confirmacao_status.py](functional_tests/test_uc007_confirmacao_status.py) |
| UC008 | Exportação individual | [test_uc008_exportacao_individual.py](functional_tests/test_uc008_exportacao_individual.py) |
| UC009 | Gestão rápida | [test_uc009_gestao_rapida.py](functional_tests/test_uc009_gestao_rapida.py) |

## Requisitos funcionais

Os requisitos do módulo são documentados em [requisitos_funcionais/requisitos-funcionais.md](requisitos_funcionais/requisitos-funcionais.md), com a organização por RF02001 a RF02009, correspondendo aos cenários de gestão de ordens de serviço desta entrega.

## Informações da atividade

- Autor: Mariana Farias de Brito
- Instituição: Instituto Federal da Paraíba - IFPB
- Disciplina: Verificação, Validação e Testes de Software
- Atividade: Mini projeto individual - N3
- Entrega: 06/11/2026

Esta entrega tem caráter documental e não executa a aplicação BVapp; o objetivo é registrar o comportamento esperado, regras de negócio e critérios de validação dos cenários.
