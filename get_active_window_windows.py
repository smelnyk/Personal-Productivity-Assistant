"""
This module provides functionality to get the currently active window's process name on Windows.

Functions:
    get_active_window: Get the name of the process owning the currently active window.
"""

import win32gui
import win32process
import psutil

def get_active_window():
    """
    Get the name of the process owning the currently active window.

    Returns:
        str: The name of the process owning the currently active window, or None if no active window is found.
    """
    # Get the handle of the foreground window
    hwnd = win32gui.GetForegroundWindow()

    if hwnd:
        # Get the process ID associated with the window handle
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        try:
            # Use psutil to get the process name based on PID
            process = psutil.Process(pid)
            return process.name()
        except psutil.NoSuchProcess:
            return None
    return None