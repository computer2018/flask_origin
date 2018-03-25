#!/usr/bin/python
#coding=utf-8

"""
表单类
参考文档：http://wtforms.readthedocs.io/en/latest/

字段类型            说明
StringField         文本字段
TextAreaField       多行文本字段
PasswordField       密码文本字段
HiddenField         隐藏文本字段
DateField           文本字段，值为datetime.date格式
DateTimeField       文本字段，值为datetime.datetime格式
IntegerField        文本字段，值为整数
DecimalField        文本字段，值为decimal.Decimal
FloatField          文本字段，值为浮点数
BooleanField        复选框，值为True和False
RadioField          一组单选框
SelectField         下拉列表
SelectMultipleField 下拉列表，可选择多个值
FileField           文件上传字段
SubmitField         表单提交按钮
FormField           把表单作为字段嵌入另一个表单
FieldList           一组指定类型的字段

"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, RadioField, \
    TextAreaField, DateField, BooleanField, FileField, DateTimeField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import CheckboxInput, PasswordInput, TextInput

from validator import passwordValid


class LoginForm(FlaskForm):
    """ 定义登录表单 """
    username = StringField(label='UserName', validators=[DataRequired("请输入用户名")],
        description="请输入用户名",
        render_kw={"required": "required", "class": "form-controal"})
    password = PasswordField('密码', validators=[DataRequired()])
    language = RadioField('编程语言',
        choices=[('cpp', 'C++'), ('py', 'Python'), ('java', 'Java')])
    code = TextAreaField('代码')
    date = DateField('日期')
    is_checked = BooleanField('是否已经通过验证')
    submit = SubmitField('登录')

class ding_talk_form(FlaskForm):
    """ 钉钉机器人 """
    username = StringField(label="消息", validators=[DataRequired()],
        render_kw={"required": 'required', "placeholder": "请输入所需要发送的消息"},
        description="请输入所需要发送的消息")
    language = SelectField('选择群机器人',
        choices=[("https://oapi.dingtalk.com/robot/send?access_token=94d1da532a09862ee37789652168202b008aa352c6f109f8d5bf97225141969a", 'Lab120'), ("https://oapi.dingtalk.com/robot/send?access_token=25a7ead4dbc3e3ea4ece0e7879a22626a39c0cf00acf281965574340695618a4", '计算机群'), ('java', '其他群')])

    send_model=RadioField('选择发送模式',
        choices=[("value发送倒计时", '发送倒计时'), ("value发送文本中内容", '发送文本中内容')])






'''


class auto_dingtalk_send_form(FlaskForm):
    """ 钉钉机器人 """
    StartTime = StringField(label="消息", validators=[DataRequired()],
        render_kw={"required": 'required', "placeholder": "请输入开始准备比赛的时间"},
        description="请输入开始准备比赛的时间")
        

    EndTime = StringField(label="消息", validators=[DataRequired()],
        render_kw={"required": 'required', "placeholder": "请输入比赛结束时间"},
        description="请输入比赛结束时间")
        
    date = DateField('日期')

        

    language = SelectField('选择群机器人',
        choices=[("nxp", 'Lab120'), ("computer_competition", '计算机群'), ('java', '其他群')])

'''

class auto_dingtalk_send_form(FlaskForm):
    """ 钉钉机器人 """
    StartTime = StringField('请输入比赛开始日期')
    EndTime = StringField('请输入比赛结束日期')
    date = StringField('日期')

    language = SelectField('选择群机器人',
        choices=[("nxp", 'Lab120'), ("computer_competition", '计算机群'), ('java', '其他群')])



class control_form(FlaskForm):
    """ 钉钉机器人 """

    language = SelectField('选择门状态',
        choices=[(1, '开'), (2, '关')])





class RegistForm(FlaskForm):
    """ 用户注册 """
    username = StringField(label="用户名", validators=[DataRequired()],
        render_kw={"required": 'required', "placeholder": "请输入用户名"},
        description="输入用用户邮箱注册")
    password = PasswordField('密码', validators=[DataRequired("请输2入密码"), passwordValid])

    language = RadioField('编程语言',
        choices=[('cpp', 'C++'), ('py', 'Python'), ('java', 'Java')]) #后者为网页上显示，前者为后端

    # def validate_password(self, field):
    #     print(field)
    #     password = field.data
    #     if len(password) != 6:
    #         raise ValidationError("密码必须是6位")
    #     if not password.isdigit():
    #         raise ValidationError("密码必须是数字")
    #     return password

    # def validate_password(self, username):
    #     return


class UploadForm(FlaskForm):
    """ 文件上传 """
    image = FileField(label="文件上传", validators=[DataRequired()],
        render_kw={"required": 'required', "class": "form-control"},
        )