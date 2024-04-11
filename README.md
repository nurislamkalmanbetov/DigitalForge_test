# DIGITALFORGE - test project
DIGITALFORGE - test project</p>

## Установка

1. **Склонируйте репозиторий на свой локальный компьютер:**

    ```bash
    git clone https://github.com/your_username/your_project.git
    ```

2. **Создайте файл `.env` в корневой директории проекта и укажите в нем необходимые переменные окружения:**

    ```plaintext
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=your_database_url
    ```

3. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Примените миграции для создания базы данных:**

    ```bash
    python manage.py migrate
    ```

5. **Загрузите начальные данные из файла `data.json`:**

    ```bash
    python manage.py loaddata data.json
    ```

## Создание суперпользователя

    ```bash
    python manage.py createsuperuser
    ```


<ol>
  <li>Copy .env-example and paste environment variables in .env file with your values</li>
  <li>Change direction to the folder with <b>docker-compose.yml</b> file</li>
  <li>Run the command: <b>docker-compose up -d --build</b></li>
  <li>Run the command: <b>docker-compose exec app python3.6 manage.py migrate</b></li>
  <li>Create a superuser account with the command: <b>docker-compose exec app python3.6 manage.py createsuperuser</b></li>
  <li>Browse to one of the following links:       http://127.0.0.1:8000       http://localhost:8000</li>
</ol>

<b>Production Version</b>

<ol>
  <li>First of all, go to the <b>settings.py</b> file and change DEBUG option to False   DEBUG = False</li>
  <li>Then change direction to the folder with <b>docker-compose.yml</b> file</li>
  <li>Run the command: <b>docker-compose -f production.yml up -d --build</b></li>
  <li>Create a superuser account with the command: <b>docker-compose -f production.yml exec app python3.6 manage.py createsuperuser</b>. 
  But be careful. If you see message about unapplied migrations, type <b>Ctrl+C</b> to exit from operation. Wait till project applied migrations automatically. After 15-20 seconds try to run the command again, and if there won't be any messages or warnings, create superuser account.</li>
  <li>Browse to one of the following links:       http://127.0.0.1       http://localhost</li>
</ol>

![1](static/img/admin-1.png)
![2](static/img/admin-2.png)
![3](static/img/admin-3.png)
![4](static/img/admin-4.png)
![5](static/img/admin-5.png)
![6](static/img/1.png)
![7](static/img/2.png)
![8](static/img/3.png)
![9](static/img/4.png)
