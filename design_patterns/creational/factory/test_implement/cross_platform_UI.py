from abc import ABC, abstractmethod


class CreateDialog:
    @abstractmethod
    def create_button(self):
        """Subclasses must implement this"""
        pass

    def create_dialog(self, dialog_type):
        if dialog_type == "windows":
            return WindowsDialog()
        elif dialog_type == "mac":
            return MacDialog()
        else:
            raise Exception("OS type not supported")


class WindowsDialog(CreateDialog):
    def create_button(self):
        return WindowsButton()


class MacDialog(CreateDialog):
    def create_button(self):
        return MacButton()


class Button(ABC):
    @abstractmethod
    def render():
        """Subclasses must implement this"""
        pass

    @abstractmethod
    def on_click():
        """Subclasses must implement this"""
        pass


class WindowsButton(Button):
    def render(self):
        print("Render windows button")

    def on_click(self):
        print("Clicking windows button")


class MacButton(Button):
    def render(self):
        print("Render mac button")

    def on_click(self):
        print("Clicking mac button")


if __name__ == "__main__":
    dialog_type = input("Please enter the OS type: ")
    dialog = CreateDialog().create_dialog(dialog_type)
    button = dialog.create_button()
    button.render()
    button.on_click()
