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
    number_remote_files = run('ls -1 /data/web_static/releases/ | grep "web_static_*" | wc -l')
    
    if int(number) < 1:
        number = 1

    if len(local_files) > int(number):
        local(f"ls -1 versions/ | head -n -{int(number)} "
              "| xargs -I % rm versions/%")
    
    
    if number_remote_files > number:
        run(f"ls -1 /data/web_static/releases/ | grep 'web_static_*' | head -n -{int(number)} "
            "| xargs -I % rm -rf /data/web_static/releases/%")
    
