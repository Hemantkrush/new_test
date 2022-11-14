from django.db import models

# Create your models here.


class CommonClass(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class College(CommonClass):
    address = models.CharField(max_length=100)
    est_year = models.DateField()

    class Meta:
        db_table = 'clg'

    def __str__(self):
        return self.name

class Principle(CommonClass):
    exp = models.FloatField()
    salary = models.IntegerField()
    college = models.OneToOneField(College, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'princi'

    def __str__(self):
        return f"{self.id} -- {self.name}"

class Department(CommonClass):
    staff_count = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="depts")

    class Meta:
        db_table = 'dept'

    def __str__(self):
        return self.name

    
    def create_department():
        dept = Department(name='IT', staff_count=35, college_id=1)
        dept.save()
        return dept
    
    @classmethod
    def bulk_create_departments(cls):
        all_depts = cls.objects.bulk_create([Department(name='Biology', staff_count=12, college_id=3),
                                            Department(name='Physics', staff_count=18, college_id=2)])
        return all_depts
    
class Student(CommonClass):
    age = models.IntegerField()
    marks = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='studs', null=True)

    class Meta:
        db_table = 'stud'

    def __str__(self):
        return f"{self.id} -- {self.name}"


class Subject(CommonClass):
    is_practical = models.BooleanField(default=False)
    student = models.ManyToManyField(Student, related_name='sub')

    class Meta:
        db_table = 'subject'

    def __str__(self):
        return f"{self.id} -- {self.name}"








    