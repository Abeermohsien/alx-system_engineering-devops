#!/usr/bin/env python3
# fabric filer.
from fabric import task


@task
def pack(c):
    """pack"""
    c.run("touch holbertonwebapp.tar.gz")
    c.run("tar --exclude='*.tar.gz' -cvzf holbertonwebapp.tar.gz .")


@task
def deploy(c):
    """depoly"""
    c.user = "ubuntu"
    c.put("holbertonwebapp.tar.gz", "/tmp")
    c.run("mkdir /tmp/holbertonwebapp")
    c.run("tar -C /tmp/holbertonwebapp -xzvf /tmp/holbertonwebapp.tar.gz")


@task
def clean(c):
    """remove"""
    c.run("rm holbertonwebapp.tar.gz")
