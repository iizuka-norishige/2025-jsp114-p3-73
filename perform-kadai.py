import ollama
import time
import argparse


# ArgumentParserオブジェクトを作成し、スクリプトの説明を追加
parser = argparse.ArgumentParser(description="指定されたファイルに記載されたプロンプトを読み込んで実行するスクリプト")

# コマנדライン引数としてファイルパスを受け取る設定。
parser.add_argument('file', type=open, help='ユーザプロンプトファイル')
parser.add_argument('-s', type=open, help='システムプロンプトファイル')
parser.add_argument('-m', type=str, help='モデル名')

# 引数を解析
args = parser.parse_args()


# システムプロンプトの設定
if args.s:
    sprompt = args.s.read()
else:
    sprompt = "あなたは親切なアシスタントです。日本語で回答します。"


# ファイル名の表示
#
print(f'# {args.file.name}')

# システムプロンプトの表示
# print(f"システムプロンプト：{sprompt}")
print("## システムプロンプト：")
print(sprompt)


# ファイル内容を変数に代入
prompt = args.file.read()

# print(f"ユーザプロンプト：¥n{prompt}")
print("")
print("## ユーザプロンプト：")
print(prompt)


# モデル名の指定
if args.m:
    model_name = args.m
else:
    model_name = 'gemma3:4b'

# モデル名を表示
# print(f'モデル名：{model_name}')


# メッセージの作成
messages = [
    {'role': 'system',
       'content': sprompt},
    {'role': 'user',
       'content': prompt}
]


print("")
print("## レスポンス：")

# 時間測定開始
start = time.perf_counter()

# チャットリクエストの送信
response = ollama.chat(model=model_name, messages=messages)

# レスポンスの表示
print(response['message']['content'])

# 時間測定終了
end = time.perf_counter()

# レスポンスのtoken数を取得
token_count = len(response['message']['content'].split())

# 1秒あたりのトークン数
tok_per_second = token_count / (end - start)

# 処理時間の表示
print("")
print("## まとめ")
print(f'- 課題ファイル名：{args.file.name}')
print(f'- モデル名：{model_name}')
print(f"- 処理時間: {end - start:.3f}秒")
print(f"- トークン数: {token_count} tokens")
print(f"- 1秒あたりのトークン数: {tok_per_second:.3f} tok/sec")
print("")
print("## コピペ用まとめ")
print(f'{args.file.name},{model_name},{end - start:.3f},{token_count},{tok_per_second:.3f}')
print("")
