import pandas as pd
import subprocess
import os
from os import path

test = subprocess.Popen(["python", "-m", "unittest", "discover", "-s", "test", "-p", "UserMenu.py"], stdout= subprocess.PIPE)
output = test.communicate()[0].decode('utf-8')

if path.exists("TestCaseOutput.txt"):
    os.remove("TestCaseOutput.txt")

with open("TestCaseOutput.txt", 'w') as f:
    arrayTestCase = output.replace("b'", '').replace("'", "").replace("\n", ' ').split(' ')
    for row in arrayTestCase:
        f.write(row + "\n")

read_file = pd.read_csv(r'./TestCaseOutput.txt', header=None)
read_file.columns = ['Test_Case_Name', 'Status']
read_file.to_csv(r'./TestCaseOutput.csv', index=None)

