"""
This module provides functions to write analysis reports, default configurations, and log active window data.
"""

import csv
import time
import os

from config import LOG_FOLDER_BASE
from file_loaders import load_browsers_list
from utils import get_chrome_url, get_safari_url, get_edge_url, extract_domain, get_log_file_name


def analysis_report_writer(text):
    """
    Write the analysis report to a text file.

    Args:
        text (str): The analysis report text to write.
    """
    log_file_path = os.path.join(LOG_FOLDER_BASE, 'analysis', get_log_file_name(".txt"))
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    with open(log_file_path, "w", encoding="utf-8") as file:
        file.write(text)


def defaults_config_writer(items, current_type):
    """
    Write default configuration items to a text file.

    Args:
        items (list): A list of configuration items to write.
        current_type (str): The type of configuration (e.g., 'productive', 'unproductive').
    """
    config_folder_path = os.path.join(LOG_FOLDER_BASE, 'config')
    config_file_path = os.path.join(config_folder_path, f"{current_type}.txt")

    os.makedirs(config_folder_path, exist_ok=True)

    if not os.path.exists(config_file_path):
        with open(config_file_path, "w", encoding="utf-8") as file:
            for item in items:
                file.write(item + "\n")


def file_writer(get_active_window_func):
    """
    Log the active window data, including browser URLs, to a CSV file.

    Args:
        get_active_window_func (function): A function that returns the current active window's application name and title.
    """
    browsers_names = load_browsers_list()
    previous_active_app = None
    elapsed_time = 0

    while True:
        try:
            current_active_app = get_active_window_func()
            if not current_active_app:
                current_active_app = "No active app"

            if current_active_app in browsers_names:
                current_browser_url = {
                    "Google Chrome": get_chrome_url,
                    "chrome": get_chrome_url,
                    "Safari": get_safari_url,
                    "Microsoft Edge": get_edge_url,
                    "msedge": get_edge_url
                }.get(current_active_app, lambda: None)()

                if current_browser_url:
                    current_browser_domain = extract_domain(current_browser_url)
                    if current_browser_domain:
                        current_active_app += f" | {current_browser_domain}"

            if previous_active_app and previous_active_app != current_active_app:
                log_file_path = os.path.join(LOG_FOLDER_BASE, 'logs', get_log_file_name())
                os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
                log_entry = [previous_active_app, elapsed_time]

                print(log_entry[0], log_entry[1])

                with open(log_file_path, "a", newline='', encoding="utf-8") as log_file:
                    writer = csv.writer(log_file, quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(log_entry)
                elapsed_time = 0
            else:
                elapsed_time += 1

            previous_active_app = current_active_app
            time.sleep(1)  # Log every second
        except KeyboardInterrupt:
            print("Logging stopped.")
            break
        except Exception as e:
            print(f"Error: {e}")