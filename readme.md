Djangoのお勉強用です。  

# はじめに

Python仮想環境に必要なパッケージをrequirements.txtにまとめています。以下のコマンドでインストールしてください。  

```shell
pip install -r requirements.txt
```

.で始まるディレクトリはgit管理対象外にしています。  
※ローカルではPython仮想環境のディレクトリを".venv"として作成していることの名残です。  

# 使い方

ローカルサーバを起動し、 http://127.0.0.1:8000/api/command/ にwebブラウザでアクセスします。  
テキストを1つ要素に持つデータがあり、登録すると一覧が表示される仕組みになっています。  
