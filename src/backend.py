from pathlib import PurePath

import eel


def start_eel():
    script_dir = PurePath("src", "web")

    eel.init(script_dir)
    eel.start('index.html', mode="chrome-app")