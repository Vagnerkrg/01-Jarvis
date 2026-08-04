# Testing Foundation

## Objetivo

Definir o padrão de testes automatizados do Jarvis AI Engineering Learning OS.

A suíte de testes garante que os componentes principais do sistema mantenham comportamento consistente durante a evolução do projeto.

---

## Framework

Framework principal:

- pytest

Execução:

```bash

pytest

Estrutura

Cada componente principal deve possuir um arquivo de teste correspondente:

core/router      -> tests/test_router.py
core/runtime     -> tests/test_runtime.py
core/workflow    -> tests/test_workflow.py
core/planner     -> tests/test_planner.py
Padrões de Teste

Os testes devem:

Validar comportamento público dos módulos
Cobrir fluxos principais de execução
Ser independentes entre si
Evitar dependências externas desnecessárias
Ser executados antes de qualquer alteração estrutural
Processo de Desenvolvimento

Toda nova funcionalidade deve seguir:

Criar implementação
Criar testes correspondentes
Executar suíte completa
Commitar somente com testes passando
Estado Atual

Componentes Core validados:

Request Router
Agent Runtime
Workflow Engine
Planning Engine

Resultado atual:

13 passed