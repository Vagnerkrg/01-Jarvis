# Configuração da Arquitetura

## Introdução

Este documento descreve os princípios e padrões utilizados para configuração dos componentes da arquitetura do sistema.

O objetivo é centralizar configurações, evitar valores espalhados pelo código e facilitar a manutenção e evolução do ambiente.

---

# Princípios de Configuração

A configuração do sistema deve seguir os seguintes princípios:

## Centralização

Todas as configurações importantes devem possuir um local definido.

---

## Separação de Ambiente

Configurações específicas de desenvolvimento, testes e produção devem ser isoladas.

---

## Segurança

Informações sensíveis nunca devem ser armazenadas diretamente no código.

Exemplos:

- Chaves de API.
- Tokens.
- Credenciais.
- Dados privados.

---

## Flexibilidade

A troca de modelos, providers ou parâmetros deve ocorrer sem alteração de código.

---

# Estrutura de Configuração

A estrutura esperada:

```text
config/

├── settings.yaml

├── models.yaml

├── providers.yaml

└── environments/
    │
    ├── development.yaml
    ├── testing.yaml
    └── production.yaml

    Configuração do Modelo

A configuração do modelo deve definir:

Nome do modelo.
Provider utilizado.
Parâmetros de execução.
Limites de contexto.

Exemplo:

model:
  name: modelo-local
  provider: ollama
  temperature: 0.7
  max_tokens: 2048
Configuração de Providers

Cada Provider deve possuir sua própria configuração.

Exemplo:

providers:

  ollama:
    enabled: true
    host: localhost
    port: 11434
Ambientes
Desenvolvimento

Utilizado durante implementação e testes locais.

Características:

Modelos locais.
Logs detalhados.
Ambiente controlado.
Testes

Utilizado para validação automatizada.

Características:

Configuração isolada.
Dados controlados.
Execução previsível.
Produção

Ambiente destinado ao uso final do sistema.

Características:

Configurações otimizadas.
Controle de acesso.
Monitoramento.
Integração com AI Runtime

O AI Runtime será responsável por consumir as configurações.

Fluxo:

Configuração
      │
      ▼
Model Manager
      │
      ▼
Provider
      │
      ▼
Modelo LLM
Variáveis de Ambiente

Informações sensíveis devem utilizar variáveis de ambiente.

Exemplo:

AI_MODEL=
AI_PROVIDER=
OLLAMA_HOST=
API_KEY=
Regras
Nenhuma configuração crítica deve estar espalhada pelo código.
Alterações de configuração devem ser rastreáveis.
Novos providers devem possuir documentação própria.
Modelos devem ser configuráveis.
Evolução Futura

O sistema poderá suportar:

Configuração dinâmica.
Seleção automática de modelos.
Perfis de execução.
Configurações por agente.
Configuração remota.
Referências
ai-runtime.md
components.md
communication-flow.md
ADR-001-arquitetura-da-infraestrutura-de-ia.md