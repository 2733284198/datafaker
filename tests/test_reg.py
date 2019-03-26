#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import re

from datafaker.reg import reg_float, reg_keyword, reg_args, reg_cmd


def test_reg_float():
    assert 45.22 == reg_float('wer45.22')


def test_reg_keyword():
    assert 'name' == reg_keyword("wer[:name]234e")
    assert 'age(1,10)' == reg_keyword("wer[:age(1,10)]234e")


def test_reg_args():
    assert ['20', '45'] == reg_args("varchar(20,45)")
    assert ['20', '45', '1'] == reg_args("varchar(20,45,1)")
    assert ['/home/lovelife'] == reg_args("enum(/home/lovelife)")
    assert ['20', ] == reg_args("varchar(20)")


def test_reg_cmd():
    assert 'varchar' == reg_cmd('varchar(20)')
    assert 'varchar' == reg_cmd('varchar')
    assert 'int' == reg_cmd('int')