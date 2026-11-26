# 🛡️ Skill: Scope Guard (Validador de Escopo & Conformidade)

Esta skill protege o estudante e o pesquisador de segurança contra testes indevidos, garantindo conformidade legal e aderência estrita às regras de programas de Bug Bounty.

---

## 🎯 Por que esta skill existe?

No mundo da cibersegurança, **testar sem escopo ou fora dos limites é crime ou motivo de banimento imediato** em plataformas como Bugcrowd, HackerOne e Intigriti.

Como cada programa de Bug Bounty possui políticas exclusivas (alguns permitem APIs, outros proíbem subdomínios, alguns vetam testes de rate limit), o **Scope Guard** atua como uma camada inteligente de proteção:
* Se o ambiente for seu (laboratório, localhost, VPS própria): basta enviar o link. O agente libera os testes permitidos sem burocracia.
* Se for um programa de Bug Bounty: você cola o escopo do programa. O agente extrai o que é permitido (**In-Scope**), o que é proibido (**Out-of-Scope**) e impede que você cometa erros graves que possam queimar sua reputação.

---

## 🚀 Como usar

### 1. Para sites ou laboratórios próprios:
Envie simplesmente:
> *"Esse site é meu laboratório local: http://localhost:3000"*

### 2. Para programas de Bug Bounty:
Cole o escopo ou use o prompt:
> *"Estou no programa da [Empresa] no Bugcrowd. Aqui está o escopo: [cole a lista de alvos e regras]. Quero analisar o alvo [domínio]."*

O agente analisa a política, confirma se o alvo é elegível e instrui testes 100% aderentes às regras de engajamento.
