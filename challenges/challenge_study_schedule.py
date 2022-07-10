# starting project
def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    if target_time is None:
        return None

    students_number = 0

    for entry, out in permanence_period:
        if type(entry) != int or type(out) != int:
            return None
        if entry <= target_time <= out:
            students_number += 1

    return students_number
