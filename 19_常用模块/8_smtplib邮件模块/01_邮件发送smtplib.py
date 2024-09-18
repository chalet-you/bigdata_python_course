# _*_ coding : utf-8 _*_
# @Time : 2024/7/27 14:06
# @Author : chalet.you
# @File : 07_邮件发送smtplib
# @Project : bigdata_python_course

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
# 登录邮件服务器
smtp_obj = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
smtp_obj.login("937259669@qq.com", "akfmfkvffbgtbcbj")  # 括号中对应的是发件人邮箱账号、邮箱密码【用于登录第三方客户端/服务的专用密码，适用于登录以下服务：POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV 服务】
smtp_obj.set_debuglevel(1)  # 显示调式信息

# 设置邮件头信息
msg = MIMEText(_text="Hello，你好，这是一份Python代码测试的邮件，请自行忽略这次的测试", _subtype="plain", _charset="utf-8")
# msg["From"] = Header("from <937259669@qq.com>")  # 发送者
# msg["To"] = Header("to")  # 接收者
# msg["From"] = Header("from <937259669@qq.com>")  # 发送者
# msg["To"] = Header("to <1521907011@qq.com>, <461022755@qq.com>")  # 接收者
msg["From"] = formataddr(('发送者', '937259669@qq.com')) # 发送者
msg["To"] = ','.join([formataddr(('收件者1', '1521907011@qq.com')), formataddr(('收件者2', '461022755@qq.com')), formataddr(('收件者3', 'chalet.you@gmail.com'))])  # 接受者
msg["Subject"] = Header("Python代码测试使用", "utf-8")  # 主题

# 发送
smtp_obj.sendmail("937259669@qq.com", ["1521907011@qq.com", "461022755@qq.com", "chalet.you@gmail.com"], msg.as_string())

# 关闭连接
smtp_obj.quit()
