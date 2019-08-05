import unittest

from buzz import generator


def test_sample_single_word():
    list_data = ("foo", "bar", "foobar")
    word = generator.sample(list_data)
    assert word in list_data


def test_sample_multiple_words():
    list_data = ("foo", "bar", "foobar")
    words = generator.sample(list_data, 2)
    assert len(words) == 2
    assert words[0] in list_data
    assert words[1] in list_data
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
