#!/usr/bin/python
#coding=utf-8



"""
表单练习
"""
import os
from flask import Flask, render_template, request, flash
from forms import RegistForm, UploadForm, ding_talk_form, auto_dingtalk_send_form, control_form

from ding_talk_send import DtalkRobot, the_time_send

#以下为笔者所写的数据库操作
from mysql import MoonMysql
import pymysql





app = Flask(__name__)
# 文件上传的目录
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'medias')


#以下为数据库操作
@app.route('/control/', methods=['GET', 'POST'])
def control():
    #希望之后可以在网页端添加所要发送的机器人怎么办呢？
    form = control_form()
    #if form.validate_on_submit():#检测是不是POST请求
    #if True:
    if request.method == 'POST':
        
        print(form.language.data)

        print("dsfaf ")
        app_write = MoonMysql
        app_write.update_control_data(NAME_DATA='DOOR1',STATUS_DATA=form.language.data)





    return render_template("control.html", form=form)







@app.route('/ding_talk/', methods=['GET', 'POST'])
def ding_talk():
    #希望之后可以在网页端添加所要发送的机器人怎么办呢？
    form = ding_talk_form()
    if form.validate_on_submit():
        webhook = form.language.data#机器人种类
        print(webhook)

        print(form.send_model.data)

        if form.send_model.data=='value发送文本中内容':
            robot = DtalkRobot(webhook)
            print(form.username.data)
            msg = form.username.data
            print(robot.sendText(msg))

        if form.send_model.data=='value发送倒计时':
            robot = the_time_send
            robot.time_send(webhook=webhook)

    return render_template("ding_talk.html", form=form)



#以下为数据库操作
@app.route('/auto_dingtalk_send/', methods=['GET', 'POST'])
def auto_dingtalk_send():
    #希望之后可以在网页端添加所要发送的机器人怎么办呢？
    form = auto_dingtalk_send_form()
    if form.validate_on_submit():#检测是不是POST请求
    #if True:
        
        print(form.language.data)
        print(form.StartTime.data)
        print(form.EndTime.data)
        print(form.date.data)
        print("dsfaf ")
        app_write = MoonMysql
        app_write.update_time(TIME_TYPE='START_TIME',TIME_DATA=form.StartTime.data , TASK=form.language.data)
        app_write.update_time(TIME_TYPE='END_TIME',TIME_DATA=form.EndTime.data , TASK=form.language.data)





    return render_template("auto_dingtalk_send.html", form=form)






@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    """ 注册页面 """
    form = RegistForm()
    if form.validate_on_submit():
        data = form.data
        # TODO 处理业务逻辑
        print(data)
        
    return render_template("regist.html", form=form)


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    """ 文件上传 """
    form = UploadForm()
    if form.validate_on_submit():
        print("teset_way")
        print(request.files['image'])
        image = form.data["image"]



        if image:
            # 文件的全路径
            filename = os.path.join(UPLOAD_PATH, image.filename)
            image.save(filename)
            flash("文件上传成功")
            return 'Success!'
        else:
            return 'No File.'
    else:
        print(form.errors)
    return render_template("upload.html", form=form)

@app.route('/cat/')
def cat(name):
    """ 新闻类别页面 """
    
    #return render_template('cat.html' %name, name=name)
    return render_template('cat.html')


@app.route('/')

def main():
    return render_template("index.html")


@app.route('/yuncontrol')
def yuncontrol():
    return render_template("yuncontrol.html")






app.config['SECRET_KEY'] = 'a random string'
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True, processes=200) 