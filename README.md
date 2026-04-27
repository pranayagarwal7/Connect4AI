# Connect 4 AI

Python Connect Four with a minimax AI. Runs in the browser via Streamlit or on the desktop via Pygame.

---

## Running it

### Browser

```bash
streamlit run app.py
```

### Desktop (Pygame)

Two players:
```bash
python connect4.py
```

vs AI:
```bash
python connect4_with_ai.py
```

---

## Setup

```bash
git clone https://github.com/pranayagarwal7/Connect4AI.git
cd Connect4AI
pip install -r requirements.txt
```

For Pygame desktop mode, install the extra dep:
```bash
pip install -r requirements-desktop.txt
```

---

## How the AI works

Minimax with alpha-beta pruning at depth 5. It scores every 4-cell window across rows, columns, and diagonals, with extra weight on center-column control. Alpha-beta prunes branches that can't change the result, so it stays fast.

---

## Technologies

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pygame](https://img.shields.io/badge/pygame-black?style=for-the-badge&logo=pygame&logoColor=white)

</div>

<div align="center">

![Minimax](https://img.shields.io/badge/Algorithm-Minimax-red?style=for-the-badge)
![Alpha-Beta](https://img.shields.io/badge/Pruning-Alpha--Beta-orange?style=for-the-badge)
![Game Dev](https://img.shields.io/badge/Domain-Game%20Dev-blue?style=for-the-badge)

</div>

---

## What's next

v2 will probably replace the hand-coded scoring with a small neural network. Generate self-play games, collect board states and outcomes, train a few dense layers in scikit-learn or PyTorch to predict the best column, drop it in where the minimax scorer lives. Same board, same UI.

---

## License

MIT

---

*I've only beaten the AI 3 times out of 10. Think you can do better?*
