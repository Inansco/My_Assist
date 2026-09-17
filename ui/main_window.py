"""
Project: Inansco AI Assistant

File: ui/main_window.py

Main application window.
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton,
)

from core.assistant import Assistant


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.assistant = Assistant()

        self.setWindowTitle("Inansco AI Assistant")
        self.resize(900, 650)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Talk to Inansco...")

        self.send_button = QPushButton("Send")

        layout.addWidget(self.chat)
        layout.addWidget(self.input)
        layout.addWidget(self.send_button)

        central.setLayout(layout)

        self.send_button.clicked.connect(self.send_message)
        self.input.returnPressed.connect(self.send_message)

    def send_message(self):
        message = self.input.text().strip()

        if not message:
            return

        self.chat.append(f"You: {message}")

        reply = self.assistant.process(message)

        self.chat.append(f"Inansco: {reply}\n")

        self.input.clear()