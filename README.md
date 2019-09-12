# Сайт столярной мастерской на Django

## Функционал

- Навигация по страницам(Главная, Проекты, Магазин, ...)
- Вывод всех Проектов в виде галереи. Страница деталей проекта.
- Каталог товаров во вкладке Магазин. Страница деталей товара. Работа с корзиной покупок (добавление, изменение, удаление)
- Аутентификация пользователя
- Требование аутентификации при попытке добавить товар в корзину. Отображение корзины с товарами только у вошедших пользователей

### Что сделано

- Исходные страницы преобразованы в шаблоны с использованием {%extends ...%}, {%include ... %}
- подключены статические файлы
- Созданы модели базы данных
- Настроенны URL страниц
- Созданы представления, В том числе представления-классы для вкладок Проекты и Магазин

## Для запуска

```json
virtualenv v_env
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Используемые библиотеки

- **ckeditor** - реализация WYSIWYG-поля для наполнения Проектов
- **allauth** - аутентификация пользователей
- **django-crispy-forms** - форма логина пользователей
