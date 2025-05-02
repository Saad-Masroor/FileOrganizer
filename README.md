# 📂 File Organizer CLI Tool

A **simple, efficient**, and **automated** CLI tool to **organize your files** into predefined categories such as **Images**, **Documents**, **Videos**, **Music**, and **Archives**.

## Features

- 📂 **Automatic Organization**: Automatically organizes your **Downloads folder** in real-time using the **Watchdog** library.
- 🛠️ **Manual Organization**: Easily organize any folder of your choice via the CLI.
- 🔄 **Real-time Monitoring**: The app monitors file activity and organizes new files as they are downloaded.
- ⚙️ **Customizable Configuration**: Configure which folder to watch and other settings.
- 🧹 **Clean and Modular Structure**: Easy to extend and maintain.

## Tech Stack

- 🐍 **Python 3.x**
- 🛠️ **Watchdog**: File system monitoring for real-time updates.
- 🗂️ **pathlib**, **shutil**, **os**: For handling file operations.

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Saad-Masroor/FileOrganizer.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd FileOrganizer
   ```
3. **Create a virtual environment (optional, but recommended)**:
   ```bash
   python -m venv venv
   ```
4. **Activate the virtual environment**:
   - On Windows
    ```bash
   .\venv\Scripts\activate
    ```
  - On Mac
    ```bash
    source venv/bin/activate
    ```
5. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
6. **Run The Tool**:
   ```bash
   python main_auto.py
   ```
  - Follow the prompts to set up your configuration, or reset it if needed.

  - The tool will start monitoring the folder for new files.

**Usage**
Auto-Organize: The app automatically organizes files in your specified folder (e.g., Downloads) into categories like Images, Documents, Videos, Music, and Archives.

Manual Organization: You can also organize a specific folder manually with:
  ```bash
  python manual_organizer.py
  ```

**Releases**
You can find the latest release of the **FileOrganizerApp** in the [Releases](https://github.com/Saad-Masroor/FileOrganizer/releases) section of this repository. The .exe version is available for Windows users.

**Author**
Saad Bin Masroor
[LinkedIn](https://www.linkedin.com/in/saad-masroor-481015227/)

