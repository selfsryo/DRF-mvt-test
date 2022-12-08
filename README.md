# DRF-mvt-test

## 概要
- [Django公式のGeoDjangoチュートリアル](https://docs.djangoproject.com/ja/3.2/ref/contrib/gis/tutorial/)を実施<br>
- [djangorestframework-mvt](https://github.com/corteva/djangorestframework-mvt)を実装


## Docker version
```sh
docker version --format '{{.Server.Version}}'
20.10.11
```

## 環境構築
```sh
cp ./geodjango/.env.sample ./geodjango/.env
# 任意の情報を入力
vi ./geodjango/.env
cp ./postgres/.env.db.sample ./postgres/.env.db
# 任意の情報を入力
vi ./postgres/.env.db
docker compose up --build -d
```

## 管理者作成
```sh
docker container exec -it geodjango python3 manage.py createsuperuser
```

## データのインポート
```sh
docker container exec -it geodjango python3 manage.py shell -c "from world import load; load.run()"
```

## 使用データ
以下`./geodjango/world/data`に格納（クリックでダウンロードされます）<br>
https://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip


## Browsable API
コンテナを起動した状態で以下にアクセス<br>
http://localhost:8000/world/

## djangorestframework-mvt
データのインポート後、以下からベクトルタイルを配信
http://localhost:8000/api/mvt/?tile={z}/{x}/{y}
