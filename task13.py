# You are given a JSON file containing data about employees in a company. And another JSON file containign
# salaries for the different departments. Write a Python function that reads this file, parses the JSON data,
# modifies it by adding a new key-value pair to each employee dictionary, and stores another json file a list
# of dictionaries containing information about each employee with the added key-value pair.

import json

def edit_files(departments_salary: str, employees: str, updated_file: str):
    with open(departments_salary, 'r') as departments_salary:
        salary_json = departments_salary.read().lower()
        salary_json = json.loads(salary_json)
    with open(employees, 'r') as employees:
        employees_json = employees.read()
        employees_json = json.loads(employees_json)

    for item in employees_json['employees']:
        item['salary'] = None
        item['salary'] = item['department'].lower()
        item['salary'] = salary_json.get(item['salary'], None)
    with open(updated_file,  'w') as updated_file:
        json.dump(employees_json, updated_file)
def main():
    edit_files('needed_files/departments_salary.json', 'needed_files/employees.json', 'needed_files/updated_employees.json')


if __name__ == "__main__":
    main()
    exit(0)