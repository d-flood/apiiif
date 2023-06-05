import pytest

from apiiif.resource_properties import LanguageString


def test_language_string():
    assert LanguageString(en=['test']).dict(exclude_unset=True) == {
        'en': ['test']
    }


def test_language_string_raises_value_error():
    with pytest.raises(ValueError):
        LanguageString()
