#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import logging

logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)

#on screen
ch = logging.StreamHandler()
#ch.setLevel(logging.WARNING)
ch.setLevel(logging.DEBUG)
#into file
fh = logging.FileHandler("logging_module.log")
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s:  %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

#把screen和file的句柄交给Logger接口执行
logger.addHandler(ch)
logger.addHandler(fh)

logger.debug("debug msg ......")
logger.info("info msg ......")
logger.warning("warning msg ......")
logger.error("error msg ......")