# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import jieba
import os
import wordcloud
from selenium import webdriver
import time
import random
import emoji
from selenium.webdriver.chrome.options import Options
import demjson
import json
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import imageio
from wordcloud import ImageColorGenerator
target_url="https://matsuri.icu/channel/672328094" #嘉然主页
file_dir='./comments/'
diana=["嘉", "然", "洗脚婢", "主人","矮","萝"]
ava=["晚", "顶碗", "水母", "爹","笨"]
bella=["贝", "队长","大聪明","拉"]
carol=["珈", "王力口","乐"]
eileen=["乃", "0", "淋", "琳","坏女人","tom"]
rsq=["细说","口水","烧","骚","风情"]
memberdict={"ava":ava,"bella":bella,"carol":carol,"diana":diana,"eileen":eileen}
def get_urls(url):
    urls=[]
    try:
        # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # d = webdriver.Chrome(options=chrome_options)
        d=webdriver.Chrome()
        d.get(url)
        time.sleep(3.0)
        js = "var q=document.documentElement.scrollTop=10000"
        d.execute_script(js)
        i=0
        for link in d.find_elements_by_css_selector("data-v-70444b60"):
            url=link.get_attribute('href')
            # if "detail" in url:
            i+=1
            if i%2==0:
                print(url)
                urls.append(url)
        return urls
    except:
        return " ERROR "
