from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. List-based dictionary implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ListDictionary(BaseDictionary):

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        self.wordfrelist = words_frequencies
        # print(self.wordfrelist)
        # print(self.wordfrelist[0].word)

def search(self, word: str) -> int:
    """
    search for a word
    @param word: the word to be searched
    @return: frequency > 0 if found and 0 if NOT found
    """

    listlen = len(self.wordfrelist)
    i = 0
    while i < listlen:
        if i == 0:
            search_list = [self.wordfrelist[0].word]
        else:
            search_list.append(self.wordfrelist[i].word)
        i = i + 1
    # print(search_list)
    if word in search_list:
        index = search_list.index(word)
        # print(search_list[index])
        return search_list[index]
    else:
        return 0

def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
    """
    add a word and its frequency to the dictionary
    @param word_frequency: (word, frequency) to be added
    @return: True whether succeeded, False when word is already in the dictionary
    """

    self.wordfrelist.append(word_frequency)

    if self.search(word_frequency.word):
        # print("good")
        return True
    else:
        # print("bad")
        return False

def delete_word(self, word: str) -> bool:
    """
    delete a word from the dictionary
    @param word: word to be deleted
    @return: whether succeeded, e.g. return False when point not found
    """
    listlen = len(self.wordfrelist)
    i = 0
    while i < listlen:
        if i == 0:
            search_list = [self.wordfrelist[0].word]
        else:
            search_list.append(self.wordfrelist[i].word)
        i = i + 1
    for word in search_list:
        self.wordfrelist.pop(search_list.index(word))
        # print(self.wordfrelist)
        return True
    else:
        print("not found")
        return False

def split(self,word:str):
    return list(word)

def autocomplete(self, prefix_word: str) -> [WordFrequency]:
    """
    return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
    @param prefix_word: word to be autocompleted
    @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
    """
    print(prefix_word)
    prefix_word_letter_list = self.split(prefix_word)
    len_prefix_word_letter_list = len(prefix_word_letter_list)
    autoword_list = []
    top3list = []
    xindex = 0
    for x in self.wordfrelist:
        letter_list = x.word
        while xindex < len_prefix_word_letter_list:
            print(xindex)
            if prefix_word_letter_list[xindex] in letter_list:
                find = True
            else:
                find = False
            xindex+=1
        if find:
            autoword_list.append(x)
    autoword_list_len = len(autoword_list)
    y=0
    while y < autoword_list_len:
        i = 0
        while i < autoword_list_len-1:
            if autoword_list[i].frequency < autoword_list[i + 1].frequency:
                popword = autoword_list.pop(i)
                autoword_list.insert(i + 1,popword)
            i += 1
        y+=1
    print(autoword_list)
    time = 0
    while time < 3:
        top3list.append(autoword_list[time])
    return top3list
