def filtered_text(input_text):

    """ This function create list of words filtered from bad words and special chars.
    :input_text: string from user input
    :type input_text: string
    :return: list which contains all the words except special chars and bad words 
    :rtype: list
    """

    bad_words = ['as', 'a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if', 'he', 'she', 'it', 'this', 'my', 'i']
    bad_chars = [',', '.', '!', '?', '-']
    
    input_text = input_text.lower()
    
    for i in bad_chars:
    
        if i in input_text:
        
            input_text = input_text.replace(i, ' ')
            
    filtered_list = input_text.split()
    
    for j in bad_words:
    
        while j in filtered_list:
        
            filtered_list.remove(j)
            
    return filtered_list
    
    
def unique_words_count(text):

    """ This function create list of tuples in which each tuple contains of pair 'word':'frequency of this word'. Then we sort this list 
        by the frequency of words.
    :param text: cleaned list of words
    :type text: list
    :return: sorted list of tuples
    :rtype: list of tuples
    """

    # We need to form list that will include elements which represent frequency of each word 
    
    frequency_list = [text.count(text[x]) for x in range(len(text))]

    # We form list of tuples by using zip function and then translate this list to dictionary to avoid duplicates

    frequency_dict = dict(zip(text, frequency_list))

    """ We sort our dictionary using reverse and then using key parameter with function lambda - this give us possibility to sort by 
      values in dictionary
    """

    frequency_list_sorted = sorted(frequency_dict.items(), key = lambda x: x[1], reverse = True)

    return frequency_list_sorted

    
user_input = "This is my favourite text. Let's try to analyze it. I love this text. I love Python."

cleaned_text = filtered_text(user_input)

print('Total words quantity:', len(cleaned_text))
print('Text dictionary:', set(cleaned_text))

words_count = unique_words_count(cleaned_text)

keywords = {}

for i in range(3):

    keywords[words_count[i][0]] = words_count[i][1]
    
print(keywords)
