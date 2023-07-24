import django
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from django.conf import settings
import random
settings.configure()
django.setup()
from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Subject
from datacenter.models import Commendation
from datacenter.models import Teacher


PRAISE  = ['Молодец!',
           'Это как раз то, что нужно!',
           'Ты на верном пути!',
           'Ты многое сделал, я это вижу!']


def fix_marks(schoolkid):
    student_grades = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    student_grades.update(points=5)


def remove_chastisements(schoolkid):
    chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisement.delete()


def create_commendation(schoolkid, subject):
    try:
    	schoolchild = Schoolkid.objects.get(full_name__contains=schoolkid)
    except MultipleObjectsReturned:
        print('Найдено больше одного. Введите ФИО')
    except ObjectDoesNotExist:
        print('Не найдено такого имени')
    class_lesson = Lesson.objects.filter(subject__title__contains=subject,
                                         year_of_study__contains=6,
                                         group_letter__contains="А").order_by('year_of_study').first()
    Commendation.objects.create(text=random.choice(PRAISE),
                                created=class_lesson.date,
                                schoolkid=schoolchild,
                                subject=class_lesson.subject,
                                teacher=class_lesson.teacher)
    remove_chastisements(schoolkid)


def main():
    schoolkid = input()
    subject = input()
    fix_marks(schoolkid)
    remove_chastisements(schoolkid)
    create_commendation(schoolkid, subject)


if __name__ == '__main__':
    main()
