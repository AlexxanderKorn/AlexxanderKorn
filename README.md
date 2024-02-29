# Инфо проект

## Структура репозитория:

* `develop/` - инструменты разработки;
* `docs/` - документация;

## Процесс разработки и требования к коду

* В качестве модели ветвления - [Gitflow](https://habr.com/ru/post/106912/):
    * Основные ветки: `master` и `develop`, формат названия веток:
        * `release/*` - релизные ветки;
        * `feature/*` - ветки с новым функционалом или доработками;
        * `bugfix/*` - витки с исправлениями багов;
        * `hotfix/*` - ветки с хотфиксами;
* В качестве стандарта оформления кода - [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
  со следующими исключениями:
    * Ограничение на длинны строки с кодом соответствует ограничению Pycharm (120 символов);
    * Можно импортировать не только пакеты и модули, но и классы и функции;
* Докстринги на модули, классы и функции;
* Аннотация функций обязательна, ориентир - [PEP 484](https://www.python.org/dev/peps/pep-0484/);
* Автотесты;
* Код в `main` и `dev` изменяется только посредством пулл реквестов:
    * Code review перед мержем пулл-реквеста в `dev` (хот фикса в `main`);
    * Перед созданием пулл-реквеста в `main` или `dev` вся разница в коммитах с целевой веткой должна быть
        [сквошена](https://htmlacademy.ru/blog/boost/tools/how-to-squash-commits-and-why-it-is-needed) до одного коммита
        (сквошенная ветка пушится в репозиторий через `git push --force`, аккуратнее с `--force`).

## Установка (Linux, MacOS)

1. Настроить [SSH авторизацию];
   
2. Выполнить:
    ```
    ssh://git@<ссылка на проект в гит>.git
    git checkout dev
    python3 -m venv env
    source env/bin/activate
    ```

3. Установить:
    * Для MacOS:
        1. Установить библиотеки (только один раз):
            ```
            brew install libpq
            echo 'export PATH="/usr/local/opt/libpq/bin:$PATH"' >> ~/.zshrc
            
            ```
        2. Обновить пути к библиотекам (при каждой установке проекта):
            ```
            export LDFLAGS="-L/usr/local/lib -L/usr/local/opt/openssl/lib -L/usr/local/opt/readline/lib"
            ```

4. Установить переменные окружения (нужны для служебных сервисов) ?

```
source env/bin/activate

```

5. Создать Docker образ, запустить / остановить его

```

cd /Users/aakorneev/PycharmProjects/AlexxanderKorn 

- На случай ошибки с кредами:
vim ~/.docker/config.json 
- Здесь:
Delete the line with credsStore from ~/.docker/config.json.
Or rename credsStore to credStore

*** Локально забильдить и запустить:
docker build -t bot_app .
docker run -d --name info-bot --restart=always bot_app
docker run --dns=8.8.8.8 --dns=8.8.8.4 --dns=192.168.2.1 -d --name info-bot --restart=always alexxanderkorn/infobot

*** Билд для DockerHub и Яндекс Cloud:
- Забильдить в DockerHub:
docker build -t alexxanderkorn/infobot .

- Запушить в DockerHub:
docker push alexxanderkorn/infobot

- Проставить тег для образа в облаке:
docker tag alexxanderkorn/infobot cr.yandex/b1gdh39cpm637gtpkhop/alexxanderkorn/infobot

- Запушить в облако:
docker push cr.yandex/b1gdh39cpm637gtpkhop/alexxanderkorn/infobot

- Перезапустить консоль:
source "/Users/aakorneev/.zshrc"

- Запуск в облаке Яндекс:
ssh alkorn@178.154.202.238

- Аутентификация:
curl -H Metadata-Flavor:Google 169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token | \
cut -f1 -d',' | \
cut -f2 -d':' | \
tr -d '"' | \
sudo docker login --username iam --password-stdin cr.yandex

- Запуск образа:
docker run --dns=8.8.8.8 --dns=8.8.8.4 --dns=192.168.2.1 --name info-bot --restart=always cr.yandex/crp076bjab1vv5rlg688/alexxanderkorn/infobot

- Удалить контейнер и образ
docker rm info-bot
docker rmi bot_app

docker ps -a
```