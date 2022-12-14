from datetime import datetime

import pytest

from aluraflix_api.videos.models import Video

pytestmark = pytest.mark.django_db


def test_create(video):
    assert Video.objects.exists()
    assert video.id


def test_str(video):
    assert video.titulo == str(video)


def test_create_and_modified_at(video):
    assert isinstance(video.created_at, datetime)
    assert isinstance(video.modified_at, datetime)


def test_one_to_many(video, categoria):
    assert video.categoria
