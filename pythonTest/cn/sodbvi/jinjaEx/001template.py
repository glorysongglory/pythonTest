#!/usr/bin/python
# -*- coding: <encoding name> -*-
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('result'))
template = env.get_template('001.j2')
arg={"a":1,"b":2,"c":3,"d":4,"e":5,"中文":"中文值"}
content = template.render(arg)
fo = open('result/output/001.txt','w',encoding= 'utf8')
fo.write(content.encode().decode('utf-8'))
fo.close()


