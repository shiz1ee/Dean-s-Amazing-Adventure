from pathlib import Path
from settings import *
from level import Level
from pytmx.util_pygame import load_pygame

BASE_DIR = Path(__file__).resolve().parent
TMX_PATH = BASE_DIR.parent / 'data' / 'levels' / 'omni.tmx'

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Deans Amazing Adventure')

        self.tmx_maps = {0: load_pygame(TMX_PATH)}
        print(self.tmx_maps)


        self.current_stage = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run()
            
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()

    