from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def rating_counter(movie: dict) -> float:
            if (
                len(str(movie["country"]).split(",")) > 1
                and movie["rating_kinopoisk"] != "0"
                and movie["rating_kinopoisk"] != ""
            ):
                return float(movie["rating_kinopoisk"])

            return 0

        result = list(filter(lambda x: x != 0, list(map(rating_counter, list_of_movies))))

        return sum(result) / len(result)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def counter(movie: dict) -> int:
            if movie["rating_kinopoisk"] != "" and float(movie["rating_kinopoisk"]) >= rating:
                return str(movie["name"]).count("и")

            return 0

        return sum(list(map(counter, list_of_movies)))
