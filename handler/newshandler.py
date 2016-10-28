# -*- coding: utf-8 -*-
# !/usr/bin/env python

__author__ = 'Elf'

import tornado.web
import requests

import json


class NewsHanler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        ostan = args[0]
        daste= args[1]
        url_ = "http://www.servicefarsi.com/api/news/8716045084098/4/item="+daste + ",page=1/ "
        response = requests.get(url_)
        url2 = "http://www.servicefarsi.com/api/news/8716045084098/4/item="+ostan+",page=1/"
        response_ostan = requests.get(url2)
        id_ostan = requests.get("http://www.servicefarsi.com/api/news/8716045084098/2/")
        id_status = requests.get("http://www.servicefarsi.com/api/news/8716045084098/1/")
        id_status = json.loads(id_status.text)
        id_status = id_status['res']
        id_ostan = json.loads(id_ostan.text)
        id_ostan = id_ostan['res']
        response_ostan = json.loads(response_ostan.text)
        data_ostan = response_ostan['res']
        response_data = json.loads(response.text)
        data = response_data['res']
        sid1 = response_data['res'][0]
        sid2 = response_data['res'][1]
        sid3 = response_data['res'][2]
        self.render("index.html", data=data, sid1=sid1, sid2=sid2, sid3=sid3, data_ostan=data_ostan, id_ostan=id_ostan,
                    id_status=id_status,one=ostan,two=daste)

    def post(self, *args, **kwargs):
        ostan = self.get_argument("ostan",None)
        daste = self.get_argument("daste",None)
        url = "/"+ ostan+"-"+daste
        self.redirect(url)


class NewsBodyHanler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        response = requests.get("http://www.servicefarsi.com/api/news/8716045084098/4/item=0,page=3/ ")

        url = "http://www.servicefarsi.com/api/news/8716045084098/7/item=" + args[0]
        response_body = requests.get(url)
        response_body = json.loads(response_body.text)
        response_body_data = response_body['res']
        res = response.text
        response_data = json.loads(res)
        data = response_data['res']
        sid1 = response_data['res'][0]
        sid2 = response_data['res'][1]
        sid3 = response_data['res'][2]
        self.render("body_news.html", sid1=sid1, sid2=sid2, sid3=sid3, response_body_data=response_body_data)
    def post(self, *args, **kwargs):
        pass
