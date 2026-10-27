# Sentiment — IPGP as of 2026-10-28

資料來源狀態: yf (rec_summary / recommendations / insider / major_holders) 回傳資料但 Yahoo cookie/crumb 取得失敗, 可能為快取值; Reddit (r/wallstreetbets, r/stocks) 無法連線; StockTwits DNS 解析失敗; WebSearch 僅回傳聚合站與鏡像頁, 可信度低。散戶情緒面實質缺資料。

## Analyst consensus

9 位分析師 (yf rec_summary):

| 評等 | 人數 | 占比 |
|---|---|---|
| Strong Buy | 2 | 22.2% |
| Buy | 4 | 44.4% |
| Hold | 2 | 22.2% |
| Sell | 0 | 0.0% |
| Strong Sell | 1 | 11.1% |

**BUY 合計 (Strong Buy + Buy): 6 / 9 = 66.7%**; Hold 22.2%; Sell 合計 11.1%。

- 近期變動: yf `recommendations` 回傳的三個期間 (0m / -1m / -2m) 分布完全相同, 無升降評等明細, 疑似為快取或未更新。
- 聚合站 WebSearch 提到 2026-05-06 Needham 由 Hold 升至 Buy (Fintel 來源, 未經 yf 交叉驗證)。若屬實, 與上述「三期間不變」的結果不一致, 需以即時資料確認。
- 目標價 (聚合站, 互相不一致, 皆未驗證):
  - Walnut Invest: 平均 $124.14 (稱 7 位分析師, 但評等合計為 9 位)
  - Naga: 平均 $133.50, 區間 $120–$152
  - Public.com: 平均 $131.40 (5 位分析師, 日期不明)
- 目前股價: 無可靠即時報價。yf 內部交易最新成交價約 $85.30–$86.09 (2026-10-02); 聚合站另有 $80.89 (10-07) 與 $78.34 兩個數字。本報告以 $78–$86 區間理解, 估值比對請以即時報價為準。

## Retail social

- **Reddit**: 無法取得 (r/wallstreetbets 與 r/stocks 的 JSON 端點被擋)。WebSearch 未找到 2026 年 IPGP 相關 Reddit 討論串。**tilt: 無法判定**。
- **StockTwits**: 無法取得 (DNS 解析失敗)。
- **X / 新聞聊天**: WebSearch 僅得到預測網站與技術分析鏡像頁 (內容為自動生成, 不可作為散戶情緒依據), 未見可引用的散戶原文。
- **聲量 (buzz)**: 無法量化, 與常態比較亦無依據。
- **引用**: 本次無可引用的散戶原文 (無資料來源可取得)。
- **Themes**: 無資料。依可得資訊, 市場焦點為 (1) 股價自 2026 年 2 月高點 (約 $135–$150, 由 yf 交易價格推得) 回落至 $80 上下, (2) 大股東持續出售, (3) 分析師目標價仍高於現價。以上為由交易資料推論, 非散戶言論。

## Insider activity

視窗: 2026-04-28 至 2026-10-28 (6 個月)。金額單位: USD M。

| 類別 | 買進 (USD M) | 賣出 (USD M) | 淨額 (USD M) | 筆數 |
|---|---|---|---|---|
| 10% 大股東實體 (IP Fibre Devices Ltd, Valentin Gapontsev Trust) | 0.00 | 21.17 | -21.17 | 6 |
| 董事 Scherbakov Eugene A (同時為 10% 持有人) | 0.00 | 0.55 | -0.55 | 3 |
| 其他董事 / 高管 (CFO Mammen 1.20, 董事 Desmond 0.18, 董事 Tang 0.18, GC Lopresti 0.11) | 0.00 | 1.66 | -1.66 | 4 |
| 董事 Peeler John R | 0.20 | 0.00 | +0.20 | 1 |
| **合計** | **0.20** | **23.38** | **-23.18** | **14** |

