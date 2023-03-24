import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader



def load_template():
    env = Environment(loader=FileSystemLoader('templates/'))
    index_template = env.get_template('template.html')
    return index_template


if __name__ == '__main__':
    index_template = load_template()
    age = datetime.datetime.now().year
    year_foundation = 1920
    context = {'year': age-year_foundation}

    with open('index.html', mode='w',  encoding='utf-8') as  result:
        result.write(index_template.render(context))

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()





