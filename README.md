
# Tree Folder Structure UI

Python Tkinter Windows application that allows users to visualize a folder structure in a tree view format using JSON input. Additionally, users can select one or more files from the tree view and attach them to a text area at the bottom of the screen and detach using python Tkinter

## Installation (for Windows)

For other operation systems it will be same the executing command can be different refer the docs for that

Ensure you have Python installed on your Windows system. You can download and install Python from the official website: https://www.python.org/downloads/

make sure Tkinter is installed (This should be automatically installed)

Setup a virtual environment

```bash
  Clone the repo or download these files

  1.tree_folder_structure.py
  2.tree_folder_structure_data.json

```
Run the Python script by executing the following command:
```bash
    python tree_folder_structure.py
```
    
Explore the Folder Structure:

    1. Once you run the script, a Tkinter window will open displaying the   folder structure from the JSON file in a tree view format.
    2. You can expand/collapse folders by clicking on the arrow icons next to folder names.
    3. Select one or more files by clicking on them in the tree view.

Attach Selected Files:

    1.  Click the "Attach" button located at the bottom of the window to attach the selected files (Use CTRL for multiple files selection).
    2.  The names of the attached files will be listed in the text area below the tree view.

Detach Files:

    To remove attached files, select their names in the text area and click the "Detached" button

Customize:

    You can modify the tree_folder_structure_data.json file to represent your desired folder structure for testing different scenarios. The JSON file is preloaded feel free to update it without changing the key names

