from pathlib import Path
import sys


def how_big_are_you(filename):
    file_path = Path(filename)
    if file_path.exists():
        size = file_path.stat().st_size
        return size
    
    else:
        print("file dose not exist")


def reverse_files(ini, output):
    file_size = how_big_are_you(ini)

    with open(ini, 'rb') as f1:
        with open(output, 'wb') as f2:
            for i in range(file_size - 1, -1, -1):
                f1.seek(i)
                data = f1.read(1)
                f2.write(data)


def In_N_Out():
    if len(sys.argv()) < 3:
        exit
    inn = sys.argv[1]
    out = sys.argv[2]
    reverse_files(inn, out)
    

if __name__ == "__main__":
    In_N_Out()
