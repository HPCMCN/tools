#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-10-10 11:35:33
# grep = type("grep", (), {"py": 111})

def _after_param():
    while True:
        try:
            cmd_param = input()
            if __file__.endswith(cmd_param) is True:
                continue
            yield cmd_param
        except:
            return

class CmdParam(object):
    def __init__(self):
        self._after_params = [cmd for cmd in _after_param()]
    
    def __getitem__(self, item):
        return self._after_params[item]



cmd_list = CmdParam()

if __name__ == "__main__":
    for cmd in cmd_list:
        print(cmd)
