"""
    Package main sources
"""


from sftp_uploader.applications.dependency_container import DependencyContainer as __DependencyContainer
from sftp_uploader.services.applications import sftp_uploader as __sftp_uploader
from sftp_uploader.services.applications import git_manipulation as __git_manipulation

from sftp_uploader.services.applications.sftp_uploader import update_files
"""
    For user fast link, for example call it just 
    
    Example:
        from sftp_uploader import update_files
"""


def init_dependencies():
    """
        Initialize dependency wiring
    """
    dependency_container = __DependencyContainer()
    dependency_container.init_resources()
    dependency_container.wire(modules=[__sftp_uploader,
                                       __git_manipulation])


init_dependencies()

