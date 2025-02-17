# polls/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Question
from django.utils import timezone

class QuestionDetailViewTests(TestCase):

    def setUp(self):
        """Create a sample question for testing."""
        self.question = Question.objects.create(
            question_text="Sample Question?",
            pub_date=timezone.now() - timezone.timedelta(days=1)
        )

    def test_detail_view_with_valid_question(self):
        """Test that the detail view works for a valid question."""
        url = reverse('polls:detail', args=(self.question.id,))  # Create the URL dynamically
        response = self.client.get(url)  # Simulate a GET request

        # Assertions
        self.assertEqual(response.status_code, 200)  # Ensure the status code is 200 (OK)
        self.assertTemplateUsed(response, 'polls/detail.html')  # Ensure the correct template is used
        self.assertContains(response, self.question.question_text)  # Ensure the question text is displayed

    def test_detail_view_with_nonexistent_question(self):
        """Test that accessing a non-existent question returns a 404 error."""
        url = reverse('polls:detail', args=(999,))  # Use a non-existent question ID
        response = self.client.get(url)

        # Assertions
        self.assertEqual(response.status_code, 404)  # Ensure a 404 error is returned for a non-existent question
