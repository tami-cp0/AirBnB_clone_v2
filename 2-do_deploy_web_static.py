#!/usr/bin/python3
#  Fabric script that distributes an archive to your web servers
from fabric.api import run, put, env, local
from datetime import datetime
import os
env.user = "ubuntu"
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
    """Deploys static releases to servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path).split(".")[0]
        tar_file = os.path.basename(archive_path)
        # Upload the archive to the remote server
        put(archive_path, f"/tmp/{tar_file}")
        # remove file
        run(f"rm -rf /data/web_static/releases/{archive_filename}/")
        # Create directory for extraction
        run(f"mkdir -p /data/web_static/releases/{archive_filename}/")
        # Extract the archive
        run(f"tar -xzvf /tmp/{tar_file} -C "
            f"/data/web_static/releases/{archive_filename}/")
        # Remove the temporary archive file
        run(f"rm /tmp/{tar_file}")
        # Move files to the appropriate location
        run(f"mv /data/web_static/releases/{archive_filename}"
            f"/web_static/* /data/web_static/releases/{archive_filename}/")
        # Remove the now empty web_static directory
        run(f"rm -rf /data/web_static/releases/{archive_filename}/web_static")
        # remove the current symbolic link
        run("rm -rf /data/web_static/current")
        # Update symbolic link
        run(f"ln -s /data/web_static/releases/"
            f"{archive_filename}/ /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception as e:
        return False
