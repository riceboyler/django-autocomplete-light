from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class RelatedModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name or super(RelatedModel, self).__str__()


@python_2_unicode_compatible
class TestMtm(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    relation = models.ManyToManyField(RelatedModel)

    def __str__(self):
        return self.name or super(RelatedModel, self).__str__()


@python_2_unicode_compatible
class TestFk(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    relation = models.ForeignKey(RelatedModel)

    def __str__(self):
        return self.name or super(RelatedModel, self).__str__()


@python_2_unicode_compatible
class TestOto(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    relation = models.OneToOneField(RelatedModel)

    def __str__(self):
        return self.name or super(RelatedModel, self).__str__()
