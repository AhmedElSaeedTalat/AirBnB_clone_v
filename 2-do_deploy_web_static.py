#!/usr/bin/python3
""" distributes an archive to your web servers """
from fabric.api import *
import re
env.hosts = [
        'ubuntu@52.23.178.138',
        'ubuntu@100.25.29.150'
        ]


def do_deploy(archive_path):
    if archive_path is None:
        return False
    put(archive_path, '/tmp/')
    file_name = re.findall('(?<=versions/).+', archive_path)
    file_name = file_name[0]
    sudo(f"mkdir -p /data/web_static/releases/{file_name.strip('.tgz')}/")
    arg = f"/data/web_static/releases/{file_name.strip('.tgz')}/"
    op1 = sudo(f"tar -xzf /tmp/{file_name} -C {arg}")
    op2 = sudo(f"rm /tmp/{file_name}")
    if op1.failed or op2.failed:
        return False
    arg = f"/data/web_static/releases/{file_name.strip('.tgz')}/web_static/*"
    sudo(f"mv {arg} /data/web_static/releases/{file_name.strip('.tgz')}/")
    arg = f"/data/web_static/releases/{file_name.strip('.tgz')}/web_static/"
    sudo(f"rm -rf {arg}")
    op3 = sudo("rm -rf /data/web_static/current")
    if op3.failed:
        return False
    arg = f"/data/web_static/releases/{file_name.strip('.tgz')}/"
    op4 = sudo(f"ln -s {arg} /data/web_static/current")
    if op4.failed:
        return False
    return True
