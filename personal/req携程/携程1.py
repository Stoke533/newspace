import requests
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pprint

# opt = Options()
# opt.add_argument("--disable-blink-features=AutomationControlled")
# web = webdriver.Chrome(chrome_options=opt)
#
#
# web.find_element(By.XPATH, '//*[@id="outerContainer"]/div/div[3]/div')


# 设置UA池
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.37',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 YaBrowser/21.6.0.616 Yowser/2.5 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 OPR/77.0.4054.277 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Whale/2.10.123.42 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Vivaldi/4.0.2312.33 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Brave/91.1.25.70 Safari/537.36',
]

# 数据包url
url1 = 'https://flights.ctrip.com/international/search/api/search/batchSearch?v=0.3158621369572654'

headers = {
    'User-Agent': random.choice(user_agent_list),
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Content-Length': '828',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'MKT_CKID=1683855484831.6ca23.j6u7; GUID=09031065219194724659; _RSG=Q64SkN1BeWFsmGtg3grAjA; _RDG=28976899c01ab52bbf3b363617f33ac211; _RGUID=f8282c15-ee70-419a-ab4a-d6a0eadd0c36; _bfaStatusPVSend=1; _abtest_userid=78e823a8-da47-461c-bd16-0a8f5239b042; login_uid=5352C3BCDB70A34C07AF4EFE1EACAC79; login_type=0; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; DUID=u=5352C3BCDB70A34C07AF4EFE1EACAC79&v=0; IsNonUser=F; UUID=2CCDBF32B2AD44E5B887AD21C3F577FD; IsPersonalizedLogin=T; cticket=DCCC5DEA3868763CE55C7008732B8BCD53DC79C14F20A71F4DADBA65153A4DB3; MKT_CKID_LMT=1684486154725; _RF1=2408%3A8226%3A9d11%3A7030%3A8cf%3A29ba%3Aeae%3A13b9; MKT_Pagesource=PC; __zpspc=9.4.1684486154.1684486172.2%234%7C%7C%7C%7C%7C%23; _jzqco=%7C%7C%7C%7C1684486155240%7C1.1329724916.1683855484828.1684486154732.1684486172495.1684486154732.1684486172495.0.0.0.10.10; FlightIntl=Search=[%22CAN|%E5%B9%BF%E5%B7%9E(CAN)|32|CAN|480%22%2C%22HAK|%E6%B5%B7%E5%8F%A3(HAK)|42|HAK|480%22%2C%222023-05-21%22]; _bfi=p1%3D10320673302%26p2%3D0%26v1%3D28%26v2%3D0; _bfaStatus=success; _bfa=1.1683855484678.2j7ip9.1.1684486154569.1684568077086.7.29.1; _bfs=1.2; _ubtstatus=%7B%22vid%22%3A%221683855484678.2j7ip9%22%2C%22sid%22%3A7%2C%22pvid%22%3A29%2C%22pid%22%3A10320673302%7D',
    'Origin': 'https://flights.ctrip.com',
    'Referer': 'https://flights.ctrip.com/online/list/oneway-can-hak?_=1&depdate=2023-05-21&cabin=Y_S_C_F',
    'Scope': 'd',
    'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sign': '83de029b05276ccf60c9efa7015a901f',
    'Token': '1001TqhiOtJqTW0XYnpR73jq7J30yZceHqYBzJDsw4lYa3jzpJb6jslvlXEgzE3gEPZifow9sJpQyZdJXswbGyd6JAqwoTvqnJplwcqvpqjDZyktEtzWkSxMY9pw5DJF4RtdR49wbAjBAE1sJSpw7TjBTWm6vt9EBLR5cySojmlwMXwTUROYsqWcDRFdeA1K8FjQkjhHEUHy0EcPiG9YAEqcYzTy9Ez5YLAyMLvd8WOke39xT0K98jmqyaLI9gwgmj5TwBmeckEH6I1tw05iAaRgEmqYGSyNBil6Y0nWfAehBYL1jGEkbYTqyScWoBepQybAjsEH0Yb3ybXiB9Y3ajdqKNBEBnIUqeH6wdnE50Y6heQfKh1E0srnE5liP8yMPYGEZ0iH3J0zRfEkqYdLwdmyD8j5qEMOyPAEHGjQ4jaE9FiDdJpFYBQWQ9YO5iBmelzWLsJZoeqHYTQRLEtlYOzwaDwDAEgoJoceLXYUE0misZJP1Kl4Y0GJtOYzkEbGYfGydsIloEplwbYkQIMUyLHYX4iPBwToYmtw8LJmsvPtYkZwlpxqhyLQY4Yn3InLeApYTkY5PEcsImFitEXY40v6SI7dKlzv49ec1YHqiN0Y9Mj8cIAELYZaxamiUSJsTez8E7ojD7WmAIfHED4i5Y5FiNwbtjZXraBKQpeB0EUFWtJ6aIBUIOYFoEa3JPSYaPRAFyoDWt9y1Fe9gRB7WGZwclyp4wacrHpKFYFAYSbINSYo6R8tyU0WfdymOe3nRP4WgzRTavfpIAmwQO',
    'Transactionid': '28288725b6f14403b5c1de23e2168d74',

}

# playload中‘transactionID: "137ed66fcb3f473b9cc9a8579647b644"
# headers中的sign值
# sign 值逆向

res = requests.post(url=url1, headers=headers).json()
pprint.pprint(res)
