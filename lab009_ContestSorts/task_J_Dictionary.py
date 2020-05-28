# Блондинка Даша любит решать кроссворды на латинском языке, пользуясь орфографическим словарем.
# Часто Даша отгадывает последние буквы слова и долго ищет каким словам подходит такая концовка.
# Она мечтает о словаре, где бы слова были разбиты на главы по количеству букв в слове и написаны задом наперед.
# Помогите ей составить такой словарь по заданному орфографическому словарю латинском языка.

# Формат входных данных:
# В первой строке содержится единственное целое число N(1 ≤ N ≤ 100) — количество латинских слов в словаре.
# Далее следует N слов по одному слову на строку. Все слова состоят только из маленьких латинских букв.
# Общее количество слов на входе не превышает 100. Длина каждого слова не превосходит 15 символов.

# Формат результата
# Длина слов в данном блоке. На следующих строках слова задом наперед и исходное слово через пробел в лексикографическом порядке.

debug = False
# debug = True
TESTS = [(['eucharis', 'fittonia', 'tagetes'], ['7', 'setegat tagetes', '8', 'ainottif fittonia', 'sirahcue eucharis'])]


def sort_revers_word(input_list: list):
    dictionary = {}
    result_list = []

    for item in input_list:
        if len(item) not in dictionary.keys():
            dictionary[len(item)] = [item[::-1]]
        else:
            dictionary[len(item)].append(item[::-1])
    # print(dictionary)

    keys_list = list(dictionary.keys())
    keys_list.sort()

    for item in keys_list:
        result_list.append(str(item))
        partition_list = dictionary[item]
        partition_list.sort()
        for word in partition_list:
            result_list.append('{0} {1}'.format(word, word[::-1]))
    
    # print(result_list)

    return result_list


if __name__ == '__main__':
    for test in TESTS:
        testing_function = sort_revers_word
        result = testing_function(test[0])
        assert result == test[1], "Input: {0}, correct: {1}, output: {2}".format(test[0], test[1], result)

    count = int(input())
    words = []
    for i in range(count):
        words.append(input())

    result = sort_revers_word(words)

    for i in result:
        print(i)
