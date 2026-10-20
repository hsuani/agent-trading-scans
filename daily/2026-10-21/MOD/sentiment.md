# Sentiment — MOD as of 2026-10-21

## 資料來源與限制

- `pipeline/tools/yf.py` 沒有 `ratings` 與 `holders` 子命令，改用 `rec_summary`、`recommendations`、`insider`、`major_holders`、`inst_holders`。
- Yahoo cookie/crumb 取得失敗，但回傳資料可用（依指示視為 cache 正常）。
- Reddit 與 StockTwits 依指示未直接抓取，標示為 DATA_UNAVAILABLE。
- X 與新聞聊天以 WebSearch 取得，結果多為聚合網站與低品質轉載，無可直接引用的散戶貼文。
- 股價來源彼此不一致（見下方），本報告未能確認 2026-10-21 收盤價。

## Analyst consensus

Yahoo `rec_summary`（當期）：1 strong buy / 8 buy / 0 hold / 0 sell / 0 strong sell，合計 9 家。
近 4 個月：-3m 為 8 家（1 SB + 7 B），目前 9 家，多出 1 家 Buy；未見降評紀錄。

近期評等動向（來自 WebSearch，未與原始研究報告核對）：

| 日期 | 機構 | 動作 | 目標價 |
|---|---|---|---|
| 2026-05-26 | B. Riley | 上調 | $250 → $264 |
| 2026-05-28 | Oppenheimer | 上調，Outperform | $271 → $325 |
| 2026-06-22 | DA Davidson | 重申 Buy | $330 |
| 2026-07-30 | KeyCorp | 下調，維持 Overweight | $370 → $280 |
| 2026-09-02 | KeyBanc | 重申 Overweight | 未取得 |
| 2026-04-13 | Zacks Research | 由 strong-buy 降至 hold（量化評等，非 sell-side） | — |

目標價共識來源不一致，需留意：
- Barchart：$341.44
- Fintel（2026-08-28）：平均 $334.96，區間 $282.80–$449.40
- Benzinga：平均 $265，最高 $355

評等計數來源亦不一致：MarketBeat 相關報導提及 7 Buy + 2 Hold，與 Yahoo 的 0 Hold 不符。本報告以 Yahoo 為主表。

股價參考（彼此衝突，僅供參考）：Benzinga 9/4 收盤 $194.66；Barchart 未註明日期 $208.06；搜尋摘要提及 10/2 收盤 $178.20。52 週區間 $111.18–$323.25（Investing.com）。

## Retail social

- **Reddit**：DATA_UNAVAILABLE。依指示未直接抓取 r/wallstreetbets 與 r/stocks，WebSearch 也未回傳 MOD 相關討論串。
- **StockTwits**：DATA_UNAVAILABLE。依指示未抓取。
- **X / 新聞聊天**：搜尋結果以聚合網站為主。一篇 2026-05 文章稱 MOD 出現在「熱門」清單、社群討論度上升，但未指出具體催化劑。
- **聲量**：無可靠量化樣本，無法與平時比較。搜尋結果中沒有高聲量的證據，但樣本太少，不能據此判定為低聲量。
- **語氣**：樣本不足，不做 bullish / bearish 判定。可得的市場面訊號如下：
  - Barchart 指股價自近期高點回落逾 20%，技術面由 64% Buy 訊號轉為 8% Sell，且未見分析師降評。
  - Benzinga 指 put/call ratio 0.23，解讀為偏多；空單佔流通股 6.0%，且呈下降趨勢。
- **主題**（來自新聞標題，非散戶貼文）：data center 題材是否被高估；氣候解決方案（Climate Solutions）部門受關注程度；盈利成長故事是否仍成立。

## Insider activity

觀察窗口：2026-04-21 至 2026-10-21。

Net 6mo：**$0 買入，約 $27.83M 賣出**（公開市場 Sale，共 6 筆）。

