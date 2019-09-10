def text_format(text, symbols_to_filter, water_words):
    """
    Custom function to format input user text.
    :param text: input text.
    :param symbols_to_filter: list of forbidden punctuation, that is might be filtered.
    :param water_words: list of senseless words.
    :type text: string.
    :type symbols_to_filter: list.
    :type water_words: list of words.
    :return: The function returns list of separated words.
    :rtype: return type 'list'.
    """
    for i in symbols_to_filter:
        if i in text:
            text = text.replace(i, '')

    formatted_text = text.lower().split(' ')

    for i in water_words:

        for j in formatted_text:
            if i == j:
                formatted_text.remove(j)

    return formatted_text


def quantity(formatted_text):
    """
    The function calculate quantity of words from already formatted text.
    :param formatted_text: list of words.
    :type formatted_text: Any countable collection.
    :return: The function returns number of elements of inputted collection.
    :rtype: return type 'int'.
    """
    words_quantity = len(formatted_text)

    return words_quantity


def unique_list(formatted_text):
    """
    This function is used to collect only unique words of text.
    :param formatted_text: list of words.
    :type formatted_text: possible types: 'list', 'tuple' etc.
    :return: Function returns string of unique words of text.
    :rtype: return type 'string'.
    """
    unique_words = set(formatted_text)

    unique_dictionary = ', '.join(unique_words)

    return unique_dictionary


def words_dictionary(formatted_text):
    """
    Function helps to built a dictionary, where key is word and value - number of times its appearing in text.
    :param formatted_text: list of words.
    :type formatted_text: possible types: 'list', 'tuple' etc.
    :return: The function returns a dictionary.
    :rtype: return type 'Dict'.
    """
    dict_words = {}

    for i in formatted_text:
        if i not in dict_words:
            dict_words[i] = 1

        else:
            dict_words[i] += 1

    return dict_words


def keywords(dict_words):
    """
    Function puts input dictionary in descending order; then return most commonly used words from dictionary.
    :param dict_words: dictionary.
    :type dict_words: Dict.
    :return: The function returns string value of the most frequently elements.
    :rtype: return type 'string'.
    """
    frequency_list = sorted(dict_words.items(), key=lambda z: z[1], reverse=True)

    user_request = input('\nEnter a number of needed keywords quantity: ')

    while not user_request.isdigit():
        user_request = input('\nEnter a NUMBER of needed keywords quantity: ')

    keywords_list = [f'{i} - {j}' for i, j in frequency_list]

    keywords_value = [keywords_list[i] for i in range(int(user_request))]

    key_str = '; '.join(keywords_value)

    return key_str


def favourite_words(words_quantity, dict_of_words):
    """
    Function to help output frequency of words.
    :param words_quantity: General quantity of words in text.
    :param dict_of_words: dictionary of words.
    :type words_quantity: int.
    :type dict_of_words: Dict.
    :return: The function returns frequency of every word in percentage view.
    :rtype: return type 'string'
    """
    initial_list = []
    frequency_of_words = ''

    for key, value in dict_of_words.items():
        initial_list.append(f'{key} - {value * words_quantity / 100}%, ')

    frequency_of_words = frequency_of_words.join(initial_list)

    return frequency_of_words


#                       Body of program
#  Initialize block

# President Trump talks about Greenland. Trump wants to buy this place. Greenland is a Danish island. // Checking out
user_text = input('\nEnter your text: ')

sym_to_filter = [',', '.', '!', '"', ':', ';', '?', '*', '-', '_', '+', '|', '/', '(', ')', '\'']

water_p1 = ['a', 'an', 'the', 'to', 'at', 'of', 'on', 'by', 'for', 'i', 'you', 'he', 'she', 'it', 'in', 'as', 'is']
water_p2 = ['are', 'am', 'was', 'were', 'this', 'those', 'that', 'what', 'why', 'where', 'when', 'how', 'no', 'yes']
water_p3 = ['do', 'did', 'does', 'don\'t', 'doesn\'t', 'such', 'so', 'ever', 'never', 'has', 'have', 'been', 'be']
water_p4 = ['from', 'but', 'and', 'or', 'also', 'which', 'its', 'into', 'within', 'while', 'not', 'would', 'after']
water = water_p1 + water_p2 + water_p3 + water_p4


edited_text = text_format(user_text, sym_to_filter, water)        # Text formatting

quantity_of_words = quantity(edited_text)
print(f'\nThis text contains {quantity_of_words} words.')         # Words quantity

text_dictionary = unique_list(edited_text)
print('\nText dictionary: ', text_dictionary)                     # Text dictionary

dictionary_of_words = words_dictionary(edited_text)               # Dict of unique words

text_keywords = keywords(dictionary_of_words)
print('\nKeywords:', text_keywords)                              # Keywords

frequency = favourite_words(quantity_of_words, dictionary_of_words)
print('\nThe most favourite words are: ', frequency)              # Frequency
