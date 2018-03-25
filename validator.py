#!/usr/bin/python
#coding=utf-8

from wtforms.validators import ValidationError

def passwordValid(form, field):
    """ 密码验证 """
    password = field.data
    if len(password) != 6:
        raise ValidationError("1密码必须是6位")
    if not password.isdigit():
        raise ValidationError("1密码必须是数字")
    return password
