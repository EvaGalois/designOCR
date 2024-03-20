from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a QLabel for displaying the image
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)  # Center the image horizontally and vertically

        # Load the image using QPixmap
        pixmap = QPixmap('temp\\20231106141515.png')
        self.image_label.setPixmap(pixmap)

        # Create a vertical layout and add the image label to it
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        central_widget.setLayout(layout)

        self.setWindowTitle('Image Viewer')
        self.setGeometry(100, 100, 800, 600)  # Set the initial size of the window

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
