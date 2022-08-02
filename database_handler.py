from sys import exit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile

from database_handler.database_handler_controller import Controller

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.__window = self.setup_ui('./database_handler/screen.ui')
        self.link_components()
    
    def setup_ui(self, ui_file_name):
        """
        Inicializar interface
        """
        ui_file = QFile(ui_file_name)
        loader = QUiLoader()
        return loader.load(ui_file)

    def link_components(self):
        """
        Vincular componentes da interface
        """
        self.__main_tab = self.__window.main_tab

        self.__table_widget_general = self.__window.table_widget__general
        self.__table_widget_skills = self.__window.table_widget__skills
        self.__table_widget_experience = self.__window.table_widget__experience
        self.__table_widget__formation = self.__window.table_widget__formation
        self.__table_widget_projects = self.__window.table_widget__projects
        self.__table_widget_blog = self.__window.table_widget__blog

        self.__button_save = self.__window.button__save
        self.__button_add = self.__window.button__add
        self.__button_remove = self.__window.button__remove

        self.__button_add.clicked.connect(self.add_line)
        self.__button_remove.clicked.connect(self.remove_line)
        self.__button_save.clicked.connect(self.save)

    def init(self):
        """
        Renderizar janela
        """
        self.__window.show()
        self.load_tabs()

    def load_tabs(self):
        """
        Carregar dados das tabelas
        """
        for tab in self.get_all_tabs():
            controller = Controller()
            options = controller.get_data(self.get_number_tab(tab))

            if not options: continue
            for line in options:
                number_rows = tab.rowCount()
                tab.insertRow(number_rows)

                number_column = 0
                for _ in range(len(line)):
                    tab.setItem(number_rows , number_column, QTableWidgetItem(line[number_column]))
                    number_column += 1

    def add_line(self):
        """
        Adicionar linha na lista atual
        """
        tab = self.get_instance_tab(self.get_current_tab())
        number_rows =  tab.rowCount()
        tab.insertRow(number_rows)

    def remove_line(self):
        """
        Remover linha na lista atual
        """
        tab = self.get_instance_tab(self.get_current_tab())
        selected = tab.currentRow()
        tab.removeRow(selected)

    def save(self):
        """
        Salvar dados
        """
        tab = self.get_instance_tab(self.get_current_tab())
        controller = Controller()
        data = []
        for row_number in range(tab.rowCount()):
            row = {}
            for column_number in range(tab.columnCount()):
                item = tab.item(row_number, column_number)
                column = tab.horizontalHeaderItem(column_number).text()

                row[column] = item.text()
            
            data.append(row)

        success, message = controller.save_data(data, self.get_current_tab())
        if success:
            show_message(self, 'Processo finalizado', 'Dados salvos com sucesso!')
        else:
            show_message(self, 'Erro', f'Erro ao salvar dados: {message}!')


    def get_current_tab(self):
        """
        Retorna a Tab atual do usuário
        """
        return self.__main_tab.currentIndex()

    def get_all_tabs(self):
        """
        Retorna a Tab atual do usuário
        """
        return [
            self.__table_widget_general,
            self.__table_widget_skills,
            self.__table_widget_experience,
            self.__table_widget__formation,
            self.__table_widget_projects,
            self.__table_widget_blog
        ]

    def get_number_tab(self, tab):
        """
        Retorna o numero da Tab com base no nome
        """
        if tab == self.__table_widget_general:
            return 0
        elif tab == self.__table_widget_skills:
            return 1
        elif tab == self.__table_widget_experience:
            return 2
        elif tab == self.__table_widget__formation:
            return 3
        elif tab == self.__table_widget_projects:
            return 4
        elif tab == self.__table_widget_blog:
            return 5

    def get_instance_tab(self, number_tab):
        """
        Retorna o numero da Tab com base no nome
        """
        if number_tab == 0:
            return self.__table_widget_general
        elif number_tab == 1:
            return self.__table_widget_skills
        elif number_tab == 2:
            return self.__table_widget_experience
        elif number_tab == 3:
            return self.__table_widget__formation
        elif number_tab == 4:
            return self.__table_widget_projects
        elif number_tab == 5:
            return self.__table_widget_blog
        

def show_message(container, title, message):
    return QMessageBox.information(container, title, message)


if __name__ == '__main__':
    app = QApplication([])
    
    window = Main()
    window.init()

    exit(app.exec())