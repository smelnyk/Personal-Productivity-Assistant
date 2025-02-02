"""
This module provides functionality to get the currently active window's owner name and title on macOS.

Classes:
    AppListener: A class to listen for active window changes and retrieve the active window's details.

Functions:
    get_active_window: Get the currently active window's owner name and title.
"""

import objc
from Foundation import NSObject, NSNotificationCenter
from Quartz import (
    CGWindowListCopyWindowInfo,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID
)


class AppListener(NSObject):
    def __init__(self):
        """
        Initialize the AppListener and set up notifications.
        """
        objc.super(AppListener, self).init()
        if self is None:
            return
        self.setup_notifications()

    def get_active_window(self):
        """
        Get the currently active window's owner name and title.

        Returns:
            tuple: A tuple containing the owner name and window title.
        """
        options = kCGWindowListOptionOnScreenOnly
        window_list = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
        for window in window_list:
            if window.get('kCGWindowLayer') == 0:  # Standard windows have layer 0
                owner_name = window.get('kCGWindowOwnerName', 'Unknown')
                window_title = window.get('kCGWindowName', 'Unknown')
                return owner_name, window_title
        return None, None
