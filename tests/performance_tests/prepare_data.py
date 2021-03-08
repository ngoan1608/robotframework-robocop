from shutil import copytree
from pathlib import Path


for i in range(1, 1001):
    new_dir = Path(Path(__file__).parent, 'test_data', str(i)).absolute()
    copytree(r'C:\Users\barte\Desktop\robotframework-robocop\tests\atest\rules', new_dir)