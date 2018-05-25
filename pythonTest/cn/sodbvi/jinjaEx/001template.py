#!/usr/bin/python
# -*- coding: <encoding name> -*-
import os;

from jinja2 import Environment, PackageLoader

filedict = {'apiaction': 'Action.java', 'entity': '.java', 'mapper': 'Mapper.java', 'service': 'Service.java',
            'xml': '.xml'}
env = Environment(loader=PackageLoader('result'))
workPath = os.path.dirname(os.path.realpath(__file__))
env.trim_blocks = True


def genCode(jsonStr, dirname, fileName):
    template = env.get_template(dirname + '.j2')
    content = template.render(jsonStr)
    moduleName = jsonStr['module'];
    modulePath = workPath + '\\result\\output\\' + moduleName + '\\'
    childPath = modulePath + dirname
    filePath = childPath + '\\' + moduleName.capitalize() + fileName
    if (not os.path.exists(childPath)):
        os.makedirs(childPath)

    fo = open(filePath, 'w', encoding='utf8')
    fo.write(content.encode().decode('utf-8'))
    fo.close()


def pre(jsonStr):
    for key, value in filedict.items():
        genCode(jsonStr, key, value)


if __name__ == '__main__':
    jsonStr = {"package": "com.hi.webapp.hipro.keyword1", "module": "keyword1", "name": "proKeyword1",
               "uri": "/test/keyword1",
               "des": "关键词表", "table": "PRO_KEYWORD1", "fieldList": [
            {"name": "id", "column": "ID", "type": "long", "dbtype": "BIGINT", "getset": "N", "startend": "N",
             "des": "主键"},
            {"name": "createDate", "column": "CREATE_DATE", "type": "Date", "dbtype": "TIMESTAMP", "getset": "N",
             "startend": "Y", "des": "创建时间"},
            {"name": "updateDate", "column": "UPDATE_DATE", "type": "Date", "dbtype": "TIMESTAMP", "getset": "N",
             "startend": "Y", "des": "更新时间"},
            {"name": "deleteTag", "column": "DELETE_TAG", "type": "String", "dbtype": "VARCHAR", "getset": "N",
             "des": "逻辑标志"},
            {"name": "wallId", "column": "WALL_ID", "type": "long", "dbtype": "BIGINT", "getset": "Y", "des": "所属活动ID"},
            {"name": "actType", "column": "ACT_TYPE", "type": "String", "dbtype": "VARCHAR", "getset": "Y",
             "des": "活动类型"},
            {"name": "keyWord", "column": "KEY_WORD", "type": "String", "dbtype": "VARCHAR", "getset": "Y",
             "des": "关键词"}]}
    pre(jsonStr)
