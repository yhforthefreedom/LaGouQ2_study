# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         yaml_study
# Description:  
# Author:       SNQU
# Date:         2020/6/11
#-------------------------------------------------------------------------------
import yaml

with open("yaml_testdata.yaml") as f:
    data = yaml.safe_load(f)
print(data)