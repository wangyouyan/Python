#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import shutil
import zipfile

#s = file("test_json.py")
#d = file("new_json.py","wb")
#d.write(s.read())
#shutil.copyfileobj(s,d,length=20)
#shutil.copytree("1","2")
#shutil.rmtree("2")
shutil.make_archive("2_mew.zip",format="zip",root_dir="2")