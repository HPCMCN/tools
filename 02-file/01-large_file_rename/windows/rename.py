#coding=utf-8
import re
import os

path = input("请指明批量处理的文件夹: \n")
name_list = os.listdir(path)
name_list.remove("rename.py")
rename_list = filter(lambda name: not re.match(r"^\d", name), name_list)
for name in rename_list:
	nb = re.search(r"\d-", name).group()
	print(name[name.index(nb):])
	new_name = name[name.index(nb):]
	os.system("move \"{}\" \"{}\"".format(name, new_name))

