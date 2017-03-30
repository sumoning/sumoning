#!/usr/bin/env python
#!_*_coding:utf-8_*_

import requests
import re
import urllib2 
from pprint import pprint
from station import stations
import traceback
import json
from prettytable import PrettyTable

class TrainGet(object):
    def __init__(self,task):
        self.mode = task.mode


def cli(fromstation,tostation,date):
    try:
        fstation = stations.get(fromstation.decode('utf-8'))
        tstation = stations.get(tostation.decode('utf-8'))
    except:
        traceback.print_exc() 
    #
    
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date, fstation, tstation)
    req = urllib2.Request(url)  
    r = urllib2.urlopen(req).read() 

    return json.loads(r)['data']
    
    
def Shuaixuan(typelist,ret):
    result  = {}
    if typelist:
        for row in ret:
            if row.get('queryLeftNewDTO',''):
                data = row.get('queryLeftNewDTO','')
                for re in [record for record in typelist if record != 'o' ]:
                    if re.upper() in data['station_train_code']:
                        result.update({data['station_train_code']:[data['from_station_name'],data['to_station_name'],data['start_time'],data['arrive_time'],data['lishi'],data['swz_num'],data['tz_num'],data['zy_num'],data['ze_num'],data['gr_num'],data['rw_num'],data['yw_num'],data['rz_num'],data['yz_num'],data['wz_num']]})
                if 'o' in typelist:
                    if data['station_train_code'].startswith('C') or data['station_train_code'].startswith('G') or data['station_train_code'].startswith('D') or data['station_train_code'].startswith('Y') or data['station_train_code'].startswith('T') or data['station_train_code'].startswith('K') or data['station_train_code'].startswith('Z'):
                        pass
                    else:
                        result.update({data['station_train_code']:[data['from_station_name'],data['to_station_name'],data['start_time'],data['arrive_time'],data['lishi'],data['swz_num'],data['tz_num'],data['zy_num'],data['ze_num'],data['gr_num'],data['rw_num'],data['yw_num'],data['rz_num'],data['yz_num'],data['wz_num']]})
    else:
        for row in ret:
            if row.get('queryLeftNewDTO',''):
                data = row.get('queryLeftNewDTO','')
                result.update({data['station_train_code']:[data['from_station_name'],data['to_station_name'],data['start_time'],data['arrive_time'],data['lishi'],data['swz_num'],data['tz_num'],data['zy_num'],data['ze_num'],data['gr_num'],data['rw_num'],data['yw_num'],data['rz_num'],data['yz_num'],data['wz_num']]})
    
    
    return result
    
    
    
    
def ChaXun(task):
    trains= PrettyTable()
    trains.field_names=["车次","出发车站","到达车站","出发时间","到达时间","历时","商务座","特等座","一等座","二等座","高级软卧","软卧","硬卧 ","软座 ","硬座","无座"]  
    
    ret = None
    ret = cli(task['from'],task['to'],task['date'])
    
    
    result = Shuaixuan(task['mode'],ret)
    
    for k,v in result.items():
        trains.add_row([k,v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9],v[10],v[11],v[12],v[13],v[14]])
        
    return trains
    
    
    
def parse_station():
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9002"  
    req = urllib2.Request(url)  
    r = urllib2.urlopen(req).read()  
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', r.decode('utf-8'))  
    stations = dict(stations)
    pprint(stations,indent=4)
    
    
if __name__ == "__main__":
    parse_station()
