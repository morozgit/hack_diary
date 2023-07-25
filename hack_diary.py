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


LAUDATORY_PHRASES  = ['Молодец!',
           'Это как раз то, что нужно!',
           'Ты на верном пути!',
           'Ты многое сделал, я это вижу!']


def fix_marks(schoolkid):
    student_grades = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    student_grades.update(points=5)


def remove_chastisements(schoolkid):
    chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisement.delete()


def get_shoolchild(schoolkid):
    try:
        schoolchild = Schoolkid.objects.get(full_name__contains=schoolkid)
    except Schoolkid.MultipleObjectsReturned:
        schoolchild = Schoolkid.objects.get(full_name__contains=schoolkid).first()
    except Schoolkid.DoesNotExist:
        schoolchild = None
    return schoolchild


def create_commendation(schoolkid, subject):
    schoolchild = get_shoolchild(schoolkid)
    if schoolchild:
        class_lesson = Lesson.objects.filter(subject__title__contains=subject,
                                            year_of_study=schoolchild.year_of_study,
                                            group_letter=schoolchild.group_letter).order_by('?').first()
    else:
        print('Ученик не найден. Поробуйте поискать другого')
    if class_lesson:
        Commendation.objects.create(text=random.choice(LAUDATORY_PHRASES),
                                    created=class_lesson.date,
                                    schoolkid=schoolchild,
                                    subject=class_lesson.subject,
                                    teacher=class_lesson.teacher)
    else:
        print('Предмет не найден. Поробуйте ввести другой')
    remove_chastisements(schoolkid)


def main():
    schoolkid = input()
    subject = input()
    fix_marks(schoolkid)
    remove_chastisements(schoolkid)
    create_commendation(schoolkid, subject)


if __name__ == '__main__':
    main()
