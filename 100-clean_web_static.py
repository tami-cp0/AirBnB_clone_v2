#!/usr/bin/python3
"""
This file contains a script that deletes out-of-date archives
"""
from fabric.api import env, run, local
import os
env.user = 'ubuntu'
env.hosts = ['54.157.167.117', '54.160.75.58']


def do_clean(number=0):
    """
    Deletes out-of-date archives from the versions folder.

    Args:
        number (int, optional): The number of recent archives to keep.
            Defaults to 0, which removes all but the most recent.

    Returns:
        None
    """
    local_files = os.listdir("versions")

    # store remote files
    # number_remote_files = run('ls -1 /data/web_static/releases/ |'
    #                           ' grep "web_static_*" | wc -l')
    number = int(number)
    if number < 1:
        number = 1

    if len(local_files) > number:
        local(f"ls -t versions/ | grep 'web_static_*' |"
              f" tail -n +{number + 1} "
              "| xargs -I % rm versions/%")

    # run(f"ls -t /data/web_static/releases/ | grep 'web_static_*' |"
    #     f"tail -n +{int(number) + 1} |"
    #     "xargs -I % rm -rf /data/web_static/releases/%")

    # Delete unnecessary archives on the servers releases folder
    cmd_list = 'ls -t /data/web_static/releases'
    cmd_tail_h = 'tail -n +{} |'.format(number + 1)
    cmd_tail_b = 'xargs -I {{}} rm -rf /data/web_static/releases/{{}}'
    run(f"{cmd_list} | {cmd_tail_h} {cmd_tail_b}")
