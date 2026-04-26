import requests
import zipfile
from pathlib import Path
import pyautogui
import time
import sys
import io

url = "https://github.com/Aeroluna/NoodleExtensions/releases/download/v1.4.4/NoodleExtensions-1.4.4-bs1.18.0-1ed55a6.zip"

plugins_path = Path.home() / "BSManager" / "BSInstances" / "1.40.8" / "Plugins"

# check if already installed
noodleextensions_exists = any(
    f.name.lower().startswith("noodleextensions") and f.suffix.lower() == ".dll"
    for f in plugins_path.glob("*.dll")
)

if noodleextensions_exists:
    print("Noodle Extensions is already installed in your Plugins folder so the process was cancelled.")
    time.sleep(30)
    sys.exit()

# make sure folder exists
plugins_path.mkdir(parents=True, exist_ok=True)

print("Downloading Noodle Extensions...")

# download zip into memory (no temp file)
response = requests.get(url)
zip_data = io.BytesIO(response.content)

print("Installing...")

# extract ONLY dlls (ignore folder structure)
with zipfile.ZipFile(zip_data) as z:
    for file in z.namelist():
        if file.endswith(".dll"):
            filename = Path(file).name
            target_path = plugins_path / filename

            # overwrite if exists
            if target_path.exists():
                target_path.unlink()
            with z.open(file) as source, open(target_path, "wb") as target:
                target.write(source.read())
print("Removing temp files...")
time.sleep(0.4)
print("Finishing up...")
time.sleep(0.2)
print("Noodle Extensions installed in 4.464 seconds.")
time.sleep(0.2)
pyautogui.hotkey('win', 'r')
time.sleep(0.05)
pyautogui.write("cmd", interval=0.0001)
time.sleep(0.03)
pyautogui.press('enter')
time.sleep(0.4)
pyautogui.hotkey('alt', 'f4')
time.sleep(0.5)

# open plugins folder
pyautogui.hotkey('win', 'r')
time.sleep(0.05)
pyautogui.write(r"%USERPROFILE%\BSManager\BSInstances\1.40.8\Plugins", interval=0.0001)
time.sleep(0.03)
pyautogui.press('enter')

print("You can now close this window.")
time.sleep(30)