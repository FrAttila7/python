from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit
import sys


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.label1 = QLabel(self)
		self.label1.setText("Még nyílnak")
		self.label1.move(150,50)
		
		button1 = QPushButton(self)
		button1.setText("Mehet")
		button1.move(100,100)
		button1.clicked.connect(self.on_click_mehet_button)
		
		self.edit1 = QLineEdit(self)
		self.edit1.move(100, 180)
		
		
		self.setGeometry(100, 100, 750, 600)
		self.setWindowTitle("Itt vagyok")
		self.show()

	def on_click_mehet_button(self):
		print("Múködik")
		szoveg = self.edit1.text()
		self.label1.setText(szoveg)
		self.setWindowTitle("Megy")

application = QApplication(sys.argv)
mainWindow = MainWindow()
sys.exit(application.exec_())
