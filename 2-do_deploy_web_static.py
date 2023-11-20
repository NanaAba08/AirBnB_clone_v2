#!/usr/bin/python3
"""
Fabric script to distribute an archive to web
servers using the do_deploy function.
"""

from fabric.api import *
from os import path

# Define the web server IPs and username for Fabric
env.hosts = ['34.232.76.165', '54.208.30.45']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """
    Distribute the compressed web static package to web servers.

    :param archive_path: Path to the compressed archive on the local machine.
    :return: True if deployment is successful, False otherwise.
    """

    try:
        # Check if the archive file exists
        if not path.exists(archive_path):
            return False

        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract filename without extension to use as timestamp
        timestamp = archive_path.split('/')[-1].split('.')[0]

        # Create target directory for deployment
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'.format(timestamp))

        # Uncompress the archive to the target directory
        run('sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # Remove the uploaded archive
        run('sudo rm /tmp/{}.tgz'.format(timestamp))

        # Move contents into the target directory
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* '
            '/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        # Remove the extraneous web_static directory
        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'
            .format(timestamp))

        # Delete pre-existing symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('sudo ln -s /data/web_static/releases/web_static_{}/ '
            '/data/web_static/current'.format(timestamp))

        # Return True on success
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
