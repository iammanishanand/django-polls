from django.test import TestCase
from django.urls import reverse
from .models import Question
from django.utils import timezone

class PollsViewTests(TestCase):

    def setUp(self):
        # Creating a sample question for tests
        self.question = Question.objects.create(
            question_text="Sample Question?",
            pub_date=timezone.now() - timezone.timedelta(days=1)
        )

    def test_home_page(self):
        """Test that the home page shows the correct data."""
        response = self.client.get(reverse('polls:index'))  # Simulate a GET request to the home page
        self.assertEqual(response.status_code, 200)  # Check that the status code is 200 (OK)
        self.assertTemplateUsed(response, 'polls/index.html')  # Ensure the correct template is used
        self.assertContains(response, "Sample Question?")  # Verify if the question text is in the response

    def test_detail_view(self):
        """Test that the detail view works for a given question."""
        url = reverse('polls:detail', args=(self.question.id,))  # Reverse generates the URL for the detail page
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Check that the status code is 200 (OK)
        self.assertTemplateUsed(response, 'polls/detail.html')  # Ensure the correct template is used
        self.assertContains(response, "Sample Question?")  # Ensure the question text appears

    def test_detail_view_with_no_question(self):
        """Test the detail view for a non-existent question."""
        url = reverse('polls:detail', args=(999,))  # Using an invalid question ID (999)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)  # Ensure we get a 404 status code for an invalid question
