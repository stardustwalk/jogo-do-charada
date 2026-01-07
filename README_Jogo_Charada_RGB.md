# 🎭 Jogo do Charada RGB

Jogo de lógica em Python baseado em charadas e percepção visual.  
O jogador deve identificar **duas informações diferentes ao mesmo tempo**:

1. A **palavra** que aparece (ex: “vermelho”, “azul”, “verde”)  
2. A **cor real do texto** em que a palavra está escrita  

Tudo isso usando **apenas uma dica**.

O jogo brinca com a confusão entre leitura e percepção de cores, inspirado no efeito Stroop.

---

## 🧠 Como o jogo funciona

- O jogo sorteia:
  - A **cor real do texto**
  - A **palavra exibida**
- Uma **charada** é apresentada como dica
- Um áudio é reproduzido para criar clima
- O jogador responde:
  1. Qual é a **palavra escrita**
  2. Qual é a **cor real do texto**
- O jogo informa se:
  - Acertou as duas
  - Acertou apenas uma
  - Errou ambas

---

## ▶️ Como executar

### Pré-requisitos
- Python 3.x
- Biblioteca `pygame`

Instale o pygame:
```bash
pip install pygame
```

Execute o jogo:
```bash
python main.py
```

---

## 📁 Estrutura do projeto
```
jogo-charadas-python/
├─ main.py
├─ riddle.ogg
└─ README.md
```

> O arquivo de áudio deve estar na mesma pasta do script para funcionar corretamente.

---

## 🔊 Áudio
O jogo utiliza um arquivo de áudio (`riddle.ogg`) reproduzido com `pygame.mixer`.  
Caso o áudio não seja encontrado ou o sistema não suporte, o jogo continua funcionando normalmente.

---

## 💻 Observações técnicas
- O jogo roda no **terminal**
- As cores do texto usam **códigos ANSI**
- Recomenda-se usar:
  - Windows Terminal
  - PowerShell moderno
  - Terminal Linux / macOS

---

## 🎯 Objetivo do projeto
Projeto autoral criado para praticar:
- Lógica de programação
- Estruturas condicionais
- Randomização
- Interação com usuário
- Uso de bibliotecas externas (pygame)
- Criatividade aplicada a jogos simples

---

## 🧪 Status
✔ Funcional  
✔ Projeto autoral  
✔ Código mantido simples, priorizando clareza e estabilidade  
