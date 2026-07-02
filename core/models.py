from django.db import models
class Recipe(models.Model):
    nomi = models.CharField()
    tavsifi = models.TextField()
    tayyorlash_vaqti = models.IntegerField()
    muallif = models.CharField()
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-yaratilgan_sana']

    def __str__(self):
        return self.nomi
