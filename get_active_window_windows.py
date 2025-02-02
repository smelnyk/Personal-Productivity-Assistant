import win32gui
import win32process
import win32api
import win32con
import os

def get_active_window():
    """
    Get the name of the process owning the currently active window.

    Returns:
        str: The name of the process owning the currently active window, or None if no active window is found.
    """
    # Get the handle of the foreground window
    hwnd = win32gui.GetForegroundWindow()
    h_process = None

    if hwnd:
        # Get the process ID associated with the window handle
        pid = win32process.GetWindowThreadProcessId(hwnd)[1]

        try:
            # Open the process with required access rights
            h_process = win32api.OpenProcess(
                win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ,
                False,
                pid
            )

            # Get the list of modules in the process
            h_module = win32process.EnumProcessModules(h_process)[0]

            # Get the full path of the executable
            exe_path = win32process.GetModuleFileNameEx(h_process, h_module)

            # Extract the executable name from the path
            exe_name = os.path.splitext(os.path.basename(exe_path))[0]

            return exe_name
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            # Close the process handle
            if h_process:
                win32api.CloseHandle(h_process)
    return None