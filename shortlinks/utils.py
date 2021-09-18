from django.conf import settings
from random import choice
from string import ascii_letters, digits


SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 6)
AVAIABLE_CHARS = ascii_letters + digits


def create_random_url(chars=AVAIABLE_CHARS):

    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )


def create_shortened_url(model_instance):

    random_code = create_random_url()
    model_class = model_instance.__class__

    if model_class.objects.filter(shorter_url=random_code).exists():
        return create_shortened_url(model_instance)

    return random_code

