def clear_text(text):
    """This function removes non-text characters and words from text, leads to lowercase and detir one line per word list
    :param text: working text
    :type text: str
    :return: text without extra characters
    :rtype: str
    """

    words = [' this ', ' from ', ' to ', ' is ', ' are ', ' was ', ' were ', ' will ', ' would', ' the ', ' could ', ' and ', ' or ', ' of ', ' if ']

    symbols = ['.', ',', '!', '?', '"', '(', ')', ' – ', '– ' ]

    for i in symbols:
        text = text.replace(i, ' ')

    for i in words:
        text = text.replace(i, ' ')

    new_text = text.lower()

    return new_text.split()


def count_words(unique_text, unique_words ):

    """
    This function counts how many times each word is repeated.
    :param unique_tex: Clear text
    :param unique_words: Set unique words
    :type unique_tex: List
    :type unique_words: Set
    :return: Dictionary with a series of repetitions
    :rtype: Dictionary
    """

    dic_worlds = {}

    for i in unique_words:

        dic_worlds[i] = unique_text.count(i)

    sorted_words = sorted(((value, key) for (key, value) in dic_worlds.items()))

    return  sorted_words


def print_top_words(counter):
    """This function prints the top 3 frequency words
    :param counter: sorted list
    :type counter: list
    :return: A couple of words and frequency
    :rtype: str
    """

    top = [-1, -2, -3 ]

    for i in top:

       print (f' {counter[i][1]} - {counter[i][0]},')


def percent_of_text(counter):
    """
    This function displays the ratio of the word to the number of words in the text as a percentage on the screen.
     :param counter: sorted list
     :type counter: list
     :return: A couple of words and percent
     :rtype: str
     """
    unique_text_len = len(unique_words)
    for i in reversed(range(unique_text_len)):

        print(f'{counter[i][1]} - {int(counter[i][0] / unique_text_len * 100)}%,')


text =  'Meet my family. There are five of us – my parents, my elder brother, my baby sister and me. First, meet my mum and dad, Jane and Michael. My mum enjoys reading and my dad enjoys playing chess with my brother Ken. My mum is slim and rather tall. She has long red hair and big brown eyes. She has a very pleasant smile and a soft voice. My mother is very kind and understanding. We are real friends. She is a housewife. As she has three children, she is always busy around the house. She takes care of my baby sister Meg, who is only three months old. My sister is very small and funny. She sleeps, eats and sometimes cries. We all help our mother and let her have a rest in the evening. Then she usually reads a book or just watches TV. My father is a doctor. He is tall and handsome. He has short dark hair and gray eyes. He is a very hardworking man. He is rather strict with us, but always fair. My elder brother Ken is thirteen, and he is very clever. He is good at Maths and always helps me with it, because I can hardly understand all these sums and problems. Ken has red hair and brown eyes. My name is Jessica. I am eleven. I have long dark hair and brown eyes. I am not as clever as my brother, though I try to do my best at school too. I am fond of dancing. Our dancing studio won The Best Dancing Studio 2015 competition last month. I am very proud of it. I also like to help my mother with my little sister very much. Our family is very united. We love each other and always try to spend '
unique_text = clear_text(text)
unique_words = set(unique_text)
counter = count_words(unique_text, unique_words)



print (f" The number of words in the text {len(unique_text)}")
print (f" The number of unique words in the text {len(unique_words)}")
print (" Keywords: ")
print ( print_top_words(counter))
print (percent_of_text(counter))