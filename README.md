# PyReqGen

PyReqGen is a Python tool designed to simplify the process of managing project dependencies by automatically generating `requirements.txt` files. It scans your Python project directory, identifies all imported modules, and extracts their version information, helping you create accurate and up-to-date dependency lists.

## Features

- **Automatic Dependency Detection**: PyReqGen analyzes your Python project files to identify all imported modules, including both standard library modules and third-party packages.
- **Version Extraction**: It extracts version information for third-party packages using multiple methods, ensuring comprehensive dependency resolution.
- **Output Customization**: PyReqGen generates a `requirements.txt` file containing all detected dependencies, allowing for easy customization and sharing.
- **Ease of Use**: With a simple command-line interface, PyReqGen streamlines the process of managing project dependencies, saving you time and effort.

## Usage

1. Clone or download the PyReqGen repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Run the script by executing `python pyreqgen.py`.
4. Enter the path to your Python project directory when prompted.
5. PyReqGen will scan your project, extract dependencies, and generate a `requirements.txt` file.


