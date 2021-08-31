from main.models import Vacancy


def get_vacancy_count(message):
    answer = ''
    qty = Vacancy.objects.filter(vacancy_name__icontains=message).count()

    if qty == 0:
        answer = 'No vacancy'
    else:
        answer = 'There is {} vacancy'.format(qty)

    return answer
