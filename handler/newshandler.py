# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'Elf'

import tornado.web
import requests

import json


class NewsHanler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        response = requests.get("http://www.servicefarsi.com/api/news/8716045084098/4/item=0,page=3/ ")
        response_ostan = requests.get("http://www.servicefarsi.com/api/news/8716045084098/4/item=19,page=1/")
        response_ostan = json.loads(response_ostan.text)
        data_ostan = response_ostan['res']
        response_data = json.loads(response.text)
        data = response_data['res']
        sid1 = response_data['res'][0]
        sid2 = response_data['res'][1]
        sid3 = response_data['res'][2]
        self.render("index.html",data=data,sid1 = sid1,sid2=sid2,sid3=sid3,data_ostan = data_ostan)

    def post(self, *args, **kwargs):
        pass


class NewsBodyHanler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        response = requests.get("http://www.servicefarsi.com/api/news/8716045084098/4/item=0,page=3/ ")
        id_ostan = requests.get("http://www.servicefarsi.com/api/news/8716045084098/2/")
        id_status = requests.get("http://www.servicefarsi.com/api/news/8716045084098/1/")
        id_status = json.loads(id_status.text)
        id_status = id_status['res']
        id_ostan = json.loads(id_ostan.text)
        id_ostan = id_ostan['res']
        url = "http://www.servicefarsi.com/api/news/8716045084098/7/item=" + args[0]
        response_body = requests.get(url)
        response_body = json.loads(response_body.text)
        response_body_data = response_body['res']
        response_data = json.loads(response.text)
        data = response_data['res']
        sid1 = response_data['res'][0]
        sid2 = response_data['res'][1]
        sid3 = response_data['res'][2]
        self.render("body_news.html",sid1 = sid1,sid2=sid2,sid3=sid3,response_body_data = response_body_data,id_ostan = id_ostan,
                    id_status=id_status)


    def post(self, *args, **kwargs):
        pass