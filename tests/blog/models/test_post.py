import datetime as dt
from model_mommy import mommy
from freezegun import freeze_time
import pytest

from blog.models import Post

pytestmark = pytest.mark.django_db

def test_published_posts_only_returns_published_status():
    post = mommy.make('blog.Post', status=Post.PUBLISHED)
    mommy.make('blog.Post', status=Post.DRAFT)
    expected = [post]

    assert list(Post.objects.published()) == expected


def test_draft_posts_only_returns_draft_status():
    post = mommy.make('blog.Post', status=Post.DRAFT)
    mommy.make('blog.Post', status=Post.PUBLISHED)
    # expected = [post]

    assert list(Post.objects.drafts()) == [post]


@freeze_time(dt.datetime(2020, 1, 1), tz_offset=0)
def test_pubslihed_action():
    post = mommy.make('blog.Post', status=Post.DRAFT, published=None)
    post.publish()

    assert post.status == Post.PUBLISHED
    assert post.published == dt.datetime(2020, 1, 1, tzinfo=dt.timezone.utc)
