import regex

class Chinese_character:
    def __init__(self, hanzi):
        hanzi = hanzi
        english_gloss = None
        hanzi_error = "亲爱的用户，请输入一个汉子.\nDear user, please enter one Chinese character."

        try:
            len(hanzi.split()) == 1
            regex.search(r'p{Han}', hanzi)
        except:
            return hanzi_error
# None of this can really be tested properly without a web scraping component, so I'll test the skeletons for now.