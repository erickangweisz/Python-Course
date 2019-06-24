# coding=utf-8
# Un alumno desea saber cual será su calificación final en la
# materia de Algoritmos. Dicha calificación se compone de los
# siguientes porcentajes:
#   · 55% del promedio de sus tres calificaciones parciales.
#   · 30% de la calificación del examen final.
#   · 15% de la calificación de un trabajo final.

AVERAGE_PARTIALS = 55
FINAL_EXAM = 30
FINAL_WORK = 15

def final_qualification_by_criteria_of_qualification_in_matter_of_algorithms():
    try:
        average_partial_1 = float(input('Enter qualification of first partial:\n'))
        average_partial_2 = float(input('Enter qualification of second partial:\n'))
        average_partial_3 = float(input('Enter qualification of third partial:\n'))
            
        final_exam_qualification = float(input('Enter qualification of final exam:\n'))
        final_work_qualification = float(input('Enter qualification of final work:\n'))
    except:
        print 'Qualification must be a number'

    if (__qualification_is_correct(average_partial_1)
    and __qualification_is_correct(average_partial_2)
    and __qualification_is_correct(average_partial_3)
    and __qualification_is_correct(final_exam_qualification) 
    and __qualification_is_correct(final_work_qualification)):
        partials = [average_partial_1, average_partial_2, average_partial_3]
        
        total_qualification = __get_qualification_percent(__average(partials), AVERAGE_PARTIALS)        
        total_qualification += __get_qualification_percent(final_exam_qualification, FINAL_EXAM)
        total_qualification += __get_qualification_percent(final_work_qualification, FINAL_WORK)
        print 'Total qualification: ' + str(total_qualification)
    else:
        print 'Qualification must be between 0 and 10'

def __qualification_is_correct(qualification):
    if qualification >= 0 and qualification <= 10:
        return True
    else:
        return False

def __get_qualification_percent(qualification, percent):
    return (float(qualification) * percent) / 100

def __average(list):
    return sum(list) / len(list)

final_qualification_by_criteria_of_qualification_in_matter_of_algorithms()