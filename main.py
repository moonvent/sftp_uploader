from sftp_uploader.applications.dependency_container import DependencyContainer
from dependency_injector.wiring import Provide, inject

from sftp_uploader.applications.sftp_uploader import SftpUploader


@inject
def update_files(sftp_upload: SftpUploader = Provide[DependencyContainer.SftpUploader]):
    sftp_upload.upload_to_remote()


if __name__ == "__main__":
    dependency_container = DependencyContainer()
    dependency_container.init_resources()
    dependency_container.wire(modules=[__name__])

    update_files()

