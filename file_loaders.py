"""
This module provides functions to load lists of browsers, productive applications,
unproductive applications, and to aggregate time spent on each application from CSV log files.
"""

import os
import csv

from config import BROWSERS_FILE, LOG_FOLDER_BASE, PRODUCTIVE_FILE, UNPRODUCTIVE_FILE
from utils import get_log_file_name


def load_browsers_list():
    """
    Load the list of browser names from the file.

    Returns:
        list: A list of browser names.
    """
    try:
        with open(os.path.join(LOG_FOLDER_BASE, BROWSERS_FILE), 'r', encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: {BROWSERS_FILE} not found.")
        return []


def load_productive_list():
    """
    Load the list of productive applications from the file.

    Returns:
        list: A list of productive applications.
    """
    try:
        with open(os.path.join(LOG_FOLDER_BASE, PRODUCTIVE_FILE), 'r', encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: {PRODUCTIVE_FILE} not found.")
        return []


def load_unproductive_list():
    """
    Load the list of unproductive applications from the file.

    Returns:
        list: A list of unproductive applications.
    """
    try:
        with open(os.path.join(LOG_FOLDER_BASE, UNPRODUCTIVE_FILE), 'r', encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: {UNPRODUCTIVE_FILE} not found.")
        return []


def load_csv_log_files(current_day_only=False):
    """
    Load the CSV log files and aggregate the time spent on each application.

    Args:
        current_day_only (bool): If True, only load the current day's log file.

    Returns:
        dict: A dictionary with application domains as keys and total time spent as values.
    """
    app_time_dict = {}
    current_day_file = get_log_file_name()

    for filename in os.listdir(os.path.join(LOG_FOLDER_BASE, 'logs')):
        if filename.endswith('.csv'):
            if current_day_only and filename != current_day_file:
                continue
            file_path = os.path.join(LOG_FOLDER_BASE, 'logs', filename)
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    if len(row) == 2:
                        app_domain, time = row
                        app_domain = app_domain.strip().lower()
                        time = int(time.strip())
                        if app_domain in app_time_dict:
                            app_time_dict[app_domain] += time
                        else:
                            app_time_dict[app_domain] = time

    return app_time_dict