(換算校驗: 以 IP Fibre 2026-10-02 一筆為例, 15,361 股 × 約 $85.66 ≈ $1.32M, 與 yf Value 欄位 $1,315,515 相符。)

- **淨流向: 明顯淨賣出**, 金額約 $23.2M。
- **Notable**:
  - CFO Timothy Mammen 於 2026-05-22 以 $119.60–$120.37 賣出 9,975 股, 約 $1.20M。
  - GC Angelo Lopresti 於 2026-06-29 以 $110.33 賣出 1,000 股。
  - 董事 John Peeler 於 2026-08-26 以 $72.84–$74.57 買進 2,710 股, 約 $0.20M, 為本視窗內唯一買進, 且價位低於其他賣出價。
  - 大股東 IP Fibre Devices Ltd 於 2026-06-29 以 $100.19–$106.40 賣出 65,700 股, 約 $6.81M, 為視窗內單筆最大賣出。
- **Pattern 觀察 (推論, 需驗證)**: IP Fibre Devices 於 2025-09 至 2026-02 間約每月出售一次 (多為約 64,167 股的固定數量), 2026-03 至 05 無交易, 2026-06 之後再度出售。Gapontsev Trust 亦有規模相近的定期賣出。若這些交易屬預先設定的 10b5-1 計畫, 則反映的是流動性或分散持股需求, 而非對短期前景的判斷。SEC Form 4 的計畫註記未能由 yf 取得, 無法確認。
- 2026-05-12 董事年度股票獎勵 (價值 $0) 已排除於金額計算。

## Ownership shifts

- insidersPercentHeld: 39.0%
- institutionsPercentHeld: 75.5%
- institutionsCount: 492
- 資料異常: institutionsFloatPercentHeld 回傳 1.238 (超過 100%), 不納入判讀。
- 趨勢: yf 只提供當前快照, 無時間序列, **無法判定機構持股增減方向**。
- 注意: 內部人持股 39% 主要來自 Gapontsev 家族相關實體 (10% 大股東), 而該等實體正是上述淨賣出的來源。因此「內部人持股高」與「內部人淨賣出」同時存在, 不應解讀為矛盾, 而應理解為家族控制股東在減持。

## Net sentiment score

**Composite: 中性偏混合 (Neutral / mixed), 信心: 低-中。**

- 分析師面: **偏多 (bullish, 中等信心)**。BUY 66.7%, 目標價區間高於現價 (但目標價來源不一、未驗證)。
- 內部人面: **偏空 (bearish, 中等信心)**。6 個月淨賣出 $23.2M, 幾乎全部來自大股東實體與 CFO; 唯一買進為董事 Peeler 的小額買進。
- 散戶面: **無資料, 無法評分**。
- 信心受限原因: 散戶資料全數缺失; 分析師資料可能為快取; 股價與目標價來源互相矛盾。

**Divergence flag: 是 (yes)** — 分析師偏多與內部人 (大股東) 淨賣出方向相反。依慣例, 大股東因分散持股或計畫性減持而賣出, 其訊號強度通常低於公司高管的公開市場買進或賣出, 因此此背離的資訊價值需保守看待。散戶端無資料, 無法判定是否也出現第三方背離。

## Data gaps and follow-ups

1. yf 回傳的 rec_summary 三期間相同, 且 recommendations 無升降評等明細: 需以即時 Yahoo 資料或 Refinitiv/FactSet 確認是否為快取。
2. Needham 2026-05-06 升評等 (聚合站) 未經 yf 驗證。
3. 目標價 (Walnut $124 / Naga $133.5 / Public $131.4) 來源不一, 需以券商原始研究報告或付費資料源核對。
4. Reddit / StockTwits 端點不可用, 散戶情緒需於可連線環境補抓後更新。
5. 10b5-1 計畫註記未取得, 需查 SEC EDGAR Form 4 確認大股東賣出是否屬預定計畫。

SENTIMENT REPORT COMPLETE
