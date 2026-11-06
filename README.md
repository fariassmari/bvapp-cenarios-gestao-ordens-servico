# BVApp - Cenários de testes funcionais

## Contexto da atividade

Este repositório foi organizado como entrega de um mini projeto individual para a disciplina de Verificação, Validação e Testes de Software. A proposta consiste em registrar cenários documentais do módulo de Gestão de Serviços do BVapp, descrevendo os passos esperados, as condições de uso e os resultados pretendidos para cada caso.

A atividade foi desenvolvida por Mariana Farias de Brito, com foco em análise documental e validação de requisitos, sem execução da aplicação. A entrega foi pensada como uma conferência de comportamento esperado, em que os cenários funcionam como base para revisão, alinhamento e futura automação de testes.

## Informações da atividade

- Autor: Mariana Farias de Brito
- Instituição: Instituto Federal da Paraíba - IFPB
- Disciplina: Verificação, Validação e Testes de Software
- Atividade: N3 - mini projeto individual
- Entrega e apresentação: 06/11/2026

Esta entrega reúne dez cenários documentais do módulo de Gestão de Serviços do BVapp. Cada cenário descreve ações esperadas, regras de negócio e resultados pretendidos. Nenhum cenário foi executado neste repositório; a revisão é documental e focada na conferência dos fluxos esperados, sem rodar a aplicação BVapp.

## Objetivo

Este repositório reúne cenários de testes funcionais para a aplicação de gestão de Ordens de Serviço (OS) e ativos relacionados.

## Objetivo geral

Documentar e validar os principais casos de uso do sistema, cobrindo fluxos de manutenção, autorização, cancelamento, busca, detalhes, ativos associados, confirmação de status e exportação.

## Estrutura do projeto

```text
bvapp-cenarios/
├── functional_tests/
│   ├── test_uc001_manter_ordem_servico.py
│   ├── test_uc002_autorizacao_crud.py
│   ├── test_uc003_cancelamentos_crud.py
│   ├── test_uc004_busca_filtros_ordenacao.py
│   ├── test_uc005_detalhes_conta.py
│   ├── test_uc006_ativos_associados.py
│   ├── test_uc007_confirmacao_status.py
│   ├── test_uc008_exportacao_listagem.py
│   ├── test_uc009_exportacao_individual.py
│   └── test_uc010_gestao_rapida.py
└── README.md
```

## Casos de uso contemplados

- UC001 - Manter Ordem de Serviço
- UC002 - Autorização CRUD
- UC003 - Cancelamentos CRUD
- UC004 - Busca, filtros e ordenação
- UC005 - Detalhes da conta
- UC006 - Ativos associados à Ordem de Serviço
- UC007 - Confirmação de status
- UC008 - Exportação da listagem
- UC009 - Exportação individual
- UC010 - Gestão rápida

## Autor

Mariana Farias de Brito
