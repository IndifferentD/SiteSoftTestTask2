import pymorphy3


class MorphAnalyzer(pymorphy3.MorphAnalyzer):

    def get_all_forms(self, word):
        parsed_word = self.parse(word)[0]

        cases = ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct']
        numbers = ['sing', 'plur']

        all_forms = []

        for number in numbers:
            for case in cases:
                form = parsed_word.inflect({number, case})
                if form:
                    all_forms.append(form.word)

        return all_forms


morph_analyzer = MorphAnalyzer()
