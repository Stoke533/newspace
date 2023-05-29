import random
import time
# 滑动函数
def roll_window_to_bottom(browser, stop_length=None, step_length=300):
    """selenium 滚动当前页面，向下滑
    :param browser: selenium的webdriver
    :param stop_length: 滑动的最大值
    :param step_length: 每次滑动的值
    """
    original_top = 0
    while True:  # 循环向下滑动
        if stop_length:
            if stop_length - step_length < 0:
                browser.execute_script("window.scrollBy(0,{})".format(stop_length))
                break
            stop_length -= step_length

        browser.execute_script("window.scrollBy(0,{})".format(step_length))
        time.sleep(0.5 + random.random())  # 停顿一下
        check_height = browser.execute_script(
            "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
        if check_height == original_top:  # 判断滑动后距顶部的距离与滑动前距顶部的距离
            break
        original_top = check_height


# 次函数用于滑动页面，实现js等信息加载， 保障自动化爬虫数据采集的鲁棒性