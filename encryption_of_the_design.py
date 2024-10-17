# ID послыки - 121208273
"""Шифрование инструкции.

Название файла:
    encryption_of_the_design.py

Описание:
    Данный скрипт расшифровывает сжатую инструкцию для марсохода

Использование:
    python encryption_of_the_design.py

Входные данные:
    - Строка - инструкция.

Выходные данные:
    - Строка - расшифрованная инструкция

Пример:
    Ввод:
        3[a]2[bc]
    Вывод:
        aaabcbc

Зависимости:
    Убедитесь, что все необходимые зависимости установлены.
    В данном случае используется стандартная библиотека Python.

Пример запуска:
    Для запуска программы используйте команду:
    python encryption_of_the_design.py
"""


def decoding(instruction: str) -> str:
    """Функция расшифровки инструкции."""
    def decode_substring(index: int) -> tuple[str, int]:

        result_str = ''
        multiplier = 0

        while index < len(instruction):

            current_char = instruction[index]

            if current_char.isdigit():
                multiplier = multiplier * 10 + int(current_char)

            elif current_char == '[':
                decoded_substring, index = decode_substring(index + 1)
                result_str += decoded_substring * multiplier
                multiplier = 0

            elif current_char == ']':
                return result_str, index

            else:
                result_str += current_char

            index += 1

        return result_str, index

    decoded_instruction, _ = decode_substring(0)

    return decoded_instruction


def main():
    """Основная функция программы."""
    instruction_str = input()
    result_str = decoding(instruction_str)
    print(result_str)


if __name__ == '__main__':
    main()
