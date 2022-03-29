from pathlib import Path, PurePath

import eel


def start_eel():
    script_dir = PurePath(Path(__file__).parent.resolve(), "web")

    eel.init(script_dir)
    eel.start('index.html', mode="chrome-app")


if __name__ == "__main__":
    start_eel()