| 日期 | 內部人 | 職位 | 類型 | 股數 | 金額（USD） |
|---|---|---|---|---|---|
| 2026-06-01 | McGinnis Eric S | Officer | Sale | 38,082 | 10.86M |
| 2026-06-01 | Laszlo Arthur Jr | Officer | Sale | 900 | 0.27M |
| 2026-06-16 | Ashleman Eric D | Director | Sale | 15,000 | 4.33M |
| 2026-06-18 | Agen Brian Jon | Officer | Sale | 38,282 | 11.30M |
| 2026-06-18 | McGinnis Eric S | Officer | Sale | 1,020 | 0.30M |
| 2026-09-10 | Agen Brian Jon | Officer | Sale | 4,306 | 0.78M |

非現金或非買賣性質，未計入淨額：
- 2026-09-10 Agen 衍生性證券行使 5,269 股。
- 2026-08-20 董事股票獎勵，8 位董事各 812–1,389 股。
- 2026-05-20 與 2026-05-26 股票獎勵，包括 CEO Brinker 於 5/26 獲授 215,464 股、CFO Lucareli 於 5/26 獲授 73,873 股。

重點觀察：
- **CEO（Brinker）**：窗口內無公開市場賣出；最近一筆賣出為 2025-12-02，約 $5.12M。
- **CFO（Lucareli）**：窗口內無公開市場賣出；最近一筆賣出為 2026-02-17，約 $4.29M。
- **賣出主力**：Officer Agen（合計約 $12.1M）、Officer McGinnis（合計約 $11.2M）、Director Ashleman（約 $4.3M）。
- **歷史買入**：過去約 19 個月僅見一筆公開市場買入，為 2025-03-03 董事 Wulfsohn 買入 2,530 股，每股 $79.43。
- **是否為 10b5-1 預先排程**：工具輸出未提供，DATA_UNAVAILABLE。

## Ownership

- 內部人持股：1.94%（`insidersPercentHeld`）。
- 機構持股比率：`institutionsPercentHeld` 為 101.19%，超過 100%，屬資料異常（可能是流通股或股本基準不一致，或重複計算）。本報告不採用此數字。
- 機構家數：811（`institutionsCount`）。

前十大機構（13F，截至 2026-06-30）：

| 機構 | 持股比率 | 季度股數變化 |
|---|---|---|
| BlackRock | 5.40% | -29.8% |
| Vanguard Capital Management | 4.48% | +0.7% |
| Vanguard Portfolio Management | 4.15% | -6.7% |
| Capital Research Global Investors | 2.79% | -13.2% |
| Paradigm Capital Management | 2.74% | -0.1% |
| Invesco | 2.38% | +3.3% |
| Artisan Partners | 2.24% | +20.7% |
| State Street | 2.20% | -21.3% |
| Geode Capital Management | 2.17% | -8.3% |
| Fuller & Thaler | 2.10% | +3.2% |

- 前十大合計持股約 30.7%，約 1,629 萬股。
- 10 家中 6 家減持、4 家增持，合計持股呈淨減少。
- 最大減持為 BlackRock（-29.8%），最大增持為 Artisan Partners（+20.7%）。
- 目前僅有 6 月底的 13F 資料。Q3 13F 最晚約 11 月中旬才會公布，因此無法判斷最新季度趨勢。

## Net sentiment score

| 面向 | 判定 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 偏多 | 中 | 9 Buy / 0 Hold / 0 Sell，目標價多數高於前述股價參考區間 |
| 內部人 | 偏空 | 中 | 6 個月內 $27.8M 公開市場賣出、0 買入；可能含預先排程，無法排除 |
| 機構 | 中性 | 低 | 前十大 6 減 4 增，幅度不一；樣本僅到 6 月底 |
| 散戶 | DATA_UNAVAILABLE | — | Reddit、StockTwits 未取得；X 與新聞樣本不足 |

**綜合判定：中性（信心：低）**。分析師偏多與內部人大量賣出方向相反，散戶端無資料可供平衡。

Divergence flag：
- 分析師 vs 內部人：**是**，方向相反。
- 散戶 vs 分析師：**無法判定**，散戶資料為 DATA_UNAVAILABLE。

## 限制

- 目標價與評等計數來源衝突，結論只能視為方向性參考。
- 股價來源衝突，無法精確計算目標價上行空間。
- 機構持股比率超過 100%，已排除不用。
- 內部人賣出是否預先排程未知，不能直接推論為看空訊號。

SENTIMENT REPORT COMPLETE
