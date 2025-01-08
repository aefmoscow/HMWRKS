class WordsFinder:
    def __init__(self):
        self.file_names = ()
    def get_all_words(self, file_names):
        all_words = {}
        with open(self.file_names) as file:
            for inwrite_string in file_names:
            all_words[(strings_positions, byte)] = inwrite_string

        return

# Пример выполнения программы:
finder2 = WordsFinder('73test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
