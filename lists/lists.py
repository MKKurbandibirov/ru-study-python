class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        def list_max(input_list: list[int]) -> int:
            maximum = input_list[0]

            for elem in input_list:
                if maximum < elem:
                    maximum = elem

            return maximum

        if not input_list:
            return input_list

        maximum = list_max(input_list)
        for ind in range(len(input_list) - 1):
            if input_list[ind] > 0:
                input_list[ind] = maximum

        return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        def binary_search(
            input_list: list[int], query: int, start: int = 0, end: int = len(input_list) - 1
        ) -> int:
            if end < start:
                return -1

            mid = (start + end) // 2

            if input_list[mid] == query:
                return mid
            elif input_list[mid] < query:
                return binary_search(input_list, query, mid + 1, end)
            else:
                return binary_search(input_list, query, start, mid - 1)

        return binary_search(input_list, query)
