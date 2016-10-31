# scanner_QRCode
QRコードをカメラで読み取り、解読するプログラム  

scanner_QRCode_usbCamera.py : USBカメラによるQRコードの読み取り
scanner_QRCode_picamera.py : Raspberry Pi CameraによるQRコードの読み取り  

##必要ライブラリ
openCV 2.4.9.1  
zbar  
Pillow
numpy

##ライブラリのインストール
sudo apt-get install python-openCV  
sudo apt-get install python-zbar  
sudo apt-get install python-pillow  
sudo pip install numpy  


##動作確認環境  
Linux Rasbian  
Python 2.7.9  