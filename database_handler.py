from sys import exit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import QFile

from database_handler.controllers.General import Controller as GeneralController
from database_handler.controllers.Skills import Controller as SkillsController
from database_handler.controllers.Experience import Controller as ExperienceController
from database_handler.controllers.Formation import Controller as FormationController
from database_handler.controllers.Projects import Controller as ProjectsController
from database_handler.controllers.Blog import Controller as BlogController

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
        self.__table_widget_general = self.__window.table_widget__general
        self.__table_widget_skills = self.__window.table_widget__skills
        self.__table_widget_experience = self.__window.table_widget__experience
        self.__table_widget__formation = self.__window.table_widget__formation
        self.__table_widget_projects = self.__window.table_widget__projects
        self.__table_widget_blog = self.__window.table_widget__blog

        self.__button_general = self.__window.button__general
        self.__button_skills = self.__window.button__skills
        self.__button_experience = self.__window.button__experience
        self.__button_formation = self.__window.button__formation
        self.__button_projects = self.__window.button__projects
        self.__button_blog = self.__window.button__blog

        self.__button_general.clicked.connect(self.save_general)
        self.__button_skills.clicked.connect(self.save_skills)
        self.__button_experience.clicked.connect(self.save_experience)
        self.__button_formation.clicked.connect(self.save_formation)
        self.__button_projects.clicked.connect(self.save_projects)
        self.__button_blog.clicked.connect(self.save_blog)

    def init(self):
        """
        Renderizar janela
        """
        self.__window.show()
        self.init_general()
        self.init_skills()
        self.init_experience()
        self.init_formation()
        self.init_projects()
        self.init_blog()


    def init_general(self):
        """
        Inicializar tab Geral
        """
        controller = GeneralController()
        options = controller.get_data()
        for line in options:
            number_rows = self.__table_widget_general.rowCount()
            self.__table_widget_general.insertRow(number_rows)

            number_column = 0
            for _ in range(len(line)):
                self.__table_widget_general.setItem(number_rows , number_column, QTableWidgetItem(line[number_column]))
                number_column += 1


    def init_skills(self):
        """
        Inicializar tab Skills
        """
        controller = SkillsController()
        options = controller.get_data()
        for line in options:
            number_rows = self.__table_widget_skills.rowCount()
            self.__table_widget_skills.insertRow(number_rows)

            number_column = 0
            for _ in range(len(line)):
                self.__table_widget_skills.setItem(number_rows , number_column, QTableWidgetItem(line[number_column]))
                number_column += 1

    def init_experience(self):
        """
        Inicializar tab Experience
        """
        controller = ExperienceController()
        options = controller.get_data()
        for line in options:
            number_rows = self.__table_widget_experience.rowCount()
            self.__table_widget_experience.insertRow(number_rows)

            number_column = 0
            for _ in range(len(line)):
                self.__table_widget_experience.setItem(number_rows , number_column, QTableWidgetItem(line[number_column]))
                number_column += 1

    def init_formation(self):
        """
        Inicializar tab Formation
        """
        controller = FormationController()
        options = controller.get_data()
        for line in options:
            number_rows = self.__table_widget__formation.rowCount()
            self.__table_widget__formation.insertRow(number_rows)

            number_column = 0
            for _ in range(len(line)):
                self.__table_widget__formation.setItem(number_rows , number_column, QTableWidgetItem(line[number_column]))
                number_column += 1

    def init_projects(self):
        """
        Inicializar tab Projects
        """
        controller = ProjectsController()
        options = controller.get_data()
        for line in options:
            number_rows = self.__table_widget_projects.rowCount()
            self.__table_widget_projects.insertRow(number_rows)

            number_column = 0
            for _ in range(len(line)):
                self.__table_widget_projects.setItem(number_rows , number_column, QTableWidgetItem(line[number_column]))
                number_column += 1

    def init_blog(self):
        """
        Inicializar tab Blog
        """
        controller = BlogController()
        options = controller.get_data()
        for line in options:
            number_rows = self.__table_widget_blog.rowCount()
            self.__table_widget_blog.insertRow(number_rows)

            number_column = 0
            for _ in range(len(line)):
                self.__table_widget_blog.setItem(number_rows , number_column, QTableWidgetItem(line[number_column]))
                number_column += 1

    def save_general(self):
        """
        Salvar dados tab Geral
        """
        controller = GeneralController()
        data = []
        for row_number in range(self.__table_widget_general.rowCount()):
            row = []
            for column_number in range(self.__table_widget_general.columnCount()):
                row.append(self.__table_widget_general.item(row_number, column_number).text())
            
            data.append(tuple(row))

        controller.save_data(data)

    def save_skills(self):
        """
        Salvar dados tab Skills
        """
        controller = SkillsController()
        data = []
        for row_number in range(self.__table_widget_skills.rowCount()):
            row = []
            for column_number in range(self.__table_widget_skills.columnCount()):
                row.append(self.__table_widget_skills.item(row_number, column_number).text())
            
            data.append(tuple(row))

        controller.save_data(data)

    def save_experience(self):
        """
        Salvar dados tab Experience
        """
        controller = ExperienceController()
        data = []
        for row_number in range(self.__table_widget_experience.rowCount()):
            row = []
            for column_number in range(self.__table_widget_experience.columnCount()):
                row.append(self.__table_widget_experience.item(row_number, column_number).text())
            
            data.append(tuple(row))

        controller.save_data(data)

    def save_formation(self):
        """
        Salvar dados tab Formation
        """
        controller = FormationController()
        data = []
        for row_number in range(self.__table_widget__formation.rowCount()):
            row = []
            for column_number in range(self.__table_widget__formation.columnCount()):
                row.append(self.__table_widget__formation.item(row_number, column_number).text())
            
            data.append(tuple(row))

        controller.save_data(data)

    def save_projects(self):
        """
        Salvar dados tab Projects
        """
        controller = ProjectsController()
        data = []
        for row_number in range(self.__table_widget_projects.rowCount()):
            row = []
            for column_number in range(self.__table_widget_projects.columnCount()):
                row.append(self.__table_widget_projects.item(row_number, column_number).text())
            
            data.append(tuple(row))

        controller.save_data(data)

    def save_blog(self):
        """
        Salvar dados tab Blog
        """
        controller = BlogController()
        data = []
        for row_number in range(self.__table_widget_blog.rowCount()):
            row = []
            for column_number in range(self.__table_widget_blog.columnCount()):
                row.append(self.__table_widget_blog.item(row_number, column_number).text())
            
            data.append(tuple(row))

        controller.save_data(data)


if __name__ == '__main__':
    app = QApplication([])
    
    window = Main()
    window.init()

    exit(app.exec())