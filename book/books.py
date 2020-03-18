# -*- coding:utf-8 -*-

from urllib import requests
from bs4 import BeautifulSoup
import os


if __name__ == "__main__":
    target = "https://www.biqubao.com/book/17570/"
    req = requests.get(url=target)
    req.encoding = 'gbk'
    save_path = '/Users/jinghuang/desktop/spider/book'
    root_path = 'https://www.biqubao.com'
    # print(req)
    soup = BeautifulSoup(req.text, "html.parser")
    list_tag = soup.div(id="list")
    # print(list_tag)
    title = list_tag[0].dl.dt.string
    print(title)
    dir_path = save_path + '/' + title
    if not os.path.exists(dir_path):
       # os.path.join(save_path, title)
        os.mkdir(dir_path)

    for dd_tag in list_tag[0].dl.find_all('dd'):
        chapter_name = dd_tag.string
        print(dd_tag.a.get('href'))
        chapter_url = root_path + dd_tag.a.get('href')
        chapter_req = requests.get(url=chapter_url)
        chapter_req.encoding = 'gbk'
        chapter_soup = BeautifulSoup(chapter_req.text, "html.parser")
        chapter_tag = chapter_soup.div.find(id='content')
        content_text = str(chapter_tag.text)
        with open(dir_path+'/'+chapter_name+'.txt', 'w') as f:
            f.write('本文网址:'+chapter_url)
            f.write(content_text)

        
        