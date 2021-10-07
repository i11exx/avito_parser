# Парсер Авито

## Требования:
Версия Python - от 3.6.х
## Функционал:
**Сбор данных:** 
1. Наименование автомобиля
2. Год выпуска
3. Дата публикации
4. URL товара с сайта https://www.avito.ru/

### Для запуcка скрипта:
```
git clone https://github.com/i11exx/avito_parser.git
cd avito_parser
pip install -r pip-requirements.txt
python main.py
```

### В файле _parser.py_ в функции get_page можно поменять параметр url и запустить _main.py_
`url = 'https://www.avito.ru/moskva/avtomobili/audi/q7-ASgBAgICAkTgtg3elyjitg3UrSg' # Вместо указанного значения, вставьте ссылку вашего запроса`


