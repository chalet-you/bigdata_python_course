# _*_ coding : utf-8 _*_
# @Time : 2024/9/18 22:01
# @Author : chalet.you
# @File : 01_网易邮箱发送邮件到其他邮箱
# @Project : bigdata_python_course

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# 定义SMTP服务
mail_host = "smtp.163.com"
port = 465
mail_user = "18721055830@163.com"
mail_password = "TLuGbLsKpECAz8BB"  # 这里是授权码非登陆密码，是用于登录第三方邮件客户端的专用密码

# 定义发邮件用户
sender = "18721055830@163.com"
# 定义收邮件用户
receivers = ["937259669@qq.com", "1521907011@qq.com", "461022755@qq.com"]

"""邮件的内容部分"""
# 定义邮件主题
title = "带有附件图片的主题邮件"
# 定义邮件正文
msg = "这是一封用python代码发送的邮件，带有图片的附件，注意请不用回复，谢谢"
# 信息的转化
message = MIMEText(_text=msg, _subtype="plain", _charset="utf8")

"""邮件的附件部分_图片部分"""
image_path = "F:/datas/图片资源/1.jpg"
image_part = MIMEImage(open(image_path, mode="rb").read(), image_path.split(".")[-1])
# Content-Disposition：保证图片是可以显示的
# attachment：保证已发送的附件可以预览与下载
image_part.add_header("Content-Disposition", "attachment", filename=image_path.split("/")[-1])

# 邮件的内容与附件进行拼接起来
m = MIMEMultipart()
m.attach(message)
m.attach(image_part)



# 设置邮件发送者
m["From"] = "{}".format(sender)
# 设置邮件接收者
m["To"] = ",".join(receivers)
# 设置主题
m["Subject"] = title

# 设置SMTP服务【网易邮箱】
server = smtplib.SMTP_SSL(mail_host, port)
# 登录
server.login(mail_user, mail_password)

# 邮件的发送
server.sendmail(sender, receivers, m.as_string())

# 退出
server.quit()

