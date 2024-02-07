# Write your solution after the ExamSubmission class
# DO NOT CHANGE THE CLASS
class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    def __str__(self):
        return f"Exam submission (examinee: {self.examinee}, points: {self.points})"

    # WRITE YOUR OWN SOLUTION HERE:


def passed(submissions: list, lowest_passing: int):
    passing = [
        submission for submission in submissions if submission.points >= lowest_passing
    ]
    return passing


# You may use the following code to test your function:

if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)

    passes = passed([s1, s2, s3, s4, s5], 15)
    for passing in passes:
        print(passing)
