# reviews/models.py

from django.db import models
from users.models import User
from tours.models import Tour

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.tour.name} by {self.user.username}"
