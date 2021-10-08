import random
from rest_framework import status
from rest_framework.test import APITestCase, APISimpleTestCase, APITransactionTestCase
from rest_framework.test import APIRequestFactory
from core.models import Page, ContentBase, ContentVideo, ContentAudio, ContentText
from core.views import PageViewSet
from .factories import ContentVideoFactory, ContentAudioFactory, ContentTextFactory, PageFactory


class TestCaseForPage(APITestCase):
    """
    Testing:
    """

    def setUp(self):
        """Page creation"""
        self.page1_title = 'First page'
        self.page2_title = 'Second page'
        self.page1 = PageFactory.create(title=self.page1_title)
        self.page2 = PageFactory.create(title=self.page2_title)
        self.cv_max = 10

        """Content creation"""
        for cv in range(self.cv_max):
            setattr(self, f'cv{cv}_ro', random.randint(0,100))
        for cv in range(self.cv_max):
            setattr(self, f'cv{cv}', ContentVideoFactory.create(
                                        title=f'video {cv}',
                                        url_video=f'video_url {cv}',
                                        url_subtitles=f'subtitles_url {cv}',
                                        ))

        """Place Content on Page"""
        for cv in range(self.cv_max//2):
            self.page1.contentbase_set.add(
                    getattr(self, f'cv{cv}'),
                    through_defaults={
                        'relative_order' : getattr(self, f'cv{cv}_ro')})
        for cv in range(self.cv_max//2, self.cv_max):
            self.page2.contentbase_set.add(
                    getattr(self, f'cv{cv}'),
                    through_defaults={
                        'relative_order' : getattr(self, f'cv{cv}_ro')})

    def test_create_page(self):
        """Check page creation"""
        self.assertEqual(self.page1.title, self.page1_title)
        self.assertEqual(self.page2.title, self.page2_title)

    def test_create_videos(self):
        """Check content creation"""
        for cv in range(self.cv_max):
            self.assertEqual(ContentVideo.objects.get(id=cv+1).title, f'video {cv}')

    def test_video_order_on_page(self):
        """Check detail API view"""
        request_factory = APIRequestFactory()
        request = request_factory.get(
            path='/api/v1/pages/',
             format='json')
        page_content_view = PageViewSet.as_view({'get': 'retrieve'})
        response = page_content_view(request, pk=1)
        self.assertEqual(len(response.data['content']), self.cv_max//2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)