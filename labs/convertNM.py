import os

N_VALUE = "8"
M_VALUE = "10"

current_dir = os.getcwd()
for i in [i for i in os.listdir() if os.path.isdir(i) and "venv" not in i]:
    path = os.path.join(current_dir, i, "src")
    sources = [os.path.join(path,i) for i in os.listdir(path) if ".wrl" in i]
    for filepath in sources: 
        with open(filepath, "r") as f:
            all_lines = f.read()
        editted = all_lines.replace("<N>", N_VALUE).replace("<M>", M_VALUE)
        with open(filepath, "w") as f:
            f.write(editted)