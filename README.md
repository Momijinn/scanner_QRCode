# scanner_QRCode
QRコードをカメラで読み取り、解読するプログラム  

scanner_QRCode_usbCamera.py : USBカメラによるQRコードの読み取り  
scanner_QRCode_picamera.py : Raspberry Pi CameraによるQRコードの読み取り  

##必要ライブラリ
openCV 2.4.9.1  
zbar  
Pillow  
numpy  
picamera  

##ライブラリのインストール
sudo apt-get install python-opencv  
sudo apt-get install python-zbar  
sudo apt-get install python-pillow  
sudo apt-get install python-picamera  
sudo apt-get install python-numpy  


##動作確認環境  
Linux Rasbian  
Python 2.7.9  