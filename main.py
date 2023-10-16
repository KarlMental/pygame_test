import pygame
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Robin Hood')
    pygame.mouse.set_visible(0)
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    character = Player([0, 0])
    i = 0
    while 1:
        i += 1
        game_clock = pygame.time.Clock()
        game_clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
        
        if len(pygame.event.get()) == 0:
            character.idle()

        character.move(pygame.key.get_pressed())
        screen.fill((250, 250, 250))
        screen.blit(character.get_animation(i//3), character.pos)
        pygame.display.flip()


if __name__ == '__main__':
    main()