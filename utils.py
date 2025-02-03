"""
This module provides utility functions for various tasks such as retrieving URLs from browsers,
extracting domains from URLs, converting time durations to human-readable formats, generating log file names,
loading CSV strings into dictionaries, and setting applications to start automatically on system login (macOS only).
"""

import subprocess
import platform
import datetime
from urllib.parse import urlparse

def get_chrome_url():
    """
    Get the current URL from the active tab in Google Chrome.

    Returns:
        str: The current URL or a message indicating no Chrome window is open.
    """
    if platform.system() == 'Darwin':
        script = """
        tell application "Google Chrome"
            if (count of windows) is not 0 then
                set currentTab to active tab of front window
                set currentURL to URL of currentTab
                return currentURL
            else
                return "No Chrome window open"
            end if
        end tell
        """
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return result.stdout.strip()

    if platform.system() == 'Windows':
        from pywinauto import Application

        # Connect to the Chrome application
        app = Application(backend='uia')
        app.connect(title_re=".*Chrome.*")

        # Access the top window of Chrome
        dlg = app.top_window()

        # Retrieve the value from the address bar
        return dlg.child_window(title="Address and search bar", control_type="Edit").get_value()


def get_safari_url():
    """
    Get the current URL from the active tab in Safari.

    Returns:
        str: The current URL or a message indicating no Safari window is open.
    """
    if platform.system() == 'Darwin':
        script = """
        tell application "Safari"
            if (count of windows) is not 0 then
                set currentTab to current tab of front window
                set currentURL to URL of currentTab
                return currentURL
            else
                return "No Safari window open"
            end if
        end tell
        """
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return result.stdout.strip()

def get_edge_url():
    """
    Get the current URL from the active tab in Microsoft Edge.

    Returns:
        str: The current URL or a message indicating no Edge window is open.
    """
    if platform.system() == 'Darwin':
        script = """
        tell application "Microsoft Edge"
            if (count of windows) is not 0 then
                set currentTab to active tab of front window
                set currentURL to URL of currentTab
                return currentURL
            else
                return "No Edge window open"
            end if
        end tell
        """
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return result.stdout.strip()

    if platform.system() == 'Windows':
        from pywinauto import Application

        # Connect to the Chrome application
        app = Application(backend='uia')
        app.connect(title_re=".*Edge.*")

        # Access the top window of Esge
        dlg = app.top_window()

        # Retrieve the value from the address bar
        return dlg.child_window(control_type="Edit", found_index=0).get_value()

def extract_domain(url):
    """
    Safely extract the domain from a given URL.

    Args:
        url (str): The URL to extract the domain from.

    Returns:
        str: The domain of the URL, or None if an error occurs.
    """
    if not url.startswith(("http://", "https://")):
        url = f"http://{url}"

    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        return domain
    except Exception as e:
        print(f"Error extracting domain: {e}")
        return None

def humanize_time(seconds):
    """
    Convert a time duration from seconds into a human-readable format.

    Args:
        seconds (int): The time duration in seconds.

    Returns:
        str: The time duration in a human-readable format (e.g., "1h 2m 3s").
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_str = ""
    if hours > 0:
        time_str += f"{hours}h "
    if minutes > 0:
        time_str += f"{minutes}m "
    if seconds > 0 or time_str == "":
        time_str += f"{seconds}s"
    return time_str.strip()

def get_log_file_name(extension=".csv"):
    """
    Generate a log file name based on the current date.

    Args:
        extension (str): The file extension for the log file.

    Returns:
        str: The generated log file name.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d") + extension

def load_csv_to_dict(csv_string):
    """
    Load a CSV string into a dictionary.

    Args:
        csv_string (str): The CSV string to load.

    Returns:
        dict: A dictionary with keys and values from the CSV string.
    """
    csv_dict = {}
    lines = csv_string.split('\n')
    for line in lines:
        try:
            id, key, value = line.split(',')
            csv_dict[key.strip()] = value.strip()
        except ValueError:
            continue
    return csv_dict

def set_app_autostart():
    """
    Set the application to start automatically on system login (macOS only).

    Returns:
        str: The result of the AppleScript execution.
    """
    if platform.system() == 'Darwin':
        script = """
        tell application "System Events"
            if not (exists login item "Personal-Productivity-Assistant") then
                make new login item at end with properties {path:"/Applications/Personal-Productivity-Assistant.app", hidden:false}
            end if
        end tell
        """
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return result.stdout.strip()