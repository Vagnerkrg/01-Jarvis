# AI Engineering Learning OS

# Official Development Environment

## Ambiente Oficial de Desenvolvimento


---

# Document Control


| Campo | Valor |
|---|---|
| Documento | 005_DEVELOPMENT_ENVIRONMENT.md |
| Categoria | Engenharia do Sistema |
| Tipo | Development Specification |
| Status | Official |
| Versão | 1.0 |
| Controle | Manual |
| Autor | Vagner Ferreira |
| Criado em | 2026-08-04 |


---

# Histórico de Versões


| Versão | Data | Descrição |
|---|---|---|
| 1.0 | 2026-08-04 | Primeira especificação oficial do ambiente de desenvolvimento |


---

# 1. Introduction


O AI Engineering Learning OS será desenvolvido como um sistema de engenharia de longo prazo.


Para garantir evolução consistente, o ambiente de desenvolvimento deve possuir:


- padronização;
- documentação;
- reprodutibilidade;
- isolamento;
- controle de dependências.


Este documento define o ambiente oficial utilizado para desenvolver, testar e evoluir o sistema.


---

# 2. Relationship With Architecture


O documento:



003_PROJECT_ARCHITECTURE.md



define:



Como o sistema funciona.



O documento:



004_REPOSITORY_STRUCTURE.md



define:



Onde cada componente vive.



Este documento define:



Como o ambiente executa esse sistema.



---

# 3. Environment Philosophy


O ambiente do projeto segue quatro princípios:


---

# 3.1 Reproducibility First


Qualquer ambiente deve conseguir reproduzir:



Código

Dependências

Configurações

Execução



O objetivo é evitar:



Funciona apenas na minha máquina.



---

# 3.2 Isolation


O desenvolvimento deve ocorrer em ambientes isolados.


Exemplo:



Project Environment

    ↓

Virtual Environment

    ↓

Project Dependencies



---

# 3.3 Explicit Dependencies


Toda dependência deve ser declarada.


Evitar:



Dependência instalada manualmente

Sem registro



Preferir:



requirements.txt

pyproject.toml

lock files



---

# 3.4 Automation Over Manual Setup


Sempre que possível:


Processos repetitivos devem ser automatizados.


Exemplo:



Environment Creation

Dependency Installation

Testing

Validation



---

# 4. Development Environment Goals


O ambiente deve permitir:


- desenvolvimento local;
- execução de testes;
- experimentação controlada;
- integração contínua;
- reprodução futura.


---

# 5. Official Environment Model


O modelo oficial:



Operating System

    ↓

Python Runtime

    ↓

Virtual Environment

    ↓

Dependencies

    ↓

Project Code

    ↓

Execution



---

# 6. Supported Development Platforms


O ambiente deve priorizar:


## Primary Platform



Windows



Motivo:


Ambiente principal de desenvolvimento inicial.


---

## Secondary Platforms


Suporte futuro:



Linux

macOS

Docker Environment

Cloud Environment



---

# 7. Development Environment Principle


A arquitetura não deve depender de uma máquina específica.


O ambiente deve permitir:



Novo Computador

    ↓

Setup Documentado

    ↓

Ambiente Funcional

    ↓

Projeto Executando



---

# 8. Environment Ownership


O ambiente pertence ao projeto.


Não deve depender:


- de configurações pessoais;
- instalações globais;
- caminhos fixos;
- ferramentas não documentadas.


---

# 9. Final Definition


O ambiente oficial do AI Engineering Learning OS é:



Um ambiente isolado, documentado e reproduzível,
capaz de suportar desenvolvimento, testes,
experimentação e evolução contínua do sistema.

# 10. Python Environment

## Ambiente Python Oficial


Python será a linguagem principal de desenvolvimento do AI Engineering Learning OS.


A escolha segue os objetivos do projeto:


- desenvolvimento de sistemas de IA;
- integração com modelos de linguagem;
- processamento de dados;
- automação;
- desenvolvimento de agentes.


---

# 11. Python Version Strategy


O projeto deve utilizar versões estáveis e suportadas do Python.


Versão inicial definida:



Python 3.12+



---

# 12. Python Compatibility


O código deve buscar compatibilidade dentro da versão principal definida.


Exemplo:



Python 3.12

    ↓

Python 3.13 (futuro)



Migrações de versão devem ser planejadas.


---

# 13. Python Environment Rules


O desenvolvimento deve seguir:



One Project

    ↓

One Environment

    ↓

