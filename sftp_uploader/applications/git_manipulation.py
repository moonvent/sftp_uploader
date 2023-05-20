"""
    Work with git
"""


from git import DiffIndex, Repo

from sftp_uploader.applications.logs import CustomLogger


class CustomGit:
    """
        Custom git class for our manipulations

        Attributes:
            __repo (Repo): local repo path
    """
    __repo: Repo = None
    logger: CustomLogger = None

    def __init__(self,
                 logger: CustomLogger,
                 ) -> None:
        self.logger = logger
        self.__repo = Repo('.')

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

        
