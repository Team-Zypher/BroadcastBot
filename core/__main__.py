from .. import zbot
from .utils import load_plugins
import logging
import glob
from pathlib import Path

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)


path = "core/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_plugins(shortname.replace(".py", ""))
print("Successfully deployed your bot!! Visit @ZypherxBotz..")
if __name__ == "__main__":
    bot.run_until_disconnected()
