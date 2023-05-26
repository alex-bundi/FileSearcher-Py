import tkinter as tk

def main():
    root = tk.Tk() # Main window and its dimensions
    root.title("Text Search")
    root.geometry("300x150")

    handle_input()
    root.mainloop()

def handle_input():
    label = tk.Label(text= "Search for what:")
    entry = tk.Entry()
    label.grid(row=0, column=0, padx=5,sticky="w") # Left align
    entry.grid(row=0, column=1)

if __name__ == "__main__":
    main()