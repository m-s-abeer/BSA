from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Problem(models.Model):
    oj_name = models.CharField(max_length=20)
    prob_id = models.CharField(max_length=100)
    slug = models.SlugField(allow_unicode=True, max_length=100, unique=True, editable=False)
    name = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100, blank=True)
    note = models.TextField(max_length=100, blank=True)
    link = models.URLField(max_length = 1000)

    def __str__(self):
        return self.oj_name + ' - ' + self.prob_id + ' : ' + self.name

    def clean(self, *args, **kwargs):
        self.slug = slugify(self.oj_name) + '-' + slugify(self.prob_id)
        s = Problem.objects.all().filter(slug=self.slug)
        if s.exists():
            raise ValidationError('"' + self.slug + '" already exists.')
        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def get_absoulte_url(self):
        return reverse('problems')
        return reverse('problems:problem_detail', kwargs={'slug':self.slug})
