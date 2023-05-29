# 导入浏览器的对象
from selenium import webdriver
# 导入时间模块  内置
import time
# 导入元素定位功能
from selenium.webdriver.common.by import By
# 导入数据请求模块
import requests
# 导入数据解析模块
import parsel

# 实例化一个浏览器的对象
# driver 是一个变量的名字 赋值给它
driver = webdriver.Chrome()

# 打开一个浏览器的窗口
driver.get('https://www.jsyks.com/kmy-mnks')
# 强制等待
time.sleep(2)


# 窗口最大化
driver.maximize_window()
# 隐式等待  针对全局
driver.implicitly_wait(10)

# 答题的环节
# 定位到题目
# driver.find_element_by_css_selector()  # 弃用的方法
# 开发者工具 F12 右键+检查--> 元素面板 elements
lis = driver.find_elements(By.CSS_SELECTOR, '.Content>li')
# print(len(lis))
# print(lis)
# 列表 for 遍历
"""
css 语法
. 属性提取器
> 取下级标签
# ID提取器
::text 文本提取
"""
for li in lis:
    time.sleep(0.5)
    # get_attribute 属性值得提取
    rid = li.get_attribute('c')
    url = f'https://tiba.jsyks.com/Post/{rid}.htm'
    html_data = requests.get(url=url).text
    # < Response[200] >  返回的一个响应体的对象 200请求成功了
    # .text 获取响应体对象的文本数据
    # print(response)
    # 解析数据 --> 转对象
    selector = parsel.Selector(html_data)
    answer = selector.css('#question u::text').get()
    # print(answer)
    # 重新的赋值
    if answer == '对':
        answer = '正确'
    elif answer == '错':
        answer = '错误'
    # print(answer)
    bs = li.find_elements(By.CSS_SELECTOR, 'b')
    for b in bs:
        choose = b.text
        if answer in choose:
            # 如果正确的答案 在选项中 进行一个点击的操作
            # click() 点击操作
            b.click()


# 提交试卷的点击
driver.find_element(By.CSS_SELECTOR, '.btnJJ').click()

# 添堵
input()

# 关闭浏览器
driver.quit()
