# import sftp_uploader
from sftp_uploader.applications.pre_commit_actions import pre_commit_actions
from sftp_uploader.services.applications.git_manipulation import add_sftp_upload_in_prehook


if __name__ == "__main__":
    pre_commit_actions()
    # add_sftp_upload_in_prehook()
    ...

