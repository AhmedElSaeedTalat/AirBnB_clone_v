#!/usr/bin/python3
""" distributes an archive to your web servers """
from fabric.api import run, put, env
import os
env.hosts = [
        '52.23.178.138',
        '100.25.29.150'
        ]


def do_deploy(archive_path):
    """do_deploy(archive_path): to deploy static code"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')
        file_name = file_name[-1]
        pth = f"/data/web_static/releases"
        no_tgz_file = file_name.strip('.tgz')
        run(f"mkdir -p {pth}/{no_tgz_file}/")
        run(f"tar -xzf /tmp/{file_name} -C {pth}/{no_tgz_file}/")
        run(f"rm /tmp/{file_name}")
        run(f"mv {pth}/{no_tgz_file}/web_static/* {pth}/{no_tgz_file}/")
        run(f"rm -rf {pth}/{no_tgz_file}/web_static/")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {pth}/{no_tgz_file}/ /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False
