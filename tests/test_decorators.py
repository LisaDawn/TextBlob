# -*- coding: utf-8 -*-
import unittest
from nose.plugins.attrib import attr
from nose.tools import *  # PEP8 asserts

from text.decorators import requires_nltk_corpus
from text.exceptions import MissingCorpusException


class Tokenizer(object):

    @requires_nltk_corpus
    def tag(self, text):
        raise LookupError


@attr("py27_only")
def test_decorator_raises_missing_corpus_exception():
    t = Tokenizer()
    with assert_raises(MissingCorpusException):
        t.tag('hello world')

if __name__ == '__main__':
    unittest.main()
