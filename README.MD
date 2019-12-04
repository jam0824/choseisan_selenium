# 使う前に
seleniumが必要です。

```
pip install selenium
```

chromedriverも必要なのでカレントディレクトリに入れておいてください。

https://chromedriver.chromium.org/downloads

# 使い方
```
python choseisan.py イベント名 取得日数 "時間"
```

(例)
```
python choseisan.py jasstふりかえり 30 "22:00～24:00"
```

翌日から30日分の日付で調整さんを用意します。

jasst kyushuというイベント用に作ったため土日は抜かす処理が入っています。

時間の部分はそこに入れた文字列を日付の後ろにつけるだけなので、なんでもいいです。