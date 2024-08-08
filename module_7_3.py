class WordsFinder:
    file_find=''
    def __init__(self,*file_names):
        self.file_names = list(file_names)


    def get_all_words(self):
        dict_data = {}
        for file in self.file_names:
            word_1 = []
            str2 = ''
            with open(file, 'r', encoding="utf-8") as file:
                for line in file:
                    str1 = line.replace('\n', '')
                    str1 = str1.replace(',',' ').replace('.',' ').replace("!",' ')
                    str2 = str2 + str1
            word_1.extend(str2.split())
            dict_data[file.name] = word_1
        return dict_data
    def find(self,word):
        dict_find = {}
        for name, words in self.get_all_words().items():
            dict_find[name] = words.index(word.lower()) + 1
        return dict_find
    def count(self,word):
        dict_find = {}
        for name, words in self.get_all_words().items():
            dict_find[name] = words.count(word.lower())
        return dict_find

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего