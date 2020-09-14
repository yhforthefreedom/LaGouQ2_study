# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         test_start_calc_case
# Description:  
# Author:       yanghao
# Date:         2020/6/11
# -------------------------------------------------------------------------------
import pytest
import yaml


def getdata():
    with open("./calc_para.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


@pytest.mark.parametrize('a,b,result', getdata(),
                         ids=["整数", "浮点数", "bignum", 'minus', 'float+int'])
class Teststart_calc:
    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='mul')
    def check_mul(self, start_calc, a, b, result):
        assert result == start_calc.mul(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["mul"])
    def check_div(self, start_calc, a, b, result):
        try:
            assert result == start_calc.div(a, b)
        except Exception:
            raise Exception("除数不能为0")

    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='add')
    def check_add(self, start_calc, a, b, result):
        assert result == start_calc.add(a, b)

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["add"])
    def check_sub(self, start_calc, a, b, result):
        assert result == start_calc.sub(a, b)
