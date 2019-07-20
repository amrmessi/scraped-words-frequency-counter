import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    for post_text in soup.findAll('a', {'class': 'browse-movie-title'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)
    print("\ncleaned list =======>\n")
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_words_list = []
    for word in word_list:
        symbols = "1234567890\':\\ +)(*&^%$#@"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            print(word)
            clean_words_list.append(word)
    print("\nthe frequency of each word is ====>\n")
    create_dictionary(clean_words_list)


def create_dictionary(clean_words_list):
    word_count = {}
    for word in clean_words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1),reverse=True):
        print(key,value)


start("https://yts.pm/browse-movies")