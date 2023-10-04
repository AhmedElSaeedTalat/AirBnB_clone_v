#!/usr/bin/python3
""" distributes an archive to your web servers """
from fabric.api import *
import re
import os
env.hosts = [
        'ubuntu@52.23.178.138',
        'ubuntu@100.25.29.150'
        ]


def do_deploy(archive_path):
    """do_deploy(archive_path): to deploy static code"""
    if archive_path is None or os.path.exists(archive_path) is False:
        return False
    put(archive_path, '/tmp/')
    file_name = re.findall('(?<=versions/).+', archive_path)
    file_name = file_name[0]
    op1 = run(f"mkdir -p /data/web_static/releases/{file_name.strip('.tgz')}/")
    if op1.failed:
        return False
    arg = f"/data/web_static/releases/{file_name.strip('.tgz')}/"
    op2 = run(f"tar -xzf /tmp/{file_name} -C {arg}")
    if op2.failed:
        return False
    op3 = run(f"rm /tmp/{file_name}")
    if op3.failed:
        return False
    arg = f"/data/web_static/releases/{file_name.strip('.tgz')}/web_static/*"
    op4 = run(f"mv {arg} /data/web_static/releases/{file_name.strip('.tgz')}/")
    if op4.failed:
        return False
    arg = f"/data/web_static/releases/{file_name.strip('.tgz')}/web_static/"
    op5 = run(f"rm -rf {arg}")
    if op5.failed:
        return False
    op6 = run("rm -rf /data/web_static/current")
    if op6.failed:
        return False
    arg = f"/data/web_static/releases/{file_name.strip('.tgz')}/"
    op7 = run(f"ln -s {arg} /data/web_static/current")
    if op7.failed:
        return False
    return True
