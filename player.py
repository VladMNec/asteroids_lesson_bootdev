import pygame
import circleshape
from constants import *
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.lives = PLAYER_LIVES
        self.invuln = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)
        # change player color while respawn invulnerable
        if self.invuln > 0:
            pygame.draw.polygon(screen, (255, 0, 0), self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
        self.invuln -= dt

        if keys[pygame.K_a]:
            left = dt * -1
            self.rotate(left)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            back = dt * -1
            self.move(back)

        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.timer = PLAYER_SHOT_COOLDOWN

    def respawn(self):
        # reset player to starting position and give period of invulnerability
        if self.invuln <= 0:
            self.invuln = 1.2
            self.lives -= 1
            self.position.x = SCREEN_WIDTH / 2
            self.position.y = SCREEN_HEIGHT / 2

        if self.lives == 0:
            raise SystemExit("Game over!")
