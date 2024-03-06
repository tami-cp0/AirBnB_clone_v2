#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
from datetime import datetime
from fabric.api import local
import os


def do_pack():
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
