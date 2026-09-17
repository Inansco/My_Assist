"""
Project: Inansco AI Assistant
File: app.py
Purpose: Entry point of the application.

Author: Efada Monday
Version: 0.1
"""

import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()