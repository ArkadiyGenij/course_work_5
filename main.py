from src.utils.db_script import create_table, insert_data
from src.utils.utils import collecting_vacancies, creating_dictionary_list, get_print


def main():
    list_of_company = ["Caltat", "RedLab", "Центр финансовых технологий", "BRANDPOL",
                       "Offer Now", "Безлимит", "Datanomica", "DNS Технологии",
                       "Яндекс", "Тинькофф", "ЧУ ДО Московская школа программистов"]

    vacancies_list = []

    for search_query in list_of_company:
        coll_vacancies = collecting_vacancies(search_query)
        vacancies_list_item = {search_query: creating_dictionary_list(coll_vacancies)}
        vacancies_list.append(vacancies_list_item)

    create_table()
    insert_data(vacancies_list)

    while True:
        input_user = input("""
1. Получить список всех компаний и количество вакансий у каждой компании
2. Получить список всех вакансий с указанием названия компании,названия вакансии и зарплаты и ссылки на вакансию.
3. Получить среднюю зарплату по вакансиям
4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.
5. Получить список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
Наберите стоп или stop для выхода из программы
""").lower().strip()
        if get_print(input_user) == "стоп":
            break


if __name__ == '__main__':
    main()
