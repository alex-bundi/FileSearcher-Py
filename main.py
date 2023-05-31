from pathlib import Path
from read_files import ReadContents

class ScanDocument:
    read_contents = ReadContents()
    src_dir = None # To avoid "AttributeError: type object 'ScanDocument' has no attribute 'src_dir"
    

    def __init__(self, src_dir) -> None:
        ScanDocument.src_dir = src_dir

    @classmethod
    def get_docs(cls) -> None:
        """Prompts user for source file path."""
        while True:
            cls.dir_path = Path(cls.src_dir)
            if cls.dir_path.is_dir(): # If provided path exists in the OS.
                break
            else:
                cls.src_dir = input("Invalid directory. Please enter a valid directory: ").strip()
        
        return cls.dir_path
    
    def get_files(self):
        """Retrieves exclusively the files located in the main directory."""

        # Gets only the files in the root directory.
        self.read_contents.present_files = [(file_path.name, file_path.suffix) for file_path in self.dir_path.iterdir() if file_path.is_file()]
        
        print("Files in Root Directory:")
        
        self.ext = {}
        for file_name, file_extension in self.read_contents.present_files:
            print(f"{file_name}, ", end= "") # File names
            if file_extension in self.ext: # File extensions
                self.ext[file_extension] += 1
            else:
                self.ext[file_extension] = 1
        print("\n")
        print(f"Extensions:\n{self.ext}")


    def choose_file_type(self) -> str:
        self.pick_type = input("Which file type(s) do you want to scan? ").strip().lower()
        if self.pick_type == ".txt": # Read .txt files
            return self.read_contents.read_txt()
        elif self.pick_type == ".docx":
            return self.read_contents.read_docx()
        elif self.pick_type == ".pdf":
            print(self.read_contents.read_pdf())


def main():
    scan_document = ScanDocument(src_dir= input("Directory: ").strip())
    scan_document.get_docs()
    scan_document.read_contents.src_path = ScanDocument.get_docs()
    scan_document.get_files()
    scan_document.choose_file_type()



if __name__ == "__main__":
    main()