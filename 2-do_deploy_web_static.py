#!/usr/bin/python3
""" distributes an archive to your web servers """
from fabric.api import *
import os
from datetime import datetime
import re
env.hosts = [
        '52.23.178.138',
        '100.25.29.150'
        ]


def do_pack():
    """ do_pack(): packs dir """
    date = datetime.now().isoformat()
    date = re.findall('\\d+', date)
    date = ''.join(date)
    name = f'web_static_{date}.tgz'
    local("mkdir -p versions")
    local(f"tar -czvf ./versions/{name} ./web_static")
    if res.succeeded:
        return f"versions/{name}"
    else:
        return None


def do_deploy(archive_path):
    """do_deploy(archive_path): to deploy static code"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')
        file_name = file_name[-1]
        pth = "/data/web_static/releases"
        no_tgz_file = file_name.strip('.tgz')
        run("mkdir -p {}/{}/".format(pth, no_tgz_file))
        run("tar -xzf /tmp/{} -C {}/{}/".format(file_name, pth, no_tgz_file))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/{}/web_static/* {}/{}/"
            .format(pth, no_tgz_file, pth, no_tgz_file))
        run("rm -rf {}/{}/web_static/".format(pth, no_tgz_file))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/{}/ /data/web_static/current".format(pth, no_tgz_file))
        print("New version deployed!")
        return True
    except Exception:
        return False
