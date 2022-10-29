import csv
from django.core.management.base import BaseCommand

from add.models import Putin_order


class Command(BaseCommand):
    """
    Чтение из файла csv
    """
    def handle(self, *args, **kwargs):
        with open('data1.csv', 'r', encoding='utf-8') as csvfile:

            csv_reader = csv.reader(csvfile, delimiter=',')
            # Пропускаем первую итерацию
            next(csv_reader)
            # Проходим циклом по названию колонок и добавляем данные в нужные столбцы
            for line in csv_reader:
                Putin_order.objects.create(
                    id=line[0],
                    doc_name=line[1],
                    chapter_num=line[2],
                    chapter_name=line[3],
                    link=line[4],
                )
        pass