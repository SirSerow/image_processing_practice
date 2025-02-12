# Basics of Python Image Processing  
# Python画像処理の基礎

**Objective / 目的:**  
- **English:** Introduce the fundamentals of image processing using Python, focusing on practical applications with the Pillow and OpenCV libraries.  
- **日本語:** PythonとPillowおよびOpenCVライブラリを用いた画像処理の基本概念を、実践的な応用を通して学びます。

---

## Topics Covered / 講義内容

1. **Opening, Resizing, and Saving Images Using Pillow**  
   **Pillowを用いた画像の読み込み、リサイズ、保存**

2. **Reading and Saving Images with OpenCV and Picamera**  
   **OpenCVとPicameraを用いた画像の読み込みと保存**

3. **Practice Task: Resizing an Image and Saving It Using OpenCV**  
   **演習課題: OpenCVを使用した画像のリサイズと保存**


---

### Environment Setup / 環境設定

This excersise is using notebook, so before running the code you need to setup the environment and run the the notebook server / この演習はノートブックを使用しているため、コードを実行する前に環境を設定し、ノートブックサーバーを実行する必要があります。

1. **Start python virtual environment / Python仮想環境を起動する**  
   ```bash
   source myenv/bin/activate
   ```

2. **Start Jupyter Notebook Server / Jupyter Notebookサーバーを起動する**  
   ```bash
    jupyter notebook
    ```
3. **Open the notebook file in the browser / ブラウザでノートブックファイルを開く**
   Server address: [http://campi:8888/](http://campi:8888/)



---

## 1. Opening, Resizing, and Saving Images Using Pillow  
## 1. Pillowを用いた画像の読み込み、リサイズ、保存

**Pillow Overview / Pillowの概要:**  
- **English:** Pillow is a widely-used Python library for opening, manipulating, and saving image files. It supports various image formats (e.g., JPEG, PNG, BMP), making it a versatile tool for basic image processing tasks.  
- **日本語:** Pillowは、画像ファイルの読み込み、操作、保存を行うための広く利用されているPythonライブラリです。JPEG、PNG、BMPなど、さまざまな画像フォーマットに対応しており、基本的な画像処理タスクにおいて非常に有用です。

**Key Concepts / 主要な概念:**  
- **Opening Images / 画像の読み込み:** Loading image files into Python for processing.  
  画像ファイルをPythonに読み込み、処理する。  
- **Resizing Images / 画像のリサイズ:** Adjusting the dimensions (width and height) of images.  
  画像の幅や高さを調整する。  
- **Saving Images / 画像の保存:** Writing processed images back to disk in various formats.  
  処理後の画像をさまざまな形式でディスクに保存する。

**Practical Applications / 応用例:**  
- **English:** Preparing images for web usage by reducing file size; standardizing image dimensions for machine learning inputs; converting images between formats.  
- **日本語:** 画像のファイルサイズを縮小してウェブ用に最適化する、機械学習の入力用に画像サイズを統一する、画像フォーマットを変換するなど。

---

## 2. Reading and Saving Images with OpenCV and Picamera  
## 2. OpenCVとPicameraを用いた画像の読み込みと保存

**OpenCV Overview / OpenCVの概要:**  
- **English:** OpenCV is a powerful, open-source computer vision library that provides extensive functionalities for image and video processing.  
- **日本語:** OpenCVは、画像および動画処理のための強力なオープンソースのコンピュータビジョンライブラリです。

**Key Concepts / 主要な概念:**  
- **Reading Images / 画像の読み込み:** Loading images into Python using OpenCV functions.  
  OpenCVの関数を使用して画像を読み込む。  
- **Saving Images / 画像の保存:** Exporting processed images to various file formats.  
  処理した画像をさまざまなファイル形式で保存する。

**Picamera Integration / Picameraとの連携:**  
- **English:** The Picamera library enables direct interaction with the Raspberry Pi camera module, allowing captured images to be processed further with OpenCV.  
- **日本語:** Picameraライブラリを使用すると、Raspberry Piのカメラモジュールと直接連携でき、キャプチャした画像をOpenCVでさらに処理することが可能です。

**Practical Applications / 応用例:**  
- **English:** Capturing images from the Raspberry Pi camera for real-time processing; implementing computer vision applications such as object detection; developing custom image processing pipelines.  
- **日本語:** Raspberry Piカメラから画像をキャプチャしてリアルタイム処理を行う、物体検出などのコンピュータビジョンアプリケーションを実装する、特定のプロジェクト向けにカスタムの画像処理パイプラインを開発する。

---

## 3. Practice Task: Resizing an Image and Saving It Using OpenCV  
## 3. 演習課題: OpenCVを使用した画像のリサイズと保存

**Objective / 目的:**  
- **English:** Gain hands-on experience by resizing an image using OpenCV and saving the processed image to disk.  
- **日本語:** OpenCVを使用して画像をリサイズし、処理後の画像をディスクに保存することで、実践的なスキルを身につけます。

**Steps / 手順:**  
1. **Load an Image / 画像の読み込み:**  
   - **English:** Use OpenCV to read an image file into Python.  
   - **日本語:** OpenCVを用いて画像ファイルをPythonに読み込みます。

2. **Resize the Image / 画像のリサイズ:**  
   - **English:** Apply OpenCV functions to adjust the image dimensions to a specified size.  
   - **日本語:** OpenCVの機能を利用して、画像のサイズを指定の寸法に調整します。

3. **Save the Image / 画像の保存:**  
   - **English:** Write the resized image back to disk in the desired format.  
   - **日本語:** リサイズした画像を希望の形式でディスクに保存します。

**Considerations / 注意点:**  
- **Aspect Ratio / アスペクト比:**  
  - **English:** Maintain the aspect ratio to avoid distortion, unless intentional changes are desired.  
  - **日本語:** 意図的な変更がない限り、画像の歪みを防ぐためにアスペクト比を維持してください。  
- **Interpolation Methods / 補間方法:**  
  - **English:** Use appropriate interpolation methods provided by OpenCV to ensure high-quality resizing.  
  - **日本語:** 高品質なリサイズを実現するために、OpenCVが提供する適切な補間方法を使用してください。  
- **Verification / 確認:**  
  - **English:** Compare the original and resized images to verify that the output meets expectations.  
  - **日本語:** 元の画像とリサイズした画像を比較し、出力が期待通りであるか確認してください。

---

## Additional Resources / 追加リソース

- [Image Processing With the Python Pillow Library (English)](https://realpython.com/image-processing-with-the-python-pillow-library/)  
- [Getting Started with Python Image Processing Using OpenCV (English)](https://www.youngwonks.com/blog/Getting-started-with-Python-Image-Processing-using-OpenCV)  
- **日本語リソース:**  
  - 「Python 画像処理 Pillow OpenCV」で検索すると、Qiitaなどで多数の日本語チュートリアルや記事が見つかります。

---

**Note / 注意:**  
- **English:** The practical implementation of these tasks will be provided in a separate code file.  
- **日本語:** これらの課題の実際の実装は、別のコードファイルで提供されます。  
- **English:** Ensure that the Pillow and OpenCV libraries are installed in your Python environment before starting the exercises.  
- **日本語:** 演習を始める前に、Python環境にPillowとOpenCVライブラリがインストールされていることを確認してください.
