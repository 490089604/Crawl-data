#!/usr/bin/env python3
#coding=utf-8
# @Time    : 2018/5/9 16:57
# @Author  : Changfa Wu
#用于登录东北大学校园网
import requests
import html5lib
import re
from bs4 import BeautifulSoup


s = requests.Session()
url_login = 'http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&'
'''
action: login
ac_id: 1
user_ip: 
nas_ip: 
user_mac: 
url: 
username: 
password: 
save_me: 0
'''
formdata = {
    'action':'login',
    'ac_id': 1,
    'username': '',#输入账号
    'password': '',#输入密码
    'save_me' : 1
}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}

r = s.post(url_login, data = formdata, headers = headers)
content = r.text
soup = BeautifulSoup(content, 'html5lib')
# captcha = soup.find('img', id = 'captcha_image')这里是验证码操作
# if captcha:
#     captcha_url = captcha['src']
#     re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
#     captcha_id = re.findall(re_captcha_id, content)
#     print(captcha_id)
#     print(captcha_url)
#     captcha_text = input('Please input the captcha:')
#     formdata['captcha-solution'] = captcha_text
#     formdata['captcha-id'] = captcha_id
#     r = s.post(url_login, data = formdata, headers = headers)
# with open('contacts.txt', 'w+', encoding = 'utf-8') as f:
#     f.write(r.text)

