import time
from picamera2 import Picamera2
import os
import cv2  # OpenCV library for image processing
import numpy as np


def initialize_camera():
    """
    Initialize the Picamera2 instance and configure streams.
    Picamera2 インスタンスを初期化し、ストリームを設定します。
    """
    picam2 = Picamera2()

    # Create a configuration with main, lores, and raw streams
    # main、lores、raw ストリームを含む設定を作成します
    config = picam2.create_still_configuration(
        main={"size": (1920, 1080)},  # Main stream at 1920x1080 resolution
        lores={"size": (640, 480), "format": "YUV420"},  # Low-resolution stream
        raw={"format": "SRGGB10"},  # Raw stream
    )

    picam2.configure(config)
    return picam2


def capture_images(picam2, directory):
    """
    Capture images from different streams and save them to the specified directory.
    異なるストリームから画像をキャプチャし、指定されたディレクトリに保存します。

    Parameters:
    picam2 (Picamera2): The initialized Picamera2 object. 初期化された Picamera2 オブジェクト。
    directory (str): The directory where the images will be saved. 画像を保存するディレクトリ。
    """
    if not os.path.exists(directory):
        os.makedirs(
            directory
        )  # Create the directory if it doesn't exist. ディレクトリが存在しない場合は作成します。

    picam2.start()
    time.sleep(
        2
    )  # Allow the camera to adjust to lighting conditions. カメラが照明条件に適応するために2秒待ちます。

    # Capture images from each stream
    # 各ストリームから画像をキャプチャします
    main_image_path = os.path.join(directory, "main_image.jpg")
    lores_image_path = os.path.join(directory, "lores_image.jpg")
    raw_image_path = os.path.join(directory, "raw_image.dng")

    # Capture the main image
    # main 画像をキャプチャします
    picam2.capture_file(main_image_path, name="main")

    # Capture the lores image and convert to RGB
    # lores 画像をキャプチャし、RGB に変換します
    lores_frame = picam2.capture_array("lores")
    lores_rgb = cv2.cvtColor(lores_frame, cv2.COLOR_YUV2RGB_I420)
    cv2.imwrite(lores_image_path, lores_rgb)

    # Capture the raw image
    # raw 画像をキャプチャします
    picam2.capture_file(raw_image_path, name="raw")

    print(f"Main image saved to {main_image_path}")
    print(f"Lores image saved to {lores_image_path}")
    print(f"Raw image saved to {raw_image_path}")

    picam2.stop()


def main():
    """
    Main function to initialize the camera and capture images from different streams.
    カメラを初期化し、異なるストリームから画像をキャプチャするメイン関数。
    """
    picam2 = initialize_camera()
    try:
        capture_images(picam2, "pictures")
    finally:
        picam2.close()  # Ensure the camera is properly closed. カメラが適切に閉じられるようにします。


if __name__ == "__main__":
    main()
