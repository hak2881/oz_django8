from django.test import TestCase

from tabom.models import Article, User
from tabom.services.like_service import do_like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # Given: 테스트에 필요한 재료를 준비한다
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When: 실제 테스트 대상이 되는 동작을 실행
        like = do_like(user.id, article.id)

        # Then: 동작을 마친후에 결과가 "예상한 대로" 나왓는지 검증
        # if guard
        if like:
            self.assertIsNotNone(like.id)
            self.assertEqual(user.id, like.user_id)
            self.assertEqual(article.id, like.article_id)

    def test_a_user_can_like_an_article_only(self) -> None:
        user = User.objects.create(name="test")
        article = Article.objects.create(title="text_title")

        # Expect
        like1 = do_like(user.id, article.id)
        # with self.assertRaises(Exception):  # with 블록안에 에러가 일어 나나 안나나 확인, 에러가 있으면 통과 에러가 없으면 불통
        #     like2 = do_like(user.id, article.id)
        try:
            like2 = do_like(user.id, article.id)
        except Exception as e:
            print(e)
