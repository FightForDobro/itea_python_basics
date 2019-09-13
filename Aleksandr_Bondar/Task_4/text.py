

def text_prepare(text_to_prepare):

    """ This function prepares the raw text for analyze. It lowers the case, removes chars based on 'exclude_chars' variable, split text to words based on space character,
removes words based on 'exclude_words' variable.
:param text_to_prepare: string to exctract words from
:type text_to_prepare: string
:return: list, which consist of words, with special chars anb words filtered
:rtype: list
"""

    text_to_prepare = text_to_prepare.lower()

    for i in exclude_chars:
        
        text_to_prepare = text_to_prepare.replace(i,' ')

    list_chars_filtered = [x.strip() for x in text_to_prepare.split()]
       
    for j in exclude_words:

        while j in list_chars_filtered:

            list_chars_filtered.remove(j)
                    
                    
    list_chars_words_filtered = list_chars_filtered.copy()

    return list_chars_words_filtered


def words_count(text_to_count):

    """ This function forms list of tuples, each tuple consist of pair 'word':'word's repetition in text'. All repetitive values are removed. In first stage, function forms a list
of each word repetition. The second stage is to form a dictionary from this list, it's done in order to remove duplicates. At third stage, this dictionary is sorted based on values
in reversed order.
:param text_to_count: List of string elements.
:type text_to_count: list
:return: Sorted list of tuples, each tuple consist of pair 'word':'word's repetition in text'
:rtype: list of tuples
"""

    words_count_list = [text_to_count.count(text_to_count[x]) for x in range(len(text_to_count))]

# To make a dict in order to remove duplicates
    
    words_count_dict = dict(zip(text_to_count,words_count_list))
    
# To sort dictionary based on values in reverse order

    words_count_list_sorted = sorted(words_count_dict.items(), key = lambda x: x[1], reverse = True)
    
    return words_count_list_sorted


def words_percentage(words_to_count):

    """ This function calculates percentage of word's repetition in text. It takes list of tuples from function 'words_count', and based on second position of each tuple,
function calculates the rate of word in first tuple position. Output is list of tuples as well, but instead of word repetition, word's appearance percentage is inserted.
:param words_to_count: list of tuples, where first position in each tuple is the word, second position - word's repetition
:type words_to_count: list of tuples
:return: list of tuples, where first position in each tuple is the word, second position - word's appearance in percents
:rtype: list of tuples
"""

    words_percentage = []
    
    for i,j in words_to_count:

        word_percentage = (j / len(text_normalized))*100
        
        word_tuple = tuple([i,round(word_percentage,2)])

        words_percentage.append(word_tuple)

    return words_percentage
        

exclude_words = [
    'as','a','an','the','from','to','is','are','was','were','will','would','could','and','or','of',
    'if','he','she','it','this','that','my','in','on','be','by','into']

exclude_chars = ['.',',','!','?','"',' - ','(',')']


text = input('enter text: ')
text_normalized = text_prepare(text)

amount_of_words = len(text_normalized)
print('Total amount of words is:', amount_of_words)

amount_of_dict = len(set(text_normalized))
print('\nTotal amount of unique words is:', amount_of_dict, 'unique words are: \n', set(text_prepare(text)))


words_count_list = words_count(text_normalized)

first_word = words_count_list[0][0]
first_word_co = words_count_list[0][1]

second_word = words_count_list[1][0]
second_word_co = words_count_list[1][1]

third_word = words_count_list[2][0]
third_word_co = words_count_list[2][1]

print('\n3 most used words are:\n',first_word,' : ',first_word_co,'\n',second_word,' : ',second_word_co,'\n',third_word,' : ',third_word_co)

print('\nThe words percentage is: \n', dict(words_percentage(words_count_list)))

print('\nTHE END')
 
