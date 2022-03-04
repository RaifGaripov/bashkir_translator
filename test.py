import ctypes
import os
import sys

from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QShortcut,
    QPlainTextEdit,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QWidget,
)


def translate(inp):
    outp_string = "Trasnlated!"
    return outp_string


# Subclass QMainWindow
class Translator(QMainWindow):
    def __init__(self):
        super().__init__()

        # widgets
        self.inp = QPlainTextEdit()
        self.outp = QPlainTextEdit()
        self.translate_btn = QPushButton()

        self.layout = QHBoxLayout()
        self.widget = QWidget()
        self.shortcut_translate = QShortcut(QKeySequence("Ctrl+Return"), self)

        self.layout.addWidget(self.inp)
        self.layout.addWidget(self.translate_btn)
        self.layout.addWidget(self.outp)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.showMaximized()

        self.set_widgets_style()

    def set_widgets_style(self):
        # window settings
        self.setWindowTitle("Переводчик с башкирского на русский")
        self.setStyleSheet("background: #E8EAF6")
        self.setWindowIcon(
            QIcon(os.path.join(os.path.dirname(__file__), "baru.png")))

        # textbox settings
        self.setStyleSheet("QPlainTextEdit { font-family: Verdana, sans-serif;"
                           " font-size: 18pt;}")

        self.inp.setPlaceholderText("Введите башкирский текст")
        self.outp.setReadOnly(True)

        # button settings
        self.translate_btn.setText("→")
        self.translate_btn.setStyleSheet(
            '''
           QPushButton {
                background-color: #00BFFF;
                color: #FFFFFF;
                border-style: outset;
                padding: 2px;
                font: bold 20px;
                border-width: 6px;
                border-radius: 10px;
                border-color: #2752B8;
            }
            QPushButton:hover {
                background-color: #82CAFF;
            }
            '''
        )

        # connections
        self.translate_btn.clicked.connect(self.get_translate)
        self.shortcut_translate.activated.connect(self.get_translate)

    def get_translate(self):
        inp = self.inp.toPlainText()

        if inp:
            outp = translate(inp)

            self.outp.setPlainText(outp)


if __name__ == "__main__":

    # set taskbar logo
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)

    window = Translator()
    window.show()

    sys.exit(app.exec())
