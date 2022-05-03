from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self):
        pass


class WindowButton(Button):

    def render(self):
        print("Window button")

    def onClick(self):
        print("Window button clicked")


class HTMLButton(Button):

    def render(self):
        print("HTML button")

    def onClick(self):
        print("HTML button clicked")




class Dialog(ABC):
    """Dialog UI for windows and web"""

    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def createButton(self) -> None:
        pass



class WindowDialog(Dialog):

    def render(self) -> None:
        print("Window dialog rendering")

    def createButton(self) -> Button:
        return WindowButton()


class WebDialog(Dialog):

    def render(self) -> None:
        print("Web dialog rendering")

    def createButton(self) -> Button:
        return HTMLButton()


def read_platform() -> Dialog:

    platform = {
        "window": WindowDialog(),
        "web": WebDialog()
    }

    while True:
        pf = input("Enter the platform (window, web): ")
        if pf in platform:
            return platform[pf]
        print(f"Unknown output quality option: {pf}.")



def main(pf: Dialog):

    pf.render()

    button = platform.createButton()

    # calling button onclick
    button.onClick()


if __name__ == "__main__":
    platform = read_platform()
    main(platform)
