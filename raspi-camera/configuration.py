import time
from picamera2 import Picamera2, Preview
import os


def initialize_camera():
    """
    Initialize the Picamera2 instance and configure settings.
    Picamera2 インスタンスを初期化し、設定を構成します。
    """
    picam2 = Picamera2()

    # Create a custom configuration with specific resolution and format
    # 特定の解像度とフォーマットでカスタム設定を作成します
    config = picam2.create_still_configuration(
        main={"size": (1280, 720), "format": "RGB888"}
    )

    picam2.configure(config)

    # Adjust camera controls
    # カメラのコントロールを調整します
    picam2.set_controls(
        {
            "Brightness": 0.5,  # Range: -1.0 to 1.0, default is 0.0
            "Contrast": 1.0,  # Range: 0.0 to 2.0, default is 1.0
            "Saturation": 1.5,  # Range: 0.0 to 2.0, default is 1.0
            "Sharpness": 1.0,  # Range: 0.0 to 2.0, default is 1.0
            "ExposureTime": 20000,  # In microseconds
            "AwbMode": "Incandescent",  # Auto White Balance mode
        }
    )

    return picam2


def capture_image(camera, directory, filename):
    """
    Capture an image and save it to the specified directory with the given filename.
    画像を撮影し、指定されたディレクトリに指定されたファイル名で保存します。

    Parameters:
    camera (Picamera2): The initialized Picamera2 object. 初期化された Picamera2 オブジェクト。
    directory (str): The directory where the image will be saved. 画像を保存するディレクトリ。
    filename (str): The name of the file to save the image as. 画像を保存するファイル名。
    """
    if not os.path.exists(directory):
        os.makedirs(
            directory
        )  # Create the directory if it doesn't exist. ディレクトリが存在しない場合は作成します。

    filepath = os.path.join(directory, filename)
    camera.start_preview(
        Preview.NULL
    )  # Start the preview window. プレビューウィンドウを開始します。
    camera.start()  # Start the camera. カメラを起動します。
    time.sleep(
        2
    )  # Allow the camera to adjust to settings. カメラが設定に適応するために2秒待ちます。
    camera.capture_file(filepath)
    print(
        f"Image saved to {filepath}"
    )  # Notify that the image has been saved. 画像が保存されたことを通知します。
    camera.stop_preview()  # Stop the preview window. プレビューウィンドウを停止します。
    camera.stop()  # Stop the camera. カメラを停止します。


def main():
    """
    Main function to initialize the camera and capture an image with custom settings.
    カメラを初期化し、カスタム設定で画像を撮影するメイン関数。
    """
    camera = initialize_camera()
    try:
        capture_image(camera, "pictures", "custom_image.jpg")
    finally:
        camera.close()  # Ensure the camera is properly closed. カメラが適切に閉じられるようにします。


if __name__ == "__main__":
    main()
