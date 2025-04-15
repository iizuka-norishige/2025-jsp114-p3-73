# 2025-jsp114-p3-73

<!-- # Short Description -->

第114回日本病理学会での発表に関するコードを公開しています。

- **perform-kadai.py** : 課題検討を実行するコード
- **mk-command.py** : `perform-kadai.py` を連続的に実行するためのコマンドリストを作成するコード
- **perform-stepbystep.sh** : `mk-command.py` で作成したコマンドリストを１行ずつ実行するコード
- **Modelfile** : OllamaにLLMモデルを設定する際に利用したMODELFILEのテンプレート


## 課題検討結果

PC(GPUなし)とMac(GPUあり)とに有意な差を感じなかったので、Mac(GPUあり)のものを掲載する。

- [Gemma3:1B](result-gemma3_1b-mac.html)
- [Gemma3:4B](result-gemma3_4b-mac.html)
- [Gemma3:12B](result-gemma3_12b-mac.html)
- [Llama3-ELYZA-JP-8B](result-llama3-elyza_8b-mac.html)
- [Phi-4:14B](result-phi4_14b-mac.html)



<!-- # Badges -->

[![Github issues](https://img.shields.io/github/issues/iizuka-norishige/2025-jsp114-p3-73)](https://github.com/iizuka-norishige/2025-jsp114-p3-73/issues)
[![Github forks](https://img.shields.io/github/forks/iizuka-norishige/2025-jsp114-p3-73)](https://github.com/iizuka-norishige/2025-jsp114-p3-73/network/members)
[![Github stars](https://img.shields.io/github/stars/iizuka-norishige/2025-jsp114-p3-73)](https://github.com/iizuka-norishige/2025-jsp114-p3-73/stargazers)
[![Github top language](https://img.shields.io/github/languages/top/iizuka-norishige/2025-jsp114-p3-73)](https://github.com/iizuka-norishige/2025-jsp114-p3-73/)
[![Github license](https://img.shields.io/github/license/iizuka-norishige/2025-jsp114-p3-73)](https://github.com/iizuka-norishige/2025-jsp114-p3-73/)

# Tags

`LLM` `python` `pathology`

# Installation

Python ライブラリの `ollama` が必要です。

# Minimal Example
```
python perform-kadai.py -m 'LLM_model' -s 'System_Prompt_File' 'User_Prompt_File'
```

# Contributors

- [iizuka-norishige](https://github.com/iizuka-norishige)

<!-- CREATED_BY_LEADYOU_README_GENERATOR -->

# License

Code is under the [MIT license](https://choosealicense.com/licenses/mit/)
