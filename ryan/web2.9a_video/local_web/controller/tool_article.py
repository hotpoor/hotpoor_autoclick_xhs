#!/bin/env python
# coding=utf-8
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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import cv2
import numpy as np
from PIL import Image, ImageDraw
from PIL import ImageFont
import sys
from selenium import webdriver
import time
from random import randrange


@tornado.gen.coroutine
def get_article_info(short_link):
    # short_link = argv_dir.get("--link",None)
    print("short_link:", short_link)
    browser = webdriver.Chrome()
    b = short_link.find('http')
    a = short_link.find('，复制')
    short_link = short_link[b:a]
    browser.get(short_link)
    browser.minimize_window()
    time.sleep(3)
    small_pic = browser.find_element_by_class_name("small-pic")
    div_i_imgs = small_pic.find_elements_by_tag_name("i")
    num = 0
    image_links = []
    t = int(round(time.time() * 1000))  # 毫秒级时间戳
    # download user img
    # a = browser.find_element(By.CLASS_NAME, 'left-img')
    # icon = a.find_element(By.TAG_NAME, 'img').get_attribute('src').split('?imageView2')[0]
    # aim_response = requests.get(icon)
    # f = open(os.path.join(os.path.dirname(__file__), '../static/icon/icon.jpg'), "ab")
    # f.write(aim_response.content)  # 多媒体存储content
    # f.close()

    # -------------------------convert user img
    # print('converting user icon to circle')
    # print('converting user icon to circle')
    # print('converting user icon to circle')
    # # Open the input image as numpy array, convert to RGB
    # img = Image.open(os.path.join(os.path.dirname(__file__), "../static/icon/icon.jpg")).convert("RGB")
    # npImage = np.array(img)
    # h, w = img.size
    # # Create same size alpha layer with circle
    # alpha = Image.new('L', img.size, 0)
    # draw = ImageDraw.Draw(alpha)
    # draw.pieslice([0, 0, h, w], 0, 360, fill=255)
    # # Convert alpha Image to numpy array
    # npAlpha = np.array(alpha)
    # # Add alpha layer to RGB
    # npImage = np.dstack((npImage, npAlpha))
    # # Save with alpha
    # i = Image.fromarray(npImage)
    # # 修改像素
    # i.thumbnail(size=(100, 100), resample=Image.ANTIALIAS)
    # i.save(os.path.join(os.path.dirname(__file__), "../static/icon/icon.png"))
    # print('process done! new png file saved!')
    # print('process done! new png file saved!')
    # print('process done! new png file saved!')

    # get user id

    a = browser.find_element(By.CLASS_NAME, 'name-detail')
    poster_name = a.text
    # end
    # get item id
    item_id = browser.current_url.split('/')[5]

    # download imgs
    for div_i_img in div_i_imgs:
        link = "https://%s?imageView2/2/w/1080/format/jpg" % (
            div_i_img.get_attribute("style").split("https://")[1].split("?imageView2/2/")[0])
        aim_url = link
        print(aim_url)
        aim_response = requests.get(aim_url)
        f = open(os.path.join(os.path.dirname(__file__), '../static/upload/%s_%s.%s' % (t, num, "jpg")), "ab")
        f.write(aim_response.content)  # 多媒体存储content
        f.close()
        image_links.append("/static/upload/%s_%s.%s" % (t, num, "jpg"))
        num += 1
    print(num)
    print(image_links)

    # ----resize img
    for i in image_links:
        # ----resize
        i1 = (os.path.join(os.path.dirname(__file__), '../%s' % i))
        img = cv2.imread(i1, cv2.IMREAD_UNCHANGED)
        width = 600
        height = 800
        dim = (width, height)
        print('resizing the img... file name: %s' % i)
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite(i1, resized)
        print('resize suceed!')

        # --- concatenation ---

        print('candidate name: ...%s' % i1)
        # icon = os.path.join(os.path.dirname(__file__), '../static/icon/icon.png')
        loop_img = (i1)
        i0 = Image.open(os.path.join(os.path.dirname(__file__), '../static/icon/logo.png'))
        # i1 = Image.open(icon)
        i2 = Image.open(loop_img)
        layer = Image.new('RGBA', (600, 800), (0, 0, 0, 0))
        # r, g, b, a = i1.split()
        i2.convert('RGBA')
        layer.paste(i2, (0, 0))
        # i1.convert('RGBA')
        # layer.paste(i1, (70, 40), mask=a)
        i0.convert('RGBA')
        # random
        x = randrange(0,500)
        y = randrange(0,650)
        layer.paste(i0, (x, y), i0)
        draw = ImageDraw.Draw(layer)
        font_path = (os.path.join(os.path.dirname(__file__), 'font.ttf'))
        font = ImageFont.truetype(font_path, 15, encoding="unic")
        #
        x = randrange(0, 550)
        y = randrange(0, 750)
        draw.text((x, y), '@%s' % poster_name, (254, 254, 254), font=font)

        loop_img = loop_img.replace('jpg', 'png')
        print('rename jpg to png')
        print(loop_img)
        loop_img = loop_img.replace('upload', 'resize')
        print('rename upload to resize')
        print(loop_img)
        layer.save(loop_img)
        print('concatenation successful')

        # concatenate poster id name

    # replacement for text
    title = browser.find_element_by_class_name("title").text
    content = browser.find_element_by_class_name("content").text
    title = title.replace('唇泥', '口红唇釉')
    title = title.replace('puco', '口红博主推荐的')
    title = title.replace('PUCO', '口红博主推荐的')
    content = content.replace('唇泥', '口红唇釉')
    content = content.replace('puco', '口红博主推荐的')
    content = content.replace('PUCO', '口红博主推荐的')
    title = title.replace('#', '')
    content = content.replace('#', '')
    title = title.replace('@', '')
    content = content.replace('@', '')
    print('text replacement done!')
    # end

    # get user id number
    print('getting user id num...')
    a = browser.find_element(By.CLASS_NAME, 'left-img')
    a.click()
    browser.switch_to.window(browser.window_handles[1])
    poster_id = browser.current_url.split('user/profile/')[1]

    #vidify
    resize_path = (os.path.join(os.path.dirname(__file__), '../static/resize/'))
    vid_path = (os.path.join(os.path.dirname(__file__), '../static/vid/'))
    os.system('ffmpeg -y -f image2 -r 1.3 -pattern_type glob -i \"%s/*.png\" -pix_fmt yuv420p %stest.mp4' % (resize_path, vid_path))

    result = {
        "type": "news",
        # "icon": icon,
        "image_num": num,
        "title": title,
        "content": content,
        "image_links": image_links,
        "t": t,
        "poster_name": poster_name,
        "poster_id": poster_id,
        "item_id": item_id
    }
    result_json = json_encode(result)
    f = open(os.path.join(os.path.dirname(__file__), '../static/files/%s.%s' % (t, "json")), "ab")
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
        short_link = self.get_argument("short_link", None)
        if not short_link:
            self.finish({"info": "error", "about": "no short link"})
            return
        result = yield get_article_info(short_link)
        self.finish({"info": "ok", "result": result})


class GetArticleJsonAPIHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        t = self.get_argument("t", None)
        if not t:
            self.finish({"info": "error", "about": "no t"})
            return
        f = open(os.path.join(os.path.dirname(__file__), '../static/files/%s.%s' % (t, "json"))).read()
        result = json_decode(f)
        self.finish({"info": "ok", "result": result})


class MakeVideoArticleAPIHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def post(self):
        imgs = json_decode(self.get_argument("imgs", "[]"))
        t = self.get_argument("t", None)
        if not t:
            self.finish({"info": "error"})
            return
        num = 0
        img_remove_list = []
        for img in imgs:
            b64_data = img.split(';base64,')[1]
            data = base64.b64decode(b64_data)
            img_path = os.path.join(os.path.dirname(__file__), '../static/temp/%s_%s.%s' % (t, num, "png"))
            img_path_jpg = os.path.join(os.path.dirname(__file__), '../static/temp/%s_%s.%s' % (t, num, "jpg"))
            f = open(img_path, "ab")
            f.write(data)  # 多媒体存储content
            f.close()
            f_cv = cv2.imread(img_path)
            cv2.imwrite(img_path_jpg, f_cv)
            num += 1
            img_remove_list.append(img_path)
            img_remove_list.append(img_path_jpg)
        imgs_path = os.path.join(os.path.dirname(__file__), '../static/temp')
        video_path = os.path.join(os.path.dirname(__file__), '../static/temp')
        os.system(
            "ffmpeg -y -r 1 -f image2 -i %s/%s_%%d.%s -vcodec libx264 %s/%s.mp4" % (imgs_path, t, "jpg", video_path, t))
        for img_path in img_remove_list:
            os.remove(img_path)
        self.finish({"info": "ok", "video": "/static/temp/%s.mp4" % (t)})
