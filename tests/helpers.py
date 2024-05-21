from random import choice

from apiiif.resource_properties import ImageService
from apiiif.resource_types import IIIFImage, Annotation
from apiiif.factory import SingleLanguageFactory

FACTORY = SingleLanguageFactory()


def get_image():
    random_int = choice(range(1, 100))
    return IIIFImage(
        id=f"http://example.org/iiif/book1/res/page{random_int}.jpg",
        width=800,
        height=1200,
        service=[ImageService(id="http://example.org/iiif/book1/imageanno/page1")],
    )


def get_homepage():
    return FACTORY.homepage("http://example.com/homepage", "label")


def get_iiif_image():
    return FACTORY.IIIF_image(
        "http://example.com/thumbnail", "http://example.com/iiif_root", 100, 200
    )


def get_annotation():
    return Annotation(
        id="http://example.org/iiif/book1/annotation/p0001-image",
        target="http://example.org/iiif/book1/canvas/p1",
    )
