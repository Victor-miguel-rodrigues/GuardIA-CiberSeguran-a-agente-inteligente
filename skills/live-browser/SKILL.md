---
name: live-browser
description: Use quando o estudante quer abrir e inspecionar uma aplicação web em tempo real no navegador embutido no painel lateral do harness, visualizando telas, requisições e logs de laboratório lado a lado com a mentoria.
---

# Skill: Navegador Integrado em Tempo Real (Live Browser)

Esta skill orienta como utilizar o navegador embutido do harness (como no Google Antigravity) para abrir qualquer aplicação web, laboratório ou página local diretamente em um painel lateral (*Side Pane*), permitindo visualizar o que acontece em tempo real enquanto conversa com o DIO Agent.

---

## 🎯 Quando usar esta skill

Use esta skill quando:
- O estudante quer visualizar e interagir com uma aplicação web (DVWA, Juice Shop, React app, API doc, dashboard) sem sair da janela do editor.
- O estudante precisa demonstrar o que está vendo na tela para tirar dúvidas de layout, bugs visuais ou fluxo de navegação.
- Em desafios de cibersegurança e pentest, para acompanhar visualmente as requisições, respostas HTTP e renderização das páginas vulneráveis.
- Para coletar capturas de tela (screenshots) e evidências diretamente no fluxo de trabalho.

---

## 🤖 Comportamento do Agente ao detectar uma URL

Sempre que o estudante enviar um link ou IP de laboratório/projeto (ex: `http://192.168.1.7:8080`, `localhost:3000`):
1. **Gere o comando pronto para uso:** Formate em bloco de texto copiável `/browser <URL>`.
2. **Oriente a navegação em conjunto:** Explique onde clicar e o que analisar na tela enquanto o painel estiver aberto ao lado.
3. **Solicite as evidências:** Indique quando tirar o print para o relatório.

---

## 🚀 Como acionar o navegador em tempo real

### 1. Pelo comando `/browser` (Método direto e universal)
No campo de mensagem do chat, digite:
```text
/browser <URL_DO_SEU_APP>
```

**Exemplos:**
- Laboratório local de pentest (DVWA): `/browser http://192.168.1.7:8080`
- OWASP Juice Shop: `/browser http://localhost:3000`
- Projeto em desenvolvimento: `/browser http://localhost:5173`
- Documentação online: `/browser https://dio.me`

Ao enviar o comando, o harness abre uma janela de navegador acoplada ao lado direito da sua tela, exibindo a aplicação em tempo real.

### 2. Pelo ícone na barra lateral do ambiente
Se a interface do seu harness exibir o ícone de globo/navegador na barra lateral de ferramentas (Sidecar), clique nele e insira a URL desejada na barra de navegação superior do painel.

---

## 🔍 O que observar em tempo real durante os testes

Ao abrir o aplicativo na tela lateral, o estudante e o agente trabalham em dupla:

| O que você vê no navegador | O que o agente orienta |
| :--- | :--- |
| **Página inicial / Formulário** | O agente explica o propósito do formulário e quais parâmetros estão sendo enviados |
| **Mensagens de erro ou telas brancas** | O agente ajuda a diagnosticar erros de backend ou de console |
| **Respostas inesperadas (ex: PoC de injeção)** | O agente valida se a vulnerabilidade foi demonstrada e orienta o print de evidência |
| **Código-fonte da página (Inspecionar)** | O agente explica o que procurar no HTML/JS (campos ocultos, endpoints de API) |

---

## 📸 Fluxo de Coleta de Evidências

Durante projetos práticos e desafios da DIO:
1. Navegue até a tela que demonstra o resultado do seu teste.
2. Tire um print da janela lateral em tempo real (utilizando o atalho do seu sistema operacional ou ferramenta de captura).
3. Salve a imagem na pasta `docs/images/` do seu projeto.
4. Compartilhe o que observou com o agente para que ele adicione o achado no seu relatório técnico ou `README.md`.

---

## 🛡️ Dicas e Boas Práticas

- **Endereços Locais:** Para acessar aplicações rodando no seu próprio computador, certifique-se de que o servidor local está ativo antes de rodar o comando `/browser`.
- **Modo Responsivo:** Você pode redimensionar a largura do painel lateral para testar a responsividade do seu site em formato mobile ou desktop.
- **Console do Desenvolvedor:** Em ambientes que suportam DevTools integradas, use `F12` ou clique com o botão direito para inspecionar requisições da aba Network.
