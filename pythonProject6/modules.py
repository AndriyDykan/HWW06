import sqlite3


class Students:
    TABLE_NAME = 'students'

    def __init__(self, name: str, _id: int, group: str):
        self.name = name
        self._id = _id
        self.group = group


class Subjects:
    TABLE_NAME = 'subjects'

    def __init__(self, sb_name: str, mark: int, teacher: int, time: int, owner_id: int):
        self.subject = sb_name
        self.mark = mark
        self.teacher = teacher
        self.time = time
        self.owner_id = owner_id

    @classmethod
    def find_best_student(cls, number_of_students: int = 1):
        querry = f"SELECT students.id, students.name, AVG(subjects.mark) AS average_mark FROM students INNER JOIN subjects ON students.id = subjects.owner_id GROUP BY students.id, students.name ORDER BY average_mark DESC LIMIT {number_of_students} ;"
        with sqlite3.connect('hw06.db') as con:
            cur = con.cursor()
            cur.execute(querry)
            result = cur.fetchall()
        return result

    @classmethod
    def find_best_student_subject(cls, subject: str):
        query = f"SELECT students.id, students.name AS student_name, subjects.sb_name AS subject_name, AVG(subjects.mark) AS average_mark " \
                f"FROM students " \
                f"INNER JOIN subjects ON students.id = subjects.owner_id " \
                f"WHERE subjects.sb_name = '{subject}' " \
                f"GROUP BY students.id, student_name, subject_name " \
                f"ORDER BY average_mark DESC LIMIT 1;"

        with sqlite3.connect('hw06.db') as con:
            cur = con.cursor()
            cur.execute(query)
            result = cur.fetchall()

        return result

    @classmethod
    def find_average_in_group_by_subject(cls, subject: str):
        query = f"SELECT students.group_name, AVG(subjects.mark) AS average_mark " \
                f"FROM students " \
                f"INNER JOIN subjects ON students.id = subjects.owner_id " \
                f"WHERE subjects.sb_name = '{subject}' " \
                f"GROUP BY students.group_name;"

        with sqlite3.connect('hw06.db') as con:
            cur = con.cursor()
            cur.execute(query)
            result = cur.fetchall()

        return result

    @classmethod
    def find_avg_at_all(cls):
        query = f"SELECT AVG(subjects.mark) FROM subjects;"

        with sqlite3.connect('hw06.db') as con:
            cur = con.cursor()
            cur.execute(query)
            result = cur.fetchall()

        return result

    @classmethod
    def find_all_teachers_subject(cls, teachers_name: str):
        query = f"SELECT teachers.tc_name, teachers.subject_way FROM teachers WHERE teachers.tc_name =  '{teachers_name}';"

        with sqlite3.connect('hw06.db') as con:
            cur = con.cursor()
            cur.execute(query)
            result = cur.fetchall()

        return result

    @classmethod
    def find_all_students_by_group(cls, group_name: str):
        query = f"SELECT students.name, students.group_name FROM students WHERE students.group_name =  '{group_name}';"

        with sqlite3.connect('hw06.db') as con:
            cur = con.cursor()
            cur.execute(query)
            result = cur.fetchall()

        return result

    @classmethod
    def seven(cls, group_name: str, subject_name: str):
        query = f"SELECT students.name AS student_name, subjects.mark " \
                f"FROM students " \
                f"INNER JOIN subjects ON students.id = subjects.owner_id " \
                f"WHERE students.group_name = '{group_name}' " \
                f"AND subjects.sb_name = '{subject_name}';"

        with sqlite3.connect('hw06.db') as con:
            cur = con.cursor()
            cur.execute(query)
            result = cur.fetchall()

        return result

    @classmethod
    def eight(cls, teacher_name: str):
        query = f"SELECT AVG(subjects.mark) AS average_mark " \
                f"FROM students " \
                f"INNER JOIN subjects ON students.id = subjects.owner_id " \
                f"INNER JOIN teachers ON subjects.teacher = teachers.id " \
                f"WHERE teachers.tc_name = '{teacher_name}';"

        with sqlite3.connect('hw06.db') as con:
            cur = con.cursor()
            cur.execute(query)
            result = cur.fetchall()

        return result

    @classmethod
    def nine(cls, student_name: str):
        query = f"""
                SELECT subjects.sb_name AS course_name
                FROM subjects
                INNER JOIN students ON subjects.owner_id = students.id
                WHERE students.name = '{student_name}';
            """
        with sqlite3.connect('hw06.db') as con:
            cur = con.cursor()
            cur.execute(query)
            result = cur.fetchall()

        return set(row[0] for row in result)
    @classmethod
    def find_courses_by_student_and_teacher(cls,student_name, teacher_name):
        query = f"""
            SELECT subjects.sb_name AS course_name
            FROM subjects
            INNER JOIN students ON subjects.owner_id = students.id
            INNER JOIN teachers ON subjects.teacher = teachers.id
            WHERE students.name = '{student_name}' AND teachers.tc_name = '{teacher_name}';
        """
        with sqlite3.connect('hw06.db') as con:
            cur = con.cursor()
            cur.execute(query)
            result = cur.fetchall()

        return set(row[0] for row in result)