from pathlib import Path

def how_big_are_you(filename):
    file_path = Path(filename)
    if file_path.exists:
        size = file_path.stat().st_size
        return size
    
    else:
        print("file dose not exist")