# Configuração do Ollama Runtime

## Introdução

Este documento descreve a instalação e configuração do Ollama como primeiro runtime oficial de Inteligência Artificial do projeto.

O Ollama será utilizado como camada inicial de execução de modelos locais, permitindo que o Copilot utilize modelos de linguagem sem dependência obrigatória de serviços externos.

---

# Objetivo

Configurar um ambiente local capaz de:

- Executar modelos de linguagem.
- Validar comunicação com modelos locais.
- Servir como base para implementação do AI Runtime.
- Permitir testes iniciais do Model Manager.

---

# Ambiente Utilizado

## Sistema Operacional

```text
Windows
Python
Python 3.12.3
Ambiente Virtual
.venv

Local:

C:\Projetos\01-Jarvis\.venv
Runtime de IA
Ollama

Versão instalada:

0.32.5

Validação:

ollama --version

Resultado:

ollama version is 0.32.5
Instalação

O Ollama foi instalado utilizando o instalador oficial para Windows.

Após a instalação, o runtime foi validado através do comando:

ollama --version
Modelo Inicial Oficial
llama3.1:8b

O primeiro modelo utilizado pelo projeto será:

llama3.1:8b

Informações:

Tamanho:
4.9 GB

Instalação:

ollama pull llama3.1:8b

Validação:

ollama list

Resultado esperado:

NAME           SIZE

llama3.1:8b    4.9 GB
Execução do Modelo

Para iniciar uma sessão utilizando o modelo:

ollama run llama3.1:8b

Exemplo de teste realizado:

Você é o primeiro modelo de IA integrado ao meu Copilot pessoal. Explique em uma frase qual é sua função.

Resposta obtida:

Meu objetivo é fornecer suporte e sugestões para melhorar seu código,
ajudando-o a criar soluções mais eficientes e escaláveis através da análise
do conteúdo e das regras de programação subjacentes.
Arquitetura Atual

Neste momento, o fluxo validado é:

Usuário

   │

   ▼

Terminal

   │

   ▼

Ollama Runtime

   │

   ▼

llama3.1:8b

   │

   ▼

Resposta do Modelo
Próxima Evolução

O Ollama será integrado futuramente através da camada:

AI Runtime

Fluxo planejado:

Copilot

   │

   ▼

AI Runtime

   │

   ▼

Model Manager

   │

   ▼

Ollama Provider

   │

   ▼

llama3.1:8b
Próximos Passos
Implementar Model Manager.
Criar Provider Ollama.
Criar interface de comunicação com modelos.
Adicionar testes de integração.
Permitir troca futura de providers.
Referências
ADR-001-arquitetura-da-infraestrutura-de-ia.md
ai-runtime.md
components.md
communication-flow.md