from apiiif.resource_properties import Choice
from .helpers import get_homepage, get_iiif_image, FACTORY as factory


def test_language_string():
    assert factory.langugae_string('test').dict(exclude_unset=True) == {
        'en': ['test']
    }


def test_requiredStatement():
    requiredStatement = factory.requiredStatement('label', 'value')
    assert requiredStatement.dict(exclude_unset=True) == {
        'label': {
            'en': ['label']
        },
        'value': {
            'en': ['value']
        }
    }


def test_thumbnail():
    thumbnail = factory.thumbnail('http://example.com/thumbnail', 100, 200)
    assert thumbnail.id == 'http://example.com/thumbnail'
    assert thumbnail.type == 'Image'
    assert thumbnail.format == 'image/jpeg'
    assert thumbnail.width == 100
    assert thumbnail.height == 200


def test_logo():
    logo = factory.logo('http://example.com/logo', 100, 200)
    assert logo.id == 'http://example.com/logo'
    assert logo.type == 'Image'
    assert logo.format == 'image/png'
    assert logo.width == 100
    assert logo.height == 200


def test_homepage():
    homepage = get_homepage()
    assert homepage.id == 'http://example.com/homepage'
    assert homepage.type == 'Text'
    assert homepage.format == 'text/html'
    assert homepage.language == ['en']
    assert homepage.label.dict(exclude_none=True) == {'en': ['label']}


def test_partOf():
    partOf = factory.partOf('http://example.com/partOf')
    assert partOf.id == 'http://example.com/partOf'
    assert partOf.type == 'Collection'


def test_provider():
    homepage = factory.homepage('http://example.com/homepage', 'label')
    # setup homepage but don't test because it is covered above
    provider = factory.provider('http://example.com/provider', 'label',
                                homepage)
    assert provider.id == 'http://example.com/provider'
    assert provider.type == 'Agent'
    assert provider.label.dict(exclude_none=True) == {'en': ['label']}
    assert provider.homepage == [homepage]
    assert provider.logo[0].id == 'http://example.com/provider'
    assert provider.logo[0].type == 'Image'
    assert provider.logo[0].format == 'image/png'
    assert provider.logo[0].width == 100
    assert provider.logo[0].height == 100


def test_choice():
    choice = factory.choice(['item1', 'item2'])
    assert choice.type == 'Choice'
    assert choice.items == ['item1', 'item2']


def test_imageService():
    imageService = factory.imageService('http://example.com/imageService')
    assert imageService.id == 'http://example.com/imageService'
    assert imageService.type == 'ImageService3'
    assert imageService.profile == 'level0'


def test_collection():
    collection = factory.collection('http://example.com/collection', 'label',
                                    'attribution_label', 'attribution_value')
    assert collection.id == 'http://example.com/collection'
    assert collection.type == 'Collection'
    assert collection.label.dict(exclude_none=True) == {'en': ['label']}
    assert collection.requiredStatement.dict(exclude_none=True) == {
        'label': {
            'en': ['attribution_label']
        },
        'value': {
            'en': ['attribution_value']
        }
    }


def test_manifest():
    manifest = factory.manifest('http://example.com/manifest',
                                'label',
                                summary='summary text',
                                rights='http://example.com/rights',
                                attribution=('attribution_label',
                                             'attribution_value'),
                                partOf_url='http://example.com/partOf')
    assert manifest.id == 'http://example.com/manifest'
    assert manifest.type == 'Manifest'
    assert manifest.label.dict(exclude_none=True) == {'en': ['label']}
    assert manifest.summary.dict(exclude_none=True) == {'en': ['summary text']}
    assert manifest.rights == 'http://example.com/rights'
    assert manifest.requiredStatement.dict(exclude_none=True) == {
        'label': {
            'en': ['attribution_label']
        },
        'value': {
            'en': ['attribution_value']
        }
    }
    assert manifest.partOf.id == 'http://example.com/partOf'
    assert manifest.partOf.type == 'Collection'


def test_canvas():
    canvas = factory.canvas('http://example.com/canvas', 'label', 100, 200,
                            'paged')
    assert canvas.id == 'http://example.com/canvas'
    assert canvas.type == 'Canvas'
    assert canvas.label.dict(exclude_none=True) == {'en': ['label']}
    assert canvas.height == 100
    assert canvas.width == 200
    assert canvas.behavior == ['paged']


def test_IIIF_image():
    IIIF_image = get_iiif_image()
    assert IIIF_image.id == 'http://example.com/thumbnail'
    assert IIIF_image.type == 'Image'
    assert IIIF_image.format == 'image/jpeg'
    assert IIIF_image.width == 100
    assert IIIF_image.height == 200
    assert IIIF_image.service[0].dict(exclude_none=True) == {
        'id': 'http://example.com/iiif_root',
        'type': 'ImageService3',
        'profile': 'level0'
    }


def test_annotation_page_single_image():
    iiif_image = get_iiif_image()
    annotation_page = factory.annotation_page('http://example.com',
                                              'http://example.com/canvas',
                                              iiif_image)
    assert annotation_page.id == 'http://example.com/annotationpage'
    assert annotation_page.items[0].id == 'http://example.com/annotation'
    assert annotation_page.items[0].body == iiif_image


def test_annotation_page_choice():
    iiif_image1 = get_iiif_image()
    iiif_image2 = get_iiif_image()
    annotation_page = factory.annotation_page('http://example.com',
                                              'http://example.com/canvas',
                                              [iiif_image1, iiif_image2])
    assert isinstance(annotation_page.items[0].body, Choice)
