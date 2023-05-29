from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import random
import prettytable as pt
from selenium.webdriver.common.action_chains import ActionChains

# 初步传参
def afferent():
    username = str(input('请输入登录账号：'))
    password = str(input('请输入密码：'))
    name = str(input('请输入姓名：'))
    userID = str(input('请输入身份证号码：'))
    phone = str(input('请输入电话号码：'))
    date = str(input('清输入出发日期（年-月-日）：'))
    return username, password, name, userID, phone, date

# 时间转换函数
def date_trans(date):
    year = date.split('-')[0]
    month = date.split('-')[1]
    days = date.split('-')[2]
    return year, month, days

# 登录函数
def login(username, password):
    web.get("https://passport.ctrip.com/user/login?BackUrl=https%3A%2F%2Fflights.ctrip.com%2Fonline%2Fchannel%2Fdomestic#ctm_ref=c_ph_login_buttom")
    time.sleep(2)

    web.find_element_by_xpath('//*[@id="nloginname"]').send_keys(username)
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="npwd"]').send_keys(password)
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="normalview"]/form/div[2]/div[2]/label').click()
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="nsubmit"]').click()
    # 处理验证
    time.sleep(15)

# 页面滑动
def roll_window_to_bottom(browser, stop_length=None, step_length=300):
    """
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

# 航班信息
def air_data(date):
    # 时间转换
    year = date.split('-')[0]
    month = date.split('-')[1]
    days = date.split('-')[2]
    # 输入出发地, 到达地
    web.find_element_by_xpath('//*[@id="searchForm"]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div[1]/input').click()
    web.find_element_by_xpath(
        '//*[@id="searchForm"]/div/div/div/div[2]/div[1]/div/div[1]/div/div/div[1]/input').send_keys('广州')
    time.sleep(1)

    web.find_element_by_xpath('//*[@id="searchForm"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[1]/input').click()
    web.find_element_by_xpath(
        '//*[@id="searchForm"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[1]/input').send_keys('海口')
    time.sleep(1)
    # 选择单程
    web.find_element_by_xpath('//*[@id="searchForm"]/div/div/div/div[1]/ul/li[1]/span').click()
    time.sleep(1)

    # 点击搜索_机票信息
    web.find_element_by_xpath('//*[@id="searchForm"]/div/button').click()
    time.sleep(1)


    try:
        # 确认出行提醒
        web.find_element_by_xpath('//*[@id="outerContainer"]/div/div[3]/div').click()
        time.sleep(1)
    except:
        pass

    # 获取新页面的url
    url = web.current_url
    # print(url)


    # 获取航班信息部分
    date_url = f'https://flights.ctrip.com/online/list/oneway-can-hak?_=1&depdate={year}-{month}-{days}&cabin=Y_S_C_F'

    web.get(date_url)

    try:
        # 确认出行提醒
        web.find_element_by_xpath('//*[@id="outerContainer"]/div/div[3]/div').click()
        time.sleep(2)
    except:
        pass

    # # 调用滑动函数
    roll_window_to_bottom(web)
    # 等待网站响应完毕
    time.sleep(5)
    # 滑动到页面顶端
    js1 = "window.scrollTo(0, 0)"
    web.execute_script(js1)
    # web.execute_script("document.body.style.zoom='0.5'")

    # 获取航班信息
    air_data_list = web.find_elements_by_xpath('//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div')
    time.sleep(5)
    # print(len(air_data_list))

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
        # 此处改动， 删除了button
        cont = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div/div[2]/div[2]'
        print(f'您选择了第{select}趟航班！')
    else:
        cont = '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[1]/div/div/div/div/div[2]/div[2]/button'
        print(f'您选择了第1趟航班！')
    time.sleep(5)
    # 点击按钮
    print('11111111111111111111111111111')

    web.find_element_by_xpath(cont).click()
    # 等待响应
    time.sleep(5)

    #----------------------------------------------
    # 获取目标航班下可选套餐
    if select != '1':
        # 获取数据
        sel_pac = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div[2]/div'
        print(f'选择了第{select}趟航班！')
    else:
        sel_pac = '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[1]/div/div/div/div[2]/div'
        print('选择了第1趟航班！')
    # 点击显示套餐信息：
    # web.find_element_by_xpath(sel_pac).click()
    print('-----------------------------------------------')
    time.sleep(5)
    # 获取套餐信息
    package = web.find_elements_by_xpath(sel_pac)
    print(package)
    print('======================================')

    # 判断可选套餐是否有多个，若有只返回第一个套餐，第0个为介绍
    if len(package) > 1:
        package = package[1:2]
    # 展示第一个套餐信息
    for item in package:
        res = item.text
        print(res)
    # 选购套餐
    if '选购' in res:
        print('进入选购分支')
        find_foc = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div[2]/div[2]/div[5]/div/div[2]'
        # 点击套餐选购按钮
        print('555555555555555555555555555555')
        web.find_element_by_xpath(find_foc).click()
        time.sleep(6)

        # 获取选购套餐信息
        foc_search = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div[2]/span/div/div'
        foc_res = web.find_elements_by_xpath(foc_search)
        print('77777777777777777777777777777777777777777')
        time.sleep(3)

        # 选择无保险套餐
        finally_search = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div[2]/span/div/div[1]/div[2]/button'
        print('88888888888888888888888888888888888888')
        # 点击预订
        web.find_element_by_xpath(finally_search).click()

    # 直接预订
    else:
        # list = ['2','6','9','13','14','15','18','19','20','21']
        # for num in list: num
        if select == '1':
            finally_search = '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[1]/div/div/div/div[2]/div[2]/div[5]/div/div[2]'
        elif (select == '4' or select == '5' or select == '12'):
            finally_search = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div[2]/div[1]/div[5]/div/div[2]'
        else:
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[22]/div/div/div[2]/div[3]/div[5]/div/div[2]'
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[21]/div/div/div[2]/div[2]/div[5]/div/div[2]'
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[20]/div/div/div[2]/div[2]/div[5]/div/div[2]'
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[19]/div/div/div[2]/div[2]/div[5]/div/div[2]'
                              # # 18
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[18]/div/div/div[2]/div[2]/div[5]/div/div[2]'
                              # # 17
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[17]/div/div/div[2]/div[2]/div[5]/div/div[2]'
                              # #16
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[16]/div/div/div[2]/div[2]/div[5]/div/div[2]'
                              # #15
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[15]/div/div/div[2]/div[2]/div[5]/div/div[2]'
                              # #14
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[14]/div/div/div[2]/div[2]/div[5]/div/div[2]'
                              # #13
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[13]/div/div/div[2]/div[2]/div[5]/div/div[2]'
                              # #12
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[12]/div/div/div[2]/div[1]/div[5]/div/div[2]'
                              # #9
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[9]/div/div/div[2]/div[2]/div[5]/div/div[2]'
                              # #6
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[6]/div/div/div[2]/div[2]/div[5]/div/div[2]'
                              # #5
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[5]/div/div/div[2]/div[1]/div[5]/div/div[2]'
                              # #4
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[4]/div/div/div[2]/div[1]/div[5]/div/div[2]'
                              # #2
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[2]/div/div/div[2]/div[2]/div[5]/div/div[2]'
                              # '//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[2]/div/div/div[2]/div[2]/div[5]/div/div[2]'
            finally_search = f'//*[@id="hp_container"]/div[2]/div/div[3]/div[3]/div[2]/span/div[{select}]/div/div/div[2]/div[2]/div[5]/div/div[2]'

        # 点击预订
        time.sleep(6)
        web.find_element_by_xpath(finally_search).click()
        print('过')

# 预订信息
def search(name, userID, phone):
    time.sleep(2)
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
    web.find_element_by_xpath('//*[@id="p_name_0"]').send_keys(name)
    time.sleep(2)
    # 输入身份证号

    web.find_element_by_xpath('//*[@id="p_card_no_0"]').click()
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="p_card_no_0"]').send_keys(userID)
    time.sleep(2)
    # 输入手机号
    web.find_element_by_xpath('//*[@id="p_cellphone_0"]').click()
    time.sleep(1)
    web.find_element_by_xpath('//*[@id="p_cellphone_0"]').send_keys(phone)
    time.sleep(2)
    # 点击下一步处理
    # 进入预定界面
    # web.find_element_by_xpath('//*[@id="J_saveOrder"]').click()


if __name__ == '__main__':
    # 接收初步传入参数
    username, password, name, userID, phone, date = afferent()
    opt = Options()
    opt.add_argument("--disable-blink-features=AutomationControlled")
    web = webdriver.Chrome(chrome_options=opt)
    # 全局隐式等待
    web.implicitly_wait(10)
    # 调用登录函数
    login(username, password)
    # 调用航班信息
    air_data(date)
    # 调用预订信息
    search(name, userID, phone)