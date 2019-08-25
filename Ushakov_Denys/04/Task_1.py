# Text Analyzer


def calculate_words_in_text(text):
    """
    Function calculates element in list(in our case in the text) using len
    :param text: some list of strings
    :type text: list
    :return: return quantity of list
    :rtype: int
    """

    return len(text)


def find_unique_words(words, s_dict):
    """
    Function finds unique word in list(in our case in the text) using set and dict
    :param s_dict: dict with frequency
    :param words: some list of strings
    :type words: list
    :return: return all unique
    :rtype: tuple
    """
    keywords_list = []

    a = s_dict
    
    for word in set(words):

        if s_dict[word] == 1:

            keywords_list.append(word)

    return keywords_list


def help_print_all_unique_word(words):
    """
    Function help print unique words like string
    :param words: list of words
    :type: list
    :return: string of unique words
    :rtype: str
    """

    words_list = []
    word_string = ''

    counter = 1
    for word in words:

        if counter != len(unique_words):

            counter += 1
            words_list.append(f'{word}, ')

        else:

            words_list.append(f'{word}')

    return word_string.join(words_list)


def find_frequent_words(s_dict):
    """
    Function finds keywords in dict(in our case in the text) using sorted
    :param s_dict: dict in which key is a word and value is quantity of repeats in text
    :type s_dict: dict
    :return: return sorted dict by value
    :rtype: object sorted
    """

    return sorted(s_dict.items(), key=lambda x: x[1], reverse=True)


def help_print_keyword(s_tuple):  # im created this fucn to print more then 3 keywords
    """
    Function allows to print as many keywords as yo like
    :param s_tuple: list of tupels which each tupel have word and quantity
    :type s_tuple: list of tupels
    :return: formatstring
    :rtype: str
    """

    keyword_list = []
    keyword_string = ''
    counter = 0
    f_elem_counter = 0

    while counter != 3:

        keyword_list.append(f'{counter+1}: {s_tuple[f_elem_counter][0]} appears ')
        keyword_list.append(f'{s_tuple[f_elem_counter][1]} times\n')

        f_elem_counter += 1
        counter += 1
    return keyword_string.join(keyword_list)


def adopt_word_in_dict(text):
    """
    Function adopt list of words in dict in which key is a word and value is quantity of repeats in text
    :param text: some list of strings
    :type text: list
    :return: return unsorted dict
    :rtype: dict
    """

    word_dict = {}

    # Makes dict form list
    for word in text:

        if word not in word_dict.keys():

            word_dict[word] = 1

        else:

            word_dict[word] += 1

    return word_dict


def calculate_frequency_of_all_world(s_dict):
    """
    Function calculate frequency of all word in text then change dict to reversed list
    :param s_dict: sorted dict
    :type s_dict: dict
    :return: frequency of all words in percentage
    :rtype: str
    """

    freq_list = []
    freq_text = ''

    # Calculate freq for each word
    for key, value in s_dict.items():

        s_dict[key] = int(value / word_quantity * 100)

    # Add it to list
    for key, value in s_dict.items():

        freq_list.append(f'{key} = ')
        freq_list.append(f'{str(value)}% ')

    return freq_text.join(freq_list)


def adapts_text_to_correct_format(text):
    """
    Function delete connectives and punctuation from text
    :param text: some text
    :type text: str
    :return: text without connectives and punctuation
    :rtype: list
    """

    # This block filters forbidden punctuation
    for i in forbidden_punctuation:
        text = text.replace(i, '')

    text = text.lower().split(' ')  # split text on individual elements

    # This block filters forbidden connectives
    for j in forbidden_connectives:

        while j in text:

            for i in text:

                index = text.index(i)

                if j == i:

                    text.pop(index)

                    break

    return text


main_text = 'I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn’t really happy.'

# List of forbidden things
forbidden_punctuation = ['.', ',', '?', '!', '"', ':', ';', '...', '-', '–', '—', '(', ')', '[', ']']
forbidden_connectives = ['i', 'and', 'so', 'or', 'in', 'to', 'at', 'on', 'a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'if', 'he', 'she', 'it', 'this', 'my', 'of', 'we', 'who', 'by', 'the', 'so', 'that', 'they', 'as', 'our', 'when', 'which', 'do', 'be', 'but', 'else', 'have', 'with']
# ----------------------------------------------------------------------------------------------------------------------

# Part where function come to life :)
adapted_text = adapts_text_to_correct_format(main_text)

adapted_dict = adopt_word_in_dict(adapted_text)

word_quantity = calculate_words_in_text(adapted_text)

unique_words = find_unique_words(adapted_text, adapted_dict)

keyword = find_frequent_words(adapted_dict)

help_print_keyword(keyword)

all_word_freq = calculate_frequency_of_all_world(adapted_dict)

# ----------------------------------------------------------------------------------------------------------------------

# Printing part
print(f'In your text: {word_quantity} words\n')

print(f'In your text you have {len(unique_words)} unique words, your unique words is: {help_print_all_unique_word(unique_words)}\n')

print(f'      Top 3 word:\n'
      f'{help_print_keyword(keyword)}')

print(f'frequency: {all_word_freq}')
# ----------------------------------------------------------------------------------------------------------------------
