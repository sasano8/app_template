---
theme: "black"
transition: "slide"
slideNumber: false
title: "サンプル"
---

# mkdocs初期化
``` Python
poetry run mkdocs new docs
```

# mkdocsプレビュー
``` Python
poetry run bash -c "cd docs && mkdocs serve"
```

# 開発環境構築（フロントエンドと文章執筆環境）
以下コマンドでフロントエンドと文章執筆環境用のnodejs環境を再現します。

``` shell
npm install
```


# 開発環境構築（バックエンド）

``` shell
poetry install
```

## PyCharmプラグイン導入
以下プラグインの導入と設定することで、自動でフォーマットが起動します。

- [black導入](https://black.readthedocs.io/en/stable/editor_integration.html)
- [isort導入](https://github.com/PyCQA/isort/wiki/isort-Plugins)

flake8
mypy

- filewatchプラグインを導入します
- filewatchプラグインでblackを起動スクリプトを追加します

## コーディング規約・ツール
pep8（black）スタイルに基づいてコーディングを行う。

- black: コードをpep8スタイルに自動で修正する
- flake8: pep8にしたがっているか、無効な変数が存在しているかなどチェックする
- mypy: 静的型チェックを行う
- isort: importの順序を修正する


### 設定

``` shell
flake8 --install-hook git  # コミット時にflake8を実行する
git config --bool flake8.strict true  # エラー時はコミット不可にする
```

```
https://blog.hirokiky.org/entry/2019/06/03/202745
```

flake8の拡張を好みに応じて追加してください。

```
#  flake8-blind-except
#  flake8-docstrings
#  flake8-import-order
```

# 開発環境構築（フロントエンド）
以下コマンドでフロントエンド用のnodejs環境を再現します。

``` shell
npm install
```

# 開発環境構築（文章執筆環境）
環境構築は、開発環境構築（バックエンド）と開発環境構築（フロントエンド）を参照ください。
利用する文章執筆ツールは次のとおりです。

- mkdocs（Python/静的サイトジェネレータ）
- textlint（NodeJS/文章校正）

加えて、必要に応じてエディタ用のプラグインを導入してください。

## VSCode

### プラグインの導入
VSCode用プラグインを導入する場合は、次のプラグインを導入してください。

- EditorConfig for VS Code
- vscode-textlint
- vscode-reveal（オプションです。プレゼン資料作成ツールです）

### 設定
- ユーザー設定 => 設定 => files.associations　で検索 => {"*.json", "jsonc"} を追加（jsonのコメントを許可する。これはtextlintの機能ではありません）

## PyCharm用プラグインの導入
- 未確認
- Languages & Framework -> Markdown -> enable PluntUML

## 動作確認（文書校正）
文章校正は、textlint（NodeJS）を使用します。

プラグイン導入後はエディタを再起動してください。
検証用テキストファイルで、文章校正が動作するか確認してください。

``` shell
echo "こんにちわ(笑)" > sample.md
```

上記で作成したファイルを開くと、文章校正が行われ、次のようなエラーが出力されます。

```
こんにちわ => こんにちは
http://japanknowledge.com/articles/blognihongo/entry.html?entryid=113 (ja-technical-writing/ja-no-abusage)

(笑) => （笑）
半角カッコの代わりに全角カッコを使うこと。文字のバランスが崩れるためです。
```

指摘された文章は修正する必要があります。
単純なケースであれば、コンソール上で右クリックし、自動修正もできます。

こんにちは（笑）

## カスタマイズ
- 文章校正対象ファイル拡張子は、.textlintrcでカスタマイズできます。
- prh.ymlを編集してください。


# TODO: reviewdogを導入してみたい


# textlint導入メモ
``` shell
git submodule add https://github.com/prh/rules.git prh-rules
```

clone時に再帰的にsubmoduleもcloneする。
```
git clone --recursive git+https://xxxx
```

clone時に--recursiveを忘れた場合は次のとおり。
```
git submodule update --init --recursive
```
