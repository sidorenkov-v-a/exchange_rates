# Exchange rates

**Сервис для получения списка валют.**  
**(!)Приложение выполнено в рамках тестового задания.(!)**

## Запуск приложения:
1) [Установите Docker](https://www.docker.com/products/docker-desktop)
2) [Установите docker-compose](https://docs.docker.com/compose/install/)
3) Клонируйте репозиторий с проектом:
```
git clone https://github.com/sidorenkov-v-a/exchange_rates.git
```
3) В корневой директории проекта создайте файл `.env`, в котором пропишите переменные окружения  
>Список необходимых переменных можно найти в файле `.env.example`
4) Перейдите в директорию проекта и запустите приложение
```
docker-compose up
```
## Стек технологий:   
- Django framework 3.2.6
- Django rest framework 3.12.4
- PostgreSQL 12.4
- Gunicorn 20.1.0
- Nginx 1.19.0
- Docker, docker-compose

#### Об авторе:
[Профиль Github](https://github.com/sidorenkov-v-a/)  
[Telegram](https://t.me/sidorenkov_vl)
