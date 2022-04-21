from pathlib import Path

from ..model import BaseModel


class DocumentModel(BaseModel):
    suffix = '.txt'
    read_mode = 'r'
    write_mode = 'w'
    encoding = 'utf-8'

    def __init__(self, path: str = '', contents: str | bytes = ''):
        self.set_path(path)
        self.contents = contents

    def set_id(self, identifier: str | int):
        self.set_path(str(identifier) + self.suffix)

    # noinspection PyAttributeOutsideInit
    def set_path(self, path: str):
        self.path = path
        self.pathlib_path = Path(path)
        self.filename = self.pathlib_path.name
        self.id = self.pathlib_path.stem
        self.suffix = self.pathlib_path.suffix

    def flush_contents(self):
        kwargs = {
            'file': self.path,
            'mode': self.write_mode
        }

        if self.write_mode != 'wb':
            kwargs['encoding'] = self.encoding

        with open(**kwargs) as f:
            f.write(self.contents)

    def load_contents(self) -> bytes | str:
        kwargs = {
            'file': self.path,
            'mode': self.read_mode
        }

        if self.read_mode != 'rb':
            kwargs['encoding'] = self.encoding

        with open(**kwargs) as f:
            self.contents = f.read()

        return self.contents
