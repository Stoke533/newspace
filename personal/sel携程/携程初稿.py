from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import prettytable as pt
import random


# '入参 航班号 起飞时间 到达时间 出发站 到达站 价格 姓名 身份证号码 登录账号 密码'

# username = str(input('请输入登录账号：'))
# password = str(input('请输入密码：'))
# name = str(input('请输入姓名'))
# userID = str(input('请输入身份证号码：'))
# departure = str(input('请输入出发地：'))
# destination = str(input('请输入到达地：'))
date = str(input('清输入出发日期（年-月-日）：'))
year = date.split('-')[0]
month = date.split('-')[1]
days = date.split('-')[2]

# 登录部分
opt = Options()
opt.add_argument("--disable-blink-features=AutomationControlled")

web = webdriver.Chrome(chrome_options=opt)

web.implicitly_wait(5)
# 登录选择部分没问题
print('----------------------------------------------')
# 设置隐式等待时间

web.get("https://passport.ctrip.com/user/login?BackUrl=https%3A%2F%2Fflights.ctrip.com%2Fonline%2Fchannel%2Fdomestic#ctm_ref=c_ph_login_buttom")
time.sleep(2)

web.find_element_by_xpath('//*[@id="nloginname"]').send_keys('15535157649')
time.sleep(1)
web.find_element_by_xpath('//*[@id="npwd"]').send_keys('yangjun1!')
time.sleep(1)
web.find_element_by_xpath('//*[@id="normalview"]/form/div[2]/div[2]/label').click()
time.sleep(1)
web.find_element_by_xpath('//*[@id="nsubmit"]').click()
time.sleep(15)



# 输入出发地, 到达地
web.find_element_by_xpath('//*[@id="searchForm"]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div[1]/input').click()
web.find_element_by_xpath('//*[@id="searchForm"]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div[1]/input').send_keys('广州')
time.sleep(1)
print('2222222222222222222222')
web.find_element_by_xpath('//*[@id="searchForm"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[1]/input').click()
web.find_element_by_xpath('//*[@id="searchForm"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[1]/input').send_keys('海口')
time.sleep(1)
# 选择单程
web.find_element_by_xpath('//*[@id="searchForm"]/div/div/div/div[1]/ul/li[1]/span').click()
time.sleep(1)
print('11111111111111111111111')
# 点击搜索_机票信息
web.find_element_by_xpath('//*[@id="searchForm"]/div/button').click()
time.sleep(1)
print('66666666666666666666666')

try:
    # 确认出行提醒
    web.find_element_by_xpath('//*[@id="outerContainer"]/div/div[3]/div').click()
    time.sleep(1)
except:
    pass

# 获取新页面的url
url = web.current_url
print(url)
print('----------------------------------------------')


# 获取航班信息部分
date_url = f'https://flights.ctrip.com/online/list/oneway-can-hak?_=1&depdate={year}-{month}-{days}&cabin=Y_S_C_F'

date_url1 = f'https://flights.ctrip.com/online/list/oneway-can-hak?_=1&depdate=2023-05-18&cabin=Y_S_C_F'
web.get(date_url)

try:
    # 确认出行提醒
    web.find_element_by_xpath('//*[@id="outerContainer"]/div/div[3]/div').click()
    time.sleep(2)
except:
    pass



# xpath获取各航空信息
# 初步筛选：
time.sleep(5)

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

# 调用滑动函数
roll_window_to_bottom(web)
# 等待网站响应完毕
time.sleep(5)
# 滑动到页面顶端
js1 = "window.scrollTo(0, 0)"
web.execute_script(js1)

air_data_list = web.find_elements_by_xpath('//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div')
time.sleep(5)
print(len(air_data_list))

air_list = []
num = 1
tb = pt.PrettyTable()
tb.field_names = ['编号', '航班信息', '出发', '到达', '价格']

