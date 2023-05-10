if __name__ == '__main__':
    # Assignating first line of input to variables
    num_of_subjects, num_of_students = map(int, input().split())
    # Creating the list of marks for user's input
    all_marks = [(tuple(map(float, input().split()))) for i in range(num_of_students)]
    # Zipping student_marks by the subject
    marks_by_subject = zip(*all_marks)
    # Finding the average mark for each subject
    avg_mark_by_subject = (sum(i)/num_of_students for i in marks_by_subject)
    # Rounding and printing out
    [print(round(i, 1)) for i in avg_mark_by_subject]