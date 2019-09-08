# Проект: сайт столярной мастерской

Пример сайта столярной мастерской на Django

## Функционал

- Навигация по страницам
- Вывод всех Проектов. Вывод деталей по каждому Проекту
- Вывод

### Что сделано

- Исходные страницы преобразованы в шаблоны с использованием {%extends ...%}, {%include ... %}
- подключены статические файлы
- Созданы модели базы данных

## Для запуска

``

```json
virtualenv v_env
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

## Используемые библиотеки

- **ckeditor** - реализация WYSIWYG-поля для наполнения Проектов
- **allauth** - аутентификация пользователей

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).
