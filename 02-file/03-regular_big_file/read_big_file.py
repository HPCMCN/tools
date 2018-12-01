# coding = utf-8
import time


def read_big_file1(fp, reg, size=102):
    """性能较好"""
    temp = ""
    while True:
        read_str = fp.read(size)
        temp += read_str
        if reg in temp:
            temp = temp.split(reg)
            temp, lines = temp[-1], temp[:-1]
            yield from lines
        if not read_str:
            yield temp
            break


def read_big_file2(fp, reg, size=102):
    temp = ""
    while True:
        read_str = fp.read(size)
        temp += read_str
        while reg in temp:
            index = temp.index(reg)
            yield temp[:index]
            temp = temp[index + len(reg):]
        if not read_str:
            yield temp
            break

def parse_file1():
    t = time.time()
    with open("1.txt", "r") as f:
        for line in read_big_file1(f, "{|}"):
            pass
    return time.time() - t

def parse_file2():
    t = time.time()
    with open("1.txt", "r") as f:
        for line in read_big_file2(f, "{|}"):
            pass
    return time.time() - t

if __name__ == '__main__':
    a = 0
    b = 0
    nb = 50
    for i in range(nb):
        a += parse_file1()
        b += parse_file2()
    print(parse_file1.__name__, a / nb)
    print(parse_file2.__name__, b / nb)
    # import random
    # string="abcdefghijklmnopqrstuvwxyz "
    # with open("1.txt", "w") as f:
    #     for i in range(1024*1024*10):
    #         a = random.choice(string)
    #         if i % random.randint(1, 200) == 0:
    #             f.write("{|}")
    #         f.write(a)


