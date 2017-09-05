import os
import yaml

from .exceptions import MetadataError


class FileReaderMixin(object):
    @classmethod
    def is_valid(cls, path, allowed_extensions=None):
        allowed_extensions = (allowed_extensions or [])
        if not os.path.isfile(path):
            return False

        name, ext = os.path.splitext(path)
        if ext.lstrip('.') not in allowed_extensions:
            return False

        return True

    @classmethod
    def read(cls, path):
        with open(path, 'r') as f:
            return f.read()


class MetadataMixin(object):
    @classmethod
    def annotate(cls, meta):
        for key, value in meta.items():
            func_name = 'annotate_' + key

            if hasattr(cls, func_name):
                yield (key, getattr(cls, func_name)(value))
            else:
                yield (key, value)

    @classmethod
    def parse_meta(cls, raw_metadata):
        try:
            meta = dict(yaml.load(raw_metadata))
        except yaml.scanner.ScannerError:
            raise MetadataError()

        return cls.annotate(meta)

