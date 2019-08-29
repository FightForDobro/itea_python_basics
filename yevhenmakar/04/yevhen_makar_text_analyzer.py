def calculate_word(array_for_calculating):

    """
    This function calculates quantity of words in the inputted array
    :param array_for_calculating: Array with words that have to be counted
    :type array_for_calculating: list, tuple
    :return: number of words quantity
    :rtype: int
    """

    return len(array_for_calculating)


def extract_unique_words(array_for_extracting):

    """
    This function creates a set of unique words from inputted array
    :param array_for_extracting: Array with words that have to be converted in set of unique words
    :type array_for_extracting: list, tuple
    :return: Set of unique words
    :rtype: set
    """

    return set(array_for_extracting)


def find_keywords(array_for_finding):

    """
    This function counts quantity of each words that faced in the inputted array and sorted by quantity from highest to
    lowest
    :param array_for_finding: Array with words that have to be counted and sorted
    :type array_for_finding: list, tuple
    :return: list of tuples with quantity of each word that faced in the inputted array
    :rtype: list
    """

    keywords_dict = {}
    for keywords in array_for_finding:
        keywords_dict[keywords] = array_for_finding.count(keywords)
    keywords_list = list(keywords_dict.items())
    keywords_list.sort(key=lambda x: x[1], reverse=True)

    return keywords_list


def calculate_frequency(favorite_words_array):

    """
    This function calculates frequency of words faced in the inputted array
    :param favorite_words_array: List of the words, used for calculate its frequency
    :type favorite_words_array: list, tuple
    :return: list of tuples with frequency of each word that faced in the inputted array
    :rtype: list
    """

    favorite_words_dict = {}

    for favorite_word in favorite_words_array:
        favorite_words_dict[favorite_word[0]] = round((favorite_word[1] / quantity_words * 100), 2)

    favorite_words_list = list(favorite_words_dict.items())

    return favorite_words_list


punctuation_list = ['.', ',', ';', ':', '!', '?', '/', '"', '“', '”', '\n']

not_analyzed_words = ['a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if', 'he',
                      'she', 'it', 'this', 'my', 'do', 'don’t', 'didn’t', 'wasn’t', 'weren’t', 'won’t', 'does',
                      'did', 'the', 'of', 'on', 'we’re', 'for', 'but', 'it’s', 'in', 'they', 'into']

default_text = '''
Amy normally hated Monday mornings, but this year was different. Kamal was in her art class and she liked Kamal. She 
was waiting outside the classroom when her friend Tara arrived. “Hi Amy! Your mum sent me a text. You forgot your 
inhaler. Why don’t you turn your phone on?” Amy didn’t like technology. She never sent text messages and she hated 
Facebook too. “Did Kamal ask you to the disco?” Tara was Amy’s best friend, and she wanted to know everything that was 
happening in Amy’s life. “I don’t think he likes me,” said Amy. “And I never see him alone. He’s always with Grant.” 
Amy and Tara didn’t like Grant. “Do you know about their art project?” asked Amy. “It’s about graffiti, I think,” said 
Tara. “They’re working on it at the old house behind the factory.” “But that building is dangerous,” said Amy. “Aah, 
are you worried he’s going to get hurt?" Tara teased. “Shut up, Tara! Hey look, here they come!” Kamal and Grant 
arrived. “Hi Kamal!” said Tara. “Are you going to the Halloween disco tomorrow?” “Yes. Hi Amy,” Kamal said, smiling. 
“Do you want to come and see our paintings after school?” “I’m coming too!” Tara insisted. After school, Kamal took the 
girls to the old house. It was very old and very dirty too. There was rubbish everywhere. The windows were broken and 
the walls were damp. It was scary. Amy didn’t like it. There were paintings of zombies and skeletons on the walls. 
“We’re going to take photos for the school art competition,” said Kamal. Amy didn’t like it but she didn’t say 
anything. “Where’s Grant?” asked Tara. “Er, he’s buying more paint.” Kamal looked away quickly. Tara thought he looked 
suspicious. “It’s getting dark, can we go now?” said Amy. She didn’t like zombies. Then, they heard a loud noise coming 
from a cupboard in the corner of the room. “What’s that?” Amy was frightened. “I didn’t hear anything,” said Kamal. 
Something was making strange noises. There was something inside the cupboard. “Oh no! What is it?” Amy was very 
frightened now. “What do you mean? There’s nothing there!” Kamal was trying not to smile. Suddenly the door opened with 
a bang and a zombie appeared, shouting and moving its arms. Amy screamed and covered her eyes. “Oh very funny, Grant!” 
said Tara looking bored. Kamal and Grant started laughing. “Ha ha, you were frightened!” said Grant. "Do you like my 
zombie costume?” Amy took Tara’s arm. “I can’t breathe,” she said. Kamal looked worried now. “Is she OK? It was only a 
joke.” “No she’s not OK, you idiot. She’s having an asthma attack and she forgot her inhaler.” Tara took out her phone. 
“I’m calling her dad.” Next evening was Halloween. The girls were at the school disco. “Are you better now?” asked 
Tara. “I’m fine,” said Amy. “I think it was the smell of paint that started the attack.” Tara looked around. “So, where 
are the zombies?” “I don’t know, I don’t want to see Kamal again,” said Amy. “Come on, let’s dance!” Amy and Tara were 
dancing when Grant arrived, looking worried. “Hi, someone stole my phone. Have you seen Kamal? He said he was coming 
here at eight o’clock. Can you phone him?” “Go away, idiot!” Tara didn’t stop dancing. Grant looked upset. “Tell him 
I’m looking for him,” he called as he left the disco. Tara really didn’t like Grant. Just then, Tara’s phone rang. She 
looked at it. “Ha!” she said, “I don’t believe it!” “What is it?” asked Amy. “Kamal just sent a text to everyone. 
Listen!” Tara read out Kamal’s message.
'''


while True:
    choice = input('Do you want to analyze own text or default?? Write down "own" or "default":')

    if choice == 'own':
        analyzed_text = input('Enter text: ')
        break

    elif choice == 'default':
        analyzed_text = default_text
        break

    else:
        print('Write correct answer!')
        continue

# Lowering text to avoid differentiating words by register
analyzed_text = analyzed_text.lower()

# Clearing text from punctuation marks and auxiliary words
for punctuation_marks in punctuation_list:

    analyzed_text = analyzed_text.replace(punctuation_marks, '')

separated_words_list = analyzed_text.split(' ')

list_for_analyzing = []

for i in separated_words_list:

    if i not in not_analyzed_words:
        list_for_analyzing.append(i)

# Calculating overall quantity words, defining unique words, calculating quantity and frequency of each word
quantity_words = calculate_word(list_for_analyzing)

unique_words = extract_unique_words(list_for_analyzing)

favorite_words = find_keywords(list_for_analyzing)

words_frequency = calculate_frequency(favorite_words)

# Converting lists to strings for convenient output
unique_words_string = ', '.join(unique_words)

favorite_words_string = f'{favorite_words[0][0]} - {favorite_words[0][1]}; {favorite_words[1][0]} - ' \
                        f'{favorite_words[1][1]}; {favorite_words[2][0]} - {favorite_words[2][1]} '

words_frequency_string = f'{words_frequency[0][0]} - {words_frequency[0][1]}%; {words_frequency[1][0]} - ' \
                         f'{words_frequency[1][1]}%; {words_frequency[2][0]} - {words_frequency[2][1]}% '

# Outputting reults:
print('Words quantity:', quantity_words)

print('Text dictionary:', unique_words_string)

print('Keywords:', favorite_words_string)

print('Frequency:', words_frequency_string)