# コマンド作成コード

hardware = ["mac", "mouse"]
modelollama = ["phi4:latest", "phi4:mini", "llama3-elyza:8b", "gemma3:12b", "gemma3:4b", "gemma3:1b"]
modelfname = "phi4_latest" #filenameに挿入するため、:を_に置換した名前
nkadai = range(1,5) #kadaiの数
sp = range(1,2) #spの数 #system prompt
up = range(1,6) #kadai-1..3のup #user prompt
up2 = range(1,11) #kadai-4のup
dir = "./kadai-mac/" #kadaiを置いているディレクトリの指定

for hw in hardware:
    for model in modelollama:
        modelfname = model.replace(":", "_")
        for k in nkadai:
            if k < 4:
                for s in sp:
                    for u in up:
                        print(f"python3 perform-kadai.py -m {model} -s {dir}kadai-{k}-sp-{s}.md {dir}kadai-{k}-up-{u}.md")
                        print(f"python3 perform-kadai.py -m {model} -s {dir}kadai-{k}-sp-{s}.md {dir}kadai-{k}-up-{u}.md")

            # kadai-4の時だけ、upは10個あるため
            if k == 4:
                for s in sp:
                    for u in up2:
                        print(f"python3 perform-kadai.py -m {model} -s {dir}kadai-{k}-sp-{s}.md {dir}kadai-{k}-up-{u}.md")
                        print(f"python3 perform-kadai.py -m {model} -s {dir}kadai-{k}-sp-{s}.md {dir}kadai-{k}-up-{u}.md")