Controlled Dependencies



---

# 14. Virtual Environment Strategy


## Estratégia de Ambiente Virtual


Cada instalação do AI Engineering Learning OS deve possuir um ambiente isolado.


O padrão oficial:



venv



---

# 15. Virtual Environment Structure


Estrutura esperada:



ai-engineering-learning-os/

│
├── .venv/

│
├── app/

├── core/

├── agents/

└── requirements/



---

# 16. Virtual Environment Purpose


O ambiente virtual é responsável por:


- isolar dependências;
- evitar conflitos;
- garantir versões corretas;
- facilitar reprodução.


---

# 17. Environment Activation


Exemplo Windows:


```powershell
.\.venv\Scripts\activate
``` id="q5m8vx"


Exemplo Linux/macOS:


```bash
source .venv/bin/activate
``` id="v7k3mp"


---

# 18. Environment Isolation Rule


Dependências do projeto nunca devem ser instaladas globalmente.


Evitar:



pip install package

fora do ambiente



Preferir:



ativar ambiente

↓

instalar dependências



---

# 19. Dependency Management


## Gerenciamento de Dependências


Todas as dependências devem possuir controle explícito.


---

# 20. Dependency Sources


O projeto poderá utilizar:



requirements.txt

    ou

pyproject.toml



A escolha depende da maturidade da fase do projeto.


---

# 21. Initial Dependency Strategy


Na fase inicial:


Utilizar:



requirements.txt



Motivo:


- simplicidade;
- fácil reprodução;
- compatibilidade ampla.


---

# 22. Future Dependency Strategy


Com o crescimento do projeto:


Migrar para:



pyproject.toml

Dependency Lock



Possibilitando:


- melhor gerenciamento;
- versionamento mais preciso;
- pacotes internos.


---

# 23. Dependency Organization


Dependências devem ser organizadas por finalidade.


Exemplo futuro:



requirements/

├── base.txt

├── development.txt

├── testing.txt

├── production.txt



---

# 24. Dependency Categories


## Base Dependencies


Dependências necessárias para execução:


Exemplo:



Runtime

Models

Core Libraries



---

## Development Dependencies


Ferramentas de desenvolvimento:


Exemplo:



Formatting

Linting

Debugging



---

## Testing Dependencies


Ferramentas de qualidade:


Exemplo:



pytest

coverage

evaluation tools



---

# 25. Version Pinning


Dependências importantes devem possuir versões controladas.


Exemplo:


```text
package==version

``` id="k8v5mq"


---

# 26. Dependency Update Policy


Atualizações devem ser controladas.


Fluxo:



New Version

↓

Evaluation

↓

Testing

↓

Documentation

↓

Update



---

# 27. Avoid Dependency Explosion


Novas dependências devem responder:



Qual problema esta biblioteca resolve?



Evitar:



Instalar porque parece útil.



---

# 28. Internal Package Strategy


Com a evolução do sistema:


Componentes internos poderão se tornar pacotes próprios.


Exemplo:



core

runtime

agents

skills



---

# 29. Environment Reproducibility


Um novo ambiente deve conseguir:



Clone Repository

↓

Create Environment

↓

Install Dependencies

↓

Run Validation

↓

Execute System



---

# 30. Environment Validation


Após criação do ambiente:


Deve ser possível validar:



Python Version

Installed Packages

Tests

Basic Execution



---

# 31. Final Environment Principle


O ambiente Python do AI Engineering Learning OS deve ser:



Isolado

Versionado

Reproduzível

Documentado



A infraestrutura de desenvolvimento deve ser tão organizada quanto o próprio sistema que ela suporta.

# 32. Configuration Management

## Gerenciamento de Configuração


O AI Engineering Learning OS deve separar completamente configuração e implementação.


Configurações não devem estar espalhadas pelo código.


---

# 33. Configuration Principle


O sistema segue:



Code

Configuration

Environment

=

Runtime Behavior



---

# 34. Configuration Objectives


O gerenciamento de configuração deve permitir:


- alteração de comportamento sem modificar código;
- múltiplos ambientes;
- controle de versões;
- fácil manutenção;
- segurança.


---

# 35. Configuration Layers


A configuração será organizada em camadas:



Global Configuration

    ↓

Environment Configuration

    ↓

Component Configuration

    ↓

Runtime Configuration



---

# 36. Global Configuration


Responsável por configurações gerais do sistema.


Exemplos:



Project Name

Version

Default Settings

System Limits



Localização:



config/system.yaml



