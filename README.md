## 実行方法
コマンドライン引数
```
file：元の画像ファイル名。拡張子まで含む。
num_img：生成する画像の枚数
save_path：生成する画像の保存先となるディレクトリ名
mix：連続する画像を重ね合わせる
```
実行コマンド例
入力画像の色相を８通りに変化させる
結果はimagesに格納
```
python3 colorful.py test.jpg 8 images
```
入力画像の色相を8通りに変化させ、それぞれを重ね合わせた中間の画像も生成する
結果はmix_imagesに格納
```
python3 colorful.py test.jpg 8 mix_images --mix
```