'''
Author: ZXG
Date: 2026-01-23 09:02:17
LastEditTime: 2026-01-23 14:39:25
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
from bullet import Bullet
from alien import Alien


#调试模式开关
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
            #窗口模式
            self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        else:
            #全屏模式
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.setting.screen_width = self.screen.get_rect().width
            self.setting.screen_height = self.screen.get_rect().height

        #创建一个用于存储子弹的编组
        self.bullets = pygame.sprite.Group()
        #创建一个用于存储外星人的编组
        self.aliens = pygame.sprite.Group()

        self._create_fleet()  #创建外星人群

        #设置窗口标题
        pygame.display.set_caption("Alien Invasion")
        
        #创建一艘飞船的实例
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        #游戏主循环
        while True:
            
            self._check_events()    #检查键盘和鼠标事件
            self.ship.update()      #更新飞船位置
            self.update_bullets()   #更新子弹位置
            self.update_aliens()     #更新外星人位置
            self._update_screen()   #更新屏幕上的图像
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
        elif event.key == pygame.K_SPACE:
            #按下空格键发射子弹
            self._fire_bullet()

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
        """更新屏幕上的图像 并切换到新屏幕"""
        #每次循环都重绘屏幕并更新屏幕 背景色bg_color
        self.screen.fill(self.setting.bg_color)
        #更新子弹位置 并绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #绘制飞船
        self.ship.blitme()  
        #绘制外星人
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def _fire_bullet(self):
        """创建一颗子弹 并将其加入编组bullets中 开火"""
        if len(self.bullets) < self.setting.bullets_allowed:  #限制屏幕上最多只能有3颗子弹
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """创建外星人群"""
        #创建一个外星人
        alien = Alien(self)
        #计算一行可以容纳多少个外星人
        alien_width,alien_height = alien.rect.size
        current_x = alien_width
        current_y = alien_height
        while current_y < (self.setting.screen_height - 10*alien_height):
            while current_x < (self.setting.screen_width - 2*alien_width):
                #创建一个外星人并将其加入当前行
                self._create_alien(current_x,current_y)
                #更新current_x 以便为下一个外星人留出空间
                current_x += 2 * alien_width
            #更新current_y 以便为下一行外星人留出空间
            current_y += 2 * alien_height
            #重置current_x 以便为下一行的第一个外星人设置
            current_x = alien_width

    def _create_alien(self, x_position,y_position):
        """在指定x位置创建一个外星人并将其加入编组aliens中"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def update_aliens(self):
        """更新外星人群中所有外星人的位置"""
        self.check_fleet_edges()  #检查外星人是否到达边缘
        #更新外星人位置
        self.aliens.update()

    def check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """将整群外星人下移 并改变它们的移动方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1


    def update_bullets(self):
        """更新子弹的位置 并删除已消失的子弹"""
        #更新子弹位置
        self.bullets.update()
        #删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


#如果直接运行这个文件，就创建一个游戏实例并运行游戏      
if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()