---

# 37. Environment Configuration


Responsável por diferenças entre ambientes.


Ambientes oficiais:



development

testing

production



Exemplo:



config/

├── development.yaml

├── testing.yaml

└── production.yaml



---

# 38. Component Configuration


Cada componente pode possuir configuração própria.


Exemplos:



Agent Configuration

Model Configuration

Tool Configuration

Memory Configuration



---

# 39. Runtime Configuration


Define comportamento de execução.


Exemplos:



Timeouts

Retries

Limits

Execution Parameters



---

# 40. Configuration Format


O formato preferencial:



YAML



Motivos:


- legibilidade;
- fácil manutenção;
- adequado para configurações hierárquicas.


---

# 41. Configuration Example


Exemplo:


```yaml
runtime:

  max_tokens: 4096

  timeout: 30


model:

  provider: default

  temperature: 0.7

``` id="z9m4qx"


---

# 42. Environment Variables


## Variáveis de Ambiente


Informações sensíveis ou específicas do ambiente devem utilizar variáveis de ambiente.


---

# 43. Uso de Environment Variables


Devem armazenar:


- API keys;
- tokens;
- credenciais;
- caminhos específicos;
- informações privadas.


---

# 44. Exemplos


```text
OPENAI_API_KEY

DATABASE_URL

VECTOR_DB_PATH

MODEL_PROVIDER

``` id="q6x8mv"


---

# 45. Arquivo .env


O desenvolvimento local poderá utilizar:



.env



Exemplo:


```env
MODEL_API_KEY=secret_value

ENVIRONMENT=development

``` id="r3k7mx"


---

# 46. Regra de Segurança do .env


O arquivo:



.env



Nunca deve ser versionado.


Deve existir:



.env.example



---

# 47. .env.example


Responsabilidade:


Documentar quais variáveis existem sem expor valores reais.


Exemplo:


```env
MODEL_API_KEY=

DATABASE_URL=

VECTOR_DB_PATH=

``` id="p7m5vx"


---

# 48. Secrets Management


## Gerenciamento de Segredos


Segredos devem possuir tratamento especial.


---

# 49. Segredos Nunca Devem Estar Em:


Evitar:



Código fonte

Arquivos públicos

Commits

Documentação

Logs



---

# 50. Segredos Devem Estar Em:


Preferencialmente:



Environment Variables

Secret Managers

Secure Storage



---

# 51. Configuration Precedence


Quando múltiplas configurações existirem:


Ordem de prioridade:



Runtime Override

    ↓

Environment Variables

    ↓

Environment Config

    ↓

Default Config



---

# 52. Configuration Validation


Toda configuração deve ser validada.


Exemplo:



Config Loading

↓

Schema Validation

↓

Application Start



---

# 53. Invalid Configuration


Configuração inválida deve:


- impedir execução insegura;
- gerar erro claro;
- registrar motivo.


---

# 54. Configuration Schema


Configurações importantes devem possuir schema.


Exemplo:



config/

├── schemas/

│

└── model_config.schema.yaml



---

# 55. Environment Profiles


Cada ambiente possui um objetivo.


---

## Development


Foco:



Experimentação

Debug

Velocidade



---

## Testing


Foco:



Validação

Repetibilidade

Automação



---

## Production


Foco:



Estabilidade

Segurança

Performance



---

# 56. Configuration Documentation


Toda configuração relevante deve possuir:


- descrição;
- valor esperado;
- impacto;
- exemplo.


---

# 57. Final Configuration Principle


O AI Engineering Learning OS deve seguir:



Código limpo

Configuração externa

Segredos protegidos

Ambientes separados

=

Sistema Controlável



A configuração deve permitir evolução do sistema sem alterar sua estrutura fundamental.

# 58. Development Tools

## Ferramentas Oficiais de Desenvolvimento


O AI Engineering Learning OS utilizará um conjunto padronizado de ferramentas para:


- desenvolvimento;
- manutenção;
- qualidade;
- análise;
- automação.


---

# 59. Development Tool Philosophy


As ferramentas devem:


- reduzir erros humanos;
- aumentar produtividade;
- manter padrões;
- facilitar colaboração.


---

# 60. Official Development Environment


O ambiente recomendado:



Operating System

    ↓

VS Code

    ↓

Python Environment

    ↓

Git

    ↓

Quality Tools

    ↓

Testing Tools



---

# 61. IDE Standard


## Editor Oficial


O editor recomendado:



Visual Studio Code



