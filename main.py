from pathlib import Path
from read_files import ReadContents

class ScanDocument:
    read_contents = ReadContents()
    src_dir = None # To avoid "AttributeError: type object 'ScanDocument' has no attribute 'src_dir"
    
    def __init__(self, src_dir) -> None:
        ScanDocument.src_dir = src_dir

    @classmethod
    def get_docs(cls):
        """Prompts user for source file path."""
        while True:
            cls.dir_path = Path(cls.src_dir) # type: ignore
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

    def choose_file_type(self):
        self.pick_type = input("Which file type(s) do you want to scan? ").strip().lower()
        if self.pick_type == ".txt": # Read .txt files
            self.txt_data = self.read_contents.read_txt()
            for found_files in self.txt_data: # To display file names
                print(list(found_files.keys()))
            return self.txt_data

        elif self.pick_type == ".docx":
            print(self.read_contents.read_docx())
        elif self.pick_type == ".pdf":
            for dt in self.read_contents.read_pdf(): # Get filenames
                print(f"{dt['filename']}, ", end="")
            self.read_contents.read_pdf()
        
    def search_characters(self, parser):
        self.parser = parser
        if self.pick_type == ".txt":
            pass # Solve this error TypeError: 'dict' object is not callable

        


def main():
    scan_document = ScanDocument(src_dir= input("Directory: ").strip())
    scan_document.get_docs()
    scan_document.read_contents.src_path = ScanDocument.get_docs() # type: ignore
    scan_document.get_files()
    scan_document.choose_file_type()
    #scan_document.search_characters(parser= input("Search for what: ").strip())

if __name__ == "__main__":
    main()