from fabric.api import run, env, sudo, get, put, execute,runs_once,prompt,lcd,cd
from fabric.colors import *

env.hosts=[
    'user@xxx.xxx.xxx.xxx',
    'user@xxx.xxx.xxx.xxx'
]

env.passwords={
'user@xxx.xxx.xxx.xxx:22':'passwd',
'user@xxx.xxx.xxx.xxx:22':'passwd'
}


def testssh():
    run('df -h')


