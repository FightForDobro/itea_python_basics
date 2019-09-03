from  collections import OrderedDict

def calculate_words(words):
    """ This function make сalculate words quantity
        :param words: list with all the words
        :type words: list
        :return: Return word count
        :rtype: int
    """
    sum_words = len(words)
    return sum_words

def unique_words(words):
    """ This function make extracts unique words
        :param words: list with all the words
        :type words: list
        :return: Return list with unique words
        :rtype: list
    """
    unique_words_dict = set(words)
    return unique_words_dict

def calculate_frequency(words):
    """ This function make calculate frequency for each word - word quantity / all words quantity * 100 and
        print top3 frequency words
        :param words: list with all the words
        :type words: list
        :return: bool
        :rtype: bool
    """
    text_sotr = sorted(words)  # sorted list
    words_weight = []
    dict2 = {}
    counter = 100
    counter2 = 0

    while True: # loop that writes a each unique word and its frequency to an empty list words_weight
        text_sotr1 = [i for i in text_sotr if i == text_sotr[0]]
        words_weight.append((text_sotr1[0], len(text_sotr1) / calculate_words(words) * 100))
        text_sotr2 = [i for i in text_sotr if i != text_sotr[0]]
        text_sotr = text_sotr2

        if len(text_sotr2) == 0:
            break

    dict1 = dict(words_weight) # convert list to dict

    while counter >= 0:

        for key, value in dict1.items(): #loop that sorts the dict by value

            if value >= counter:
                dict2[key] = value
                dict3 = OrderedDict(dict2)
        counter -= 1

    print("Words - frequency (%)")

    for key, value in dict3.items(): #loop that prints key and value
        print(key, value)

    print("")
    print("TOP3: words - frequency (%)")
    for key, value in dict3.items(): #loop that prints top3 value
        print(key, value)
        if counter2 == 2:
            break

        counter2 += 1

    return True

# text
text = "Our goal is to make 'Gambling Great Again' in the United States, the days of taking trips to Las Vegas are no longer needed to play the best casino games in America. Through us, you will have all the action and entertainment you need, all from the leading US casinos online. What awaits will be the most exciting online gambling US players have ever had, this includes the biggest American jackpots with multi-million-dollar prizes waiting to be won by you. To be clear, online gambling in the USA is not illegal! The US casinos supplied by our site are licensed operations that have legal backing and licensing from US gambling authorities such as the Kahnawake Gaming Commission and the Curaçao eGaming Authority. Your time playing will be protected by US online gambling laws and the real money you win is yours to keep. Time to play inside of the best online casinos for US players, playing games made by software developers from the USA, offering you the chance to win the biggest US dollar prizes anywhere on the Internet."
exclude_sym = ["{", "}", "]", "/", "(", ")", "[", ":",",", ".", "!", "?", "'", ";"] # excluded symbols
# stop words
exclude_words = ["on", "that", "your", "our", "through", "all", "had", "have", "such", "as", "what", "be", "in", "las", "us", "no", "to", "is", "are", "was", "were", "will", "would", "could", "and", "or", "if", "he", "she", "it", "this", "my", "etc", "you", "from", "the", "for", "not", "of", "with", "can", "they", "how", "into", "by", "i"]
text = text.lower() # converting text to lowercase

for i in exclude_sym: # delete excluded symbols
    text = text.replace(i, "")

text_list = text.split() # converting text to list with words
text_list_without_exclude_words = [i for i in text_list if i not in exclude_words] # delete excluded words
calculate_words_param = calculate_words(text_list_without_exclude_words)

print(f"Text has {calculate_words_param} words")
print("")
print("Unique words in text:")
print(unique_words(text_list_without_exclude_words))
print("")
print(calculate_frequency(text_list_without_exclude_words))
