class LanguageMixin:

    def __init__(self, language='EN'):
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self

        elif self.__language == 'RU':
            self.__language = 'EN'
            return self

        elif self.__language not in ['RU', 'EN']:
            raise AttributeError('property "language" of "Keyboard" object has no setter')



