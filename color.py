#!/usr/bin/env python
#!_*_coding:utf-8_*_


class ColorUnit(object):
    def __init__(self):
        # this options can be none,that means use default color
        # color_rules = {'taskid':[1,31,41],'author':[2,33,45]}
        self.personal_color_attr = {'all_attr_off':0, 'bold':1, 'underLine':4, 'blink':5, 'invert':7}
        self.personal_color_front = {'black':30, 'red':31, 'green':32, 'yellow':33, 'blue':34, 'purple':35, 'cyan':36, 'white':37}
        self.personal_color_background = {'black':40, 'red':41, 'green':42, 'yellow':43, 'blue':44, 'purple':45, 'cyan':46, 'white':47}

    def set_attribute(self, color_rules, head_str=''):
        self.color_rules = color_rules
        self.head_str = head_str

    def print_detail(self, print_dict, retract, diff_list=[]):
        if not print_dict:
            print("warning,Msg null")
            return
        if type(print_dict) != type({}):
            try:
                print_dict = eval(print_dict)
                if type(print_dict) != type({}):
                    print("error format")
                    return
            except:
                traceback.print_exc()
                return
        if self.head_str != '':
            print self.head_str ,
        if retract:
            print '        taskid', ":", print_dict['taskid'], " ",
        else:
            print 'taskid', ":", print_dict['taskid'], " ",
        print_dict.pop('taskid')
        for key in print_dict:
            if key in self.color_rules and key in diff_list:
                color_u = "\x1B[%d;%d;%dm" % (self.color_rules[key][0], self.color_rules[key][1], self.color_rules[key][2])
                print "%s:" % str(key),
                print "%s %s \x1B[0m" % (color_u, str(print_dict[key])),
            else:
                print key, ":", print_dict[key], " ",
        print ""

    def personal_color_print(self, msg, attr, color, background):
        if msg:
            color = "\x1B[%d;%d;%dm" % (self.personal_color_attr.get(attr, 1), self.personal_color_front.get(color, 'red'), self.personal_color_background.get(background, 'white'))
            print "%s %s \x1B[0m" % (color, msg)

    def personal_color_print_No_NewLine(self, msg, attr, color, background):
        if msg:
            color = "\x1B[%d;%d;%dm" % (self.personal_color_attr.get(attr, 1), self.personal_color_front.get(color, 'red'), self.personal_color_background.get(background, 'white'))
            print "%s %s \x1B[0m" % (color, msg),

