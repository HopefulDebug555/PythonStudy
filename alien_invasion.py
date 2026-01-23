'''
Author: ZXG
Date: 2026-01-23 09:02:17
LastEditTime: 2026-01-23 10:32:12
LastEditors: ZXG
Description: 
FilePath: /PythonStudy/alien_invasion.py
ZXG写的头部注释
'''
#导入所需的模块 sys 和 pygame sys是用来退出游戏的，pygame是用来创建游戏窗口和处理游戏事件的
#sys用于与 Python 解释器及其运行环境交互。通过它可以获取解释器信息、操作输入输出流、管理模块路径、控制程序退出等。
import sys
import pygame
#包含游戏设置的类 
from setting import Setting
from ship import Ship

DEBUG = True

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        
        #初始化pygame库
        pygame.init()
        
        #创建一个时钟对象 用于控制游戏循环的频率
        self.clock = pygame.time.Clock()
        #创建一个Setting类的实例 用于存储游戏设置
        self.setting = Setting()    
        if DEBUG:
            self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.setting.screen_width = self.screen.get_rect().width
            self.setting.screen_height = self.screen.get_rect().height

        #设置窗口标题
        pygame.display.set_caption("Alien Invasion")
        
        #创建一艘飞船的实例
        self.ship = Ship(self)
    def run_game(self):
        """开始游戏的主循环"""
        #游戏主循环
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            #设置每秒钟循环60次
            self.clock.tick(60)
            
    #函数名带_表示这是一个私有方法 只能在类的内部调用       
    def _check_events(self):
        #接受事件 来自键盘和鼠标
            for event in pygame.event.get():
                #如果是退出事件就退出
                if event.type == pygame.QUIT:
                    sys.exit()
                #按键按下
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)          
                #按键松开
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """响应按键按下事件"""
        if event.key == pygame.K_RIGHT:
            #self.ship.rect.x += 10
            #向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            #按下q键退出游戏
            sys.exit()

    def _check_keyup_events(self, event):
        """响应按键松开事件"""
        if event.key == pygame.K_RIGHT:
            #停止向右移动飞船
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            #停止向左移动飞船
            self.ship.moving_left = False

    #函数名带_表示这是一个私有方法 只能在类的内部调用                  
    def _update_screen(self):
        #每次循环都重绘屏幕并更新屏幕 背景色bg_color
        self.screen.fill(self.setting.bg_color)
        #绘制飞船
        self.ship.blitme()  
        pygame.display.flip()


#如果直接运行这个文件，就创建一个游戏实例并运行游戏      
if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()