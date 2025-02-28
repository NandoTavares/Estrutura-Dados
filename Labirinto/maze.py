import pygame
import numpy as np
import csv
import random
import threading
from collections import deque

class Maze:

    WALL = 0
    HALL = 1
    PLAYER = 2
    PRIZE = 3
    
    def __init__(self):
        self.M = None  # matriz que representa o labirinto
        pygame.init()
    
    def load_from_csv(self, file_path: str):
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            self.M = np.array([list(map(int, row)) for row in reader])
            
    def init_player(self):
        while True:
            posx, posy = random.randint(2, 39), random.randint(2, 39)
            if self.M[posx, posy] == Maze.HALL:
                self.init_pos_player = (posx, posy)
                break
        while True:
            posx, posy = random.randint(2, 39), random.randint(2, 39)
            if self.M[posx, posy] == Maze.HALL:
                self.M[posx, posy] = Maze.PRIZE
                break
    
    def find_prize(self, pos: (int, int)) -> bool:
        return self.M[pos[0], pos[1]] == Maze.PRIZE
    
    def is_free(self, pos: (int, int)) -> bool:
        return self.M[pos[0], pos[1]] in [Maze.HALL, Maze.PRIZE]
    
    def mov_player(self, pos: (int, int)) -> None:
        if self.M[pos[0], pos[1]] == Maze.HALL:
            self.M[pos[0], pos[1]] = Maze.PLAYER
    
    def get_init_pos_player(self) -> (int, int):
        return self.init_pos_player
    
    def solve_backtracking(self, start: (int, int)) -> bool:
        stack = deque([start])
        visitado = set()
        movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
        while stack:
            x, y = stack.pop()
            
            if self.M[x, y] == Maze.PRIZE:
                print(f"Tesouro encontrado na posição ({x}, {y})!")
                return True
            
            if (x, y) in visitado:
                continue
            
            visitado.add((x, y))
            
            for dx, dy in movimentos:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < self.M.shape[0] and 0 <= ny < self.M.shape[1]:
                    if self.M[nx, ny] != Maze.WALL and (nx, ny) not in visitado:
                        stack.append((nx, ny))
        
        print("Tesouro não encontrado.")
        return False
    
    def run(self):
        th = threading.Thread(target=self._display)
        th.start()
    
    def _display(self, cell_size=15):
        rows, cols = self.M.shape
        width, height = cols * cell_size, rows * cell_size
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Labirinto")
    
        BLACK, GRAY, BLUE, GOLD = (0, 0, 0), (192, 192, 192), (0, 0, 255), (255, 215, 0)
    
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
    
            screen.fill(BLACK)
    
            for y in range(rows):
                for x in range(cols):
                    color = {Maze.WALL: BLACK, Maze.HALL: GRAY, Maze.PLAYER: BLUE, Maze.PRIZE: GOLD}.get(self.M[y, x], GRAY)
                    pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
    
            pygame.display.flip()
