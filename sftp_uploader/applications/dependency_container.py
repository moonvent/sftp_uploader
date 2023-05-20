"""
    Describe project dependencies classes
"""


from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Factory
from sftp_uploader.applications.env_load import Settings

from sftp_uploader.applications.ssh import SSHClient as CustomSSHClient
from sftp_uploader.applications.sftp import SFTPClient as CustomSFTPClient



class DependencyContainer(DeclarativeContainer):
    """
        Contaner with all dependencies
    """

    SSHClient = Singleton(CustomSSHClient,
                          host=Settings.host,
                          port=Settings.port,
                          user=Settings.user,
                          password=Settings.password,
                          )
    SFTPClient = Singleton(SSHClient)


