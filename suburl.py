#!python3
# -*- coding:utf-8 -*-

import os
import re

pattern = re.compile(r'//[\w\.]+(googleapis|google)\.com/', re.I)

def replace(path):
    temp_f = open('temp', 'w+',encoding='UTF-8')
    try:
        with open(path,'r',encoding='UTF-8') as f:
            for line in f.readlines():
                if pattern.search(line):
                    r = pattern.sub('//127.0.0.1/', line)       
                else:
                    r = line
                temp_f.write(r)
                temp_f.write('\n')                 
                    
    except:
        print('出现解析错误')
        temp_f.close()
        temp_f = None
    if temp_f:
        temp_f.close()
        os.rename(path, '%s.bak' % path)
        os.rename('temp', path)
        os.remove('%s.bak' % path) 
    

for fpath, dirs, fs in os.walk('./docs'):
    for f in fs:        
        if re.search(r'.html$', f, re.I):
            path = os.path.join(fpath, f)
            print('处理文件', path)
            replace(path)
if os.path.exists('temp'):            
    os.remove('temp')
