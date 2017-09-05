import os

from markdown import Markdown

from .exceptions import MetadataError
from .mixins import FileReaderMixin, MetadataMixin

import dateutil.parser

_md = Markdown()


class ContentFile(FileReaderMixin, MetadataMixin):
    def __init__(self, path):
        if not ContentFile.is_valid(path):
            raise RuntimeError("'%s' is not a valid ContentFile." % path)

        dirname, filename = os.path.split(path)

        self._path = path
        self.name = filename

        self.meta, self.content = self.parse(path)
        self.meta = dict(self.meta)

    def __repr__(self):
        name, _ = os.path.splitext(os.path.basename(self._path))
        return "<%s (%s)>" % ( self.__class__.__name__, name, )

    def __unicode__(self):
        return self.content

    def __getitem__(self, key):
        return self.meta.get(key)

    @classmethod
    def is_valid(cls, path):
        file_extensions = ['md', 'markdown', 'mkd', 'mdown', ]
        return FileReaderMixin.is_valid(path, file_extensions)

    @classmethod
    def split(cls, data):
        is_meta = True
        metadata_lines = []
        md_lines = []

        for line in data.splitlines():
            if not is_meta:
                md_lines.append(line)
            else:
                metadata_lines.append(line)

            if line.startswith('---'):
                is_meta = False

        return '\n'.join(metadata_lines[:-1]), '\n'.join(md_lines)

    @classmethod
    def parse(cls, path):
        contents = cls.read(path).strip()
        raw_metadata, md = cls.split(contents)

        try:
            meta = cls.parse_meta(raw_metadata)
        except MetadataError:
            raise MetadataError(path)

        content = _md.convert(md)

        return meta, content

    ## hook for MetadataMixin
    @classmethod
    def annotate_date(cls, data):
        return dateutil.parser.parse(data)
