"""
    Work with ssh connection throught custom SSHClient
"""


from paramiko import SSHClient as ParamikoSSHClient
from paramiko import SFTPClient as ParamikoSFTPClient
from paramiko import AutoAddPolicy

from sftp_uploader.constants.applications.ssh import AUTH_TIMEOUT


class SSHClient:
    """
        Custom class for ssh connection

        Attributes:
            __ssh (paramiko.SSHClient): Main ssh client
    """
    __ssh: ParamikoSSHClient = None
    __sftp: ParamikoSFTPClient= None

    def __init__(self,
                 hostname: str,
                 port: int,
                 username: str,
                 password: str,
                 ) -> None:
        self.__ssh = ParamikoSSHClient()
        self.__ssh.set_missing_host_key_policy(AutoAddPolicy())
        self.__ssh.connect(hostname=hostname, 
                           port=port,
                           username=username,
                           password=password,
                           auth_timeout=AUTH_TIMEOUT)

    def __del__(self):
        self.__ssh.close()

    def __enter__(self):
        return self

    def __exit__(*args, **kwargs):
        return

    def __open_sftp_client(self) -> ParamikoSFTPClient:
        """
            Open sftp client
        """
        self.__sftp = self.__ssh.open_sftp()
        return self.__sftp

    def get_sftp_client(self) -> ParamikoSFTPClient:
        """
            Get sftp client if exists, in another case create and get it
        """
        return self.__sftp and self.__sftp or self.__open_sftp_client()

    
