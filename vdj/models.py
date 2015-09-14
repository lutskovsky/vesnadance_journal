from django.db import models
from django.forms import ModelForm, Textarea, DateInput, DateField


class Venue(models.Model):
    name = models.CharField(max_length=200, verbose_name="название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "зал"
        verbose_name_plural = "залы"


class Teacher(models.Model):
    name = models.CharField(max_length=200, verbose_name="имя")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "преподаватель"
        verbose_name_plural = "преподаватели"


class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name="название")
    standard_teacher_fee = models.IntegerField(default=1500, verbose_name="оплата преподавателя")
    teachers = models.ManyToManyField(Teacher)
    venues = models.ManyToManyField(Venue)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "группа"
        verbose_name_plural = "группы"


class Student(models.Model):
    name = models.CharField(max_length=200, verbose_name="имя")
    phone = models.CharField(max_length=200, verbose_name="номер телефона")
    has_discount = models.BooleanField(default=False, verbose_name="право на скидку")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ученик"
        verbose_name_plural = "ученики"


class Lesson(models.Model):
    date = models.DateField("дата")
    group = models.ForeignKey(Group, verbose_name="группа", null=True)
    teachers = models.ManyToManyField(Teacher, through='TaughtBy')

    venue = models.ForeignKey(Venue, verbose_name="зал")
    students = models.ManyToManyField(Student, through='AttendedBy', verbose_name="ученики")
    revenue = models.IntegerField("выручка", default=0)
    rent = models.IntegerField("аренда", default=0)
    comment = models.TextField("комментарий", blank=True)

    def __str__(self):
        return ' '.join([self.group.__str__(), self.date.__str__()])

    class Meta:
        verbose_name = "занятие"
        verbose_name_plural = "занятия"

class Subscription(models.Model):
    SUBSCRIPTION_TYPES = (
        ('10', '10 занятий'),
        ('15', '15 занятий'),
    )
    start_date = models.DateField("дата")
    expiry_date = models.DateField("дата")
    student = models.ForeignKey(Student, verbose_name="ученик")
    type = models.CharField(max_length=2, choices=SUBSCRIPTION_TYPES)

    class Meta:
        verbose_name = "абонемент"
        verbose_name_plural = "абонементы"

class TaughtBy(models.Model):
    teacher = models.ForeignKey(Teacher, verbose_name="преподаватель")
    lesson = models.ForeignKey(Lesson, verbose_name="занятие")
    fee = models.IntegerField(verbose_name="гонорар")

    class Meta:
        verbose_name = "преподаватель"
        verbose_name_plural = "преподаватели"

class AttendedBy(models.Model):
    student = models.ForeignKey(Student, verbose_name="ученик")
    lesson = models.ForeignKey(Lesson, verbose_name="занятие")


class LessonForm(ModelForm):
    date = DateField()
    class Meta:
        model = Lesson
        fields = ['date', 'group', 'teachers', 'venue', 'comment']
        widgets = {
            'date': DateInput,
            'name': Textarea(attrs={'cols': 80, 'rows': 5}),
        }