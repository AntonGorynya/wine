import datetime
import pandas as pd
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader


def load_template():
    env = Environment(loader=FileSystemLoader('templates'))
    index_template = env.get_template('template.html')
    return index_template


def readframe(path,  skiprows=0):
    frame = pd.read_excel(path, sheet_name='Лист1', skiprows=skiprows, na_values=None, keep_default_na=False)
    return frame


def decline_years(n):
    if n % 100 == 1:
        return 'год'
    if n % 10 == 1 and n % 100 != 11:
        return 'год'
    elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
        return 'года'
    else:
        return 'лет'


if __name__ == '__main__':
    year_foundation = 1920
    age = datetime.datetime.now().year
    age = age-year_foundation
    wines = readframe('wine.xlsx')
    categories = wines['Категория'].unique()
    context = {
        'year': f'{age} {decline_years(age)}',
        'wines': wines
    }

    index_template = load_template()
    with open('index.html', mode='w',  encoding='utf-8') as result:
        result.write(index_template.render(context))

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
