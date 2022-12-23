from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=150)


class Book(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    year = models.PositiveSmallIntegerField()
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, related_name="books",
                              on_delete=models.SET_NULL,
                              null=True)

    def __str__(self):
        return self.title


class Picture(models.Model):
    image = models.ImageField(upload_to="books")
    book = models.ForeignKey(Book, related_name="pictures",
                              on_delete=models.SET_NULL,
                              null=True)