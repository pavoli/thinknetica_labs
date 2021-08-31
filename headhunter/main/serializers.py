from rest_framework import serializers

from .models import Vacancy


class VacancySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['vacancy_name', 'vacancy_description', 'salary_min', 'salary_max',
                  'currency', 'publish_date', 'is_active'
                  ]
