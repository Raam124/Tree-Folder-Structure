import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import json
import logging

class TreeFolderStructure:
    def __init__(self, root, data):
        self.root = root
        self.data = data
        self.selected_files = []

        self.tree = ttk.Treeview(root)
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.attach_button = tk.Button(root, text="Attach", command=self.attach_files)
        self.attach_button.pack(side=tk.BOTTOM)

        self.attached_files_label = tk.Label(root, text="Attached Files:")
        self.attached_files_label.pack(side=tk.BOTTOM)

        self.attached_files_textarea = tk.Text(root, height=4)
        self.attached_files_textarea.pack(side=tk.BOTTOM)

        self.detach_button = tk.Button(root, text="Detached", command=self.detach_files)
        self.detach_button.pack(side=tk.BOTTOM)

        self.populate_treeview(self.data)

    # populate the json tree structure to the interface using recursion at start
    def populate_treeview(self, data, parent=''):
        try:
            for item in data:
                """ open=True value indicating whether the item’s children should be displayed or hidden.
                To show the tree view initially, this was set to true, and in the UI, it can be collapsed. """
                item_id = self.tree.insert(parent, 'end', text=item['name'], open=True)
                if 'children' in item:
                    self.populate_treeview(item['children'], parent=item_id)
        except Exception as e:
            # Display an error message if there's an issue with populating the tree view
            logging.error(f'An error occurred while populating the tree view : {str(e)} ')
            tk.messagebox.showerror("Error", f"An error occurred while populating the tree view")

    def attach_files(self):
        """Attach files that are selected though the UI. multiple selecton is possible using the CTRL key"""
        selected_items = self.tree.selection()
        try:
            for item in selected_items:
                file_name = self.tree.item(item, "text")
                if file_name not in self.selected_files:
                    self.selected_files.append(file_name)
            self.update_attached_files_textarea()
        except Exception as e:
            logging.error(f'An error occurred while attaching files : {str(e)} ')
            tk.messagebox.showerror("Error", f"An error occurred while while attaching files")

    def detach_files(self):
        selected_text = self.attached_files_textarea.tag_ranges(tk.SEL)
        try:
            if selected_text:
                # Get selected text and split it into lines
                selected_text_lines = self.attached_files_textarea.get(*selected_text).strip().split('\n')
                # Remove selected files from the list of attached files
                self.selected_files = [file for file in self.selected_files if file not in selected_text_lines]
                # Update the attached files text area
                self.update_attached_files_textarea()
            else:
                tk.messagebox.showinfo("Information", "Please select files to detach.")
        except Exception as e:
            logging.error(f'An error occurred while detaching files : {str(e)} ')
            tk.messagebox.showerror("Error", f"An error occurred while while detaching files")

    def update_attached_files_textarea(self):
        self.attached_files_textarea.delete("1.0", tk.END)
        for file in self.selected_files:
            self.attached_files_textarea.insert(tk.END, file + "\n")

def main():
    # Read the jason file for data and load 
    with open("tree_folder_structure_data.json") as f:
        data = json.load(f)

    # Create Tkinter window
    root = tk.Tk()
    root.title("Tree Folder Structure")

    # Create TreeFolderStructure instance
    tree_Folder_structure = TreeFolderStructure(root, data)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
