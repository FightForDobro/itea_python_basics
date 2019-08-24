# Text Analyzer


def calculate_words_in_text(text):

    return len(text)


def find_unique_words(text):

    return set(text)


def find_frequent_words(s_dict):

    return sorted(s_dict.items(), key=lambda x: x[1], reverse=True)


def adopt_word_in_dict(text):

    word_dict = {}

    for word in text:

        if word not in word_dict.keys():

            word_dict[word] = 1

        else:

            word_dict[word] += 1

    return word_dict


def calculate_frequency_of_all_world(s_dict):

    freq_list = []
    freq_text = ''

    for key, value in s_dict.items():

        s_dict[key] = int(value / word_quantity * 100)

    for key, value in s_dict.items():

        freq_list.append(f'{str(value)}% ')
        freq_list.append(f'{key} = ')

    return freq_text.join(reversed(freq_list))


def adapts_text_to_correct_format(text):

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


main_text = 'hello my name is denys name denys denys'

forbidden_punctuation = ['.', ',', '?', '!', "'", '"', ':', ';', '...', '-', '–', '—', '(', ')', '[', ']']
forbidden_connectives = ['and', 'so', 'or', 'in', 'to', 'at', 'on', 'a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'if', 'he', 'she', 'it', 'this', 'my', 'of', 'we', 'who', 'by', 'the', 'so', 'that', 'they', 'as', 'our', 'when', 'which', 'do', 'be', 'but', 'else', 'have', 'with']

adapted_text = adapts_text_to_correct_format(main_text)

adapted_dict = adopt_word_in_dict(adapted_text)

word_quantity = calculate_words_in_text(adapted_text)

unique_words = find_unique_words(adapted_text)

all_word_freq = calculate_frequency_of_all_world(adapted_dict)

keyword = find_frequent_words(adapted_dict)

a = [word for word in unique_words]

print(f'In your text: {word_quantity} words\n')

print(f'In your text you have {len(unique_words)} unique words, your unique words is: {a[0]}, {a[1]}, {a[2]}\n')

print(f'      Top 3 word:\n'
      f'1: {keyword[0][0]} appears {keyword[0][1]} times\n'
      f'2: {keyword[1][0]} appears {keyword[1][1]} times\n'
      f'3: {keyword[2][0]} appears {keyword[2][1]} times\n')

print(f'frequency: {all_word_freq}')
