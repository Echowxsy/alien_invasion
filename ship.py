import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化飞船"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞机图像
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 设置飞船位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.top = self.rect.top

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """更新飞船状态"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.top -= self.ai_settings.ship_speed_factor
        check_ishight = self.rect.top < \
            (self.screen_rect.height-self.rect.height)
        if self.moving_down and check_ishight:
            self.top += self.ai_settings.ship_speed_factor

        self.rect.top = self.top
        self.rect.centerx = self.center

    def center_ship(self):
        """飞船居中"""
        self.center = self.screen_rect.centerx
        self.top = self.screen_rect.height - self.rect.height
