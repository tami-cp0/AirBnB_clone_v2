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
    files = sorted(os.listdir("versions"))
    file_list = list()

    for file in files:
        num_with_extension = file.split("_")[-1]
        file_number = num_with_extension.split(".")[0]
        if file_number not in file_list:
            file_list.append(file_number)

    for file_number in file_list:
        if number in ["0", "1"]:
            start_index = 1
        else:
            start_index = int(number)

    for i in range(start_index, len(file_list)):
        local_file_path = f'versions/web_static_{file_list[i]}.tgz'
        local(f"rm {local_file_path}")

        remote_file_path = \
            f'/data/web_static/releases/web_static_{file_list[i]}'
        run(f"rm -rf {remote_file_path}")
