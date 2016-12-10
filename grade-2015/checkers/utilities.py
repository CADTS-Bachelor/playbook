# coding=UTF-8
import os
import time
import subprocess

EXCLUDE_DIRS = ('data', 'checkers')
FNULL = open(os.devnull, 'w')


def list_scripts(script_name):
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(script_dir)
    yield 'LiRui', os.path.join(script_dir, '../../LiRui', script_name)
    for name in filter(lambda f: os.path.isdir(os.path.join(parent_dir, f)) and f not in EXCLUDE_DIRS, os.listdir(parent_dir)):
        yield name, os.path.join(parent_dir, name, script_name)


def check_script(script_name, *args, **kwargs):
    for name, script in list_scripts(script_name):
        if os.path.isfile(script):
            start = time.time()
            try:
                times = 10
                for i in range(times):
                    subprocess.check_call(('python', script) + args, stdout=FNULL)

                cost = time.time() - start
                print('{0}: {1}ms'.format(name, int(cost * 1000 / times)))
            except subprocess.CalledProcessError as ex:
                print('{0}: error {1}'.format(name, ex.returncode))
        else:
            print('{0}: not exists'.format(name))
