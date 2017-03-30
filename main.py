#!/usr/bin/env python
#!_*_ coding:utf-8 _*_

import sys
from optparse import OptionParser
from logger_unit import line_no
import traceback
import ast
from color import ColorUnit
import time
from chaxun import ChaXun

Lieche_typedict = {'c':1,'g':2,'d':3,'t':4,'k':5,'z':6,'y':7,'o':8}

task = {}

help = """

命令行火车票查看/抢票器
Usage:
     -m g,z  -f 北京 -t 秦皇岛 -d 2017-03-22

Options:
  -m        列车类型
   c          城际
   g          高铁
   d          动车
   t          特快
   k          快速
   z          直达
   y          旅游
   o          其他
   
  -h/--help   help

"""
def rechaxun():
    print "如果再次查询相同的任务请按 0， 其他请按其他键"
    reset = raw_input('your choice: ')
    if reset == '0':
        print ChaXun(task)
    else:
        fstation = raw_input('出发车站:: ')
        tstation = raw_input('到达车站:')
        date = raw_input('出发日期:')
        mode = raw_input('列车类型:')
        task.update({'mode':mode,'from':fstation,'to':tstation,'date':date})
        print ChaXun(task)


def jiaohu():
    print "接下来想要如何操作呢？"
    print "     tips:"
    print "             1、结束查询"
    print "             2、修改参数，继续查询"
    print "             3、抢票"
    types = raw_input("your choice: ")
    print "your choice is %s"%types
    if int(types) == 1:
        print "任务结束，欢迎再次使用"
        sys.exit(1)
    elif int(types) == 2:
        rechaxun()
    elif int(types) == 3:
        print "111"
    else:
        print "输入参数错误，请重新输入，退出请按1"

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-m", "--Mode", action = 'store', dest = 'Mode', help = 'to specify the railway type')
    parser.add_option('-f', '--From', action = 'store', dest = 'From', type = 'string', help = 'the station to statrt travel')
    parser.add_option('-t', '--To', action = 'store', dest = 'To', type = 'string', help = "the station to end travel")
    parser.add_option('-d', '--Date', action = 'store', dest = 'Date', type = 'string', help = 'the date to start travel')
    color_obj = ColorUnit()
    try:
        (options, args) = parser.parse_args(sys.argv)
    except:
        for i in range(len(sys.argv)):
            if '--help' in sys.argv[i] or '-h' in sys.argv[i]:
                print help
                sys.exit(1)
        print("line:%s parse input param error,  info:%s\n" % (line_no(), sys.exc_info()[1]))
    huoche_list = None
    if options.Mode:
        huoche_list = options.Mode.split(',')
        if type(huoche_list) != type([]):
            color_obj.personal_color_print("the mode list input is not illegal,please usge like -m 'c,g' ", 'blink', 'red', 'white')
            sys.exit(1)
    if not options.From:
        color_obj.personal_color_print("you didn't specify -f from options", 'blink', 'red', 'white')
        sys.exit(1)
    if not options.To:
        color_obj.personal_color_print("you didn't specify -t to options", 'blink', 'red', 'white')
        sys.exit(1)
    date = ""
    if not options.Date:
        color_obj.personal_color_print("you didn't specify -d date options, default %s"%time.strftime('%Y-%m-%d',time.localtime()), 'blink', 'blue', 'white')
        date = time.strftime('%Y-%m-%d',time.localtime())
    else:
        date = options.Date
    task.update({'mode':huoche_list,'from':options.From,'to':options.To,'date':date})
    
    print ChaXun(task)
    while True:
        jiaohu()
   