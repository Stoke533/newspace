import requests
import re
import json
import pprint
import subprocess
import os

url = 'https://www.bilibili.com/video/BV1Ye4y1K7yB/'
headers = {
    # 浏览器身份证
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    # 从何处跳转
    'referer': 'https://search.bilibili.com/all?vt=81736090&keyword=%E5%90%9B%E7%8E%8B%E4%BD%93%E9%AA%8C%E5%8D%A1%E6%BB%B4&from_source=webtop_search&spm_id_from=333.1007&search_source=3',
    # 浏览器保存的数据 用户足迹
    'cookie': 'buvid3=29C0559C-1C1A-82FC-692F-326CBEA6BDA918038infoc; b_nut=1663393618; _uuid=7227A816-9D72-AF97-C774-3D5175F1D9B118011infoc; i-wanna-go-back=-1; buvid_fp_plain=undefined; nostalgia_conf=-1; CURRENT_BLACKGAP=0; is-2022-channel=1; fingerprint3=72ef60c67d755be71a7b5e0a2214c3a5; buvid4=9FFAA794-1E84-12E6-D96B-B652CCA3A10729971-022070420-IBgZZmhjP8bq8inO%2FAHbLnKuH3USZIEVsqRkMf%2F9aFEmgLEKDqmNGA%3D%3D; rpdid=0zbfVG4o9u|bRD6WU00|7BI|3w1OXnXq; CURRENT_QUALITY=80; LIVE_BUVID=AUTO1416717169241586; CURRENT_FNVAL=4048; hit-new-style-dyn=0; hit-dyn-v2=1; bp_video_offset_488366935=742780341683486800; sid=846qzrgc; b_ut=7; b_lsid=8FC957CC_18543D42A6A; fingerprint=927dab1108dacdd294eba99adb9c6a59; buvid_fp=927dab1108dacdd294eba99adb9c6a59; innersign=1; theme_style=light; PVID=4'
}
yuanma = requests.get(url, headers=headers).text

info = re.findall(r'<script>window.__playinfo__=(.*?)</script>', yuanma)[0]
# pprint.pprint(info)
json_data = json.loads(info)
# pprint.pprint(json_data)

audio_base_url = json_data['data']['dash']['audio'][0]['baseUrl']
video_base_url = json_data['data']['dash']['video'][0]['baseUrl']
audio_baseurl = audio_base_url + '.mp3'
video_baseurl = video_base_url + '.mp4'

audio_foc = requests.get(url=audio_baseurl, headers=headers).content
video_foc = requests.get(url=video_baseurl, headers=headers).content
audio_path = 'music\\' + '1' + '.mp3'
video_path = 'music\\' + '1' + '.mp4'
save_path = 'music\\' + '003' + '.mp4'
# 1. 打开文件
audio = open(audio_path, 'wb')
# 2. 写入音频数据
audio.write(audio_foc)
# 3. 关闭文件
audio.close()

# 1. 打开文件
audio = open(video_path, 'wb')
# 2. 写入视频数据
audio.write(video_foc)
# 3. 关闭文件
audio.close()

# ffmpeg合成音频视频
cmd = f'ffmpeg -i {video_path} -i {audio_path} -c:v copy -c:a aac -strict experimental {save_path} -hide_banner'
subprocess.run(cmd, shell=True)


