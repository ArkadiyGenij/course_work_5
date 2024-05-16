from abc import ABC, abstractmethod


class BaseHH(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass