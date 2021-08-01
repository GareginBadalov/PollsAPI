# PollsAPI
Реализовано API для системы опроса пользователей
### Инструкция по разворачиванию локально 
Клонировать репозиторий на локальную машину

    git clone https://github.com/GareginBadalov/PollsAPI.git

Создать и активировать виртуальное окружение(установка virtualenv -https://pypi.org/project/virtualenv/)

    python3 -m venv venv
    
    <venvpath>/Scripts/bin/activate.bat
    
Установить зависимости:

    pip3 install -r requirements.txt 
    
Запустить сервер django:

    python manage.py ruserver
    

### Инструкции к API для администратора:

Для отправки запросов используется basic auth

###### Admin.credentials
login - gar

password - gar

###### Получение списка всех опросов:
Отправить GET запрос по адресу 

    <localhost>:8000/api/v1/polls/
    
###### Создание опроса:
Отправить POST запрос по адресу 

    <localhost>:8000/api/v1/polls/poll/create/
c телом 

    {
    "title": <Название опроса>,
    "description": <Описание опроса>,
    "time_finish": <Время завершения опроса>}
    
###### Получение опроса:
Отправить GET запрос по адресу

    <localhost>:8000/api/v1/polls/poll/<poll_id>/

###### Редактирование опроса:
Отправить PUT запрос по адресу

    <localhost>:8000/api/v1/polls/poll/<poll_id>/
c телом 

    {
    "title": <Название опроса>,
    "description": <Описание опроса>,
    "time_finish": <Время завершения опроса>}

###### Удаление опроса:
Отправить DELETE запрос по адресу

    <localhost>:8000/api/v1/polls/poll/<poll_id>/

###### Получение списка всех вопросов:
Отправить GET запрос по адресу 

    <localhost>:8000/api/v1/polls/question/all/

###### Создание вопроса:
Отправить POST запрос по адресу 

    <localhost>:8000/api/v1/polls/question/create/
c телом 

    {
    "poll_id": <id_опроса>,
    "text": <текст вопроса>,
    "question_type": <Тип вопроса>}   возможные варианты -> ["One_choice", "Many_choices", "Text"]


###### Получение вопроса:
Отправить GET запрос по адресу 

    <localhost>:8000/api/v1/polls/question/<question_id>/

###### Редактирование вопроса:
Отправить PUT запрос по адресу 

    <localhost>:8000/api/v1/polls/question/<question_id>/
c телом 

    {
    "poll_id": <id_опроса>,
    "text": <текст вопроса>,
    "question_type": <Тип вопроса>}   возможные варианты -> ["One_choice", "Many_choices", "Text"]

###### Удаление вопроса:
Отправить DELETE запрос по адресу 

    <localhost>:8000/api/v1/polls/question/<question_id>/

###### Создание варианта ответа:
Отправить POST запрос по адресу 

    <localhost>:8000/api/v1/polls/choice/create/
c телом 

    {
    "text": <текс ответа>,
    "question":<queestion_id>}


###### Получение варианта ответа:
Отправить GET запрос по адресу 

    <localhost>:8000/api/v1/polls/choice/<choice_id>/

###### Редактирование варианта ответа:
Отправить PUT запрос по адресу 

     <localhost>:8000/api/v1/polls/choice/<choice_id>/
c телом 

    {
    "text": <текс ответа>,
    "question":<queestion_id>}

###### Удаление варианта ответа:
Отправить DELETE запрос по адресу 

    <localhost>:8000/api/v1/polls/choice/<choice_id>/
### Инструкции к API для пользователей:

Для отправки запросов используется basic auth
Администратор также может использовать эти эндпоинты

###### User.credentials
login - SimpleUser

password - simple1234

###### Получение списка активных опросов:
Отправить GET запрос по адресу 

    <localhost>:8000/api/v1/polls/active/
    
###### Отправка ответа на вопрос:
Отправить POSt запрос по адресу 

    <localhost>:8000/api/v1/polls/answer/<question_id>/

В зависимости от типа вопроса тело выглядит:

    {
    "many_choices": [<варианты ответа через запятую>]}
    
    or
    
    {
    "one_choice": <вариант ответа>}
    
    or
    
    {
    "self_text": <Текст ответа>}

###### Получение списка пройденных опросов:
Отправить GET запрос по адресу 

    <localhost>:8000/api/v1/polls/poll/finished/

