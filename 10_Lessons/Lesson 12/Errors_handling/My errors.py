class NotInRangeError(Exception):

    def __init__(self, message=None):
        super().__init__(message)

def verbose_grade(grade_int):
    if grade_int == 2:
        return "Плохо"
    elif grade_int == 3:
        return "Плохо"
    elif grade_int == 4:
        return "Хорошо"
    elif grade_int == 5:
        return "Отлично"

    raise NotInRangeError("Value from 2 to 5 expected")


# И сразу же вызовем ее

try:
    mark = verbose_grade(int(input()))
except NotInRangeError as e:
    print(e)
else:
    print(mark)
