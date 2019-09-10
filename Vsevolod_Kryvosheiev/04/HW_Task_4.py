# Home Work
# Vsevolod Kryvosheiev
# Task 4 Text Analyzer


def clear_text(sourse_text, exclude_symbol):
    """This function clear text from symbol (',', '.' and etc.), the list of characters is passed in a variable exclude_symbol

    :param sourse_text: Original text
    :param exclude_symbol: list of symbols to delete
    :type sourse_text: Str
    :type exclude_symbol: List
    :return: Cleared text
    :rtype: Str
    """
    for i in exclude_symbol:
        sourse_text = sourse_text.replace(i, '')

    return sourse_text


def unique_words(world_list, functional_words):
    """ This function clear list of words from functional words (a, an, is, etc)

    :param world_list: Full word lis
    :param functional_words: List words to clear
    :type world_list: List
    :type functional_words: List
    :return: Cleared List
    :rtype: List
    """

    return list(filter(lambda x: not x in functional_words, world_list))


def word_in_text(world_list, text_dictionary):
    """This function counts the number of occurrences of each word

    :param world_list: Source words list
    :param text_dictionary: Set unique words
    :type world_list: List
    :type text_dictionary: Set
    :return: Dictionary words and quantity
    :rtype: Dictionary
    """

    quantity_worlds = {}
    for i in text_dictionary:
        quantity_worlds[i] = world_list.count(i)

    return quantity_worlds


def print_top_words(sorted_words, qty_words):
    """This function print top frequent words

    :param sorted_words: Sorted list word and frequency
    :param qty_words: Quantity word for print
    :type sorted_words: List
    :type qty_words: Int
    :return:
    """

    print('keywords:', end=' ')
    for i in range(qty_words):

        print(f'{sorted_words[i][1]} - {sorted_words[i][0]},', end=' ')

    print()

    return


def print_percent_worlds(sorted_words, total_words):
    """This function print frequency words

    :param sorted_words: Sorted list word and frequency
    :param total_words: all world quantity
    :type sorted_words: List
    :type total_words: int
    :return:
    """

    print('frequency:', end=' ')
    for i in range(len(sorted_words)):

        print(f'{sorted_words[i][1]} - {int(sorted_words[i][0] / total_words * 100)}%,', end=' ')
    print()


raw_text = input('Enter your text: ')
# raw_text = "This is my favourite text. Let's try to analyze it. I love this text. I love Python."

# clear punctuation text
exclude_simbol = ['.', ',', '!', '?']
cleared_text = clear_text(raw_text, exclude_simbol)

# Check clear_text function
# print(cleared_text)

# Extract text dictionary - unique words
world_list = cleared_text.lower().split(' ')

functional_words = ['a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if', 'he',
                    'she', 'it', 'this', 'my', 'etc', 'i']
world_list = unique_words(world_list, functional_words)
total_words = len(world_list)
print(f'words quantity: {total_words}')

text_dictionary = set(world_list)
print(f'text_dictionary: {", ".join(text_dictionary)}')

quantity_words = word_in_text(world_list, text_dictionary)

sorted_words = sorted(((value, key) for (key, value) in quantity_words.items()), reverse=True)

print_top_words(sorted_words, 3)

print_percent_worlds(sorted_words, total_words)
