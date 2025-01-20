"""
This module implements a system tray application for personal productivity tracking.
It provides functionalities to log active window data, generate reports, and manage configurations.

Classes:
- SystemTrayApp: Represents the system tray application.

Functions:
- main: Entry point for the application.
"""

import os

if 'Contents/Resources' in os.path.abspath(__file__):
    os.environ["SSL_CERT_FILE"] = 'cacert.pem'
import sys
import threading
import platform
import subprocess
import shutil

from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QTextEdit, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt

import config
from utils import set_app_autostart
from file_writers import file_writer, analysis_report_writer, defaults_config_writer
from reports import generate_today_report, generate_all_time_report


class SystemTrayApp:
    """
    A class to represent the system tray application.
    """

    def __init__(self):
        """
        Initialize the system tray application.
        """
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)

        self.icon = self.create_icon()
        self.tray_icon = QSystemTrayIcon(self.icon, self.app)
        self.tray_icon.setVisible(True)

        self.menu = self.create_menu()
        self.tray_icon.setContextMenu(self.menu)

        self.create_default_configs()
        set_app_autostart()
        self.pull_ollama_model()

        self.logging_thread = threading.Thread(target=self.start_logging)
        self.logging_thread.daemon = True
        self.logging_thread.start()

    def create_icon(self):
        """
        Create the system tray icon.

        Returns:
            QIcon: The created icon.
        """
        pixmap = QPixmap(64, 64)
        pixmap.fill(QColor("transparent"))

        painter = QPainter(pixmap)
        painter.setBrush(QColor("black"))
        painter.drawEllipse(0, 0, 64, 64)
        painter.end()

        return QIcon(pixmap)

    def create_menu(self):
        """
        Create the context menu for the system tray icon.

        Returns:
            QMenu: The created menu.
        """
        menu = QMenu()

        if self.is_ollama_installed():
            action1 = QAction("Today Report", menu)
            action1.triggered.connect(self.on_action1_triggered)
            menu.addAction(action1)

            action2 = QAction("All Time Report", menu)
            action2.triggered.connect(self.on_action2_triggered)
            menu.addAction(action2)

            action3 = QAction("Trends Report", menu)
            action3.triggered.connect(self.on_action3_triggered)
            action3.setDisabled(True)
            menu.addAction(action3)

        menu.addSeparator()

        quit_action = QAction("Quit", menu)
        quit_action.triggered.connect(self.quit_application)
        menu.addAction(quit_action)

        return menu

    def create_default_configs(self):
        """
        Create default configuration files.
        """
        defaults_config_writer(config.PRODUCTIVE, "productive")
        defaults_config_writer(config.UNPRODUCTIVE, "unproductive")
        defaults_config_writer(config.BROWSERS, "browsers")

    def is_ollama_installed(self):
        """
        Check if the Ollama interface is installed.

        Returns:
            bool: True if Ollama is installed, False otherwise.
        """
        if shutil.which("ollama") is None:
            self.show_markdown_window(
                "<h2>To generate reports using an AI model locally on your computer, please install the Ollama interface. "
                "This will enable you to run AI models directly on your machine, ensuring privacy and control over your data.</h2>"
                "<h1>https://ollama.com/download</h1>"
            )
            return False
        return True

    def pull_ollama_model(self):
        """
        Pull the Ollama model.
        """
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
        if config.OLLAMA_MODEL in result.stdout:
            print(f"Model {config.OLLAMA_MODEL} is already present on the system.")
        else:
            print(f"Pulling model {config.OLLAMA_MODEL}...")
            subprocess.run(["ollama", "pull", config.OLLAMA_MODEL], check=True)

    def start_logging(self):
        """
        Start logging the active window data.
        """
        if platform.system() == 'Darwin':
            from get_active_window_macos import AppListener
            listener = AppListener.alloc().init()
            file_writer(listener.get_active_window)
        elif platform.system() == 'Windows':
            from get_active_window_windows import get_active_window
            file_writer(get_active_window)

    def on_action1_triggered(self):
        """
        Handle the "Today Report" action.
        """
        print("Today Report triggered")
        text = generate_today_report()
        self.show_popup_window(text)
        analysis_report_writer(text)

    def on_action2_triggered(self):
        """
        Handle the "All Time Report" action.
        """
        print("All Time Report triggered")
        self.show_popup_window(generate_all_time_report())

    def on_action3_triggered(self):
        """
        Handle the "Trends Report" action.
        """
        print("Trends Report triggered")

    def show_popup_window(self, text):
        """
        Show a popup window with the given text.

        Args:
            text (str): The text to display in the popup window.
        """
        dialog = QDialog()
        dialog.setWindowFlags(dialog.windowFlags() | Qt.WindowStaysOnTopHint)

        label = QTextEdit()
        label.setReadOnly(True)
        label.setMarkdown(text)

        layout = QVBoxLayout()
        layout.addWidget(label)
        dialog.setLayout(layout)

        screen_geometry = QApplication.desktop().screenGeometry()
        dialog.setGeometry(
            (screen_geometry.width() - dialog.width()) // 2,
            (screen_geometry.height() - dialog.height()) // 2,
            dialog.width(),
            dialog.height()
        )

        dialog.exec_()

    def run(self):
        """
        Run the system tray application.
        """
        self.app.exec_()

    def quit_application(self):
        """
        Quit the system tray application.
        """
        self.app.quit()


if __name__ == "__main__":
    app = SystemTrayApp()
    app.run()