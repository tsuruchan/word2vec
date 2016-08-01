

# word2vecを使って、wikipediaのデータを学習し、入力したキーワードに対する結果（類似度）を計算する。
---
---


## MeCab 最新辞書 "mecab-ipadic-neologd"
### ■　mecab-ipdic-neologdとは

mecab-ipadic-neologdは、Web上のリソースから新しい言葉を登録したMecab用の辞書のことです。さらに、定期的に新しい言葉をアップデートするので、最新の言葉を正しく形態素解析をすることができます。

### Step.0　必要なライブラリをインストール

~~~
brew install mecab mecab-ipadic git curl xz
~~~

### Step.1 git clone する

~~~
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
~~~

### Step.2 インストールする

~~~
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd
~~~


#### インストール先の確認法
~~~
echo `mecab-config --dicdir`"/mecab-ipadic-neologd"
~~~



### 最新の辞書を使うと?

#####  以下のような単語を判別できるようになる。

なのは ― 「魔法少女リリカルなのは」というアニメの登場人物

はがない ― 「僕は友達が少ない」の略称

がをられ ― 「彼女がフラグをおられたら」の略称

はにはに ― 「月は東に日は西に」の略称

けよりな ― 「夜明け前より瑠璃色な」の略称

### MeCab コマンドライン引数
[http://www.mwsoft.jp/programming/munou/mecab_command.html](http://www.mwsoft.jp/programming/munou/mecab_command.html)

### pythonで使う

~~~
import MeCab
mt = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
mt.parse(__TEXT__)
~~~


## 日本語wikipediaのデータをダウンロード
2.2GBぐらいのサイズがあります。

~~~
curl https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2 -o jawiki-latest-pages-articles.xml.bz2
~~~

## wikipediaのデータをテキストに変換する

wikipediaのデータファイルはXMLで記述されてているので、それを普通のテキストファイルに変換しなければならない。


### rubyのインストール
~~~
brew rbenv ruby-build
~~~

次の２行を、.bash_prifileに記述

~~~
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
~~~

これらを反映させる。

~~~
source .bash_profile
~~~

rbenvを使って、ruby等をインストール

~~~
rbenv install --list 
rbenv install 2.3.1
rbenv local 2.3.1
rbenv global 2.3.1
rbenv exec gem install wp2txt bundler
rbenv rehash
~~~

rubyがインストールできたら、wikipediaのデータをテキストファイルに変換します。

~~~
rbenv exec wp2txt --input-file jawiki-latest-pages-articles.xml.bz2
~~~

1時間弱かかります。

これが終わると、２０個ほどのファイルが生成されるので、それらを一つのファイルにまとめます。

~~~
cat jawiki-latest-pages-articles.xml-* > jawiki_wakati.txt
~~~

 これで、トレーニング用のデータセットの完成です。

## word2vecのダウンロード
どうやらsubversionを使ってダウンロードすると、URL not foundになってしまい、リモートレポジトリが死んでいる様子。

同じものがgithubにあるのでそこから拾ってきます。


~~~
git clone https://github.com/svn2github/word2vec.git
cd word2vec
make
./demo-word.sh
~~~
Macにインストールする際には、以下のようなエラーが出ます。

~~~
$ cd word2vec
$ make
gcc word2vec.c -o word2vec -lm -pthread -O3 -march=native -Wall -funroll-loops -Wno-unused-result
gcc word2phrase.c -o word2phrase -lm -pthread -O3 -march=native -Wall -funroll-loops -Wno-unused-result
gcc distance.c -o distance -lm -pthread -O3 -march=native -Wall -funroll-loops -Wno-unused-result
distance.c:18:10: fatal error: 'malloc.h' file not found
#include <malloc.h>
         ^
1 error generated.
make: *** [distance] Error 1
~~~

malloc.hが無いよーというエラー。

macOSではmalloc.hではなくstdlib.hを使うので、以下のファイルのincludeを変更。

- compute-accuracy.c
- distance.c
- word-analogy.c

~~~
// #include <malloc.h>
#include <stdlib.h>
~~~

その後、再度ビルドすればインストールできます。

#### デモコード実行例

![](https://content-jp.drive.amazonaws.com/cdproxy/templink/UEGJYRHXiFqYAA7mcoD1X9GLd3bYH75L4uytxvd7abEE0Xnc3/alt/thumb?viewBox=1449)



