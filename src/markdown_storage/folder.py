import os

from .exceptions import MarkdownError, MetadataError
from .file import ContentFile


class ContentFolder(object):
    def __init__(self, path):
        path = os.path.abspath(path)

        self._path = path
        self._files = []
        self._folders = []

        for filename in os.listdir(self._path):
            abspath = os.path.join(self._path, filename)
            if os.path.isfile(abspath):
                self._add_file(abspath)
            elif os.path.isdir(abspath):
                self._add_folder(abspath)

    def __repr__(self):
        return os.path.basename(self._path)

    def _add_file(self, filepath):
        if not ContentFile.is_valid(filepath):
            return

        dirname, filename = os.path.split(filepath)
        name, ext = os.path.splitext(filename)

        try:
            d = ContentFile(filepath)
        except (MetadataError, MarkdownError):
            return

        setattr(self, name, d)
        self._files.append(d)

    def _add_folder(self, dirpath):
        _, basename = os.path.split(dirpath)

        d = ContentFolder(dirpath)
        setattr(self, basename, d)
        self._folders.append(d)

    @property
    def folders(self):
        for folder in self._folders:
            yield folder

    @property
    def files(self):
        for file in self._files:
            yield file

    def __iter__(self):
        return iter(self._files)

    # def __next__(self):
    #     import ipdb; ipdb.set_trace()
    #     for file in self._files:
    #         return file
    #     raise StopIteration

    # def sort(self, key=None, reverse=False):
    #     return ContentIterator(self._files, key, reverse)
    #


# class ContentIterator(object):
#     def __init__(self, items, key=None, reverse=False):
#         self.items = sorted(items, key=key, reverse=reverse)
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.i >= len(self.items):
#             raise StopIteration
#
#         item = self.items[self.i]
#         self.i += 1
#
#         return item
#
#     def sorted(self, sort_key):
#         return ContentIterator(self, self.items, sort_key)
#
#
