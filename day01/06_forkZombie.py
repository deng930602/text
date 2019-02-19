import os
import sys
import time

pid = os.fork()

if pid < 0:
    sys.exit("常见子进程失败")
    # 一级子进程
elif pid == 0:
    pid = os.fork()
    # 二级子进程
    if pid ==0:
        print("真正的时间函数，二级子进程")
    else:
        os._exit(0)
else:
    os.wait()
    print('父进程要做的事情')
    time.sleep(30)
