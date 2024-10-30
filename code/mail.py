#coding=utf-8

import poplib

import email.parser, email.policy

from email import parser

from email.header import decode_header

import base64



# 邮箱账号和授权码

EMAIL_ACCOUNT = '793458423@qq.com'

EMAIL_PASSWORD = 'nagpsdyhhtdgbdef'



# POP3服务器地址和端口号

POP3_SERVER = 'pop.qq.com'

POP3_PORT = 995



# 连接到POP3服务器

conn = poplib.POP3_SSL(POP3_SERVER, POP3_PORT)



# 登录邮箱

conn.user(EMAIL_ACCOUNT)

conn.pass_(EMAIL_PASSWORD)



# 获取邮件列表

resp, mails, octets = conn.list()

print(" 共有  %d 封邮件。" % len(mails))



for index in range(len(mails)):

    resp,lines,octets = conn.retr(index +1)

    msg_content = b'\r\n'.join(lines).decode('utf-8')

    msg = parser.Parser().parsestr(msg_content)

    emailbase = {}

    for line in msg.items():

        header = line[0]

        if header in ['From','Subject','Date']:

            item = decode_header(line[1])[-1]

            code = item[1] if item[1]!=None else 'ascii'

            if isinstance(item[0],bytes):

                value = str(item[0],code)

            else:

                value =item[0]

            emailbase[header] =value

    print("-------------%d%d-------------"%(index+1,len(mails)))

    print("发信信箱："+emailbase['From'])

    print("信件主题："+emailbase['Subject'])

    print("发信时间："+emailbase['Date'])
conn.quit()
