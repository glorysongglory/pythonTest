from fabric.api import run, env, sudo, get, put, execute,runs_once,prompt,lcd,cd
from fabric.colors import *

env.hosts = ['xxx.xxx.xxx.xxx']
env.user = 'xxx'
env.password = 'xxx'


def testssh():
    run('df -h')

@runs_once
def testprint():
   print "asdfasdf"


def testsudo():
    sudo('mkdir /fab')


def testget():
    run('cd /home/hixc')
    get('fab.txt', 'fab.txt')


def testput():
    put('fab.txt', '/home/hixc/fab1.txt')


def testcolor():
    print green('green')
    print red('red')
    print yellow('yellow')


def testexcute():
    execute(testssh)
    execute(testssh)

def testonce():
    execute(testprint)
    execute(testprint)
    execute(testprint)

def testprompt():
    filename=prompt('please input filename:')
    get('/home/hixc/.bashrc','%s.sh' %filename)

def testwith():
    with cd('/home/hixc/'):
        with lcd('D:\\untitled1'):
            put('1.txt','1.txt')

