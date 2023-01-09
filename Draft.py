from PySide6 import QtWidgets, QtSql, QtCore





class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()



        self.initUi()  # Метод для инициализации интерфейса

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setWindowTitle("БД")  # Установка заголовка окна

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

    def initSQLModel(self) -> None:
        """
        Создание подключения (модели) для работы с БД

        :return: None
        """

        # Загружаем драйвер и устанавливаем БД
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('fieldlist.db')

        # Создаём модель (можно использовать кастомную)
        #self.model = EditableSQLModel()
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('field')
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Имя")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Фамилия")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Телефон")



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()