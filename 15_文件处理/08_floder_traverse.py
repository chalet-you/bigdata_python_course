# _*_ coding : utf-8 _*_
# @Time : 2024/4/24 22:44
# @Author : chalet.you
# @File : 08_floder_traverse
# @Project : bigdata_python_course

import os

dir_path = "F:/BaiduNetdiskDownload/JVM"


def print_dir_all_content(dir_path):
    content_list = os.listdir(dir_path)
    for ele in content_list:
        child_path = dir_path + "/" + ele
        if os.path.isdir(child_path):
            print(f"目录：{child_path}")
            print_dir_all_content(child_path)
        else:
            print(f"文件：{child_path}")


print_dir_all_content(dir_path)
