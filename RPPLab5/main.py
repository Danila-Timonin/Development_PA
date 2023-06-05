import cherrypy
from cherrypy.lib import static
from jinja2 import Environment, FileSystemLoader
from peewee import *
from jinja2 import Template

# подключение к базе данных SQLite
db = SqliteDatabase('visitors.db')
env = Environment(loader=FileSystemLoader('static'))


# модель посетителя
class Visitor(Model):
    id = PrimaryKeyField()
    date = DateField()
    time = TimeField()
    is_entry = TimeField()
    gender = CharField()

    class Meta:
        database = db


# создание таблицы посетителей в базе данных
db.create_tables([Visitor])


class VisitorApp:
    @cherrypy.expose
    def index(self):
        data = {'list': []}
        # данные из базы данных
        visitors = Visitor.select().order_by(Visitor.id.desc())
        for visitor in visitors:
            visitor_data = {
                'id': visitor.id,
                'date': visitor.date,
                'time': visitor.time,
                'is_entry': visitor.is_entry,
                'gender': visitor.gender
            }
            data['list'].append(visitor_data)
        tmp = env.get_template('html/index.html').render(data)
        return tmp

    @cherrypy.expose
    def add_visitor(self, date, time, is_entry, gender):
        # добавление нового посетителя
        visitor = Visitor(date=date, time=time, is_entry=is_entry, gender=gender)
        visitor.save()
        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def edit_visitor_form(self, visitor_id):
        visitor = Visitor.get_or_none(id=visitor_id)
        if visitor:
            # загрузка шаблона
            template = env.get_template('html/edit_visitor.html')
            # заполнение шаблона
            rendered_template = template.render(visitor_id=visitor_id, visitor=visitor)
            return rendered_template
        else:
            return f'Посетитель с ID {visitor_id} не найден.'

    @cherrypy.expose
    def edit_visitor(self, visitor_id, date, time, is_entry, gender):
        visitor = Visitor.get_or_none(id=visitor_id)
        if visitor:
            # изменение информации о посетителе
            visitor.date = date
            visitor.time = time
            visitor.is_entry = is_entry
            visitor.gender = gender
            visitor.save()
            raise cherrypy.HTTPRedirect('/')
        else:
            return f'Посетитель с ID {visitor_id} не найден.'

    @cherrypy.expose
    def delete_visitor(self, visitor_id):
        # поиск по id и удаление посетителя из БД
        visitor = Visitor.get_or_none(id=visitor_id)
        if visitor:
            visitor.delete_instance()
            raise cherrypy.HTTPRedirect('/')
        else:
            return f'Посетитель с ID {visitor_id} не найден.'

# конфигурации
cherrypy.config.update({
    'server.socket_host': '127.0.0.1',
    'server.socket_port': 8080,
    'tools.encode.on': True,
    'tools.encode.encoding': 'utf-8',
})

if __name__ == '__main__':
    cherrypy.quickstart(VisitorApp())
