import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QStackedWidget, \
    QHBoxLayout, QFormLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Setare titlu și dimensiuni
        self.setWindowTitle("Interfață de Control")
        self.setGeometry(100, 100, 500, 400)

        # Setare fereastra pe tot ecranul
        self.showMaximized()

        # Crearea layout-ului principal
        self.main_layout = QVBoxLayout()

        # Crearea unui stacked widget pentru pagini
        self.stacked_widget = QStackedWidget()

        # Crearea celor patru pagini
        self.page1 = QWidget()
        self.page2 = QWidget()
        self.page3 = QWidget()
        self.page4 = QWidget()

        # Adăugarea paginilor în stacked widget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        self.stacked_widget.addWidget(self.page4)

        # Adăugarea butoanelor de navigare
        self.nav_layout = QHBoxLayout()
        self.btn_page1 = QPushButton("Soil specs")
        self.btn_page2 = QPushButton("Climate control metrics ")
        self.btn_page3 = QPushButton("Mix Nutrient levels ")
        self.btn_page4 = QPushButton("Alert Dashboard")

        # Conectarea butoanelor pentru schimbarea paginilor
        self.btn_page1.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page1))
        self.btn_page2.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page2))
        self.btn_page3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page3))
        self.btn_page4.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.page4))

        # Adăugarea butoanelor în layout-ul de navigare
        self.nav_layout.addWidget(self.btn_page1)
        self.nav_layout.addWidget(self.btn_page2)
        self.nav_layout.addWidget(self.btn_page3)
        self.nav_layout.addWidget(self.btn_page4)

        # Crearea primei pagini (Umiditate din sol și Macronutrienți)
        self.page1_layout = QFormLayout()

        self.umiditate_label = QLabel("Umiditatea din sol (%):")
        self.umiditate_input = QLineEdit()

        self.macronutrienti_label = QLabel("Macronutrienți (N, P, K):")
        self.nutrient_input = QLineEdit()

        self.ph_label = QLabel("pH Sol: ")
        self.ph_input = QLineEdit()

        self.page1_layout.addRow(self.umiditate_label, self.umiditate_input)
        self.page1_layout.addRow(self.macronutrienti_label, self.nutrient_input)
        self.page1_layout.addRow(self.ph_label, self.ph_input)

        self.page1.setLayout(self.page1_layout)

        # Adăugarea layout-ului principal și a stacked widget
        self.main_layout.addLayout(self.nav_layout)
        self.main_layout.addWidget(self.stacked_widget)

        self.setLayout(self.main_layout)

        # Aplicarea stilului pentru fundal gri și text alb
        self.setStyleSheet("""
            QWidget {
                background-color: #333333;
                color: white;
            }
            QPushButton {
                background-color: #555555;
                color: white;
                border: 1px solid #777777;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
            QLineEdit {
                background-color: #444444;
                color: white;
                border: 1px solid #555555;
                padding: 10px;
                font-size: 16px;
            }
            QLabel {
                font-size: 18px;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
