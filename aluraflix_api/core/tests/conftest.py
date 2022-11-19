import pytest
from django.contrib.auth import get_user_model
from faker import Faker
from rest_framework.test import APIClient

from aluraflix_api.core.models import Categoria, Video

fake = Faker()


User = get_user_model()

pytestmark = pytest.mark.django_db


@pytest.fixture
def user():
    return User.objects.create_user(username='user1', email='user1@email.com', password='123456!!')


@pytest.fixture
def categoria_info():
    return dict(titulo=fake.name(), cor='#030ff')


@pytest.fixture
def categoria(categoria_info):
    return Categoria.objects.create(**categoria_info)


@pytest.fixture
def video_info(categoria):
    return dict(titulo=fake.name(), descricao=fake.sentence(nb_words=20), url=fake.url(), categoria_id=categoria.id)


@pytest.fixture
def video(video_info, categoria):
    return Video.objects.create(**video_info, categoria=categoria)


@pytest.fixture
def list_videos(categoria):
    list_ = [
        Video(titulo=fake.name(), descricao=fake.sentence(nb_words=20), url=fake.url(), categoria=categoria),
        Video(titulo=fake.name(), descricao=fake.sentence(nb_words=20), url=fake.url(), categoria=categoria),
        Video(titulo=fake.name(), descricao=fake.sentence(nb_words=20), url=fake.url(), categoria=categoria),
    ]
    Video.objects.bulk_create(list_)

    return list(Video.objects.all())


@pytest.fixture
def list_videos_fixed_title(categoria):
    list_ = [
        Video(titulo='Video-Jogo ', descricao=fake.sentence(nb_words=20), url=fake.url(), categoria=categoria),
        Video(titulo='Casa da moeda', descricao=fake.sentence(nb_words=20), url=fake.url(), categoria=categoria),
        Video(titulo='Jogo 2', descricao=fake.sentence(nb_words=20), url=fake.url(), categoria=categoria),
    ]
    Video.objects.bulk_create(list_)

    return list(Video.objects.all())


@pytest.fixture
def list_categorias(categoria):
    list_ = [
        Categoria(titulo=fake.name(), cor='red'),
        Categoria(titulo=fake.name(), cor='green'),
    ]
    Categoria.objects.bulk_create(list_)

    return list(Categoria.objects.all())


@pytest.fixture
def client():
    return APIClient()
