import os


BROWSERS_FILE = "config/browsers.txt"
UNPRODUCTIVE_FILE = "config/unproductive.txt"
PRODUCTIVE_FILE = "config/productive.txt"
LOG_FOLDER_BASE = os.path.expanduser("~/Personal-Productivity-Assistant")
OLLAMA_MODEL = "deepseek-r1:14b"
BROWSERS = [
    "Google Chrome", "Firefox", "Safari", "Microsoft Edge", "Opera", "Brave", "Vivaldi", "Tor Browser", "Maxthon",
    "UC Browser", "Puffin Browser", "Dolphin Browser", "Samsung Internet", "Yandex Browser", "Epic Privacy Browser",
    "Comodo Dragon", "Falkon", "Midori", "SeaMonkey", "Lynx", "Konqueror", "Qutebrowser", "Waterfox", "Slimjet",
    "SRWare Iron", "Torch Browser", "Beaker Browser", "Otter Browser", "Basilisk", "Dooble", "Avast Secure Browser",
    "Cent Browser", "Sleipnir", "Polarity Browser", "Colibri", "Blisk", "Coowon Browser", "Superbird", "Cốc Cốc",
    "SlimBrowser", "Netscape Navigator", "Internet Explorer", "Rockmelt", "Flock", "Camino", "Galeon", "K-Meleon",
    "NCSA Mosaic", "Amaya", "Arachne", "Arena", "Arora", "Baidu Browser", "BlackHawk", "Browzar", "CometBird",
    "Crazy Browser", "Cyberfox", "Deepnet Explorer", "Enigma Browser", "GreenBrowser", "IceCat", "IceDragon",
    "K-Ninja", "Lunascape", "Maelstrom", "NetSurf", "Orca Browser", "Pale Moon", "QtWeb", "Rekonq", "Sogou Explorer",
    "Sputnik Browser", "Surf", "TenFourFox", "Wyzo", "Xombrero", "ZAC Browser", "Zirco Browser", "Min", "Otter Browser",
    "Viper Browser", "Whale Browser", "LibreWolf", "Orion Browser", "Arc Browser", "Ghost Browser", "Sidekick Browser",
    "Wavebox", "Cliqz", "Avira Scout", "Dooble", "Fennec", "Hermes Browser", "Iridium Browser", "JioPages", "Kinza",
    "LibreWolf", "Naked Browser", "NetFront", "Nokia Xpress", "OmniWeb", "Orweb", "Sailfish Browser", "Sputnik Browser",
    "Sunrise Browser", "Tencent Traveler", "Tenta Browser", "UC Browser Mini", "xB Browser", "Yolo Browser",
    "Zetakey Browser", "Zvu"
]
PRODUCTIVE = [
    "slack", "finder", "terminal", "outlook", "word", "excel", "powerpoint", "pages", "numbers", "keynote",
    "evernote", "notion", "todoist", "trello", "asana", "microsoft teams", "zoom", "google meet", "forest",
    "activity monitor", "mail", "calendar", "sublimetext", "visual studio code", "atom", "xcode", "sublime merge",
    "github desktop", "sourcetree", "transmit", "parallels desktop", "vmware fusion", "virtualbox", "docker",
    "iterm2", "hyper", "zoc", "sequel", "tableplus", "dbeaver", "sequel ace", "mamp", "xampp", "docker desktop",
    "pycharm", "github", "chatgpt", "python"
]
UNPRODUCTIVE = [
    "facebook", "twitter", "instagram", "snapchat", "tiktok", "linkedin", "reddit", "pinterest", "whatsapp",
    "telegram", "discord", "skype", "facetime", "wechat", "viber", "line", "signal", "kik", "facebook messenger",
    "google hangouts", "snapchat", "tumblr", "periscope", "clubhouse", "houseparty", "mewe", "parler", "gab",
    "mastodon", "vero", "triller", "byte", "rumble", "minds", "steemit", "dlive", "bitchute", "dtube", "peertube"
]