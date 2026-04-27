# Connect 4 AI

***A Connect Four suite built in Python — from local two-player to AI opponent to a browser-based web interface.***

---

## Game Modes

### Streamlit Web App (recommended)
Single entry point with a mode picker in the browser.

```bash
streamlit run app.py
```

### Pygame Desktop
**Two-player (local PvP):**
```bash
python connect4.py
```
**vs AI:**
```bash
python connect4_with_ai.py
```

---

## Installation

```bash
git clone https://github.com/pranayagarwal7/Connect4AI.git
cd Connect4AI
pip install -r requirements.txt
```

---

## How the AI Works

The AI uses **Minimax with alpha-beta pruning** at depth 5.

- Scores board windows (4-cell slices) across all directions
- Prioritizes center-column control
- Blocks immediate threats and pursues winning sequences
- Alpha-beta cuts redundant branches — depth 5 runs fast enough for real-time play

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

## What's Next — v2 (Machine Learning)

Future versions will likely replace the hand-coded scoring with a simple neural network trained on game data:

- Collect board states and outcomes from many self-play games
- Train a basic neural network (e.g. a few dense layers with scikit-learn or PyTorch) to predict which column is the best move given a board state
- Swap the minimax scoring function with the trained model's prediction
- Keep everything else the same — same board logic, same Streamlit UI

---

## License

MIT

---

*Verdict: the minimax AI is tough — I've only won 3 out of 10. Think you can do better?*
