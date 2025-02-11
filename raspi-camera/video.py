import time
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
import os


def initialize_camera():
    """
    Initialize the Picamera2 instance and configure for video recording.
    Picamera2 インスタンスを初期化し、ビデオ録画用に設定します。
    """
    picam2 = Picamera2()

    # Create a video configuration with main and lores streams
    # main および lores ストリームを含むビデオ設定を作成します
    video_config = picam2.create_video_configuration(
        main={"size": (1920, 1080)},  # Main stream at 1920x1080 resolution
        lores={
            "size": (640, 480),
            "format": "YUV420",
        },  # Low-resolution stream for preview
        display="lores",  # Use lores stream for display
    )

    picam2.configure(video_config)
    return picam2


def record_video(picam2, directory, filename, duration):
    """
    Record a video and save it to the specified directory with the given filename.
    ビデオを録画し、指定されたディレクトリに指定されたファイル名で保存します。

    Parameters:
    picam2 (Picamera2): The initialized Picamera2 object. 初期化された Picamera2 オブジェクト。
    directory (str): The directory where the video will be saved. ビデオを保存するディレクトリ。
    filename (str): The name of the file to save the video as. ビデオを保存するファイル名。
    duration (int): The duration of the video recording in seconds. ビデオ録画の長さ（秒）。
    """
    if not os.path.exists(directory):
        os.makedirs(
            directory
        )  # Create the directory if it doesn't exist. ディレクトリが存在しない場合は作成します。

    filepath = os.path.join(directory, filename)
    encoder = H264Encoder(
        bitrate=10000000
    )  # Set encoder with specified bitrate. 指定されたビットレートでエンコーダーを設定します。

    picam2.start_preview(
        Preview.NULL
    )  # Start the preview window. プレビューウィンドウを開始します。
    picam2.start_recording(
        encoder, filepath
    )  # Start recording to the file. ファイルへの録画を開始します。

    time.sleep(
        duration
    )  # Record for the specified duration. 指定された長さの間録画します。

    picam2.stop_recording()  # Stop the recording. 録画を停止します。
    picam2.stop_preview()  # Stop the preview window. プレビューウィンドウを停止します。

    print(
        f"Video saved to {filepath}"
    )  # Notify that the video has been saved. ビデオが保存されたことを通知します。


def main():
    """
    Main function to initialize the camera and record a video.
    カメラを初期化し、ビデオを録画するメイン関数。
    """
    picam2 = initialize_camera()
    try:
        record_video(picam2, "videos", "recorded_video.h264", duration=10)
    finally:
        picam2.close()  # Ensure the camera is properly closed. カメラが適切に閉じられるようにします。


if __name__ == "__main__":
    main()
