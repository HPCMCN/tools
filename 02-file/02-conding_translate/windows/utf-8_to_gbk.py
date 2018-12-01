#coding=gbk
utf = str(input("请输入需要转化的文件:\n")) + ".py"
gbk = utf[:-3] + "[已转]" + ".py"

with open(utf, "rb") as f1, open(gbk, "wb") as f2:
    content = f1.read().decode("utf-8")
    print(gbk)
    f2.write(content.encode("gbk"))
print("转化完成!")
