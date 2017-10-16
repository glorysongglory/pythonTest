from fabric.api import run, env, roles,execute
from fabric.colors import *

env.roledefs = {
'testserver': ['user@xxx.xxx.xxx.xxx', 'user@xxx.xxx.xxx.xxx'],
'realserver': ['user@xxx.xxx.xxx.xxx', ]
}

env.passwords = {
'user@xxx.xxx.xxx.xxx:22': "passwd",
'user@xxx.xxx.xxx.xxx:22': "passwd",
'user@xxx.xxx.xxx.xxx:22': "passwd",
}

@roles('testserver')
def testssh():
    run('df -h')

@roles('realserver')
def testssh1():
    run('ls -l')

def testtask():
    execute(testssh)
    execute(testssh1)


