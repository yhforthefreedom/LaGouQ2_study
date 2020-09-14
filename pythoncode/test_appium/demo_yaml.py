# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         demo_yaml
# Description:  
# Author:       SNQU
# Date:         2020/7/2
#-------------------------------------------------------------------------------
import yaml
def getdata():
    with open("./wework_data.yaml",encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas

a=getdata()
print(a)
