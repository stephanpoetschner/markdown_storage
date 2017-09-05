import unittest
from unittest import mock

from . import test_data
from .file import ContentFile
from .mixins import FileReaderMixin, MetadataMixin


class FileReaderMixinTest(unittest.TestCase):
    @mock.patch('markdown_storage.mixins.os.path.isfile')
    def test_is_valid(self, patch_isfile):
        patch_isfile.return_value = True

        self.assertEqual(
            FileReaderMixin.is_valid('hello/world.md', ['md',]),
            True)

        self.assertEqual(
            FileReaderMixin.is_valid('hello/world.markdown', ['md', ]),
            False)

    @mock.patch('markdown_storage.mixins.os.path.isfile')
    def test_is_valid_missing_file(self, patch_isfile):
        patch_isfile.return_value = False

        self.assertEqual(
            ContentFile.is_valid('hello/world.md'),
            False)


class MetadataMixinTest(unittest.TestCase):
    def test_success(self):
        raw_meta = test_data.SAMPLE_TEXT_SPLIT[0]
        self.assertEqual(
            dict(MetadataMixin.parse_meta(raw_meta)),
            test_data.SAMPLE_METADATA)

    def test_inheritance(self):

        class InheritedMetadata(MetadataMixin):
            @classmethod
            def annotate_date(cls, data):
                return None

        meta = test_data.SAMPLE_METADATA
        parsed_meta = dict(InheritedMetadata.annotate(meta))
        self.assertEqual(
            parsed_meta['date'],
            None)


class ContentFileTest(unittest.TestCase):
    def test_split(self):
        self.assertEqual(
            ContentFile.split(test_data.SAMPLE_TEXT),
            test_data.SAMPLE_TEXT_SPLIT,
        )
