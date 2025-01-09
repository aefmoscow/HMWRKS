class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        with open(str(self.file_names), 'r', encoding='utf-8') as file:
            words = file.read().lower()
            for simb in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                words = words.replace(simb, '')
                all_words[self.file_names] = words.split()
                return all_words

    def count(self, word):
        word = word.lower()
        word_counts = {}
        for (file_name_co, word_co) in self.get_all_words().items():
            word_counts[file_name_co] = word_co.count(word)
        return word_counts

    def find(self, word):
        word = word.lower()
        word_at = {}
        for (file_name_fi, word_fi) in self.get_all_words().items():
            if word in word_fi:
                word_at[file_name_fi] = word_fi.index(word) + 1
        return word_at


# Пример выполнения программы:
finder2 = WordsFinder('73test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
