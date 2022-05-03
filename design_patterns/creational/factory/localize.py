class GreekLocalizer:

    def __init__(self) -> None:
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg: str):
        """We'll punt if we don't have a translation"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """ Simply echoes the message """

    def localize(self, msg: str):
        return msg



def get_localizer(language: str = "English") -> object:
    localizer = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer
    }

    return localizer[language]()

if __name__ == "__main__":
    e, g = get_localizer(language="English"), get_localizer(language="Greek")

    for msg in "dog cat parrot beer".split(" "):
        print(e.localize(msg), g.localize(msg))