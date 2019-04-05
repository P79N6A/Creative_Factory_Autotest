#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from applitools.eyes import Eyes
# from applitools.images import Eyes
# from applitools.core import Region
# from applitools.images import Target


import requests
import os

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
webdriver_path = os.path.join(DIR_PATH,'chromedriver')
start_mode = 'local'
get_session_url = 'http://ad.bytedance.net/ad_internal/random_session_url/'


class Driver(object):
    def __init__(self, mode, path):
        self.eyes = Eyes()
        self.eyes.api_key = 'mHHQDYWEGS5AGbjfNoVO1h4oi15w3jiQ4q9DPagYJBA110'

        if mode == 'local':
            self.driver = webdriver.Chrome(path)
        elif mode == 'docker-chrome':
            self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:32768/wd/hub',
                desired_capabilities={'browserName': 'chrome'},
            )

    def open(self):
        self.eyes.open(driver=self.driver, app_name='Creative_Factory',
                  test_name='Auto Regression Test')
        #viewport_size={'width': 800,'height': 600})

    def check_window(self, text):
        self.eyes.check_window(text)


    def get_url(self, url):
        try:
            self.driver.get(url)
        except BaseException as e:
            print(e)

    def add_cookie(self, cookies):
        self.driver.add_cookie(cookie_dict=cookies)

    def find_by_class(self, classname):
        try:
            return self.driver.find_element_by_class_name(classname)
        except BaseException as e:
            print(e)

    def set_size(self):
        self.driver.set_window_size(800,600)

    def click_elem(self, elem):
        try:
            elem.click()
        except BaseException as e:
            print(e)

    def close(self):
        self.driver.close()

    def eye_close(self):
        self.eyes.close()

if __name__ == '__main__':

    r = requests.get(get_session_url)
    res = r.json()
    get_session_key_url = res['session_url']
    res = requests.get(get_session_key_url)
    sessionid = res.json()['session_key']
    cookie = {'name':'sessionid','value':sessionid,'domain':'.toutiao.com','path':'/'}

    driver = Driver(start_mode, webdriver_path)

    driver.open()

    crative_factory_url = 'https://cc.toutiao.com/creative-factory/'
    driver.get_url(crative_factory_url)
    #driver.set_size()
    # add checkwindow 创意工具-首页
    #driver.check_window('创意工具-首页')

    # user_login_state = driver.find_element_by_xpath('//*[@id="app"]/section/header/div/div/div[3]/div/span').text
    # if user_login_state == '未登录':
    #     print('未登录')


    tuling_url = 'https://cc.toutiao.com/creative-factory/tuling/10'
    driver.get_url(tuling_url)
    driver.add_cookie(cookie)
    driver.get_url(tuling_url)
    # add checkwindow 图灵-首页
    #driver.check_window('图灵-首页')


    tuling_elem = driver.find_by_class('lazy-img base-img__body')
    try:
        tuling_elem.click()
    except BaseException as e:
        print(e)
    # add checkwindow 图灵-模板设置
    #driver.check_window('图灵-模板设置')


    miaobi_url = 'https://cc.toutiao.com/creative-factory/miaobi'
    driver.get_url(miaobi_url)
    # add checkwindow 妙笔-首页
    #driver.check_window('妙笔-首页')


    pc_pack_url = 'https://cc.toutiao.com/creative-factory/program-creative-package?source=0'
    driver.get_url(pc_pack_url)
    # add checkwindow 程序化创意包-首页
    #driver.check_window('程序化创意包-首页')


    easy_photo_url = 'https://cc.toutiao.com/creative-factory/easy-photo'
    driver.get_url(easy_photo_url)
    # add checkwindow 易拍推广页
    #driver.check_window('易拍推广页')


    jishi_0_url = 'https://cc.toutiao.com/creative-factory/jishi/0'
    driver.get_url(jishi_0_url)
    # add checkwindow 即视-模板视频
    #driver.check_window('即视-模板视频')


    jishi_1_url = 'https://cc.toutiao.com/creative-factory/jishi/1'
    driver.get_url(jishi_1_url)
    # add checkwindow 即视-智能视频
    #driver.check_window('即视-智能视频')


    jishi_2_url = 'https://cc.toutiao.com/creative-factory/jishi/2'
    driver.get_url(jishi_2_url)
    # add checkwindow 即视-智能配乐
    #driver.check_window('即视-智能配乐')

    driver.eye_close()
    driver.close()
