import xml.etree.ElementTree as ET
from pathlib import Path
import sys

target_file = sys.argv[1]
if not Path(target_file).exists():
    print(f"Error: {target_file} does not exist.")
    sys.exit(1)

target_file = Path(target_file).resolve()
print(f"Processing {target_file}...")

ET.register_namespace('android', 'http://schemas.android.com/apk/res/android')

tree = ET.parse(target_file)
root = tree.getroot()

android_ns = '{http://schemas.android.com/apk/res/android}'

attrs_to_remove = [
    f'{android_ns}isSplitRequired',
    f'{android_ns}requiredSplitTypes'
]

for attr in attrs_to_remove:
    if attr in root.attrib:
        print(f"Removing {attr}...")
        del root.attrib[attr]

application = root.find('application')
if application is not None:
    attr_lib = f'{android_ns}extractNativeLibs'
    if attr_lib in application.attrib:
        print(f"Removing {attr_lib}...")
        del application.attrib[attr_lib]

tree.write(target_file, encoding='utf-8', xml_declaration=True)