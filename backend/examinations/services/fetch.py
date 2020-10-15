from examinations.models import ExamResults


def per_exam_results(exam):
    # get all students whose results have been recorded
    student_list = []
    for i in ExamResults.objects.filter(exam=exam).values('student'):
        if i['student'] not in student_list:
            student_list.append(i['student'])

    # return all the individual results per student
    results_all_students = []
    for student in student_list:
        per_student_results = {}
        per_student_results.update({'student': student})
        y = ExamResults.objects.filter(
            exam=exam, student=student).values('subject_id', 'marks')
        results = []
        for x in list(y):
            results.append(x)
        # results of an individual student
        per_student_results.update({'subject_marks': results})
        # results of all students
        results_all_students.append(per_student_results)

    return results_all_students


def all_exam_results():
    results = []
    exams = []
    # get all exams in exam results
    for z in ExamResults.objects.values('exam'):
        if z not in exams:
            exams.append(z)
    # exam & results
    for ex in exams:
        results.append(
            {'exam': ex['exam'], 'exam_results': per_exam_results(ex['exam'])})
    return results


def per_student_results(student):
    all_results = ExamResults.objects.filter(student=student).values()
    # get exam ids
    exams = []
    for i in all_results:
        if i["exam_id"] not in exams:
            exams.append(i["exam_id"])
    totals = []
    for exam in exams:
        results = {"exam": exam}
        subject_marks = []
        # get per exam results
        for result in all_results:
            if result["exam_id"] == exam:
                subject_marks.append(
                    {'subject_id': result['subject_id'], 'marks': result['marks']})
        results["subject_marks"] = subject_marks
        totals.append(results)
    return totals


def per_class_per_subject_results(classs, subject):
    # If True
    exams = ExamResults.objects.filter(student__class_ns=classs, subject=subject).all() \
        .values("exam_id", "student_id", "marks")
    exam_ids = []
    for i in exams:
        if i["exam_id"] not in exam_ids:
            exam_ids.append(i["exam_id"])
    resultz = []
    for i in exam_ids:
        exam_results = []
        for q in exams:
            if q["exam_id"] == i:
                exam_results.append(q)
        resultz.append({"exam": i, "exam_results": exam_results})

    return resultz
