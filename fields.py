#!/usr/bin/python
#coding=utf-8

from wtforms import SelectMultipleField
from wtforms import widgets

class MultiCheckboxField(SelectMultipleField):
	""" 自定义字段类型 """
	widget = widgets.ListWidget(prefix_label=True) 
	option_widget = widgets.CheckboxInput() 