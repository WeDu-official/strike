from SAPFL import func_mapping
import time
import os
# Define a custom function to parse and execute input cod
import subprocess
def run_code(code,filepath):
    start_time = time.time()
    x = int(time.strftime('%Y%d%d%H%M%S'))

    lines = code.strip().split("\n")
    for i in range(len(lines)):
        for short, full in func_mapping.items():
            lines[i] = lines[i].replace(short, full)
    code = "\n".join(lines)
    filepathNW = len(filepath)
    filepathNW2 = filepathNW-3
    filepathnew = filepath[0:filepathNW2]
    with open(f"{filepathnew}_IA.py", "x") as file:
        file.write(f'{code}')
    y = int(time.strftime('%Y%d%d%H%M%S'))
    end_time = time.time()
    time_diff = end_time - start_time
    print(f"Finished in {time_diff:.3f} seconds")

def run(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            code = f.read()
            run_code(code,file_path)
    else:
        print(f"The file '{file_path}' does not exist")