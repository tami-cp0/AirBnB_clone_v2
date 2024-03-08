#!/usr/bin/python3
"""
This file contains a script that deletes out-of-date archives
"""
from fabric.api import env, run
from os import listdir, remove
from os.path import isfile, join


env.user = 'ubuntu'
env.hosts = ['54.157.167.117', '54.160.75.58']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1

    # Delete unnecessary archives in the versions folder
    files = [f for f in listdir('versions') if isfile(join('versions', f))]
    files.sort(reverse=True)
    for file in files[number:]:
        remove(join('versions', file))

    # Delete unnecessary archives on the servers releases folder
    cmd_list = 'ls -t /data/web_static/releases'
    cmd_tail_h = 'tail -n +{} |'.format(number + 1)
    cmd_tail_b = 'xargs -I {{}} rm -rf /data/web_static/releases/{{}}'
    run(f"{cmd_list} | {cmd_tail_h} {cmd_tail_b}")
