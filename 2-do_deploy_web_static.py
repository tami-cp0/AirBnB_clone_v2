#!/usr/bin/python3
#  Fabric script that distributes an archive to your web servers
from fabric.api import env, put, run, local
from datetime import datetime
import os

env.hosts = ['54.157.167.117', '54.160.75.58']


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    now = datetime.utcnow()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = f"versions/{archive_name}"

    if not os.path.exists("versions"):
        if local("mkdir versions").failed:
            return None

    if local(f"tar -cvzf {archive_path} web_static").succeeded:
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        return False

    archive_filename = os.path.basename(archive_path).split(".")[0]
    tar_file = os.path.basename(archive_path)

    # Upload the archive to the remote server
    if put(archive_path, f"/tmp/{tar_file}").failed:
        return False

    # remove previous archive file
    if run(f"rm -rf /data/web_static/releases/{tar_file}*").failed:
        return False

    # Create directory for extraction
    if run(f"mkdir -p /data/web_static/releases/{archive_filename}").failed:
        return False

    # Extract the archive
    if run(f"tar -xzf /tmp/{tar_file} -C "
           f"/data/web_static/releases/{archive_filename}/").failed:
        return False

    # Remove the temporary archive file
    if run(f"rm /tmp/{tar_file}").failed:
        return False

    # Move files to the appropriate location
    if run(f"mv /data/web_static/releases/{archive_filename}/web_s"
           f"tatic/* /data/web_static/releases/{archive_filename}/").failed:
        return False

    # Remove the now empty web_static directory
    if run(f"rm -rf /data/web_static/releases/"
           f"{archive_filename}/web_static").failed:
        return False
    
    # remove the symbolic link
    if run("rm -rf /data/web_static/current").failed:
        return False

    # Update symbolic link
    if run(f"ln -s /data/web_static/releases/"
           f"{archive_filename} /data/web_static/current").failed:
        return False

    return True
