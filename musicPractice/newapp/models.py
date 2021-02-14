from django.db import models

# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=20)
    catagory = (
        (1,"rock"),
        (2,"Heavy Metal"),
        (3,"Thrash Metal"),
        (4,"Others"),
    )
    genre = models.IntegerField(choices=catagory)
    dof = models.DateField()

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=20)
    artist = models.ForeignKey(Band, on_delete=models.CASCADE)
    release_date = models.DateField()
    review = (
        (1,"Best"),
        (2,"Good"),
        (3,"Worst"),
    )
    rating = models.IntegerField(choices=review)

    def __str__(self):
        return self.name
