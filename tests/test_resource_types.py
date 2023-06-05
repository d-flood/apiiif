from apiiif.resource_types import (AnnotationPage, Canvas, Manifest,
                                   Collection)
from .helpers import get_image, get_annotation


def test_add_image():
    annotation = get_annotation()
    assert annotation.body is None
    image = get_image()
    annotation.add_image(image)
    assert annotation.body == image


def test_add_multiple_images():
    annotation = get_annotation()
    annotation.add_image(get_image())
    annotation.add_image(get_image())
    annotation.add_image(get_image())
    assert annotation.body.type == 'Choice'
    assert len(annotation.body.items) == 3
    assert (annotation.body.items[0] != annotation.body.items[1] !=
            annotation.body.items[2])


def test_add_annotation():
    annotation = get_annotation()
    annotation_page = AnnotationPage(
        id='http://example.org/iiif/book1/page/p1/1')
    assert len(annotation_page.items) == 0
    annotation_page.add_annotation(annotation)
    assert len(annotation_page.items) == 1
    assert annotation_page.items[0] == annotation


def test_add_annotation_page():
    canvas = Canvas(id='http://example.org/iiif/book1/canvas/p1',
                    label={'en': ['p. 1']},
                    height=1200,
                    width=800)
    annotation_page = AnnotationPage(
        id='http://example.org/iiif/book1/page/p1/1')
    assert len(canvas.items) == 0
    canvas.add_annotation_page(annotation_page)
    assert len(canvas.items) == 1
    assert canvas.items[0] == annotation_page


def test_add_canvas():
    manifest = Manifest(id='http://example.org/iiif/book1/manifest',
                        label={'en': ['Book 1']})
    canvas = Canvas(id='http://example.org/iiif/book1/canvas/p1',
                    label={'en': ['p. 1']},
                    height=1200,
                    width=800)
    assert len(manifest.items) == 0
    manifest.add_canvas(canvas)
    assert len(manifest.items) == 1
    assert manifest.items[0] == canvas


def test_add_manifest():
    collection = Collection(id='http://example.org/iiif/collection/top',
                            label={'en': ['Top-Level Collection']})
    manifest = Manifest(id='http://example.org/iiif/book1/manifest',
                        label={'en': ['Book 1']})
    assert len(collection.items) == 0
    collection.add_manifest(manifest)
    assert len(collection.items) == 1
    assert collection.items[0] == manifest