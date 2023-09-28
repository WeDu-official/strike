from SAPFL import func_mapping
import time
import os
# Define a custom function to parse and execute input cod
import subprocess
def run_code(code):
    start_time = time.time()
    x = int(time.strftime('%Y%d%d%H%M%S'))

    lines = code.strip().split("\n")
    for i in range(len(lines)):
        for short, full in func_mapping.items():
            lines[i] = lines[i].replace(short, full)
    code = "\n".join(lines)

    with open("runned_code.py", "w") as file:
        file.write(f'{code}')

    command = "runned_code.py"
    subprocess.Popen(command, shell=True).wait()

    y = int(time.strftime('%Y%d%d%H%M%S'))

    end_time = time.time()
    time_diff = end_time - start_time
    print(f"Finished in {time_diff:.3f} seconds")

def run(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            code = f.read()
            run_code(code)
    else:
        print(f"The file '{file_path}' does not exist")