from setuptools import setup
from version import __version__

setup(
    app=['Personal-Productivity-Assistant.py'],
    version=__version__,
    data_files=[
        ('.', ['.venv/lib/python3.12/site-packages/certifi/cacert.pem'])
    ],
    options={'py2app': {
        # 'argv_emulation': False,
        'packages': ['PyQt5'],
        'iconfile': 'app_icon.icns',  # Path to your app icon file
        'emulate_shell_environment': True,
    }},
    setup_requires=['py2app'],
)