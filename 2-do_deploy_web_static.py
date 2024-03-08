#!/usr/bin/python3
"""
This file contains a script that distribute an archive to my web servers
using the function do_deploy
"""


import os
from fabric.api import *
from datetime import datetime


env.user = 'ubuntu'
env.hosts = ['34.204.95.239', '54.234.17.205']


def do_pack():
    """This function generates a .tgz archive"""
    local('mkdir -p versions')

    # generate the .tgz archive
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_{}.tgz'.format(time)
    result = local('tar -czvf {} web_static'.format(archive_path))

    # if successful return the archive path
    if result.succeeded:
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False

    print("Deploying new version")

    # extract the filename without extension
    filename = archive_path.split("/")[-1]
    name = filename[: -4]

    # define the release directory using the extracted name
    release_dir = "/data/web_static/releases/{}".format(name)

    # upload and uncompress the archive to a folder
    put(archive_path, "/tmp/")
    run("mkdir -p {}".format(release_dir))
    r = run("tar -xzf /tmp/{} -C {}".format(filename, release_dir))

    if r.failed:
        return False

    # copy files into the right directory
    run("cp -r {}/web_static/* {}".format(release_dir, release_dir))
    run("rm -rf /tmp/{} {}/web_static".format(filename, release_dir))

    # delete symbolic link from web server
    run("rm -rf /data/web_static/current")

    # create a symlink to new version of code
    run("ln -s {} /data/web_static/current".format(release_dir))

    print("New version deployed")

    return True
