import random
import pygame
import sys
import math

from src.constants import (
	BLUE, BLACK, RED, YELLOW,
	ROW_COUNT, COLUMN_COUNT,
	PLAYER, AI, PLAYER_PIECE, AI_PIECE,
	SQUARESIZE, RADIUS,
)
from src.board import (
	create_board, drop_piece, is_valid_location,
	get_next_open_row, print_board, winning_move,
)
from src.ai import minimax


def draw_board(board, screen, height):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			if board[r][c] == PLAYER_PIECE:
				pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
			elif board[r][c] == AI_PIECE:
				pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
	pygame.display.update()


board = create_board()
print_board(board)
game_over = False

pygame.init()

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
screen = pygame.display.set_mode((width, height))
draw_board(board, screen, height)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)
turn = random.randint(PLAYER, AI)

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == PLAYER:
				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
			if turn == PLAYER:
				posx = event.pos[0]
				col = int(math.floor(posx / SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, PLAYER_PIECE)

					if winning_move(board, PLAYER_PIECE):
						label = myfont.render("Player 1 wins!!", 1, RED)
						screen.blit(label, (40, 10))
						game_over = True

					turn = (turn + 1) % 2

					print_board(board)
					draw_board(board, screen, height)

	if turn == AI and not game_over:
		col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

		if is_valid_location(board, col):
			row = get_next_open_row(board, col)
			drop_piece(board, row, col, AI_PIECE)

			if winning_move(board, AI_PIECE):
				label = myfont.render("Player 2 wins!!", 1, YELLOW)
				screen.blit(label, (40, 10))
				game_over = True

			print_board(board)
			draw_board(board, screen, height)

			turn = (turn + 1) % 2

	if game_over:
		pygame.time.wait(3000)
