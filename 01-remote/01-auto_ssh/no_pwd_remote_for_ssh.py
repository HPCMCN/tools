#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-10-10 15:05:01

current_name=HPCM
current_ip=192.168.190.1
remote_path=C:/Users/w5659/.ssh

ssh-keygen -t rsa &&/
scp $HOME/.ssh/id_rsa.pub $current_name@$current_ip:$remote_path/authorized_keys
