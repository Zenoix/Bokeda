from pathlib import Path, PurePath

import eel


script_dir = PurePath(Path(__file__).parent.resolve(), "web")

eel.init(script_dir)
eel.start('main.html', mode="chrome-app")
