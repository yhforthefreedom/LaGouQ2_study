# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         do_regex
# Description:  
# Author:       yanghao
# Date:         2020/8/7
# -------------------------------------------------------------------------------
from demo_api_auto.tools.get_cookie import GetCookie
import re


class DoRegex:
    @staticmethod
    def do_regex(s: str):
        while re.search('\${(.*?)}', s):
            key = re.search("\${(.*?)}", s).group(0)
            value = re.search("\${(.*?)}", s).group(1)
            s = s.replace(key, str(getattr(GetCookie, value)))
        return s
