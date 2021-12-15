import os
import os.path
from typing import Literal
from Resources.helpers.convert_zip import CheckFile, ConvertZIP
from Resources.helpers.directory_file import DirectoryFile
from Resources.helpers.url import URL
from Resources.helpers.media_type import media_type

directory_principal = '/Resources/files/'
directory_storage_compressed = '/Resources/compressed_file/'
compressed_files_directory = '{}{}'.format(os.getcwd(), directory_storage_compressed)

def verify_access(items_path: str):
    url_prepare = URL.prepare(items_path)

    path_verify = '{}{}{}'.format(
        os.getcwd(), 
        directory_principal, 
        url_prepare
    )

    if not CheckFile.directory_exists(path_verify)[1]:
        return False
    return path_verify

class Files:
    def __init__(self, path: str) -> None:
        self.path = path

    def get_files_directories(self) -> (dict[str, list] or Literal[False]):
        directory_file = DirectoryFile()
        directory_file._path = self.path
        directory_file.start_search()

        return {
            'path': self.path,
            'directories': directory_file.directories,
            'files': directory_file.records
        }

    async def get_path_file(self) -> (dict[str, list] or Literal[False]):
        convert_zip = ConvertZIP(compressed_files_directory, self.path)

        if os.path.isdir(self.path):
            await convert_zip.start_conversion()
            return {
                'file_path': convert_zip.compressed_file_path,
                'media_type': 'application/zip',
                'file_extension': 'zip'
            }

        _, extencion = os.path.splitext(self.path)
        return {
            'file_path': self.path,
            'media_type': media_type[extencion.strip('.')],
            'file_extension': extencion
        }