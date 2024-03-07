#!/usr/bin/python3
#  Fabric script that distributes an archive to your web servers
from fabric.api import run, put, env
import os
env.user = "ubuntu"
env.hosts = ['54.157.167.117', '54.160.75.58']


def do_deploy(archive_path):
    """Deploys static releases to servers"""
    if not os.path.exists(archive_path):
        return False

    archive_filename = os.path.basename(archive_path).split(".")[0]
    tar_file = os.path.basename(archive_path)
    # Upload the archive to the remote server
    if put(archive_path, f"/tmp/{tar_file}").failed:
        return False
    # remove file
    if run(f"rm -rf /data/web_static/releases/{archive_filename}/").failed:
        return False
    # Create directory for extraction
    if run(f"mkdir -p /data/web_static/releases/{archive_filename}/").failed:
        return False

    # Extract the archive
    if run(f"tar -xzvf /tmp/{tar_file} -C "
        f"/data/web_static/releases/{archive_filename}/").failed:
        return False

    # Remove the temporary archive file
    if run(f"rm /tmp/{tar_file}").failed:
        return False

    # Move files to the appropriate location
    if run(f"mv /data/web_static/releases/{archive_filename}"
        f"/web_static/* /data/web_static/releases/{archive_filename}/").failed:
        return False

    # Remove the now empty web_static directory
    if run(f"rm -rf /data/web_static/releases/{archive_filename}/web_static").failed:
        return False

    # remove the current symbolic link
    if run("rm -rf /data/web_static/current").failed:
        return False

    # Update symbolic link
    if run(f"ln -s /data/web_static/releases/"
        f"{archive_filename}/ /data/web_static/current").failed:
        return False
    return True
