import pygame
import sys
from solver import generate_scramble, solve_cube

COLORS = {'W': (255, 255, 255), 'Y': (255, 255, 0), 'R': (255, 0, 0), 'O': (255, 165, 0), 'G': (0, 255, 0), 'B': (0, 0, 255)}
FACES = ['U', 'L', 'F', 'R', 'B', 'D']

def draw_face(screen, face, grid, x_offset, y_offset, size):
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, COLORS[grid[i][j]], (x_offset + j * size, y_offset + i * size, size, size))
            pygame.draw.rect(screen, (0, 0, 0), (x_offset + j * size, y_offset + i * size, size, size), 1)

def draw_cube(screen, cube, move_history, font):
    screen.fill((30, 30, 30))
    size = 30
    spacing = 5
    draw_face(screen, 'U', cube.faces['U'], 150, 50, size)
    draw_face(screen, 'L', cube.faces['L'], 50, 140, size)
    draw_face(screen, 'F', cube.faces['F'], 150, 140, size)
    draw_face(screen, 'R', cube.faces['R'], 250, 140, size)
    draw_face(screen, 'B', cube.faces['B'], 350, 140, size)
    draw_face(screen, 'D', cube.faces['D'], 150, 230, size)
    for i, move in enumerate(move_history[-10:]):
        text = font.render(move, True, (255, 255, 255))
        screen.blit(text, (500, 30 + i * 20))

def draw_buttons(screen, font):
    pygame.draw.rect(screen, (70, 130, 180), (50, 350, 100, 40))
    pygame.draw.rect(screen, (70, 180, 70), (170, 350, 100, 40))
    pygame.draw.rect(screen, (200, 50, 50), (290, 350, 100, 40))
    screen.blit(font.render("Scramble", True, (255, 255, 255)), (60, 360))
    screen.blit(font.render("Solve", True, (255, 255, 255)), (195, 360))
    screen.blit(font.render("Reset", True, (255, 255, 255)), (320, 360))

def run_visualizer(cube):
    pygame.init()
    screen = pygame.display.set_mode((640, 450))
    pygame.display.set_caption("Rubik's Cube Visualizer")
    font = pygame.font.SysFont(None, 24)
    clock = pygame.time.Clock()

    while True:
        draw_cube(screen, cube, cube.get_move_history(), font)
        draw_buttons(screen, font)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 <= x <= 150 and 350 <= y <= 390:
                    scramble = generate_scramble()
                    cube.scramble(scramble)
                elif 170 <= x <= 270 and 350 <= y <= 390:
                    solve_cube(cube)
                elif 290 <= x <= 390 and 350 <= y <= 390:
                    cube.reset()
        clock.tick(30)