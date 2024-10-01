# Job_test2


## Установка
Склонируйте репозиторий:
   git clone https://github.com/Gar1kRbIGALO/Job_test.git
   cd books_project

##Запуск проекта
  1. Активируйте виртуальное окружение
     python -m venv venv
     venv\scripts\activate

  2. Установите зависимости
     pip install -r requirements.txt
     
  3. Запустите веб-сервер
     python manage.py runserver

  4. Запустите gRPC-сервер
     python grpc_server.py
     
  5. Откройте PowerShell, чтобы подключиться к БД
     mysql -u root -p
     password: rjpytdf72

## Добавление книги в проект
   1. Откройте PowerShell
   2. Перейдите в job_test2
   3. В PyCharm в терминале пропишите команду python manage.py createsuperuser и создайте юзера
   4. Получите токен access заполнив данные и через веб-сервер вписав, http://127.0.0.1:8000/api/token/
   5. В PowerShell напишите:
$token = "your_access_token"
Invoke-WebRequest -Uri http://127.0.0.1:8000/api/books/create/ -Method Post -Headers @{Authorization = "Bearer $token"} -Body ($bookData | ConvertTo-Json) -ContentType "application/json"


