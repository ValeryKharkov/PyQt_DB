from PySide6 import QtWidgets, QtSql, QtCore
from form_exam import Ui_Form



class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initSQLModel()
        self.initUi()  # Метод для инициализации интерфейса
        self.initSignals() # Метод для инициализации сигналов

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setWindowTitle("Телефонная книга")  # Установка заголовка окна

        # Создание виджетов Label
        labelFirstName = QtWidgets.QLabel('Имя')
        labelLastName = QtWidgets.QLabel('Фамилия')
        labelPhone = QtWidgets.QLabel('Телефон')

        # Создание виджетов lineEdit
        self.lineEditFirstName = QtWidgets.QLineEdit()
        self.lineEditFirstName.setPlaceholderText("Введите имя")

        self.lineEditLastName = QtWidgets.QLineEdit()
        self.lineEditLastName.setPlaceholderText("Введите фамилию")

        self.lineEditPhone = QtWidgets.QLineEdit()
        self.lineEditPhone.setPlaceholderText("Введите телефон")

        # Создание кнопки add
        self.pushButtonAdd = QtWidgets.QPushButton('Добавить')

        # Создание слоя с виджетами Label
        layoutLabel = QtWidgets.QVBoxLayout()
        layoutLabel.addWidget(labelFirstName)
        layoutLabel.addWidget(labelLastName)
        layoutLabel.addWidget(labelPhone)

        # Создание слоя с виджетами lineEdit
        layoutLineEdit = QtWidgets.QVBoxLayout()
        layoutLineEdit.addWidget(self.lineEditFirstName)
        layoutLineEdit.addWidget(self.lineEditLastName)
        layoutLineEdit.addWidget(self.lineEditPhone)

        # Создание слоя DataEntry (Ввод данных)
        layoutDataEntry = QtWidgets.QHBoxLayout()
        layoutDataEntry.addLayout(layoutLabel)
        layoutDataEntry.addLayout(layoutLineEdit)

        # Создание основного слоя
        layoutMain = QtWidgets.QVBoxLayout()

        # Добавление слоёв с виджетами на основной слой
        # layoutMain.addLayout(layoutLabel)
        # layoutMain.addLayout(layoutLineEdit)
        layoutMain.addLayout(layoutDataEntry)
        layoutMain.addWidget(self.pushButtonAdd)

        # Установка основного слоя на окно
        self.setLayout(layoutMain)

        # Таблица
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.setColumnHidden(4, True)
        self.ui.tableView.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonAdd.clicked.connect(self.onPushButtonAddClicked)
        self.ui.pushButtonDel.clicked.connect(self.onPushButtonDelClicked)

    def initSQLModel(self) -> None:
        """
        Создание подключения (модели) для работы с БД

        :return: None
        """

        # Загрузка драйвера и установка БД
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('fieldlist.db')

        # db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        # db.setDatabaseName('PyQt_exam.db')

        # Создание модели
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('field')  # Выбор таблицы, с которой работает модель
        self.model.select()  # Заполнение модели данными из таблицы 'field'
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Имя")  # Установка данных для наименование заголовков таблицы
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Фамилия")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Телефон")

    def onPushButtonAddClicked(self):
        """
        Обработка нажатия на кнопку "Добавить"
        :return:
        """

        index = self.model.rowCount()
        self.model.insertRows(index, 1)
        self.model.setData(self.model.index(index, 1), self.ui.lineEditName.text())
        self.model.setData(self.model.index(index, 2), self.ui.lineEditSurname.text())
        self.model.setData(self.model.index(index, 3), self.ui.lineEditPhone.text())

        self.model.submitAll()

    def onPushButtonDelClicked(self) -> None:
        """
        Обработка нажатия на кнопку "Удалить"

        :return: None
        """

        if self.ui.tableView.currentIndex().row() > 0:
            self.model.removeRow(self.ui.tableView.currentIndex().row())
            self.model.select()

        else:
            QtWidgets.QMessageBox.question(self, 'Уведомление', 'Пожалуйста, выберите строку для удаления',
                                           QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()