# Fundamentos de Cibersegurança (Security Basics)

Este documento contém os conceitos fundamentais de segurança da informação e AppSec que o agente utiliza como base de conhecimento para orientar estudantes e desenvolvedores.

---

## 1. Tríade CIA (Os Pilares da Segurança da Informação)

Toda análise de segurança e classificação de risco avalia o impacto em pelo menos um dos três pilares da Tríade CIA:

* **Confidencialidade (Confidentiality):** Garantir que a informação seja acessível apenas por pessoas ou sistemas devidamente autorizados.
  * *Exemplo de violação:* Vazamento de credenciais, acesso público a bancos de dados ou diretórios confidenciais (`/ftp`, backups).
* **Integridade (Integrity):** Assegurar que os dados, sistemas e mensagens não sejam modificados ou destruídos de forma não autorizada ou acidental.
  * *Exemplo de violação:* Injeção de SQL que altera saldos, manipulação de parâmetros em requisições (IDOR/BOLA).
* **Disponibilidade (Availability):** Garantir que os sistemas, redes e aplicações estejam disponíveis para os usuários legítimos sempre que necessário.
  * *Exemplo de violação:* Ataques de Negação de Serviço (DoS/DDoS), travamento de banco por comandos maliciosos ou loops infinitos.

---

## 2. Diferença entre Vulnerabilidade, Ameaça e Risco

Para uma análise profissional, nunca confunda esses três termos:

* **Vulnerabilidade (Falha / Brecha):** Uma fraqueza no projeto, código ou configuração do sistema.
  * *Exemplo:* Falta de sanitização em um formulário que concatena strings em consulta SQL (CWE-89).
* **Ameaça (Agente / Vetor):** Qualquer evento ou agente capaz de explorar uma vulnerabilidade para causar dano.
  * *Exemplo:* Um atacante mal-intencionado automatizando injeções SQL na internet.
* **Risco (Impacto no Negócio):** A probabilidade de uma ameaça explorar com sucesso uma vulnerabilidade multiplicada pelo impacto financeiro, operacional e reputacional que isso causa.
  $$\text{Risco} = \text{Probabilidade} \times \text{Impacto}$$

---

## 3. Matriz Geral de Severidade (Padrão CVSS v3.1)

Os achados em auditorias e testes ofensivos são classificados em 4 níveis de severidade:

| Severidade | Pontuação CVSS | Descrição e Ação |
|:---|:---:|:---|
| 🔴 **Crítica** | 9.0 – 10.0 | Permite execução remota de código (RCE), acesso irrestrito ao banco ou controle total do servidor sem autenticação prévia. **Correção imediata prioritária.** |
| 🟠 **Alta** | 7.0 – 8.9 | Vazamento de dados sensíveis, escalada vertical de privilégios ou bypass de autenticação. Requer atenção urgente. |
| 🟡 **Média** | 4.0 – 6.9 | Falhas de controle de acesso parcial, Cross-Site Scripting (XSS) sob condições específicas ou vazamento de metadados internos. |
| 🟢 **Baixa / Info** | 0.1 – 3.9 | Exposição de banners de versão, informações públicas em arquivos JavaScript ou boas práticas de cabeçalhos ausentes. |

---

## 4. Referências e Padrões Globais

* **OWASP Top 10 (Open Web Application Security Project):** Guia das 10 vulnerabilidades mais críticas em aplicações web (A01 Broken Access Control, A03 Injection, A05 Security Misconfiguration, etc.).
* **CWE (Common Weakness Enumeration):** Catálogo formal de tipos de fraquezas de software (ex: CWE-89 para SQLi, CWE-78 para Command Injection).
* **MITRE ATT&CK:** Matriz global de táticas, técnicas e procedimentos (TTPs) usados por adversários reais no mundo real.
* **PTES (Penetration Testing Execution Standard):** Norma padrão que define as fases formais de um teste de invasão.

---

## 5. Boas Práticas de Código Defensivo (Defensive Coding)

1. **Nunca confie em entradas do usuário:** Trate todo dado vindo de fora como potencialmente hostil.
2. **Consultas Parametrizadas (Prepared Statements):** A única solução definitiva contra Injeção de SQL.
3. **Validação e Sanitização:** Aplique listas restritivas (*allowlists*) em vez de listas de bloqueio (*denylists*).
4. **Princípio do Menor Privilégio (Least Privilege):** Aplicações e conexões com o banco devem rodar com o mínimo de permissões necessárias.
5. **Defesa em Profundidade (Defense in Depth):** Múltiplas camadas de controle (validação no client, no backend, no banco e no WAF).
