# -*- coding: utf-8 -*-
import json
from urllib.request import quote,urlopen
from urllib import parse
import hashlib

class Tcsl_map(object):   ##objuct 标识继承的类

    def __init__(self):
        global AK;
        global SK;
        AK = "nWhsBZllnFQlQARyMVPQKDeqCiLcIPZd";
        SK = "6xCR37Ic4veKWWhtOw3ZBniU3oWYTWBp";
    def find_address_by_location(self,location,poi):  ## 通过经纬度找地址
        if '' != location:
            queryStr = '/geocoder/v2/?location='+str(location)+'&output=json&pois='+str(poi)+'&ak='+AK;
            encodedStr = quote(queryStr, safe="/:=&?#+!$,;'@()*[]");
            rawStr = encodedStr + SK;
            SN = hashlib.md5(parse.quote_plus(rawStr).encode("utf8")).hexdigest();
            url = "http://api.map.baidu.com/geocoder/v2/?location=" + str(location) + "&output=json&pois="+str(poi)+"&ak="+ AK +"&sn="+ SN;
            print(url);
            result = urlopen(url=url);
            tmp = json.loads(result.read().decode());
            print(tmp)
            address = tmp['result']['formatted_address'];
            country = tmp['result']['addressComponent']['country'];
            province = tmp['result']['addressComponent']['province'];
            city = tmp['result']['addressComponent']['city'];
            district = tmp['result']['addressComponent']['district'];
            town = tmp['result']['addressComponent']['town'];
            street = tmp['result']['addressComponent']['street'];
            street_number = tmp['result']['addressComponent']['street_number'];
            adcode = tmp['result']['addressComponent']['adcode'];
            sematic_description = tmp['result']['sematic_description']
            if 1 == poi:
                poi_addr = tmp['pois']['addr'];
            print("该经纬度:\t"+location+"\n对应的地址为："+country+city+district+town+street+street_number+"\n行政区划代码:"+adcode+"\npoi描述："+sematic_description );

    def find_lacation_by_address(self,address):
        if '' != address:
            queryStr = '/geocoder/v2/?address='+address+'&output=json&ak='+AK;

            # 对queryStr进行转码，safe内的保留字符不转换
            encodedStr = quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

            # 在最后直接追加上yoursk
            rawStr = encodedStr + SK;

            # md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
            # 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
            SN = hashlib.md5(parse.quote_plus(rawStr).encode("utf8")).hexdigest();
            url = "http://api.map.baidu.com/geocoder/v2/?address=" + quote(address) + "&output=json&ak="+ AK +"&sn="+ SN;
            result = urlopen(url=url);
            tmp = json.loads(result.read().decode());
            lng = tmp['result']['location']['lng']; ##经度
            lat = tmp['result']['location']['lat']; ##纬度
            print('经纬度的值分别是：\nlng={}\nlat={}'.format(str(lng),str(lat)));

    def find_addree_for_Ip(self,ip):
        queryStr = '/location/ip?ip='+ ip +'&ak='+ AK;
        encodedStr = quote(queryStr, safe="/:=&?#+!$,;'@()*[]");
        rawStr = encodedStr + SK;
        SN = hashlib.md5(parse.quote_plus(rawStr).encode("utf8")).hexdigest();
        url = "https://api.map.baidu.com/location/ip?ip="+ ip +"&ak="+ AK +"&sn="+SN;
        result = urlopen(url=url);
        tmp = json.loads(result.read().decode());
        address = tmp['address'];
        center_lng = tmp['content']['point']['x'];
        center_lat = tmp['content']['point']['y'];
        print("IP:"+ ip +"\n所在的详细地址为："+address+"\n中心城市经纬度为：lng="+center_lng+"lat="+center_lat);



cf = Tcsl_map()
ad = cf.find_lacation_by_address("广东省深圳市龙岗区彩姿南路38号");
cd = cf.find_addree_for_Ip('183.14.76.52');
cn = cf.find_address_by_location('22.67449006017823,114.12495578550005',0)
