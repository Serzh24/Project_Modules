from application.salary import Accountant
from application.db.people import People
import datetime


def main():
    a = Accountant('Linda')
    print(a.calculate_salary())
    p = People('John')
    print(p.get_employees())
    dt_now = datetime.datetime.now()
    print(dt_now)


if __name__ == '__main__':
    main()
