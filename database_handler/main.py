from sys import exit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.__window = self.setup_ui('main_screen.ui')
    
    def setup_ui(self, ui_file_name):
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()
        return loader.load(ui_file)

    def init(self):
        self.__window.show()


if __name__ == '__main__':
    app = QApplication([])
    
    window = Main()
    window.init()

    exit(app.exec())