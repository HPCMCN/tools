# coding=utf-8
def lt_one(lt_more):
    str1 = str(lt_more)
    list1 = str1.translate(str.maketrans("[]()''", "¿¿¿¿¿¿")).replace("¿", "").replace(", ", ",").split(",")
    return list1
