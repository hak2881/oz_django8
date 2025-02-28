from django.core.exceptions import BadRequest
from django.db import IntegrityError

from tabom.models import Article, Like, User


def do_like(user_id: int, article_id: int) -> Like:
    # user = User.objects.get(id=user_id)  # User 객체 가져오기
    # article = Article.objects.get(id=article_id)  # Article 객체 가져오기
    try:
        return Like.objects.create(user_id=user_id, article_id=article_id)
    except IntegrityError as e:
        if "FOREIGN KEY (`user_id`)" in e.args[1]:
            raise BadRequest(f"없는 user_id 입니다: {user_id}")
        if "FOREIGN KEY (`article_id`)" in e.args[1]:
            raise BadRequest(f"없는 article_id 입니다: {article_id}")
        raise


def undo_like(user_id: int, article_id: int) -> None:

    # LIMIT 2
    # 많으면 Multiple, 없으면 DoesNotExist
    like = Like.objects.filter(user_id=user_id, article_id=article_id).get().delete()
