'''
Author: ZXG
Date: 2026-01-23 14:09:14
LastEditTime: 2026-01-23 14:18:58
LastEditors: ZXG
Description: 
FilePath: /PythonStudy/bullet.py
ZXG写的头部注释
'''
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理子弹的类"""
    def __init__(self, ai_game):
        """在飞船当前位置创建一个子弹对象"""
        
        # 调用父类Sprite的构造方法，初始化精灵的内置属性
        super().__init__()
        
        # 从主游戏实例中获取核心资源（和Ship类逻辑一致）
        self.screen = ai_game.screen    # 游戏窗口画布
        self.setting = ai_game.setting  # 游戏配置（子弹尺寸、速度、颜色）
        self.color = self.setting.bullet_color  # 子弹颜色（从配置中获取，方便修改）
        
        #在(0,0)处创建一个表示子弹的矩形 再设置正确的位置
         # 步骤1：手动创建子弹的矩形对象（rect），和Ship类加载图片获取rect不同
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
         # 步骤2：调整子弹位置，让子弹从飞船顶部中点发射
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #存储用小数表示的子弹位置
         # 步骤3：用浮点型变量存储子弹的y坐标，实现平滑移动
        self.y = float(self.rect.y)
        
    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -= self.setting.bullet_speed
        #更新表示子弹的rect位置
        self.rect.y = self.y
        
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)