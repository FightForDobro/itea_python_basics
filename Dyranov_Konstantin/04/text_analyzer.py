text = """Meet my family. There are five of us – my parents, my elder
          brother, my baby sister and me. First, meet my mum and dad,
          Jane and Michael. My mum enjoys reading and my dad enjoys playing
          chess with my brother Ken. My mum is slim and rather tall. She has
          long red hair and big brown eyes. She has a very pleasant smile and
          a soft voice. My mother is very kind and understanding. We are real
          friends. She is a housewife. As she has three children, she is
          always busy around the house. She takes care of my baby sister Meg,
          who is only three months old. My sister is very small and funny. She
          sleeps, eats and sometimes cries. We all help our mother and let her
          have a rest in the evening. Then she usually reads a book or just
          watches TV. My father is a doctor. He is tall and handsome. He has
          short dark hair and gray eyes. He is a very hardworking man. He is
          rather strict with us, but always fair. My elder brother Ken is
          thirteen, and he is very clever. He is good at Maths and always
          helps me with it, because I can hardly understand all these sums
          and problems. Ken has red hair and brown eyes. My name is Jessica.
          I am eleven. I have long dark hair and brown eyes. I am not as
          clever as my brother, though I try to do my best at school too. I am
          fond of dancing. Our dancing studio won The Best Dancing Studio
          competition last month. I am very proud of it. I also like to help
          my mother with my little sister very much. Our family is very
          united. We love each other and always try to spend more time
          together.
       """

text = text.lower()# make text the same size

text = text.replace(".", "").replace(",", "").replace("–", "")# remove signs of foaming

not_analyze = ["i", "me", "you", "your", "we", "he", "she", "my", "our", "as",
             "us", "hem", "her", "they", "of", "for", "to", "in", "on", "or",
             "at", "it", "is", "has", "just", "very", "a", "an", "and", "are",
             "the", "as", "while", "with", "who", "will", "then", "but",
             "all", "meet", "there", "always", "because", "these", "am",
             "not", "try", "too", "am", "also", "try", "each", "more"]# Not analyze words

clear_text = [x for x in text.split() if x not in not_analyze]# delate not_analyze words from text


def len_text(x):
    """
        :the function finds the number of words in the text
        :param clear_text: text without not analyze text
        :param text_len: number of words
        :type clear_text: list
        :type text_len: int
        :return: int of number words
        :rtype: int
    """

    text_len = len(clear_text)# know the number of words

    return text_len


output_len = len_text(clear_text)
print("words quantity:", output_len)


def unique_words(words):
    """
        :the function finds the number of words in the text
        :param empty_dict: empty list
        :param count: start count
        :param dictionary_key: dictionary with keys
        :param dictionary_item: dictionary with values and keys
        :type empty_dict: dict
        :type count: int
        :type dictionary_key: dict
        :type dictionary_item: dict
        :return: 2 dictionaries with keys and values
        :rtype: dict
    """

    empty_dict = {}# create an empty dictionary

    for word in words:# fill in the empty dictionary
        count = empty_dict.get(word, 0)
        empty_dict[word] = count + 1

    dictionary_key = empty_dict.keys()# dictionary with keys
    dictionary_item = empty_dict.items()# dictionary with values and keys

    return dictionary_key, dictionary_item


output_unique = unique_words(clear_text)
print("text dictionary:", ', '.join(output_unique[0]))


def Find_keywords(dictionary):
    """
        :the function finds the number of words in the text
        :param dictionary_item: dictionary with values ​​and keys
        :param dictionary_sort: dictionary sorting
        :type dictionary_item: dict
        :return: sorted dictionary
        :rtype: dict
    """

    dictionary_item = dictionary[1]# take a dictionary with keys and meaning
    dictionary_sort = sorted(dictionary_item, key=lambda x: x[1])# sort the dictionary

    return dictionary_sort

output_keywords = Find_keywords(output_unique)
print("keywords: ", output_keywords[-1], output_keywords[-2], output_keywords[-3])

def frequency():
    print("I failed to find a solution to this problem. I reviewed the lessons"
          " and searched for solutions on the Internet, but still could not"
          " find a solution to this problem. SORRY")
