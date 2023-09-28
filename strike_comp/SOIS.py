from SAPFL import func_mapping
def conv(filepath,filesrpname,folder_name):
   file1 = open(filepath,'r')
   file2 = open(f'{folder_name}\\{filesrpname}.py','x')
   code = file1.read()
   lines = code.strip().split("\n")
   for i in range(len(lines)):
       for short, full in func_mapping.items():
           lines[i] = lines[i].replace(short, full)
   pycode = "\n".join(lines)
   file2.write(pycode)
   file1.close()
   file2.close()