import pytest

from apiiif.resource_properties import LanguageString


def test_language_string():
    assert LanguageString(en=["test"]).model_dump(exclude_unset=True) == {"en": ["test"]}


def test_language_string_raises_value_error():
    with pytest.raises(ValueError):
        LanguageString()


def test_external_auth_service_serializes_context_alias():
    from apiiif.resource_properties import ExternalAuthService

    service = ExternalAuthService(
        label={"en": ["label"]},
        failureHeader={"en": ["failure"]},
        failureDescription={"en": ["description"]},
    )

    assert service.model_dump(by_alias=True)["@context"] == "http://iiif.io/api/auth/1/context.json"
