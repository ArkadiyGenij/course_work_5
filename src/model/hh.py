import requests

from src.model.base_hh import BaseHH


class HH(BaseHH):
    """
    Класс для получения списка вакансий с сайта hh.ru
    """

    def get_vacancies(self, keyword):
        url = 'https://api.hh.ru/vacancies'
        params = {'text': keyword, 'page': 0, 'per_page': 100}
        response = requests.get(url, params=params)
        return response.json()
