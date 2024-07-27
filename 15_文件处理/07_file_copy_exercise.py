# _*_ coding : utf-8 _*_
# @Time : 2024/4/24 22:18
# @Author : chalet.you
# @File : 07_file_copy_exercise
# @Project : bigdata_python_course

f_src_path = "F:/BigdataWorkClass/Hadoop生态圈/Day05_20210423_分布式文件系统HDFS/04_软件工具/官方的安装包/hadoop-2.7.5.tar.gz"
f_dst_path = "F:/a/b/c/hadoop-2.7.5.tar_new.gz"

with open(f_src_path, "rb") as f_src:
    with open(f_dst_path, "wb") as f_dst:
        for data in f_src:
            f_dst.write(data)

print("拷贝结束")