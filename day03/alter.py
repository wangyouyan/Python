#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def email(arg):
    msg = MIMEText('%s出问题了' % arg, 'plain', 'utf-8')
    msg['From'] = formataddr(["武沛齐",'wangyankwcg.518@163.com'])
    msg['To'] = formataddr(["走人",'wangyouyan201314@163.com'])
    msg['Subject'] = "老男孩儿报警系统"

    server = smtplib.SMTP("smtp.126.com", 25)
    server.login("Wangyankwcg.518@163.com", "wyy123@!@che001")
    server.sendmail('Wangyankwcg.518@163.com', ['wangyouyan201314@163.com',], msg.as_string())
    server.quit()



if __name__ == '__main__':
    cpu = 100
    disk = 500
    ram = 50
    for i in range(1):
        if cpu > 90:
            #发送邮件提醒
            email("CPU")
        if disk > 90:
            #发送邮件提醒
            email("DISK")
        if ram > 40:
            #发送邮件提醒
            email("内存")
