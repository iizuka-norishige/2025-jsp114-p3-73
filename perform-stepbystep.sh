#!/bin/bash

# コマンドリストファイルが指定されているか確認
if [ -z "$1" ]; then
  echo "使用法: $0 コマンドリストファイル"
  exit 1
fi

# コマンドリストファイルを読み込む
command_file="$1"

# errors.txtが存在しない場合は作成
if [ ! -f errors.txt ]; then
  touch errors.txt
fi

# コマンドリストファイルを1行ずつ読み込み実行
while IFS= read -r command; do
  if ! $command; then
    echo "エラー: $command" >> errors.txt
  fi
done < "$command_file"
