class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if not input_list:
            return input_list

        maximum = max(input_list)
        for ind in range(len(input_list) - 1):
            if input_list[ind] > 0:
                input_list[ind] = maximum

        return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        if not input_list:
            return -1

        start, end = 0, len(input_list) - 1

        while start <= end:
            mid = (start + end) // 2

            if input_list[mid] == query:
                return mid

            if input_list[mid] > query:
                end = mid - 1
            elif input_list[mid] < query:
                start = mid + 1

        return -1
