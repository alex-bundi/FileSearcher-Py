import pathlib
from pathlib import Path
import docx
import PyPDF2

class ScanDocument:  # catch the error if a file does not exist

    def __init__(self, src_dir) -> None:
        self.src_dir =  src_dir

    def get_docs(self) -> None:
        while True:
            self.file_path = Path(self.src_dir)
            if self.file_path.is_dir(): # If provided path exists in the OS.
                break
            else:
                self.src_dir = input("Invalid directory. Please enter a valid directory: ").strip()
                
        # Gets only the files in the root directory.
        self.present_files = [(self.file_path.name, self.file_path.suffix) for self.file_path in self.file_path.iterdir() if self.file_path.is_file()]
        print(self.file_path)

        print("Files in Root Directory:")
        
        self.ext = {}
        for file_name, file_extension in self.present_files:
            print(f"{file_name}, ", end= "") # File names
            if file_extension in self.ext: # File extensions
                self.ext[file_extension] += 1
            else:
                self.ext[file_extension] = 1
        print("\n")
        print(f"Extensions:\n{self.ext}")
    
    def choose_file_type(self) -> str:
        self.pick_type = input("Which file type(s) do you want to scan? ").strip().lower()
        print(self.file_path)
        """
        if self.pick_type == ".txt": # Read .txt files
            for file_name, file_ext in self.present_files:
                if file_ext == ".txt":
                    #self.full_path = pathlib.PurePath(self.file_path, file_name)
                    print(self.file_path)
                    #with open(self.full_path, "r") as scanned_file: 
                        #self.data = scanned_file.read()
                        #print(self.data)
        elif self.pick_type == ".docx":
            for file_name, file_ext in self.present_files:
                if file_ext == ".docx":
                    return file_name"""
                

def main():
    scan_document = ScanDocument(src_dir= input("Directory: ").strip())
    scan_document.get_docs()
    #scan_document.choose_file_type()

if __name__ == "__main__":
    main()