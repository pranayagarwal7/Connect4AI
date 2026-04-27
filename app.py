import math
import streamlit as st

from src.ai import minimax
from src.board import (
    create_board, drop_piece, get_next_open_row,
    get_valid_locations, is_valid_location, winning_move,
)
from src.constants import AI, AI_PIECE, COLUMN_COUNT, PLAYER, PLAYER_PIECE, ROW_COUNT

st.set_page_config(page_title="Connect 4", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.board {
    display: grid;
    grid-template-columns: repeat(7, 64px);
    gap: 6px;
    background: #111827;
    padding: 14px;
    border-radius: 16px;
    width: fit-content;
    margin: 0 auto 8px auto;
}
.cell {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    transition: background 0.15s ease;
}
.empty  { background: #1f2937; }
.red    { background: #ef4444; box-shadow: 0 0 10px #ef444466; }
.yellow { background: #eab308; box-shadow: 0 0 10px #eab30866; }

div[data-testid="column"] button {
    background: #111827 !important;
    color: #9ca3af !important;
    border: 1px solid #374151 !important;
    border-radius: 8px !important;
    font-size: 12px !important;
    padding: 4px 0 !important;
    width: 100% !important;
    transition: all 0.15s ease !important;
}
div[data-testid="column"] button:hover {
    border-color: #6b7280 !important;
    color: #f9fafb !important;
}

.status {
    text-align: center;
    font-size: 15px;
    color: #9ca3af;
    margin: 6px 0 16px 0;
}
.winner {
    text-align: center;
    font-size: 22px;
    font-weight: 600;
    margin: 12px 0;
}
.title {
    text-align: center;
    font-size: 36px;
    font-weight: 600;
    letter-spacing: -1px;
    margin-bottom: 6px;
    color: #f9fafb;
}
.subtitle {
    text-align: center;
    color: #6b7280;
    font-size: 14px;
    margin-bottom: 40px;
}
</style>
""", unsafe_allow_html=True)


def init_game(mode):
    st.session_state.board = create_board()
    st.session_state.mode = mode
    st.session_state.turn = PLAYER
    st.session_state.game_over = False
    st.session_state.winner = None
    st.session_state.pending_col = None


def render_board(board):
    html = '<div class="board">'
    for r in range(ROW_COUNT - 1, -1, -1):
        for c in range(COLUMN_COUNT):
            val = board[r][c]
            if val == PLAYER_PIECE:
                cls = "red"
            elif val == AI_PIECE:
                cls = "yellow"
            else:
                cls = "empty"
            html += f'<div class="cell {cls}"></div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


def process_move(col):
    board = st.session_state.board
    mode = st.session_state.mode

    if not is_valid_location(board, col):
        return

    piece = PLAYER_PIECE if st.session_state.turn == PLAYER else AI_PIECE
    row = get_next_open_row(board, col)
    drop_piece(board, row, col, piece)

    if winning_move(board, piece):
        st.session_state.game_over = True
        if mode == "two_player":
            st.session_state.winner = "Player 1" if piece == PLAYER_PIECE else "Player 2"
        else:
            st.session_state.winner = "You"
        return

    if not get_valid_locations(board):
        st.session_state.game_over = True
        st.session_state.winner = None  # draw
        return

    st.session_state.turn = AI if st.session_state.turn == PLAYER else PLAYER

    if mode == "vs_ai" and st.session_state.turn == AI:
        ai_col, _ = minimax(board, 5, -math.inf, math.inf, True)
        if ai_col is not None and is_valid_location(board, ai_col):
            ai_row = get_next_open_row(board, ai_col)
            drop_piece(board, ai_row, ai_col, AI_PIECE)
            if winning_move(board, AI_PIECE):
                st.session_state.game_over = True
                st.session_state.winner = "AI"
                return
            if not get_valid_locations(board):
                st.session_state.game_over = True
                st.session_state.winner = None
                return
        st.session_state.turn = PLAYER


# ── Landing ──────────────────────────────────────────────────────────────────

if "mode" not in st.session_state:
    st.session_state.mode = None

if st.session_state.mode is None:
    st.markdown('<div class="title">Connect 4</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">drop · connect · win</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        if st.button("Two Player", use_container_width=True):
            init_game("two_player")
            st.rerun()
    with col2:
        if st.button("Play vs AI", use_container_width=True):
            init_game("vs_ai")
            st.rerun()

# ── Game ─────────────────────────────────────────────────────────────────────

else:
    if st.session_state.get("pending_col") is not None and not st.session_state.game_over:
        col = st.session_state.pending_col
        st.session_state.pending_col = None
        process_move(col)

    render_board(st.session_state.board)

    if st.session_state.game_over:
        if st.session_state.winner:
            color = "#ef4444" if st.session_state.winner in ("Player 1", "You") else "#eab308"
            st.markdown(
                f'<div class="winner" style="color:{color}">{st.session_state.winner} wins</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown('<div class="winner" style="color:#6b7280">Draw</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="small")
        with c1:
            if st.button("Play Again", use_container_width=True):
                init_game(st.session_state.mode)
                st.rerun()
        with c2:
            if st.button("Menu", use_container_width=True):
                st.session_state.mode = None
                st.rerun()
    else:
        if st.session_state.mode == "two_player":
            label = "Player 1's turn" if st.session_state.turn == PLAYER else "Player 2's turn"
        else:
            label = "Your turn"
        st.markdown(f'<div class="status">{label}</div>', unsafe_allow_html=True)

        cols = st.columns(COLUMN_COUNT, gap="small")
        for i, col in enumerate(cols):
            with col:
                if st.button("▾", key=f"col_{i}", use_container_width=True):
                    st.session_state.pending_col = i
                    st.rerun()

        if st.button("← Menu", use_container_width=False):
            st.session_state.mode = None
            st.rerun()
