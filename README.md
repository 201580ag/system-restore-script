# system-restore-script
This repository contains a Python script for performing system restoration tasks on Windows systems. It checks for administrator privileges, and if not, it prompts the user to run it as an administrator. The script can repair Windows using the DISM and SFC tools for system health restoration.
## System Restore Tool

This Python script provides a simple way to perform a system restore on a Windows machine. Before running the script, make sure you have the following prerequisites:

### Prerequisites

1. **Python**: Ensure you have Python installed on your Windows system. You can download it from the official website: [Python Downloads](https://www.python.org/downloads/).

2. **Administrator Privileges**: This script requires administrator privileges to execute successfully. Make sure you run it as an administrator.

### Usage

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

    ```
    git clone https://github.com/201580ag/system-restore-tool.git
    ```

2. **Navigate to the Directory**: Change your current directory to the cloned repository's directory:

    ```
    cd system-restore-tool
    ```

3. **Run the Script**: Execute the script by running the following command:

    ```
    python system_restore.py
    ```

4. **Follow the Prompts**:
   
   - You will be prompted with the question: "Do you want to perform a system restore? (y/n)"
   - Type 'y' if you want to perform a system restore, and the script will proceed.
   - Type 'n' if you want to cancel the operation.

5. **Completion**: If you chose 'y', the script will attempt to restore your system. Upon completion, you will receive a message indicating whether the operation was successful.

6. **Exit**: The script will automatically exit after completion.

Please note that this script is intended for Windows systems and may require additional configuration or adjustments depending on your specific environment.