Motivos:


- amplo suporte Python;
- integração Git;
- extensibilidade;
- comunidade;
- suporte para IA.


---

# 62. IDE Configuration


Configurações importantes:



.vscode/

├── settings.json

├── extensions.json

└── launch.json



---

# 63. Workspace Settings


O projeto deve manter configurações compartilhadas.


Exemplos:


```json
{
    "editor.formatOnSave": true,
    "python.testing.pytestEnabled": true
}

``` id="x7m3kv"


---

# 64. Recommended Extensions


Extensões recomendadas:


## Python Development



Python

Pylance

Python Debugger



---

## Git Integration



GitLens

GitHub Pull Requests



---

## Documentation



Markdown All in One

Markdown Preview Enhanced



---

# 65. Code Formatting


## Padronização de Formatação


O código deve possuir formatação automática.


Ferramenta inicial:



Black



---

Objetivo:


Garantir:


- estilo consistente;
- menor discussão estética;
- código previsível.


---

# 66. Import Organization


Ferramenta:



isort



Responsabilidade:


Organizar imports automaticamente.


---

# 67. Code Linting


## Análise Estática


Ferramenta recomendada:



Ruff



Responsabilidades:


- detectar problemas;
- verificar padrões;
- melhorar qualidade.


---

# 68. Type Checking


O projeto deve utilizar tipagem estática quando possível.


Ferramenta:



mypy



Exemplo:


```python
def load_agent(name: str) -> Agent:
    pass

``` id="t6m9qx"


---

# 69. Testing Tools


Ferramenta oficial:



pytest



Responsável por:


- testes unitários;
- testes de integração;
- automação.


---

# 70. Coverage Analysis


A cobertura de testes deve ser acompanhada.


Ferramenta:



pytest-cov



Objetivo:


Identificar:


- áreas sem validação;
- regressões;
- riscos.


---

# 71. Pre-commit Hooks


## Automação Antes do Commit


O projeto poderá utilizar:



pre-commit



Para executar automaticamente:



Formatting

Linting

Basic Validation



---

# 72. Code Quality Pipeline


Fluxo:



Developer

↓

Save Code

↓

Formatter

↓

Lint

↓

Tests

↓

Commit



---

# 73. Debugging Environment


O ambiente deve permitir:


- execução passo a passo;
- inspeção de variáveis;
- análise de erros.


Ferramentas:



Python Debugger

VS Code Debugger

Logging System



---

# 74. Logging During Development


Durante desenvolvimento:


Logs devem auxiliar:


- diagnóstico;
- entendimento;
- evolução.


Evitar:



print()



Preferir:



logging



---

# 75. Documentation Tools


Documentação deve utilizar:



Markdown



Ferramentas futuras:



MkDocs

Sphinx



---

# 76. Notebook Usage Policy


Notebooks são permitidos apenas para:


- exploração;
- análise;
- experimentos.


Não devem conter:


- lógica principal;
- componentes oficiais;
- pipelines de produção.


---

# 77. AI Development Tools


Ferramentas de IA podem ser utilizadas como apoio:


Exemplos:



Code Assistance

Documentation Assistance

Research Assistance

Testing Assistance



Porém:


A arquitetura e decisões continuam sendo responsabilidade humana.


---

# 78. Tool Selection Principle


Uma nova ferramenta deve responder:



Qual problema ela resolve?



Não adicionar ferramentas sem necessidade.


---

# 79. Final Development Tools Principle


O ambiente oficial deve fornecer:



Editor

Automação

Qualidade

Testes

Documentação

=

Desenvolvimento Profissional



As ferramentas existem para proteger a arquitetura e acelerar a evolução do sistema.

# 80. Testing Environment

## Ambiente Oficial de Testes


Os testes fazem parte do ambiente de desenvolvimento.


O ambiente de testes deve ser:


- isolado;
- reproduzível;
- automatizável;
- confiável.


---

# 81. Testing Environment Principles


O ambiente de testes deve garantir:



Same Code

Same Dependencies

Same Configuration

=

Predictable Results



---

# 82. Test Dependencies


Dependências específicas de teste devem ser separadas.


Exemplo:



requirements/

├── base.txt

├── development.txt

└── testing.txt



---

# 83. Testing Execution


Execução padrão:


```bash
pytest

``` id="m4q8vx"


---

# 84. Test Environment Configuration


Testes devem possuir configuração própria.


Exemplo:



config/testing.yaml



Permitindo:


