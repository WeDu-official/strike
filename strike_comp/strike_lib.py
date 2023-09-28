from SAPFL import func_mapping
from strike_comp import SIR
class file():
    def runfile(filepath):
        SIR.run(filepath)
    def conv(code,mode,fscn):
        if mode == 'c':
            lines = code.strip().split("\n")
            for i in range(len(lines)):
                for short, full in func_mapping.items():
                    lines[i] = lines[i].replace(short, full)
            code = "\n".join(lines)
            print(code)
        if mode == 'cf':
            lines = code.strip().split("\n")
            for i in range(len(lines)):
                for short, full in func_mapping.items():
                    lines[i] = lines[i].replace(short, full)
            code = "\n".join(lines)
            w_fscn = open(fscn,'w')
            w_fscn.write(code)
        if mode == 'f':
            with open(fscn, 'r') as f:
                code = f.read()
            lines = code.strip().split("\n")
            for i in range(len(lines)):
                for short, full in func_mapping.items():
                    lines[i] = lines[i].replace(short, full)
            code = "\n".join(lines)
            print(code)
        if mode == 'ff':
            with open(fscn, 'r') as f:
                code = f.read()
            lines = code.strip().split("\n")
            for i in range(len(lines)):
                for short, full in func_mapping.items():
                    lines[i] = lines[i].replace(short, full)
            code = "\n".join(lines)
            w_fscn = open(fscn,'w')
            w_fscn.write(code)