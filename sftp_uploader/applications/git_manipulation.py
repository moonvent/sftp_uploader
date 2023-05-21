"""
    Work with git
"""


import os
from pathlib import Path
from git import DiffIndex, Repo

from sftp_uploader.applications.logs import CustomLogger
from sftp_uploader.constants.applications.git_manipulation import GIT_IGNORE_FILENAME


class CustomGit:
    """
        Custom git class for our manipulations

        Attributes:
            __repo (Repo): local repo path
            __gitignore (str): local path to gitignore
    """
    logger: CustomLogger = None

    __repo: Repo = None
    __gitignore: str = None

    def __init__(self,
                 logger: CustomLogger,
                 ) -> None:
        self.logger = logger
        self.__get_repo()

    def __set_repo_object(self):
        self.__repo = Repo('.')

    def __is_exist_git(self) -> bool:
        """
            Check, exists git repo or not
        """
        try:
            self.__set_repo_object()

        except Exception as e:
            self.logger.exception('Git doesn\'t exist')
            return False

        else:
            return True

    def __create_repo(self):
        """
            Create git repo in local
        """
        self.__repo = Repo.init('')

    def __get_repo(self):
        """
            Init repo var
        """
        if not self.__is_exist_git:
            self.__create_repo()

        self.__set_repo_object()

    def __get_modified_files(self) -> DiffIndex:
        """
            Get modified files

            Returns:
                DiffIndex: smth like list with modified files
        """
        head_commit = self.__repo.head.commit
        result = head_commit.diff(None)
        self.logger.info(f'Find {len(result)} files to upload')
        return result

    def __get_modified_files_paths(self, 
                                   files: DiffIndex) -> list[str]:
        """
            Get modified files paths

            Args: 
                files (DiffIndex): iterable with changed files

            Returns:
                list[str]: list with mofidied files paths
        """
        return [file.a_path for file in files]

    def get_different_files_paths_from_latest_commit(self) -> list[str]:
        """
            Get modified files

            Returns:
                DiffIndex: smth like list with modified files
        """
        modified_files = self.__get_modified_files()
        paths = self.__get_modified_files_paths(files=modified_files)
        return paths

    def __is_exist_gitignore(self) -> bool:
        return os.path.exists(GIT_IGNORE_FILENAME)

    def __create_gitignore(self):
        open(GIT_IGNORE_FILENAME, 
             'w').close()
        self.__repo.git.add(GIT_IGNORE_FILENAME)

    def __check_gitignore_object(self):
        if not self.__is_exist_gitignore():
            self.__create_gitignore()

    def add_to_gitignote(self, 
                         filename: str):
        """
            Add filename to gitignore if exist
        """
        self.__check_gitignore_object()

        file = Path(GIT_IGNORE_FILENAME)

        if filename not in file.read_text():
            with open(file,
                      'a') as gitignore:
                gitignore.write(f'\n{filename}\n')

