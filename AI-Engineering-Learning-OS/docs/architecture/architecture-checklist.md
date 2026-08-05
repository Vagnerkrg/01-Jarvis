# Checklist de Arquitetura

## Introdução

Este documento define o checklist utilizado para validar se novas implementações seguem os padrões arquiteturais definidos no projeto.

O objetivo é garantir consistência, qualidade e evolução segura do sistema.

---

# Checklist Geral

## Estrutura

- [ ] O componente possui responsabilidade claramente definida.
- [ ] O componente está localizado no módulo correto.
- [ ] A estrutura segue os padrões do projeto.
- [ ] Os nomes seguem as convenções definidas.

---

# Arquitetura

## Princípios

- [ ] O componente respeita baixo acoplamento.
- [ ] O componente possui alta coesão.
- [ ] As dependências estão claramente definidas.
- [ ] Interfaces foram utilizadas quando necessário.

---

# Comunicação Entre Componentes

- [ ] O componente utiliza interfaces existentes.
- [ ] Não existe acesso direto a implementações internas.
- [ ] Fluxos de comunicação estão documentados.
- [ ] Responsabilidades estão separadas.

---

# Infraestrutura de IA (AI Runtime)

## Modelos

- [ ] Comunicação com modelos passa pelo AI Runtime.
- [ ] Model Manager é utilizado como ponto central.
- [ ] Providers estão isolados.
- [ ] Configurações estão externas ao código.

---

# Agentes

Antes de criar um agente:

- [ ] Objetivo do agente definido.
- [ ] Responsabilidade documentada.
- [ ] Ferramentas necessárias identificadas.
- [ ] Ciclo de vida definido.
- [ ] Testes planejados.

---

# Configuração

- [ ] Não existem valores sensíveis no código.
- [ ] Configurações estão centralizadas.
- [ ] Variáveis de ambiente são utilizadas quando necessário.
- [ ] Diferentes ambientes são considerados.

---

# Testes

- [ ] Testes unitários criados.
- [ ] Casos de erro considerados.
- [ ] Integrações críticas validadas.
- [ ] Testes executam automaticamente.

---

# Documentação

- [ ] Documento do componente criado.
- [ ] Fluxo atualizado quando necessário.
- [ ] ADR criada caso exista decisão arquitetural.
- [ ] Referências atualizadas.

---

# Versionamento

- [ ] Branch criada seguindo padrão.
- [ ] Commits seguem convenção.
- [ ] Alterações estão organizadas.
- [ ] Histórico permanece claro.

---

# Finalização de uma Entrega

Uma entrega pode ser concluída quando:

- [ ] Implementação finalizada.
- [ ] Testes passando.
- [ ] Documentação atualizada.
- [ ] Revisão arquitetural concluída.
- [ ] Issue pronta para fechamento.

---

# Referências

- development-guidelines.md
- quality-standards.md
- testing-strategy.md
- maintenance.md
- ADR-001-arquitetura-da-infraestrutura-de-ia.md