import pathlib
from pathlib import Path
import docx
import PyPDF2

class ScanDocument:  # catch the error if a file does not exist

    def __init__(self, src_dir) -> None:
        self.src_dir =  src_dir

    def get_docs(self) -> None:
        while True:
            self.src_dir
            self.file_path = Path(self.src_dir)
            if self.file_path.is_dir() == True: # If provided path exists in the OS.
                break
            else:
                pass
        # Gets only the files in the root directory.
        self.present_files = [(self.file_path.name, self.file_path.suffix)for self.file_path in self.file_path.iterdir() if self.file_path.is_file()]
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
        self.pick_type = input("Which file type(s) do you want to scan? ")
        if self.pick_type == ".txt": # Read .txt files
            for values in list(self.ext.keys()):
                if values.endswith("e"):
                    print(values) 
        
    
    #def check_doc_type(self):
        #self.choose_file_type()
        


def main():
    scan_document = ScanDocument(src_dir= input("Directory: ").strip())
    scan_document.get_docs()
    scan_document.choose_file_type()

if __name__ == "__main__":
    main()