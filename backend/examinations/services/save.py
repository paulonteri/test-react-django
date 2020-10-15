from academics.models import Subject
from examinations.models import Exam, ExamResults
from students.models import Student


def save_results_per_student(exam, student, subject_marks):
    exam = Exam.objects.get(id=exam)
    student = Student.objects.get(student_id=student)
    saved_ids = []
    for marks in subject_marks:
        subject = Subject.objects.get(id=marks['subject_id'])
        # save results
        if ExamResults.objects.filter(student=student, exam=exam, subject=subject).exists():
            # if result is already saved, update it...
            obj = ExamResults.objects.get(
                student=student, exam=exam, subject=subject)
            obj.marks = marks['marks']
            obj.save()
            saved_ids.append(obj.id)

        else:
            # save new results
            obj = ExamResults(student=student, exam=exam,
                              subject=subject, marks=marks['marks'])

            obj.save()
            saved_ids.append(obj.id)
    # return saved values
    saved = []
    for i in saved_ids:
        for x in ExamResults.objects.filter(id=i).values("id", "exam_id", "student_id", "subject_id", "marks"):
            saved.append(x)
    return saved


def save_results_per_subject(exam, subject, student_marks):
    exam = Exam.objects.get(id=exam)
    subject = Subject.objects.get(id=subject)
    saved_ids = []
    for marks in student_marks:
        student = Student.objects.get(student_id=marks['student'])
        # save results
        if ExamResults.objects.filter(student=student, exam=exam, subject=subject).exists():
            # if result is already saved, update it...
            obj = ExamResults.objects.get(
                student=student, exam=exam, subject=subject)
            obj.marks = marks['marks']
            obj.save()
            saved_ids.append(obj.id)

        else:
            # save new results
            obj = ExamResults(student=student, exam=exam,
                              subject=subject, marks=marks['marks'])

            obj.save()
            saved_ids.append(obj.id)
    # return saved values
    saved = []
    for i in saved_ids:
        for x in ExamResults.objects.filter(id=i).values("id", "exam_id", "student_id", "subject_id", "marks"):
            saved.append(x)
    return saved
