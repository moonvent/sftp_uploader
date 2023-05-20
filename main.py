

from sftp_uploader.applications.git_manipulation import CustomGit


if __name__ == "__main__":
    print(CustomGit().get_different_files_paths_from_latest_commit())
    ...
