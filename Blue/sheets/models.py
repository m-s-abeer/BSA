from django.db import models
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class Sheet(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=20, allow_unicode=True, unique=True)
    semester = models.CharField(max_length=10)
    year = models.PositiveIntegerField()
    problem_count = models.PositiveIntegerField(default=4, null=False)
    cut_off = models.PositiveIntegerField(default=0, null=False)
    members = models.ManyToManyField(User, through='SheetMember')

    def __str__(self):
        return self.name + " ( " + self.semester + ", " + str(self.year) + " )"

    def get_absolute_url(self):
        # return reverse('sheets:single', kwargs={'slug': self.slug})
        return reverse('home')

    # incomplete
    class Meta:
        pass
        # ordering = ['']

class SheetMember(models.Model):
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE, related_name='memberships')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sheet')

    def __str__(self):
        return self.user.username
    class Meta:
        unique_together = ['sheet', 'user']

# class SheetAnnouncement(models.Model):
#     sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE, related_name='announcements')
#     subject = models.CharField(max_length=20)
#     messsage = models.TextField(max_length=200)
#
#     def __str__(self):
#         return self.subject
