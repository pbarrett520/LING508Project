from sinopy import chars2gloss # This project could be helpful for adding future features

class Chinese_character:
    HANZI_ERROR = "亲爱的用户，请输入一个汉子.\nDear user, please enter one Chinese character."
    def __init__(self, hanzi):
        self.hanzi = hanzi
        self.english_gloss = self.__get_english_gloss__(hanzi)

        if self.__is_single_chinese_character__(hanzi):
            self.hanzi_error = None
        else:
            self.hanzi_error = Chinese_character.HANZI_ERROR

    @staticmethod
    def __is_single_chinese_character__(character: str) -> bool:
        if len(character) != 1:
            return False
        # Check if string belongs to CJK unicode block
        cjk_range = (0x4E00, 0x9FFF)  # CJK Unified Ideographs
        code_point = ord(character)
        if cjk_range[0] <= code_point <= cjk_range[1]:
            return True
        else:
            return False

    @staticmethod
    def __get_english_gloss__(character: str) -> str:
        return ' '.join(chars2gloss(character))