'''
Author: ZXG
Date: 2026-01-23 09:18:36
LastEditTime: 2026-01-23 10:22:05
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
        self.bg_color = (230, 230, 230)  #浅灰色背景
        
        self.ship_speed = 1.5  #飞船速度