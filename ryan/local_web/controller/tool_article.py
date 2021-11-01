#!/bin/env python
#coding=utf-8
import os
import requests
import time
import tornado
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.escape
from tornado.escape import json_encode, json_decode
import urllib
import urllib.request

import sys
from selenium import webdriver
import time

@tornado.gen.coroutine
def get_article_info(short_link):
    # short_link = argv_dir.get("--link",None)
    print("short_link:",short_link)
    browser = webdriver.Chrome()
    b = short_link.find('http')
    a = short_link.find('，复制')
    short_link = short_link[b:a]
    browser.get(short_link)
    time.sleep(3)
    small_pic = browser.find_element_by_class_name("small-pic")
    div_i_imgs = small_pic.find_elements_by_tag_name("i")
    num = 0
    image_links = []
    t = int(round(time.time() * 1000))  # 毫秒级时间戳
    for div_i_img in div_i_imgs:
        link ="https://%s?imageView2/2/w/1080/format/jpg"%(div_i_img.get_attribute("style").split("https://")[1].split("?imageView2/2/")[0])
        aim_url = link
        print(aim_url)
        aim_response = requests.get(aim_url)
        f = open(os.path.join(os.path.dirname(__file__),'../static/upload/%s_%s.%s'%(t,num,"jpg")), "ab")
        f.write(aim_response.content)  # 多媒体存储content
        f.close()
        image_links.append("/static/upload/%s_%s.%s"%(t,num,"jpg"))
        num +=1
    print(num)
    title = browser.find_element_by_class_name("title").text
    content = browser.find_element_by_class_name("content").text
    title = title.replace('唇泥','口红唇釉')
    title = title.replace('puco', '口红博主推荐的')
    title = title.replace('PUCO', '口红博主推荐的')
    content = content.replace('唇泥','口红唇釉')
    content = content.replace('puco', '口红博主推荐的')
    content = content.replace('PUCO', '口红博主推荐的')
    title = title.replace('#','')
    content = content.replace('#','')
    result = {
        "type":"news",
        "image_num":num,
        "title":title,
        "content":content,
        "image_links":image_links,
        "t":t
    }
    result_json = json_encode(result)
    f = open(os.path.join(os.path.dirname(__file__),'../static/files/%s.%s'%(t,"json")), "ab")
    f.write(result_json.encode())  # 多媒体存储content
    f.close()
    browser.quit()
    return result



class ArticleDemoHandler(tornado.web.RequestHandler):
    def get(self):
        self.time_now = int(time.time())
        self.render("../template/demo/article.html")

class GetArticleInfoAPIHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        short_link = self.get_argument("short_link",None)
        if not short_link:
            self.finish({"info":"error","about":"no short link"})
            return
        result = yield get_article_info(short_link)
        self.finish({"info":"ok","result":result})
class GetArticleJsonAPIHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        t = self.get_argument("t",None)
        if not t:
            self.finish({"info":"error","about":"no t"})
            return
        f = open(os.path.join(os.path.dirname(__file__),'../static/files/%s.%s'%(t,"json"))).read()
        result = json_decode(f)
        self.finish({"info":"ok","result":result})
