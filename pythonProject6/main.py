from repository import init_db,check_db,update

from modules import Students,Subjects


init_db()


#print(Subjects.find_best_student())
#asd ='music'
#print(Subjects.find_best_student_subject(asd))
#print(Subjects.find_average_in_group_by_subject(asd))
#print(Subjects.find_avg_at_all())

teacher = input('enter name of teacher:')
#print(Subjects.find_all_teachers_subject(teacher))
#group = input('enter name of group:')
#print(Subjects.find_all_students_by_group(group))
#subject = input('enter subject:')
#print(Subjects.seven(group,subject))
#print(Subjects.eight(teacher))
student = input()
#print(Subjects.nine(student))
print(Subjects.find_courses_by_student_and_teacher(student,teacher))