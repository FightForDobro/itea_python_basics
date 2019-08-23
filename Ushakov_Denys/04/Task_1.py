# Text Analyzer


def calculate_words_in_text(text):

    return len(text)

def find_unique_words(text):

    a = set(text)

    return a


def find_frequent_words(text): # Закончить сортировку словаря

    count_num_dict = {}
    for i in text:
        count_num_dict[i] = text.count(i)

    value_list = []
    for key, value in count_num_dict.items():
        pass

    return count_num_dict.items()


def calculate_frequency_of_all_world(text):

    pass


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


main_text = '''On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains.'''

test_text = 'the the the the the the the'

forbidden_punctuation = ['.', ',', '?', '!', "'", '"', ':', ';', '...', '-', '–', '—', '(', ')', '[', ']']
forbidden_connectives = ['and', 'so', 'or', 'in', 'to', 'at', 'on', 'a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'if', 'he', 'she', 'it', 'this', 'my', 'of', 'we', 'who', 'by', 'the', 'so', 'that', 'they', 'as', 'our', 'when', 'which', 'do', 'be', 'but', 'else', 'have', 'with']

test_f_c = ['a', 'the', 'and', 'so']

adapted_text = adapts_text_to_correct_format(main_text)

word_quantity = calculate_words_in_text(adapted_text)

unique_words = find_unique_words(adapted_text)

keyword = find_frequent_words(adapted_text)

print(adapted_text)
print(f'In your text: {word_quantity} words')
print(f'In your text you have unique word: {len(unique_words)} your unique words is {unique_words}')  # Убрать {}
print(f'{keyword}')
