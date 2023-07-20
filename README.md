# Чтобы мама не ругалась
Сделает электронный дневник безопасным

## Красивый дневник
Для того чтобы все получилось необходимо положить файл скрипта рядом с manage.py 
### Исправление оценок Фролова Ивана Григорьевича
Запуск Django Shell
```Linux
python manage.py shell
```
Скоприровать в Django Shell
```python 
from datacenter.models import Schoolkid
from datacenter.models import Mark
ivan = Schoolkid.objects.get(full_name__contains="Фролов Иван Григорьевич")
child = Mark.objects.filter(schoolkid=ivan, points__lte=3)
```


 
