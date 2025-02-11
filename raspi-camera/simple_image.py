import time
from picamera2 import PiCamera
import os


def initialize_camera():
    """
    Initialize the PiCamera instance.
    PiCamera インスタンスを初期化します。
    """
    camera = PiCamera()
    return camera


def capture_image(camera, directory, filename):
    """
    Capture an image and save it to the specified directory with the given filename.
    画像を撮影し、指定されたディレクトリに指定されたファイル名で保存します。

    Parameters:
    camera (PiCamera): The initialized PiCamera object. 初期化された PiCamera オブジェクト。
    directory (str): The directory where the image will be saved. 画像を保存するディレクトリ。
    filename (str): The name of the file to save the image as. 画像を保存するファイル名。
    """
    if not os.path.exists(directory):
        os.makedirs(
            directory
        )  # Create the directory if it doesn't exist. ディレクトリが存在しない場合は作成します。

    filepath = os.path.join(directory, filename)
    camera.start_preview()
    time.sleep(
        2
    )  # Allow the camera to adjust to lighting conditions. カメラが照明条件に適応するために2秒待ちます。
    camera.capture(filepath)
    camera.stop_preview()
    print(f"Image saved to {filepath}")  # 画像が保存されたことを通知します。


def main():
    """
    Main function to initialize the camera and capture an image.
    カメラを初期化し、画像を撮影するメイン関数。
    """
    camera = initialize_camera()
    try:
        capture_image(camera, "pictures", "image.jpg")
    finally:
        camera.close()  # Ensure the camera is properly closed. カメラが適切に閉じられるようにします。


if __name__ == "__main__":
    main()
