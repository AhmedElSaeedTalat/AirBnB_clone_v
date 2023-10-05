#!/usr/bin/python3
""" distributes an archive to your web servers """
from fabric.api import *
import re
import os
env.hosts = [
        '52.23.178.138',
        '100.25.29.150'
        ]


def do_deploy(archive_path):
    """do_deploy(archive_path): to deploy static code"""
    if archive_path is None or os.path.exists(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        file_name = re.findall('(?<=versions/).+', archive_path)
        file_name = file_name[0]
        pth = f"/data/web_static/releases"
        run(f"mkdir -p {pth}/{file_name.strip('.tgz')}/")
        run(f"tar -xzf /tmp/{file_name} -C {pth}/{file_name.strip('.tgz')}/")
        run(f"rm /tmp/{file_name}")
        run(f"mv {pth}/{file_name.strip('.tgz')}/web_static/* \
                {pth}/{file_name.strip('.tgz')}/")
        run(f"rm -rf {pth}/{file_name.strip('.tgz')}/web_static/")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {pth}/{file_name.strip('.tgz')}/ /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False
