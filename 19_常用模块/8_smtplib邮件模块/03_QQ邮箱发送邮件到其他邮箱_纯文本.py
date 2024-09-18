# _*_ coding : utf-8 _*_
# @Time : 2024/9/18 22:01
# @Author : chalet.you
# @File : 01_QQ邮箱发送邮件到其他邮箱
# @Project : bigdata_python_course

import smtplib
from email.mime.text import MIMEText

# 定义SMTP服务
mail_host = "smtp.qq.com"
port = 465
mail_user = "937259669@qq.com"
mail_password = "akfmfkvffbgtbcbj"  # 这里是授权码非登陆密码，是用于登录第三方邮件客户端的专用密码

# 定义发邮件用户
sender = "937259669@qq.com"
# 定义收邮件用户
receivers = ["18721055830@163.com", "1521907011@qq.com", "461022755@qq.com"]

# 定义邮件主题
title = "QQ邮件测试"
# 定义邮件正文
msg = "测试邮件是否能正常使用，请不用回复，谢谢"
# 信息的转化
message = MIMEText(_text=msg, _subtype="plain", _charset="utf8")

# 设置邮件发送者
message["From"] = "{}".format(sender)
# 设置邮件接收者
message["To"] = ",".join(receivers)
# 设置主题
message["Subject"] = title

# 设置SMTP服务【网易邮箱】
server = smtplib.SMTP_SSL(mail_host, port)
# 登录
server.login(mail_user, mail_password)

# 邮件的发送
server.sendmail(sender, receivers, message.as_string())

# 退出
server.quit()

