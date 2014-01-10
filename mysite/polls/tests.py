import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Poll

class PollMethodTests(TestCase):
    def test_was_recently_published_with_future_poll(self):
        """ method was_recently_published() should return False for polls published with a future date"""
        future_poll = Poll(pub_date = timezone.now()+datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)
        
    def test_was_recently_published_with_old_poll(self):
        """ method was_recently_published() should return False for polls published with an older date"""
        future_poll = Poll(pub_date = timezone.now()-datetime.timedelta(days=30))
        self.assertEqual(future_poll.was_published_recently(), False)
        
    def test_was_recently_published_with_recent_poll(self):
        """ method was_recently_published() should return False for polls published with recent date"""
        future_poll = Poll(pub_date = timezone.now()-datetime.timedelta(hours=1))
        self.assertEqual(future_poll.was_published_recently(), True)
        
        
        