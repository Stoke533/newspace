# 线程池调度器
from concurrent.futures import ThreadPoolExecutor

def func(name):
    for i in range(100):
        print(name, i)

if __name__ == '__main__':
    # 定义线程池的大小
    with ThreadPoolExecutor(20) as t:
        # 10个任务
        # 任务提交给线程池
        t.submit(func, '周杰伦')


