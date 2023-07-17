from datacenter.models import Schoolkid
ivan = Schoolkid.objects.get(full_name__contains="Фролов Иван Григорьевич")
print(ivan)

from datacenter.models import Mark
mark = Mark.objects.all()
print(mark)
child = Mark.objects.filter(schoolkid=ivan, points__lte=3)
print(child)
Mark.objects.filter(schoolkid=ivan, points__lte=3).count()
def fix_marks(schoolkid):
	child = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
	for point in child:
		point.points = 5 
		point.save()

from datacenter.models import Chastisement
chastisement = Chastisement.objects.filter(schoolkid=ivan)
print(chastisement)
chastisement.delete()
feofan = Schoolkid.objects.get(full_name__contains="Голубев Феофан Владленович")
print(feofan)
def remove_chastisements(schoolkid):
	chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
	chastisement.delete()

from datacenter.models import Lesson
lesson = Lesson.objects.all()
print(lesson)
#ivan_group_letter = Schoolkid.objects.get(group_letter__contains="А")
lesson_group_letter = Lesson.objects.filter(group_letter__contains="А")
lesson_year_of_study = Lesson.objects.filter(year_of_study__contains=6)
lesson_6A = Lesson.objects.filter(year_of_study__contains=6, group_letter__contains="А")
print(lesson_group_letter)
print(lesson_year_of_study)
print(lesson_6A)

from datacenter.models import Subject
#math = Subject.objects.filter(title__contains="Математика")
#print(math)
math_6A = Lesson.objects.filter(subject__title__contains="Математика", year_of_study__contains=6, group_letter__contains="А")
math1_6A = math_6A[0]
print(math_6A)
print(math1_6A)

from datacenter.models import Commendation
from datacenter.models import Teacher

teacher_math = Teacher.objects.get(full_name__contains="Гуляев Лукьян Викентьевич")
print(teacher_math)

Commendation.objects.create(text="Чудо, а не ребенок", created="2019-01-05", schoolkid=ivan, subject=math1_6A.subject, teacher=teacher_math)


subjects = Subject.objects.filter(year_of_study__contains=6)
print(subjects)
subject_list = []
for subject in subjects:
	subject_list.append(subject)
	
for sub in subject_list:
	print(sub)

ru_6A = Lesson.objects.filter(subject__title__contains="Русский язык", year_of_study__contains=6, group_letter__contains="А")
print(ru_6A)
ru1_6A = math_6A[0]

for les in lesson_6A:
	print(les.subject)

Commendation.objects.create(text="Чудо, а не ребенок", created="2019-01-05", schoolkid=ivan, subject=math1_6A.subject, teacher=teacher_math)

praise = ['Молодец!', 'Это как раз то, что нужно!', 'Ты на верном пути!', 'Ты многое сделал, я это вижу!']

schoolkid = input()
subject = input()
def create_commendation(schoolkid, subject)
	schoolchild = Schoolkid.objects.get(full_name__contains=schoolkid)
	subject_6A = Lesson.objects.filter(subject__title__contains=subject, year_of_study__contains=6, group_letter__contains="А").first()
	Commendation.objects.create(text=random.choice(praise), created=subject_6A.date, schoolkid=schoolchild, subject=subject_6A.subject, teacher=subject_6A.teacher)
	
print(subject_6A)