class Vacancy:
    company_id: int
    title: str
    city: str
    salary_from: int
    salary_to: int
    link: str

    def __init__(self, company_id, title, city, salary_from, salary_to, link):
        self.company_id = company_id
        self.title = title
        self.city = city
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.link = link
