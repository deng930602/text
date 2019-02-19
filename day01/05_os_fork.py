

import os 
import sys
import time

pid = os.fork()
if pid < 0:
    sys.exit("创建进程失败")
elif pid == 0:
    print('子进程执行的函数')
else:
    print("父进程要做的事情")
    time.sleep(30)