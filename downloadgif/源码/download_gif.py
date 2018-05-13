#!/usr/bin/env python3
#上面是为了在linux和MAC环境下以exe形式运行
#coding=utf-8
#输出中文，不写会报错
import io  
import sys  
import urllib#访问url
from urllib import request
import datetime
import re#正则表达式更好的方案是使用requests
import os.path
import requests#更好的方案是使用requests
import chardet   #需要导入这个模块，检测编码格式
# 作者：吴长发
#不使用框架爬取网站GIF图片
#Scripy爬虫框架可以进行学习。
def save_file(this_download_url,path):#path是文件,this_download_url下载的url
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    time1=datetime.datetime.now()
    print (str(time1)[:-7],)#输出时间
    if (os.path.isfile(r'E:\学习\python\爬虫\downloadgif\\'[:-1] + path)):#如果path是一个存在的文件，返回True。否则返回False。
        #file_size=os.path.getsize(r'E:\学习\python\爬虫\downloadgif\\'[:-1] + path)/1024/1024
        #print ("File "+path+" ("+ str(file_size)+"Mb) already exists.")

        print ("File "+path+" (Mb) already exists.")
        return
    else:   
        print ("Downloading "+path+"...")
        r = requests.get(this_download_url,stream=True)
        file_path = r'E:\学习\python\爬虫\downloadgif\\'[:-1] + path
        #下载文件
        with open(file_path, "wb") as code:
            code.write(r.content) 
        time2=datetime.datetime.now()
        print (str(time2)[:-7],)
        print (path+" Done.")
        use_time=time2-time1
        print ("Time used: "+str(use_time)[:-7]+", ",)
        file_size=os.path.getsize(file_path)/1024/1024
        print( "File size: "+str(file_size)+" MB, Speed: "+str(file_size/(use_time.total_seconds()))[:4]+"MB/s")
def download_url(website_url):#下载对应url的代码

    header= {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = request.Request(website_url,headers=header)
    content = request.urlopen(req).read()#读取文件
    encode_type = chardet.detect(content)
    #print(encode_type)
    content = content.decode(encode_type['encoding'],'ignore') #进行相应解码，赋给原标识符（变量）,忽略有问题的编码
    print(content)
    while len(content)<100:
        print("try again...")
        content = request.urlopen(req).read()
    print("Web page all length:" +str(len(content)))
    pattern = re.compile(r"(http://s1.dwstatic.com/group1/[.0-9-a-zA-Z]*/[.0-9-a-zA-Z]*/[.0-9-a-zA-Z]*/)([.0-9-a-zA-Z]*.gif)")
    #match = pattern.search(content)
    match = pattern.findall(content)
    '''
    返回字符串
    print(match)
    这里match是一个字符串list,可以只加一个括号提取其中的用户名。
    '''
    if match:
        for i in match:

            temp_a=i[0]+i[1]
            temp_b=i[1]
            save_file(temp_a,temp_b)#原串和第一字符串
    else:
        print ("No gif found.")
#urls=["http://www.46ek.com/view/22133.html",]
urls=['http://tu.duowan.com/m/bxgif']
count=0
print (len(urls),)
print (" gifs to download...")
for i in urls:
    count+=1
    print(count)
    download_url(i)
print( "All done") 