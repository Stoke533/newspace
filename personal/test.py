import requests
import re
import random
import csv


url = 'https://search.lrn.cn/was5/web/search?channelid=286455&perpage=&searchword=&KYQMC=%E7%94%98%E8%82%83%E7%9C%81%E5%AE%95%E6%98%8C%E5%8E%BF%E8%8D%89%E5%B1%B1%E6%B2%9F%E4%B8%80%E5%B8%A6%E9%94%91%E7%9F%BF%E8%AF%A6%E6%9F%A5&XKZH=&KYQR=&YXQZ=&x=0&y=0'

# 设置UA池
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.37',
]

headers = {
    'User-Agent': random.choice(user_agent_list),
}
# 执行请求
res = requests.get(url=url, headers=headers).content.decode('utf8')
print(res)

a = re.findall()

qqq = re.findall('<li>.*(.*?).*</li>', res)
print(qqq)


# 打开目标文件
with open('data1.csv', mode='a', encoding='gbk', newline='') as f:
    f.write('简介, 许可证号, 矿业权人, 矿种, 有效期起, 有效期止\n')

# 简介
intro = re.findall('<font color=#FF0000>(.*?)</font></h2>', res)[0]
# 许可证号
permit = re.findall('<div><span>许可证号：(.*?)</span>', res)[0]
# 矿业权人
ownership = re.findall('</span><span>矿业权人：(.*?)</span><span>', res)[0]
# 矿种
mineral_species = re.findall('</span><span>矿种：(.*?)</span><span>', res)[0]
# 有效期起
s_time = re.findall('</span><span>有效期起：(.*?)</span><span>', res)[0]
# 有效期止
e_time = re.findall('</span><span>有效期止：(.*?)</span></div>', res)[0]

# 打开目标文件
with open(f'data1.csv', mode='a', encoding='gbk', newline='') as f:
    csv_write = csv.writer(f)
    # 文件标题
    csv_write.writerow(
        [intro, permit, ownership, mineral_species, s_time, e_time])



