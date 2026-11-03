# Sentiment — VRT as of 2026-11-04

> 資料說明：`yf.py` 無 `ratings`、`holders` 子命令，改用 `rec_summary`、`recommendations`、`major_holders`、`inst_holders`。Reddit 直接抓取受阻，retail 資料以 WebSearch 摘要為主，多數來源日期停在 2026-10 以前，時效性有限。

## Analyst consensus

| 評級 | 家數 | 占比 |
|---|---|---|
| Strong Buy | 3 | 10.0% |
| Buy | 23 | 76.7% |
| Hold | 4 | 13.3% |
| Sell / Strong Sell | 0 | 0.0% |
| 合計 | 30 | 買進系 86.7% / 持有 13.3% / 賣出 0% |

- 趨勢：Buy 家數由 3 個月前 21 家增至 22 → 23 家，Hold 維持 4 家，無 Sell。評級面持續偏多且略升。
- 近期目標價調整（2026-10，WebSearch 來源）：
  - Roth Capital 目標價 355 → 335 USD，維持 Buy。
  - Morgan Stanley 目標價 350 → 330 USD，維持 Overweight（10/16）。
  - Mizuho 目標價 300 → 280 USD，維持 Outperform。
  - BMO 首次覆蓋，Outperform，目標價 329 USD（10/4）。
  - GLJ Research 首次覆蓋，Sell，目標價 188 USD，為唯一明確偏空的券商。
  - RBC 於 2026-05 將目標價由 356 上調至 435 USD（Outperform）。
- 共識目標價：MarketBeat 約 335.67 USD；Investing.com 過去三個月平均約 338.15 USD。
- 注意：Investing.com 計數為 24 Buy / 4 Hold / 0 Sell，與本工具的 26 買進系不同，原因可能是 Strong Buy 歸類差異。以本工具為準。
- 工具未提供逐家券商升降評等明細，升降級事件僅能由上述新聞推得，可能不完整。

## Retail social

- Reddit：WebSearch 未找到 r/wallstreetbets 或 r/stocks 上近期 VRT 討論串，覆蓋度極低。AltIndex 統計 Reddit 提及約 6 次，遠低於 Stocktwits 的 98 次。語氣無法判定，聲量屬低。
- StockTwits / X：
  - 可得的最新 StockTwits 情緒讀數來自 2026-03，已過時，不可作為 10 月或 11 月的依據。
  - AltIndex 綜合情緒分數 74/100（偏多），日期不明。
  - Stocktwits 過往文章顯示散戶在「偏多」與「極度看多」之間擺盪；其中一則標題為「Retail's Divided」，描述財報後前景展望令散戶意見分歧。
  - Quiver Quant 有 AI 彙整的討論摘要，但其底層貼文無法檢視，僅供參考。
- 聲量：整體屬中等偏低。以提及次數看，Stocktwits 98 次相對 Reddit 6 次為主要來源，但缺乏同期基準值，無法判定相對常態的倍數。
- 語氣：整體偏多，主軸是 AI 資料中心與液冷需求，但對估值（TIKR 引用的 2026 FCF 倍數約 43.5x）仍有保留。
- 主要題材：
  - AI 資料中心與 GPU 散熱機會（引用 Morgan Stanley 關於 NVIDIA GPU 散熱約 4.8 B USD 機會的看法）。
  - 產能擴張與 backlog。
  - 估值偏高，股價波動大。
  - 2026-10 目標價下修，散戶對此解讀分歧。

## Insider activity

以 2026-05-04 至 2026-11-04 為 6 個月窗口，全部 117 筆紀錄中窗口內共 14 筆（賣出 1、行使 1、贈與 1、獎勵 11）。

| 類別 | 筆數 | 金額（USD M） |
|---|---|---|
| 公開市場買進 | 0 | 0.00 |
| 公開市場賣出 | 1 | -3.88 |
| 選擇權行使（配對上述賣出） | 1 | +0.18 |
| 股票獎勵（Award / Grant） | 11 | 0.81 |
| 贈與（Gift，無對價） | 1 | 0.00 |

- 淨 6 個月：公開市場買進 0 USD M，賣出 3.88 USD M，淨額約 -3.88 USD M。
- 主要事件：
  - Director MONSER EDWARD L，2026-09-01，以 249.43 至 256.36 USD 賣出 15,287 股，約 3.88 USD M，並同日以 11.50 USD 行使選擇權。行使與賣出量相同，為典型的行使後變現。
  - CEO ALBERTAZZI GIORDANO，2026-09-08，贈與 118,523 股，無對價，不計入買賣。
  - CFO CHAMBERLIN CRAIG 與其他高階主管於 2026-06-25 有獎勵股授予，屬薪酬性質，不計入情緒判讀。
- 解讀：窗口內無高階主管公開市場買進，唯一的現金交易為董事之行使後賣出，金額相對 VRT 市值屬小。內部人情緒為中性偏弱，不構成強烈偏空訊號。
- 內部人持股比例約 0.24%。

## Ownership shifts

- 機構持股約 84.6%，機構數 2,696 家。
- 前十大機構（資料截至 2026-06-30，為 Q2 13F，非最新季）方向大致各半：
  - 增持：JPMorgan +65.9%、T. Rowe Price +15.9%、State Street +4.4%、Morgan Stanley +3.6%、Vanguard Capital Management +0.9%。
  - 減持：Invesco -15.4%、Geode -17.0%、Bank of America -1.6%、BlackRock -3.5%、Vanguard Portfolio Management -0.1%。
- 結論：機構持股集中度高，但前十大的增減呈現多空混雜，無明顯單向資金流。Q3 13F 資料未取得，此判斷需以後續資料驗證。

## Net sentiment score

- **Composite：偏多（信心：中低）**
  - 分析師面（權重高）：偏多，買進系 86.7%，無賣出，目標價多數仍高於近期股價區間。
  - 內部人面：偏弱，窗口內僅一筆董事賣出，無公開市場買進。
  - 散戶面：偏多但資料陳舊，Reddit 幾乎無訊號，StockTwits 最新讀數為 2026-03，可信度低。
  - 機構面：持股高度集中，前十大增減互見，中性。
- 信心偏低的主因：散戶與股價資料時效性不足（部分來源停在 2026-03 至 2026-10），且 WebSearch 結果內股價數字彼此不一致（例如 262.61 與 291.67 USD），無法確認 11/04 收盤價，因此無法對目標價空間做精確換算。
- **Divergence flag：否（信心低）**
  - 分析師與散戶語氣皆偏多，未見明顯反向。
  - 但內部人（董事賣出）與估值擔憂，與分析師偏多形成小幅張力，值得後續追蹤。
  - 若後續取得 11 月實際 StockTwits 或 Reddit 讀數，需重新檢核此判斷。

SENTIMENT REPORT COMPLETE
