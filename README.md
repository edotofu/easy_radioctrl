ＬチカできたらFlaskでラジコン編（Ver.0.0.1）
========================

■.環境作成  
　pip3 install -U flask  
　pip3 install -U flask-cors  
　pip3 install -U requests  
  
■.ソース  
以下ソースをRaspberry Piにコピーして使用してください。
- [ブラウザアプリ](./templates/radioctrl.html) - ラジコン用UI
です。   
  radioctrl.html  
  ※IPアドレスおよびポート番号は環境に応じて変更してください。  
- [WEBAPI](./radioctrl_webapi.py) - Flask上でWebAPIとして動作します。  
  adioctrl_webapi.py  
  ※ポート番号は5000になっています。  
 
- [制御用アプリ](./radioctrl.py) - GPIOを制御します。    
  radioctl.py  
  ※ポート番号は環境に応じて変更してください。  
  
■.実行例  
　python3 radioctrl_webapi.py  
　python3 radioctrl.py

　  

