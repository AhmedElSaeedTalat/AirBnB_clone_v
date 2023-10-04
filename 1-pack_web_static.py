#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents """
from fabric.api import local
from datetime import datetime
import re


def do_pack():
    """ do_pack(): packs dir """
    date = datetime.now().isoformat()
    date = re.findall('\\d+', date)
    date = ''.join(date)
    name = f'web_static_{date}.tgz'
    local("mkdir -p versions")
    local(f"tar -czvf ./versions/{name} ./web_static")
