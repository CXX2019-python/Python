from lxml import etree
import requests
import re
from urllib import request
import os
# from winlock.main import *


def get_response(url):
    response = requests.get(url)
    return response.text

def text2html(text):
    html = etree.HTML(text)
    return html

def get_image():
    response = get_response('https://www.meituri.com/s/35/')

    html = text2html(response)

    img_urls = html.xpath('/html/body/div[6]/ul/li/a/img/@src')

    if not os.path.exists('F:\\imgs\\'):
        os.mkdir('F:\\imgs\\')

    count = 0
    for img_url in img_urls:
        count += 1
        request.urlretrieve(img_url,f'F:\\imgs\\第{count}张.jpg')
        print('url:'+img_url,end='\n\n')



count = 40
def get_image_with_page(page):
    global count
    response = get_response(f'https://www.meituri.com/s/35/index_{(page-1)}.html')

    html = text2html(response)

    img_urls = html.xpath('/html/body/div[6]/ul/li/a/img/@src')

    if not os.path.exists('F:\\imgs\\'):
        os.mkdir('F:\\imgs\\')


    for img_url in img_urls:
        count += 1
        request.urlretrieve(img_url, f'F:\\imgs\\第{count}张.jpg')
        print('url:'+img_url,end='\n\n')

def get_img():
    get_image()


    # 43页
    for i in range(2,45):
        get_image_with_page(i)


if __name__ == '__main__':
    get_img()



# 注意
# 需要安装requests库
# 图片路径为：F:\imgs
# 可以自己改
