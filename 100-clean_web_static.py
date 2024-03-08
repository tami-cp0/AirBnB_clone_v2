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
    if int(number) < 1:
        number = 1

    local(f"ls -1 versions/ | tail -n +{int(number) + 1} "
          "| xargs -I % rm versions/%")
    run(f"ls -1 web_static_* &> /dev/null | tail -n +{int(number) + 1} "
        "| xargs -I % rm -rf /data/web_static/releases/%")
