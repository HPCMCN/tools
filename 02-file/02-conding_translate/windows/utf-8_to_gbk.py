#coding=gbk
utf = str(input("��������Ҫת�����ļ�:\n")) + ".py"
gbk = utf[:-3] + "[��ת]" + ".py"

with open(utf, "rb") as f1, open(gbk, "wb") as f2:
    content = f1.read().decode("utf-8")
    print(gbk)
    f2.write(content.encode("gbk"))
print("ת�����!")
