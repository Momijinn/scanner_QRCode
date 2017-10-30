scanner_QRCode
====
QRコードをカメラで読み取り、解読するプログラム

## Description
RaspberryPiにおいてQRコードを読み取るためのサンプルプログラム.

USBカメラによる読み取りプログラム(scanner_QRCode_usbCamera.py)とRaspberry Pi CameraによるQRコードの読み取りプログラム(scanner_QRCode_picamera.py)がある

## Demo
[![MOVIE](http://img.youtube.com/vi/A6zZs9Yl2Bs/0.jpg)](https://www.youtube.com/watch?v=A6zZs9Yl2Bs)

## Requirement
* 動作確認環境
    * Linux Rasbian
    * Python 2.7.9

* モジュール
    ```bash
    $ sudo apt-get install python-opencv
    $ sudo apt-get install python-zbar
    $ sudo apt-get install python-pillow
    $ sudo apt-get install python-picamera
    $ sudo apt-get install python-numpy
    ```

## Usage
* USBカメラによる読み取りプログラム(scanner_QRCode_usbCamera.py)
    ```bash
    $ python scanner_QRCode_usbCamera.py
    ```

* Raspberry Pi CameraによるQRコードの読み取りプログラム(scanner_QRCode_picamera.py)
    ```bash
    $ python scanner_QRCode_picamera.py
    ```

## Install
pythonでプログラムを実行する

## Licence
This software is released under the MIT License, see LICENSE.

## Author
[Twitter](https://twitter.com/momijinn_aka)

[Blog](http://www.autumn-color.com/)