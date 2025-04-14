# jsp-114用Modelfileのテンプレート

# 曖昧さが少なくなるようにパラメータを設定しています。
# Example for creating a model from Modelfile.
# $ ollama create choose-a-model-name -f ./Modelfile

# Llama-3-ELYZA-JP-8B
# Gemma-3:1B, Gemma-3:4B, Gemma-3:12B
# phi-4:mini, phi-4

FROM /path/to/the/llm/file.gguf
PARAMETER temperature 0.1
PARAMETER num_ctx 4096
PARAMETER top_p 0.3
PARAMETER top_k 30
PARAMETER repeat_penalty 1.1
SYSTEM """
あなたは、正確かつ丁寧なアシスタントです。以下の点に留意してください。
*   具体的な用語を使用し、曖昧さを避けてください。
*   書式を統一し、一貫性のある表現で日本語で回答してください。
"""
