# 🐦 Flappy Bird Clone

Um clone do clássico jogo Flappy Bird desenvolvido em Python com Pygame, incluindo sistema completo de sons e efeitos sonoros!

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.5+-green?logo=pygame&logoColor=white)

---

## 🎮 Sobre o Jogo

Ajude o pássaro amarelo a voar entre os canos verdes sem colidir! Cada cano que você passar aumenta sua pontuação. Desafie-se e tente bater seu próprio recorde!

### ✨ Funcionalidades

- ✅ **Física realista** com gravidade e momentum
- ✅ **Sistema de pontuação** com recorde da sessão
- ✅ **Efeitos sonoros completos**:
  - 🔊 Som de pulo/voo
  - 💥 Som de colisão
  - ⭐ Som ao marcar pontos
  - 🎵 Música de fundo (opcional)
- ✅ **Geração procedural** de obstáculos
- ✅ **Animação de chão** infinito
- ✅ **Telas de início e game over**
- ✅ **Controle de áudio** (ligar/desligar música)

---

## 🎯 Como Jogar

### Controles

| Tecla | Ação |
|-------|------|
| **ESPAÇO** | Fazer o pássaro pular |
| **M** | Ligar/Desligar música de fundo |
| **ESC** | Sair do jogo |

### Objetivo

- Navegue pelos canos sem colidir
- Cada cano passado = 1 ponto
- Não bata no chão ou no teto
- Tente bater seu recorde!

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.11 ou superior
- Pygame 2.5 ou superior

### Instalação

1. **Clone o repositório**:
```bash
git clone https://github.com/AllysonGS/flappy-bird-clone.git
cd flappy-bird-clone
```

2. **Instale as dependências**:
```bash
pip install pygame
```

3. **Execute o jogo**:
```bash
python game.py
```

---

## 🔊 Sobre os Sons

O jogo inclui um sistema completo de áudio com:
- **Som de pulo** - Toca quando você pressiona ESPAÇO
- **Som de colisão** - Toca ao bater em obstáculos
- **Som de ponto** - Toca ao passar por um cano
- **Música de fundo** - Toca em loop durante o jogo

### Substituindo os Sons (Opcional)

Se quiser personalizar os sons do jogo:

1. Baixe seus próprios sons de sites como:
   - [Freesound.org](https://freesound.org)
   - [Mixkit.co](https://mixkit.co/free-sound-effects/)
   - [Zapsplat.com](https://zapsplat.com)

2. Substitua os arquivos na pasta `assets/sounds/`:
   - `jump.wav` ou `jump.mp3`
   - `hit.wav` ou `hit.mp3`
   - `point.wav` ou `point.mp3`
   - `background.mp3` (opcional)

3. O jogo aceita tanto `.wav` quanto `.mp3`

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+** - Linguagem de programação
- **Pygame 2.5+** - Biblioteca para desenvolvimento de jogos
- **Git/GitHub** - Controle de versão

---

## 📂 Estrutura do Projeto

```
flappy-bird-clone/
├── assets/
│   └── sounds/
│       ├── jump.wav          # Som de pulo
│       ├── hit.wav           # Som de colisão
│       ├── point.wav         # Som de pontuação
│       └── background.mp3    # Música de fundo
├── game.py                   # Código principal do jogo
├── README.md                 # Documentação
└── .gitignore               # Arquivos ignorados pelo Git
```
---

## 🎓 Aprendizados

Este projeto foi desenvolvido como forma de aprendizado e prática de:
- Programação orientada a objetos em Python
- Desenvolvimento de jogos com Pygame
- Lógica de física e colisões
- Gerenciamento de áudio e recursos
- Controle de versão com Git/GitHub
- Documentação de projetos

---

## 👤 Autor

**Allyson** - [GitHub](https://github.com/AllysonGS)

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests

---

## 📸 Preview

<img width="380" height="625" alt="image" src="https://github.com/user-attachments/assets/d1411203-7363-482e-9578-3e6fe6dbb8a4" />


---

⭐ Se você gostou deste projeto, considere dar uma estrela no repositório!

**Divirta-se jogando!** �
