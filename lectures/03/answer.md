# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
    - 第1回では一般的な回答であったが，今回は用語集を検索して回答しており，正しい結果が表示されている
- `--trace` で見えたツール呼び出し（ツール名と引数）：
    - search_glossary({'query': 'LoRA'})
- 1つの質問での LLM 呼び出し回数（`requests`）：
    - 2回
- 追加したツールと、docstring に書いた説明：
    - 追加したツール：
        - make_quiz 
    - docstringに書いた説明：
        - """指定した回の用語から1つを選び、確認問題と答えを返す。「第2回の確認問題を出して」のように、復習用の問題を求められたときに使う。"""

## 宿題

- 取り組んだレベル：
    - 基礎
- やったこと：
    - `search_glossary` の docstring の「query には調べたい用語を1つだけ入れる」を「まとめて入れる」に変えた
- 結果：
    - 複数の用語をスペースで結合した文字列が引数として与えられ，search_glossaryの呼び出し回数も2→1に減少した．
    - 修正後：
        > --- trace ---
        > [tool call]   search_glossary({'query': 'LoRA QLoRA'})
        > [tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
        > [usage] RunUsage(cost=Decimal('0.0007867'), details={'text_prompt_tokens': 1039}, input_text_tokens=1039, input_tokens=1039, output_tokens=190, requests=2, tool_calls=1)
    - 修正前：
        > --- trace ---
        > [tool call]   search_glossary({'query': 'LoRA'})
        > [tool call]   search_glossary({'query': 'QLoRA'})
        > [tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
        > [tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
        > [usage] RunUsage(cost=Decimal('0.0007738'), details={'text_prompt_tokens': 1196}, input_text_tokens=1196, input_tokens=1196, output_tokens=166, requests=2, tool_calls=2)
- 気づき・疑問：
    - 修正により，token数や回答への影響はないことが分かった．
    - このため，search_glossaryは用語を1つだけ入れるだけの仕様であったが，まとめて入れるように指示した方がよいと考えられる
