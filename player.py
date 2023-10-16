import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = {
                'idle': {'image': pygame.image.load('assets/player_idle.png').convert_alpha(), 'frames': 8, 'size': (128, 128)},
                'run': {'image': pygame.image.load('assets/player_run.png').convert_alpha(), 'frames': 8, 'size': (128, 128)},
                'jump': {'image': pygame.image.load('assets/player_jump.png').convert_alpha(), 'frames': 12, 'size': (128, 128)},
                'melee': {'image': pygame.image.load('assets/player_melee.png').convert_alpha(), 'frames': 28, 'size': (128, 128)},
                'dash': {'image': pygame.image.load('assets/player_dash.png').convert_alpha(), 'frames': 14, 'size': (128, 128)},
                'death': {'image': pygame.image.load('assets/player_death.png').convert_alpha(), 'frames': 24, 'size': (128, 128)},
                'attack': {'image': pygame.image.load('assets/player_attack.png').convert_alpha(), 'frames': 14, 'size': (180, 128)}
        }
        self.pos = pos
        self.speed = 5
        self.current_action = 'idle'
        self.current_x_direction = 1

    def get_animation(self, frame):
        self.sheet = self.animations[self.current_action]['image']
        frames = self.animations[self.current_action]['frames']
        x_size = self.animations[self.current_action]['size'][0]
        y_size = self.animations[self.current_action]['size'][1]
        self.image  = self.sheet.subsurface(pygame.Rect(frame%frames*x_size, 0, x_size, y_size))
        if self.current_x_direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        return self.image

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.pos[0] -= self.speed
            self.current_action = 'run'
            self.current_x_direction = -1
        if keys[pygame.K_RIGHT]:
            self.pos[0] += self.speed
            self.current_action = 'run'
            self.current_x_direction = 1
        if keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT]:
            self.pos[0] -= self.speed*1.5
            self.current_action = 'run'
            self.current_x_direction = -1
        if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]:
            self.pos[0] += self.speed*1.5
            self.current_action = 'run'
            self.current_x_direction = 1
        if keys[pygame.K_UP]:
            self.pos[1] -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos[1] += self.speed
    
    def idle(self):
        self.current_action = 'idle'