def download_comments(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    d = webdriver.Chrome(options=chrome_options)
    d=webdriver.Chrome()
    d.get(url)
    d.maximize_window()
    d.execute_script("window.scrollBy(0,600)")
    time.sleep(3.0)
    d.find_element_by_class_name('btn-primary').click()
    time.sleep(3.0)
    d.find_element_by_id('export_dropdown').click()
    d.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[4]/div[1]/div[1]/ul/li[1]/a').click()
def getgraph(wlist,file):
    wordcomment=[]
    # for file in os.listdir(file_dir):
    with open(file_dir + file, 'r',encoding='UTF-8') as f:
        dict = json.load(f)
        comments=dict["full_comments"]
    for comment in comments:
        if "text" in comment.keys():
            for word in wlist:
                if word in comment["text"]:
                    print(comment["text"])
                    wordcomment.append(comment)
    frequency={}
    for i in range(0, int(comments[-1]["time"]/60000)-int(comments[0]["time"]/60000)):
        frequency[i]=0
        for tik in wordcomment:
            if i == int(tik["time"]/60000)-int(comments[0]["time"]/60000):
                frequency[i]=frequency[i]+1
    x_list=list(frequency.keys())
    y_list=frequency.values()
    plt.plot(x_list, y_list, linestyle='solid', color='blue')
    plt.title("rsq")
    plt.xlabel("time/min")
    plt.ylabel("frequency/count")
    plt.show()
def getgraph2(dict,file):
    ava=[]
    bella=[]
    carol=[]
    diana=[]
    eileen=[]
    # for file in os.listdir(file_dir):
    with open(file_dir + file, 'r',encoding='UTF-8') as f:
        alldict = json.load(f)
        comments=alldict["full_comments"]
    for comment in comments:
        if "text" in comment.keys():
            for member in dict.keys():
                if member=="ava":
                    for word in member:
                        if word in comment["text"]:
                            # print(comment["text"])
                            ava.append(comment)
                if member=="bella":
                    for word in member:
                        if word in comment["text"]:
                            # print(comment["text"])
                            bella.append(comment)
                if member=="carol":
                    for word in member:
                        if word in comment["text"]:
                            # print(comment["text"])
                            carol.append(comment)
                if member=="diana":
                    for word in member:
                        if word in comment["text"]:
                            # print(comment["text"])
                            diana.append(comment)
                if member=="eileen":
                    for word in member:
                        if word in comment["text"]:
                            # print(comment["text"])
                            eileen.append(comment)
    frequency1 = {}
    frequency2 = {}
    frequency3 = {}
    frequency4 = {}
    frequency5 = {}
    for i in range(0, int(comments[-1]["time"]/60000)-int(comments[0]["time"]/60000)):
        frequency1[i]=0
        for tik in ava:
            if i == int(tik["time"]/60000)-int(comments[0]["time"]/60000):
                frequency1[i]=frequency1[i]+1
        frequency2[i] = 0
        for tik in bella:
            if i == int(tik["time"] / 60000) - int(comments[0]["time"] / 60000):
                frequency2[i] = frequency2[i] + 1
        frequency3[i] = 0
        for tik in carol:
            if i == int(tik["time"] / 60000) - int(comments[0]["time"] / 60000):
                frequency3[i] = frequency3[i] + 1
        frequency4[i] = 0
        for tik in diana:
            if i == int(tik["time"] / 60000) - int(comments[0]["time"] / 60000):
                frequency4[i] = frequency4[i] + 1
        frequency5[i] = 0
        for tik in eileen:
            if i == int(tik["time"] / 60000) - int(comments[0]["time"] / 60000):
                frequency5[i] = frequency5[i] + 1
    x_list1=list(frequency1.keys())
    y_list1=frequency1.values()
    plt.plot(x_list1, y_list1, linestyle='solid', color='blue',label="ava")
    x_list2 = list(frequency2.keys())
    y_list2 = frequency2.values()
    plt.plot(x_list2, y_list2, linestyle='solid', color='red',label="bella")
    x_list3 = list(frequency3.keys())
    y_list3 = frequency3.values()
    plt.plot(x_list3, y_list3, linestyle='solid', color='purple',label="carol")
    x_list4 = list(frequency4.keys())
    y_list4 = frequency4.values()
    plt.plot(x_list4, y_list4, linestyle='solid', color='pink',label="diana")
    x_list5 = list(frequency5.keys())
    y_list5 = frequency5.values()
    plt.plot(x_list5, y_list5, linestyle='solid', color='black',label="eileen")
    plt.legend()
    plt.title("asoul")
    plt.xlabel("time/min")
    plt.ylabel("frequency/count")
    plt.show()
def getgraph3(word,file):
    wordcomment=[]
    # for file in os.listdir(file_dir):
    with open(file_dir + file, 'r',encoding='UTF-8') as f:
        dict = json.load(f)
        comments=dict["full_comments"]
    for comment in comments:
        if "text" in comment.keys():
            if word in comment["text"]:
                # print(comment["text"])
                wordcomment.append(comment)
    frequency={}
    for i in range(0, int(comments[-1]["time"]/60000)-int(comments[0]["time"]/60000)):
        frequency[i]=0
        for tik in wordcomment:
            if i == int(tik["time"]/60000)-int(comments[0]["time"]/60000):
                frequency[i]=frequency[i]+1
    x_list=list(frequency.keys())
    y_list=frequency.values()
    plt.plot(x_list, y_list, linestyle='solid', color='blue')
    plt.title("rsq")
    plt.xlabel("time/min")
    plt.ylabel("frequency/count")
    plt.show()
def dictget(file):
    counts={}
    with open(file_dir + file, 'r',encoding='UTF-8') as f:
        dict = json.load(f)
        comments=dict["full_comments"]
        for comment in comments:
            if "text" in comment.keys():
                words = jieba.cut_for_search(comment["text"])
                for word in words:
                    if "快" in word:
                        continue
                    if "0" in word:
                        continue
                    if len(word) == 1:
                        continue
                    else:
                        counts[word] = counts.get(word, 0) + 1
    for k in list(counts.keys()):
        val = counts[k]
        if val == 1 or val == 2 or val == 3:
            counts.pop(k)
    #自我过滤
    counts.pop("哈哈")
    counts.pop("什么")
    # counts.pop("耸入")
    return counts
#词云生成器
def word_cloud(dict):
    #蒙版图片路径
    img=imageio.imread('abzjh-xo2nt.jpg')
    w = wordcloud.WordCloud(
        background_color='white',
        mask=img,
        # max_words=300,
        # max_font_size=300,
        # min_font_size=100,
        width=2500,
        height=3000,
        font_path='STZHONGS.TTF',
        mode='RGBA',
        # random_state=1,
        prefer_horizontal=1,
    )
    w.generate_from_frequencies(dict)
    #色彩图片路径
    color_source_image = np.array(Image.open('abzjh-xo2nt.jpg'))
    colormap = ImageColorGenerator(color_source_image)
    colored_image = w.recolor(color_func=colormap)
    #保存为图片
    colored_image.to_file('0509.png')
    # w.generate(text)

word_cloud(dictget("乃琳Queen_【3D】你做过哪些念念不忘的梦？_1620474581055.json"))
# getgraph(rsq,"嘉然今天吃什么_【3D】默契大挑战！！！_1620388423032.json")
# getgraph2(memberdict,"乃琳Queen_【3D】你做过哪些念念不忘的梦？_1620474581055.json")
# getgraph3("","乃琳Queen_【3D】你做过哪些念念不忘的梦？_1620474581055.json")


