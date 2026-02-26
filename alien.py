import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """管理外星人的类"""
    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置"""
        #调用父类Sprite的构造方法，初始化精灵的内置属性
        super().__init__()
        #从主游戏实例中获取核心资源（和Ship类逻辑一致）
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        
        #加载外星人图像并获取其rect属性
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        
        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #存储外星人准确位置的小数值
        self.x = float(self.rect.x)
    
    def update(self):
        """向右向左移动外星人"""
        self.x += self.setting.alien_speed * self.setting.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘 就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True