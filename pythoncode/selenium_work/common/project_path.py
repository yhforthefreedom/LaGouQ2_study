# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         project_path
# Description:  
# Author:       yanghao
# Date:         2020/8/14
# -------------------------------------------------------------------------------
import os

# 项目路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 截图路径
screenshot_path = os.path.join(project_path, "img")

# 日志路径
log_path = os.path.join(project_path, "log")
