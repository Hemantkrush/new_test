# exec(open(r"D:\Hemant_Py\Code_Files\Hemant_Virtual_Env\My_env\college_rel_proj\relation_app\db_shell.py").read())


from django.db.models import Q
from relation_app.models import College, Principle, Department, Student, Subject


''' Create Data '''

# print(Department.create_department())
# s1 = Student.objects.create(name='Yash', age=25, marks=71)
# Student.objects.all()


'''Bulk create'''

# print(Department.bulk_create_departments())


# princi = College.objects.all()
# for i in princi:
#     print(i.principle)      # we can fetch principle data from College model


# dept = Department.objects.all()
# for i in dept:
#     print(i.college)        # can fetch college data by Departments Model.


''' Fetch Data from Department '''  

# dep = Department.objects.get(id=2)
# # print((dep))
# c1 = dep.college
# print(c1)


''' fetch data from College '''

# c1 = College.objects.get(id=2)
# print(dir(c1))

'address', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'depts', 'est_year', 'from_db', 
'full_clean', 'get_constraints', 'get_deferred_fields', 'get_next_by_est_year', 'get_previous_by_est_year', 
'id', 'name', 'objects', 'pk', 'prepare_database_save', 'principle', 'refresh_from_db', 'save', 'save_base', 
'serializable_value', 'unique_error_message', 'validate_constraints', 'validate_unique'


# c1 = College.objects.get(id=2)
# # print(c1)

# d1 = c1.depts.all()
# print(d1)

# p1 = c1.principle.salary
# print(p1)


''' Fetch data from Student '''

# s1 = College.objects.select_related().all()
# for i in s1:
#     print(i.princi)

# std = Student.objects.get(id=1)
# print(dir(std))

'age', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'department', 'department_id', 'from_db', 
'full_clean', 'get_constraints', 'get_deferred_fields', 'id', 'marks', 'name', 'objects', 'pk', 
'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'subject_set', 
'unique_error_message', 'validate_constraints', 'validate_unique'

# std = Student.objects.get(id=1)
# print(std)

# sub = std.subject_set.all()
# for i in sub:
#     print(i)


# std = Student.objects.get(id=2)
# sub2 = std.sub.all()
# print(sub2)


# std = Student.objects.get(id=4)
# print(std)
# sub3 = std.sub.all()
# for i in sub3:
#     print(i)


''' Fetch Data with Subject '''

# sub = Subject.objects.get(id=3)
# print(dir(sub))


'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'from_db', 'full_clean', 'get_constraints', 
'get_deferred_fields', 'id', 'is_practical', 'name', 'objects', 'pk', 'prepare_database_save', 'refresh_from_db', 
'save', 'save_base', 'serializable_value', 'student', 'unique_error_message', 'validate_constraints', 'validate_unique'

# sub = Subject.objects.get(id=3)
# std1 = sub.student.all()
# for i in std1:
#     print(i)

# sub = Subject.objects.get(id=3)
# std2 = sub.pk
# print(std2)

# sub = Subject.objects.get(id=3)
# std3 = sub.delete()     # deletes.
# print(std3)

# q1 = Student.objects.filter(Q(name__startswith='H') | Q(name__endswith='t'))
# print(q1)


# q2 = Student.objects.filter(Q(name__startswith='K') & Q(name__endswith='r'))
# print(q2)


''' Forward Relationship '''

# clg= College.objects.get(id=3)
# pr1 = clg.principle
# print(pr1)      # fetch the principle from College.


# clg= College.objects.get(id=1)
# dep = clg.depts.all()
# print(dep)      # fetch department by college


# dept= Department.objects.filter(studs__name='Kuldeep')
# print(dept)


# s1 = Subject.objects.create(name="C++", is_practical=1)

# std1 = Student.objects.get(id=1)
# std2 = Student.objects.get(id=5)
# std3 = Student.objects.get(id=6)
# print(std1, std2, std3)

# sub1 = std1.sub.add(s1)       # created subject added to student.
# sub2 = std2.sub.add(s1)
# sub3 = std3.sub.add(s1)



''' Reverse Relationship '''


# rev3 = Subject.objects.filter(student__id=4)
# print(rev3)


# rev2 = Student.objects.filter(sub__name='Python')
# for i in rev2:
#     print(i)


# rev_std = Student.objects.filter(department__name='IT')
# for i in rev_std:
#     print(i)


# rev = Department.objects.filter(college__name='MGM')
# print(rev)

# rev_dept = Department.objects.get(id=2)
# clg = rev_dept.college.address
# print(clg)


# rev = College.objects.filter(principle__name='Rakesh')
# print(rev)






