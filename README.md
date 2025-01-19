# Image Uploader

This project is a Python script that monitors a folder for new images, uploads them to a specified URL using a `curl` command, and moves successfully uploaded files to another folder to avoid redundancy.
It will upload them to a server after certain amount of time and continue to keep track of newly uploaded images.

## Features
- Automatically monitors a folder for new images.
- Uploads images to a specified URL every 30 seconds.
- Moves successfully uploaded images to an `uploaded/` folder.

## Requirements
- Python 3.x
- `curl` command-line tool installed on your system.

## How to Use
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/amani-patrick/imageUploader.git
   cd imageUploader
2. **Run the script**:
```bash
python main.py 
 ```
3.**Every picture that will go in camera images it will be uploaded after 30seconds**:
```bash
Move you pictures there manually or configure your camera to save your pictures in camera_images
```