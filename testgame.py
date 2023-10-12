import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Basic Pygame program')
    pygame.mouse.set_visible(0)
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    character = {
        'x': screen.get_width()/2,
        'y': screen.get_height()/2,
        'width': 30,
        'height': 60,
        'speed': 5,
        'color': (255, 0, 0)
    }
    
    while 1:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            character['x'] -= character['speed']
        if keys[pygame.K_RIGHT]:
            character['x'] += character['speed']
        if keys[pygame.K_UP]:
            character['y'] -= character['speed']
        if keys[pygame.K_DOWN]:
            character['y'] += character['speed']
        if keys[pygame.K_a]:
            character['width'] += 1
        if keys[pygame.K_d]:
            character['width'] -= 1
        if keys[pygame.K_s]:
            character['height'] -= 1
        if keys[pygame.K_w]:
            character['height'] += 1

        screen.fill((250, 250, 250))
        pygame.draw.rect(screen, character['color'], (character['x'], character['y'], character['width'], character['height']))
        pygame.display.flip()




if __name__ == '__main__':
    main()