for item in air_data_list[:-1]:
    # 航班
    flight = str(item.find_element_by_xpath(".//span[@class='plane-No']").text)
    # 起飞信息
    start_time = str(item.find_element_by_xpath(".//div[@class='depart-box']").text)
    # 到达信息
    arrive_time = str(item.find_element_by_xpath(".//div[@class='arrive-box']").text)
    # 价格
    price = str(item.find_element_by_xpath(".//span[@class='price']").text) + '起'

    # print(f'航班{flight}, 起飞{start_time}，到达{arrive_time}, 价格{price}')
    # print('----------------------------')

    msg = {
        '航班信息': flight,
        '出发': start_time,
        '到达': arrive_time,
        '价格': price,
    }

    air_list.append(msg)
    tb.add_row([num, flight, start_time, arrive_time, price])
    num += 1

print(tb)

select = str(input('请输入您想购买的航班：'))

# 点击订票按钮
if select != '1':
    cont = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div/div[2]/div[2]/button'
    print(f'选择了第{select}趟航班！')
else:
    cont = '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[1]/div/div/div/div/div[2]/div[2]/button'
    print(f'选择了第1趟航班！')
print('77777777777777777777777777')
web.find_element_by_xpath(cont).click()
# element = web.find_element_by_css_selector('div[class*="flight-action"]')
# web.execute_script('arguments[0].click();', element)
print('6666666666666666666666666')
time.sleep(5)

# 获取目标航班下可选套餐
if select != '1':
    sel_pac = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div[2]/div'
    print(f'选择了第{select}趟航班！')
else:
    sel_pac = '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[1]/div/div/div/div[2]/div'
    print('选择了第1趟航班！')
# 点击显示套餐信息：
web.find_element_by_xpath(sel_pac).click()
# 获取套餐信息
package = web.find_elements_by_xpath(sel_pac)
print(package)
print(len(package))

# 判断可选套餐是否有多个，若有只返回第一个套餐，第0个为介绍
if len(package) > 1:
    package = package[1:2]
# 展示第一个套餐信息
for item in package:
    res = item.text
    print(res)
    print('...................................')
# 选购套餐
if '选购' in res:
    # 套餐3选购
    find_foc = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div[2]/div[2]/div[5]/div/div[2]'
    # 点击套餐选购按钮
    web.find_element_by_xpath(find_foc).click()
    time.sleep(3)

    # 获取选购套餐信息
    foc_search = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div[2]/span/div/div'
    foc_res = web.find_elements_by_xpath(foc_search)
    time.sleep(3)
    # for item in foc_res:
    #     print(item.text)
    #     print('++++++++++++++++++++++++')
    # 选择无保险套餐
    finally_search = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div[2]/span/div/div[1]/div[2]/button'
    # 点击预订
    web.find_element_by_xpath(finally_search).click()

# 直接预订
else:
    if select == '1':
        finally_search = '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[1]/div/div/div/div[2]/div[2]/div[5]/div/div[2]'
    else:
        finally_search = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div[2]/div[1]/div[5]/div/div[2]'
    # 点击预订
    web.find_element_by_xpath(finally_search).click()

# 点击出行提醒
try:
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="outerContainer"]/div/div[3]/div').click()
except:
    pass



time.sleep(2)
# 输入乘机人

web.find_element_by_xpath('//*[@id="p_name_0"]').click()
time.sleep(0.5)
web.find_element_by_xpath('//*[@id="p_name_0"]').send_keys('杨珺')
time.sleep(2)
# 输入身份证号

web.find_element_by_xpath('//*[@id="p_card_no_0"]').click()
time.sleep(1)
web.find_element_by_xpath('//*[@id="p_card_no_0"]').send_keys('140222199812132617')
time.sleep(2)
# 输入手机号
web.find_element_by_xpath('//*[@id="p_cellphone_0"]').click()
time.sleep(1)
web.find_element_by_xpath('//*[@id="p_cellphone_0"]').send_keys('15535157649')
time.sleep(2)
# 点击下一步处理
# 进入预定界面

web.find_element_by_xpath('//*[@id="J_saveOrder"]').click()
