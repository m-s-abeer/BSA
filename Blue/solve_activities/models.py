from django.db import models
from problems.models import Problem

# from django.apps import apps

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Solve(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="solved")
    solver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="solved")
    solved_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.solver.username + ": " + self.problem.slug
#
    def get_absoulte_url(self):
        return reverse('home')

    class Meta:
        unique_together = ['solver', 'problem']
