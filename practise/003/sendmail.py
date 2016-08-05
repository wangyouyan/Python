#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


msg = MIMEText('邮件内容', 'plain', 'utf-8')
msg['From'] = formataddr(["武沛齐",'wptawy@126.com'])
msg['To'] = formataddr(["走人",'424662508@qq.com'])
msg['Subject'] = "主题"

server = smtplib.SMTP("smtp.126.com", 25)
server.login("wptawy@126.com", "WW.3945.59")
server.sendmail('wptawy@126.com', ['424662508@qq.com',], msg.as_string())
server.quit()
