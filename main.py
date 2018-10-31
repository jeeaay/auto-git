#!python
# -*- coding: UTF-8 -*-

'''
/*
 * @Author: jeay
 * @Date: 2018-10-31 16:30:12
 * @Last Modified by: jeay
 * @Last Modified time: 2018-10-31 16:33:23
 */
'''

import time
from git import Repo, Actor
# pip install gitpython

author = Actor("jeay", "wrjie@msn.cn")
committer = Actor("Auto Git", "wrjie@msn.cn")

dirList = (
    '/rsync/lmlq',
    '/rsync/kefid',
    '/rsync/bd'
)

def main(dirPath):
    repo = Repo(dirPath)
    if repo.is_dirty():
        index = repo.index
        index.add(['*'])
        index.commit('back up at ' + time.strftime('%Y-%m-%d',time.localtime(time.time())), author=author, committer=committer)
        print(dirPath + ' has committed')
    else:
        print(dirPath + ' is clean')

if __name__ == '__main__':
    for dirPath in dirList:
        main(dirPath)
