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
python orchestrator/engine/run.py -c configs/dev.yml
```

5. Создать Docker образ и запустить / остановить его

```
cd /Users/aakorneev/PycharmProjects/AlexxanderKorn 
vim ~/.docker/config.json 
Здесь:
Delete the line with credsStore from ~/.docker/config.json.
Or rename credsStore to credStore

docker build -t info_bot_app .

docker run -d --restart=always info_bot_app
docker run -d --restart=always info_bot_app --stop

docker ps
```