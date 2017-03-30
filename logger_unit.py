#!/usr/bin/env python
#!_*_coding:utf-8_*_


import logging
import inspect
import os
from os.path import join
from os.path import exists
from os.path import dirname

def enc_addlog(file_name, line_no, info, log_name):
    if not exists(dirname(log_name)):
        os.makedirs(dirname(log_name))
    logger = logging.getLogger()
    handler = logging.FileHandler(log_name)
    logger.addHandler(handler)
    formatter = logging.Formatter('%(asctime)s' + ' - %(levelname)s : %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    # create a handler to output message on the console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)  # turn on the console output
    file_name = file_name.replace("pyc", "py")
    tmp_list = file_name.rsplit('/', 2)
    if len(tmp_list) == 3:
        file_name = join(tmp_list[1], tmp_list[2])
    info = file_name + '.' + str(line_no) + ' ' + info
    logger.info(info)
    logger.removeHandler(handler)
    logger.removeHandler(stream_handler)

def line_no():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

