'''
Author: ZXG
Date: 2026-01-23 09:29:09
LastEditTime: 2026-01-23 10:24:15
LastEditors: ZXG
Description: Ship class for the alien invasion game
FilePath: /PythonStudy/ship.py
ZXG写的头部注释
'''
import pygame


class Ship:
    """管理飞船的类"""

    #ai_game 指向当前AlienInvasion实例的引⽤
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        
        # 解释：
        # ① 把主游戏实例`ai_game`的`screen`属性（游戏窗口的Display Surface对象，也就是“画布”），赋值给Ship实例的`screen`属性；
        # ② 这样Ship类里就可以通过`self.screen`操作游戏窗口，比如在窗口上绘制飞船。
        self.screen = ai_game.screen
        # 解释：
        # ① 核心概念：`rect`是Pygame中的「矩形对象（Rectangle）」，通俗说就是给“窗口、图片”套一个「看不见的矩形框」；
        # ② `ai_game.screen.get_rect()`：获取游戏窗口的矩形对象，这个矩形框和窗口尺寸完全一致，包裹着整个窗口；
        # ③ 把这个窗口矩形对象赋值给`self.screen_rect`，后续用来「定位飞船」（不用手动计算像素坐标，直接用矩形的属性定位，更方便）。
        self.screen_rect = ai_game.screen.get_rect()
        
        #加载飞船图像并获取其外接矩形
        # 解释：
        # ① `pygame.image.load()`：Pygame的图片加载函数，传入「图片文件路径」，返回一个「普通Surface对象」（也就是飞船的图片画布）；
        # ② 路径说明：`'images/ship.png'` 表示当前文件夹下有一个`images`文件夹，里面存放着`ship.png`飞船图片（必须存在这个文件夹和图片，否则会报错）；
        # ③ 把加载后的飞船图片Surface赋值给`self.image`，后续用来绘制飞船。
        self.image = pygame.image.load('images/ship.png')
        # 解释：
        # ① 给飞船图片也套一个矩形框，调用`image.get_rect()`获取飞船图片的矩形对象；
        # ② 这个矩形框的尺寸和飞船图片的尺寸完全一致，后续通过操作这个矩形框的位置，就能控制飞船图片在窗口中的位置（不用手动计算图片的像素坐标）。
        self.rect = self.image.get_rect()
        #将每艘新飞船放在屏幕底部中央
        # 解释：
        # 这是Pygame中「定位元素的核心技巧」——通过操作`rect`对象的「预设属性」来定位，不用手动计算像素。
        # ① `self.screen_rect.midbottom`：窗口矩形的「底部中点」属性（返回一个坐标元组，比如窗口1200x800的话，就是(600, 800)）；
        # ② `self.rect.midbottom`：飞船矩形的「底部中点」属性；
        # ③ 把两者赋值相等，就是「让飞船的底部中点，和窗口的底部中点对齐」，最终效果就是飞船放在屏幕底部中央；
        # ④ 补充：Pygame的`rect`还有很多常用定位属性，比如`center`（中心）、`midtop`（顶部中点）、`left`（左侧）等，后续可用来移动飞船。
        self.rect.midbottom = self.screen_rect.midbottom
        
        #飞船的移动标志
        self.moving_right = False
        self.moving_left = False
        #存储飞船的设置属性
        self.setting = ai_game.setting
        # 在飞船的属性中存储一个浮点数类型的x坐标，以便更精确地控制飞船的水平位置
        self.x = float(self.rect.x)
        
    def blitme(self):
        """在指定位置绘制飞船"""
        # 解释：
        # ① 这个方法的唯一作用：把飞船图片绘制到游戏窗口上；
        # ② 核心函数：`self.screen.blit()`——Pygame中「贴图函数」，作用是把一个Surface对象（飞船图片）贴到另一个Surface对象（游戏窗口）上；
        # ③ 参数说明：
        #    - 第一个参数`self.image`：要绘制的内容（飞船图片的Surface对象）；
        #    - 第二个参数`self.rect`：要绘制的位置（飞船的矩形对象，Pygame会自动把飞船图片贴到这个矩形框对应的窗口坐标上）；
        # ④ 注意：调用这个方法后，飞船只是被画到了“窗口画布”（self.screen）的缓冲区里，需要调用`pygame.display.flip()`刷新屏幕，才能看到飞船。
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0  :
            self.x -= self.setting.ship_speed
        # 将浮点数x坐标更新到rect对象的x属性上，以确保飞船位置的精确控制
        self.rect.x = self.x