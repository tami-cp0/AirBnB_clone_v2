#!/usr/bin/python3
#  Fabric script that distributes an archive to your web servers
from fabric.api import run, put, env, local
import os
env.user = "ubuntu"
env.hosts = ['54.157.167.117', '54.160.75.58']
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Deploys static releases to servers"""
    if not os.path.exists(archive_path):
        return False
    remote_hostnames = ['492915-web-01', '492915-web-02']
    # if os.getenv('HOSTNAME') in remote_hostnames:
    #     try:
    #         archive_filename = os.path.basename(archive_path).split(".")[0]
    #         tar_file = os.path.basename(archive_path)
    #         # remove file
    #         local(f"rm -rf /data/web_static/releases/web_static_*")
    #         # Create directory for extraction
    #         local(f"mkdir -p /data/web_static/releases/{archive_filename}/")
    #         # Extract the archive
    #         local(f"tar -xzvf {archive_path} -C "
    #               f"/data/web_static/releases/{archive_filename}/")
    #         # Remove the temporary archive file
    #         local(f"rm {archive_path}")
    #         # Move files to the appropriate location
    #         local(f"mv /data/web_static/releases/{archive_filename}/web_"
    #               f"static/* /data/web_static/releases/{archive_filename}/")
    #         # Remove the now empty web_static directory
    #         local(f"rm -rf /data/web_static/releases/"
    #               f"{archive_filename}/web_static")
    #         # Update symbolic link
    #         local(f"ln -sf /data/web_static/releases/"
    #               f"{archive_filename} /data/web_static/current")
    #         print("New version deployed!")
    #         return True
    #     except Exception as e:
    #         return False
    # else:
        try:
            archive_filename = os.path.basename(archive_path).split(".")[0]
            tar_file = os.path.basename(archive_path)
            # Upload the archive to the remote server
            put(archive_path, f"/tmp/{tar_file}")
            # remove file
            run(f"rm -rf /data/web_static/releases/web_static_*")
            # Create directory for extraction
            run(f"mkdir -p /data/web_static/releases/{archive_filename}")
            # Extract the archive
            run(f"tar -xzvf /tmp/{tar_file} -C "
                f"/data/web_static/releases/{archive_filename}/")
            # Remove the temporary archive file
            run(f"rm /tmp/{tar_file}")
            # Move files to the appropriate location
            run(f"mv /data/web_static/releases/{archive_filename}"
                f"/web_static/* /data/web_static/releases/{archive_filename}/")
            # Remove the now empty web_static directory
            run(f"rm -rf /data/web_static/releases/"
                f"{archive_filename}/web_static")
            # Update symbolic link
            run(f"ln -sf /data/web_static/releases/"
                f"{archive_filename} /data/web_static/current")
            print("New version deployed!")
            return True
        except Exception as e:
            return False
