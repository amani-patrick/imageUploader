import os
import shutil
import time
import subprocess


class ImageUploader:
    def __init__(self, watch_folder, upload_folder, upload_url):
        self.watch_folder = watch_folder
        self.upload_folder = upload_folder
        self.upload_url = upload_url

        # Create the upload folder if it doesn't exist
        os.makedirs(self.upload_folder, exist_ok=True)

    def monitor_and_upload(self):
        """Monitors the folder and uploads new images."""
        print("Monitoring folder:", self.watch_folder)
        while True:
            images = self.get_images()
            for image in images:
                image_path = os.path.join(self.watch_folder, image)
                if self.upload_image(image_path):
                    self.move_image(image)
            time.sleep(30)  # Wait 30 seconds between uploads

    def get_images(self):
        """Gets a list of images in the watch folder."""
        return [f for f in os.listdir(self.watch_folder) if f.endswith((".jpg", ".jpeg", ".png"))]

    def upload_image(self, image_path):
        """Uploads an image using a curl command."""
        try:
            command = [
                "curl",
                "-X", "POST",
                "-F", f"imageFile=@{image_path}",
                self.upload_url
            ]
            result = subprocess.run(command, capture_output=True, text=True)

            if result.returncode == 0:
                print(f"Successfully uploaded: {image_path}")
                return True
            else:
                print(f"Failed to upload {image_path}. Error: {result.stderr}")
                return False
        except Exception as e:
            print(f"Error uploading {image_path}: {e}")
            return False

    def move_image(self, image):
        """Moves the uploaded image to the uploaded folder."""
        src = os.path.join(self.watch_folder, image)
        dst = os.path.join(self.upload_folder, image)
        shutil.move(src, dst)
        print(f"Moved {image} to {self.upload_folder}")


if __name__ == "__main__":
    # Configuration
    WATCH_FOLDER = "./camera_images"  # Folder where camera saves pictures
    UPLOAD_FOLDER = "./uploaded"      # Folder to move uploaded pictures
    UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"

    # Create and run the uploader
    uploader = ImageUploader(WATCH_FOLDER, UPLOAD_FOLDER, UPLOAD_URL)
    uploader.monitor_and_upload()
