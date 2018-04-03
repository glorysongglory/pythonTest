'''
Created on 2016/3/3 16:44

@author: sodbvi
'''

import platform

profile = {
'Architecture: ': platform.architecture(),
'Linux Distribution: ': platform.linux_distribution(),
'mac_ver: ': platform.mac_ver(),
'machine: ': platform.machine(),
'node: ': platform.node(),
'platform: ': platform.platform(),
'processor: ': platform.processor(),
'python build: ': platform.python_build(),
'python compiler: ': platform.python_compiler(),
'python version: ': platform.python_version(),
'release: ': platform.release(),
'system: ': platform.system(),
'uname: ': platform.uname(),
'version: ': platform.version(),
}

for key in profile:
    print(key + str(profile[key]))
