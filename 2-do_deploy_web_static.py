#!/usr/bin/python3
#  Fabric script that distributes an archive to your web servers
from fabric.api import run, put, env
import os
env.users = ['ubuntu', 'ubuntu']
env.hosts = ['54.157.167.117', '54.160.75.58']


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    # Upload the archive to the remote server
    if put(archive_path, f"/tmp/{archive_path}",
            mirror_local_mode=True).failed:
        return False

    # Create directory for extraction
    if run(f"mkdir -p /data/web_static/releases/{archive_path[:-4]}").failed:
        return False

    # Extract the archive
    if run(f"tar -xzf /tmp/{archive_path} -C /data/web_static/releases/\
    {archive_path[:-4]}").failed:
        return False

    # Remove the temporary archive file
    if run(f"rm /tmp/{archive_path}").failed:
        return False

    # Move files to the appropriate location
    if run(f"mv /data/web_static/releases/{archive_path[:-4]}/web_static/* \
    /data/web_static/releases/{archive_path[:-4]}/").failed:
        return False

    # Remove the now empty web_static directory
    if run(f"rm -rf /data/web_static/releases/\
    {archive_path[:-4]}/web_static").failed:
        return False

    # Update symbolic link
    if run(f"ln -sf /data/web_static/releases/\
    {archive_path[:-4]} /data/web_static/current").failed:
        return False

    return True
