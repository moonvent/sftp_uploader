"""
    Work with sftp protocol with custom sftp class
"""


from sftp_uploader.applications.ssh import SSHClient
from paramiko import SFTPClient as ParamikoSFTPClient


class SFTPClient:
    """
        Custom sftp client for our needs
    """
    __ssh: SSHClient = None
    __sftp: ParamikoSFTPClient = None

    def __init__(self,
                 custom_ssh_client: SSHClient) -> None:
        self.__ssh = custom_ssh_client
        self.__sftp = self.__ssh.get_sftp_client()

    def __del__(self):
        self.__sftp.close()

