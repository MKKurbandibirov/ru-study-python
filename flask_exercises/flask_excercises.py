from flask import Flask, request, escape
from http import HTTPStatus


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    users: dict[str, str] = {}

    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.post("/user")
        def create_user() -> tuple:
            req = request.get_json()

            if "name" in req:
                user_name = req["name"]
                FlaskExercise.users[user_name] = req
                return {"data": f"User {user_name} is created!"}, HTTPStatus.CREATED

            return {"errors": {"name": "This field is required"}}, HTTPStatus.UNPROCESSABLE_ENTITY

        @app.get("/user/<user_name>")
        def get_user(user_name: str) -> tuple:
            name = escape(user_name)
            if name in FlaskExercise.users:
                return {"data": f"My name is {name}"}, HTTPStatus.OK
            return {"errors": f"User {name} not found"}, HTTPStatus.NOT_FOUND

        @app.patch("/user/<user_name>")
        def patch_user(user_name: str) -> tuple:
            name = escape(user_name)

            if name not in FlaskExercise.users:
                return {"errors": f"User {name} not found"}, HTTPStatus.NOT_FOUND

            req = request.get_json()
            if "name" in req:
                new_name = req["name"]
                del FlaskExercise.users[name]
                FlaskExercise.users[new_name] = req
                return {"data": f"My name is {new_name}"}, HTTPStatus.OK

            return {"errors": {"name": "This field is required"}}, HTTPStatus.UNPROCESSABLE_ENTITY

        @app.delete("/user/<user_name>")
        def delete_user(user_name: str) -> tuple:
            del FlaskExercise.users[user_name]

            return "", HTTPStatus.NO_CONTENT
