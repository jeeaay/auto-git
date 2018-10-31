import time
from git import Repo, Actor

author = Actor("jeay", "wrjie@msn.cn")
committer = Actor("Auto Git", "wrjie@msn.cn")
# commit by commit message and author and committer

def main():
    repo = Repo('/home/w/git/python/gittest')
    if repo.is_dirty():
        index = repo.index
        index.add(['*'])
        index.commit('back up at ' + time.strftime('%Y-%m-%d',time.localtime(time.time())), author=author, committer=committer)
        print('commit')
    else:
        print('is clean')


if __name__ == '__main__':
    main()