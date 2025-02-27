from tabom.models import Article, Like, User


def do_like(user_id: int, article_id: int) -> Like:
    # user = User.objects.get(id=user_id)  # User 객체 가져오기
    # article = Article.objects.get(id=article_id)  # Article 객체 가져오기

    return Like.objects.create(user_id=user_id, article_id=article_id)  # 객체로 저장
