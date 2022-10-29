from django.db import models


class Putin_order(models.Model):
    """
    Модель таблицы 
    """
    id = models.IntegerField(primary_key=True)
    doc_name = models.CharField(max_length = 1000)
    chapter_num = models.CharField(max_length=50)
    chapter_name = models.TextField(max_length = 1000)
    link = models.URLField()

    def __str__(self):
        return f"{self.id};" \
               f" {self.doc_name};" \
               f" {self.chapter_num};" \
               f" {self.chapter_name};" \
               f" {self.link}"
