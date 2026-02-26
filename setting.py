'''
Author: ZXG
Date: 2026-01-23 09:18:36
LastEditTime: 2026-01-23 14:35:20
LastEditors: ZXG
Description: 
FilePath: /PythonStudy/setting.py
ZXG写的头部注释
'''

class Setting:
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)  #黑色背景
        #飞船设置
        self.ship_speed = 1.5  #飞船速度
        
        #子弹设置
        self.bullet_speed = 2.5  #子弹速度
        self.bullet_width = 3    #子弹宽度
        self.bullet_height = 15  #子弹高度
        self.bullet_color = (255, 0, 0)  #红色子弹
        self.bullets_allowed = 20  #屏幕上允许的最大子弹数
        #外星人设置
        self.alien_speed = 1  #外星人速度
        self.fleet_drop_speed = 5  #外星人群向下移动的速度
        #fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        