- bancos temporários;
- modelos de teste;
- dados simulados.


---

# 85. Mock and Simulation Strategy


Componentes externos devem utilizar simulações quando necessário.


Exemplos:



External API

↓

Mock Service

LLM Provider

↓

Test Model



---

# 86. Documentation Environment


## Ambiente de Documentação


A documentação é parte oficial do sistema.


---

# 87. Documentation Structure


Documentação deve permanecer organizada:



docs/

├── architecture/

├── decisions/

├── guides/

├── references/

└── tutorials/



---

# 88. Documentation Standards


Documentos devem possuir:


- título;
- objetivo;
- contexto;
- versão;
- histórico quando necessário.


---

# 89. Markdown Standard


Formato oficial:



Markdown (.md)



Motivos:


- simples;
- versionável;
- compatível com Git;
- legível.


---

# 90. Local Setup Process


## Processo Oficial de Instalação


Um novo ambiente deve seguir:



Clone Repository

    ↓

Create Virtual Environment

    ↓

Install Dependencies

    ↓

Configure Environment Variables

    ↓

Validate Installation

    ↓

Run Application



---

# 91. Repository Clone


Exemplo:


```bash
git clone repository-url

cd ai-engineering-learning-os

``` id="x9k5mz"


---

# 92. Create Environment


Windows:


```powershell
python -m venv .venv

``` id="q4m8vx"


Linux/macOS:


```bash
python3 -m venv .venv

``` id="z7p3mq"


---

# 93. Activate Environment


Windows:


```powershell
.\.venv\Scripts\activate

``` id="n5m8qx"


Linux/macOS:


```bash
source .venv/bin/activate

``` id="r8k4mv"


---

# 94. Install Dependencies


Exemplo:


```bash
pip install -r requirements.txt

``` id="h6m3qp"


---

# 95. Environment Configuration


Criar:



.env



Baseado em:



.env.example



---

# 96. Validate Installation


Após instalação:


Executar:


```bash
python --version

``` id="p5m8qx"


e:


```bash
pytest

``` id="x3k7mv"


---

# 97. First System Execution


A primeira execução deve validar:



Configuration Loading

↓

Core Initialization

↓

Runtime Availability

↓

Basic Response



---

# 98. Environment Health Check


O sistema deve possuir futuramente:



scripts/health_check.py



Responsável por verificar:


- versão Python;
- dependências;
- configurações;
- serviços necessários.


---

# 99. Reproducibility Strategy


A reprodução completa deve seguir:



Fresh Machine

↓

Repository Clone

↓

Environment Creation

↓

Dependencies Install

↓

Validation

↓

Execution



---

# 100. Troubleshooting Strategy


Problemas comuns devem possuir documentação:


Local:



docs/troubleshooting/



Incluindo:


- erros conhecidos;
- soluções;
- comandos úteis.


---

# 101. Future Environment Evolution


O ambiente poderá evoluir para:



Local Development

    ↓

Docker Environment

    ↓

Cloud Environment

    ↓

Distributed Environment



---

# 102. Containerization Strategy


Futuro:



Docker



Objetivos:


- isolamento completo;
- implantação simplificada;
- ambientes consistentes.


---

# 103. Cloud Development Strategy


Possível evolução:



Cloud Workspaces

CI Environments

Remote Development



---

# 104. Environment Governance


Mudanças importantes no ambiente devem registrar:


- motivo;
- impacto;
- documentação;
- validação.


---

# 105. Final Environment Principle


O ambiente do AI Engineering Learning OS deve ser:



Reproduzível

Seguro

Automatizado

Documentado

Evolutivo



---

# 106. Conclusão do Documento


O ambiente oficial estabelece a base operacional para construção do sistema.


A arquitetura define o sistema.


O repositório organiza o sistema.


O ambiente permite executar e evoluir o sistema.


---

# Documento Finalizado


Documento:



005_DEVELOPMENT_ENVIRONMENT.md



Status:



Official Development Environment Specification

Version 1.0



Categoria:



Engenharia do Sistema



---

A Fundação do AI Engineering Learning OS agora possui:



001_PROJECT_MANIFESTO.md

    ↓

Identidade

002_PROJECT_ROADMAP.md

    ↓

Planejamento

003_PROJECT_ARCHITECTURE.md

    ↓

Arquitetura Oficial

004_REPOSITORY_STRUCTURE.md

    ↓

Estrutura Física

005_DEVELOPMENT_ENVIRONMENT.md

    ↓

Ambiente Oficial


---