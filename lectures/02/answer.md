# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）：Qwen/Qwen3.5-0.8B
- 自分で学習を実行したか（`executed_training_myself`）：はい
- 学習前：`format_rate` =　0.09523809523809523 / `content_rate` =　0.0
- 学習後：`format_rate` =　1.0 / `content_rate` =　0.9047619047619048
- 退行した質問：なし
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：根拠なしの質問に断定した
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：学習前はformat_error4件であったが，学習後はasserted2件，needs_review2件となった．形式は正しく表示されるようになった．
- 学習で変わったこと・変わらなかったこと：形式の崩れが改善された一方で，回答の誤りは改善したり，退行したりしている

## 宿題

- 取り組んだレベル：基礎
- 変えた設定やデータ："lora_r"を16->4に変更
- 結果（比較表や数字）：
  - lora_r=16のとき
>  "before": {
>    "label": "before",
>    "n": 21,
>    "format_rate": 0.09523809523809523,
>    "content_rate": 0.0,
>    "both_rate": 0.0,
>    "seconds": 22.1
>  },>  "after": {
>    "label": "after",
>    "n": 21,
>    "format_rate": 1.0,
>    "content_rate": 0.9047619047619048,
>    "both_rate": 0.9047619047619048,
>    "seconds": 64.9
>  },
>  "regressed": [],
  - lora_r=4のとき
>  "before": {
>    "label": "before",
>    "n": 21,
>    "format_rate": 0.09523809523809523,
>    "content_rate": 0.0,
>    "both_rate": 0.0,
>    "seconds": 39.5
>  },
>  "after": {
>    "label": "after",
>    "n": 21,
>    "format_rate": 1.0,
>    "content_rate": 0.8571428571428571,
>    "both_rate": 0.8571428571428571,
>    "seconds": 50.6
>  },
- ファインチューニングが向く場面・向かない場面についての考察：
  - 向く場面
    - 回答のフォーマットを統一したいとき
  - 向かない場面
    - 知識の誤りを修正したいとき