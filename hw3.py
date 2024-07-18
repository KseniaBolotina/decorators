import os
import datetime
import types

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            date_time = datetime.datetime.now()
            string_main_log = f'Дата и время вызова функции: {date_time}, имя функции: {
            old_function.__name__}, аргументы: {args}, {kwargs}, возвращаемое значние: {result}\n'
            with open(path, 'a', encoding='utf-8') as file:
                file.write(string_main_log)
            return result

        return new_function

    return __logger

def test_3():
    path = ('previous_HW.log')

    @logger(path)
    def flat_generator(list_of_lists):
        for list in list_of_lists:
            for item in list:
                yield item

    def test_2():
        list_of_lists_1 = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None]
        ]

        for flat_iterator_item, check_item in zip(
                flat_generator(list_of_lists_1),
                ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
        ):
            assert flat_iterator_item == check_item

        assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

        assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

    if __name__ == '__main__':
        test_2()

if __name__ == '__main__':
    test_3()
