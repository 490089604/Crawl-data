#!/usr/bin/env python3
#coding=utf-8
# @Time    : 2018/5/9 16:57
# @Author  : Changfa Wu
#用于登录东北大学校园网
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
cookie_text=''#自己的cookie_text
cookies = {'cookie':cookie_text}
url = 'http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&'
r = requests.get(url, cookies = cookies, headers = headers)
with open('ipgw_neu.txt', 'wb+') as f:
    f.write(r.content)
