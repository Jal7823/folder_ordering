[![File organizer](https://github.com/Jal7823/folder_ordering/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/Jal7823/folder_ordering/actions/workflows/python-app.yml)
[![File organizer](https://github.com/Jal7823/folder_ordering/actions/workflows/python-app.yml/badge.svg?branch=develop)](https://github.com/Jal7823/folder_ordering/actions/workflows/python-app.yml)



# File Mover Script :rocket:
This Python script is designed to organize files in the user's "Downloads" directory by moving them to specific folders based on their file extensions.

## Usage :gear:
Ensure you have Python installed on your system.

Download the script file (file_mover.py).

Open a terminal or command prompt.

Navigate to the directory where the script is located.

Run the script using the command:

```bash
python file_organizer.py
```
## Description :paperclip:

The script performs the following tasks:

Retrieves the user's home directory.
Sets up paths for specific directories such as "Downloads," "Pictures," "Documents/docs," and "Documents/excel."
Changes the current working directory to the "Downloads" directory.
Lists all files in the "Downloads" directory.
Iterates through each file and moves it to the corresponding directory based on its file extension.
File Organization Rules
Images: Files with extensions .png, .jpg, .jpg_large, and .png_large are moved to the "Pictures" directory.
PDFs: Files with the .pdf extension are moved to the "Documents/docs" directory.
CSV and Excel: Files with extensions .csv and .xls are moved to the "Documents/excel" directory.
Author


License
This project is licensed under the MIT License.