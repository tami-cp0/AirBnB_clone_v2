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

    try:
        archive_name = archive_path.split(".")[0]

        # Upload the archive to the remote server
        put(archive_path, "/tmp/")

        # Create directory for extraction
        run(f"mkdir -p /data/web_static/releases/{archive_name}")

        # Extract the archive
        run(f"tar -xzf /tmp/\
        {archive_path} -C /data/web_static/releases/{archive_name}")

        # Remove the temporary archive file
        run(f"rm /tmp/{archive_path}")

        # Move files to the appropriate location
        run(f"mv /data/web_static/releases/\
        {archive_name}/web_static/* /data/web_static/releases/{archive_name}/")

        # Remove the now empty web_static directory
        run(f"rm -rf /data/web_static/releases/{archive_name}/web_static")

        # Update symbolic link
        run(f"ln -sf /data/web_static/releases/\
        {archive_name} /data/web_static/current")

        return True
    except Exception as e:
        return False
