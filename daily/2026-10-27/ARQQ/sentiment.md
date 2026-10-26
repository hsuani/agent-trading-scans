# Sentiment — ARQQ（Arqit Quantum）as of 2026-10-27

> 資料時點注意：價格快取時間為 2026-10-26 12:44 UTC（來源 cnyes，`as_of` 欄位為空，未確認當日收盤）。Reddit、StockTwits、Yahoo 分析師端點皆被 proxy 政策拒絕（403），本報告的散戶與分析師部分資料不完整。依 proxy README 規定，未重試或繞道。

## Analyst consensus

**無可用的即時評級分布**。`recommendations` 與 `rec_summary` 皆回傳空陣列。網路搜尋只找到 2025 年底的舊資料（已過時，無法當作現況）：
- HC Wainwright：Buy，目標價 $60，最近一次更新 2025-12-18（之前為 2025-10-13）。
- MarketBeat 的評級彙整為 1 Sell、1 Buy，共識標示 Hold；Benzinga 共識目標價 $30.75（2 位分析師，日期不明）。兩家數據互相矛盾，且皆非 2026 年資料。
- 近期價格變化：散戶與內部人賣出價在 2026-07 至 10-06 為 $24–30，2026-10-13 為 $16.40，2026-10-26 快取價 $16.41（前收 $15.81，日內區間 $15.51–16.95）。股價相對 10 月初的賣出價約下跌三分之一以上。
- 結論：分析師面的評級分布、近期調整與目標價變動皆無法確認，本段應視為**資料缺口**。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：因 proxy 403 無法取得。tilt 無法判定。
- **StockTwits**：DNS 解析失敗（`getaddrinfo ENOTFOUND`），無法取得。
- **X / 新聞散戶討論**：網路搜尋未找到 2026-10 的 ARQQ 相關討論。找到的 Benzinga Bulls vs Bears 頁面顯示 put/call 比率為 1.09 與 0.17 兩組互相矛盾的數字，兩者皆不可靠，不納入判斷。
- **Buzz 量**：無法量化，無法與常態比較。
- **可參考的其他資料**：short interest 約 17.8%（來源：Benzinga 第三方頁面，日期不明）；StockScan 技術面標示 Strong Sell（17 項指標中 2 Buy、10 Sell、5 Neutral，日期不明）。這些為過時或不明日期的快照，僅供參考。
- **主題**：無法萃取。未取得任何可引用的貼文，因此本段無引述。

## Insider activity

視窗：2026-04-27 至 2026-10-27（6 個月）。

**Open-market 買入：0 筆，$0。**

**Open-market 賣出（Sale 有價格標記）合計約 $2.68M（USD M）**：

| 人員 | 職稱 | 日期範圍 | 股數 | 金額（USD M） |
|---|---|---|---|---|
| Lefebvre D'Ovidio Manfredi | Director（間接持股 Ownership = I） | 2026-07-01 | 54,444（@ $30.07–30.24） | 1.64 |
| Leaver Andrew | CEO | 2026-07-02 至 10-13（5 筆） | 20,217 | 0.48 |
| Willcocks Patrick | General Counsel | 2026-06-30 至 10-06（5 筆） | 7,709 | 0.21 |
| Bers Jennifer | Officer | 2026-06-22 | 8,288（@ $21.42） | 0.18 |
| Feenan Paul | Officer | 2026-07-02 至 10-06（4 筆） | 3,377 | 0.08 |
| Wilder Ben Simon | COO | 2026-07-02 至 10-06（4 筆） | 1,441 | 0.04 |
| Nilan Nicholas William | Officer | 2026-07-02 至 10-06（3 筆） | 1,509 | 0.04 |
| Ritchie Garth | Director | 2026-07-02 至 10-06（4 筆） | 805 | 0.02 |

- 賣出分布：2026-06 底至 07 初與 10 月初為兩波集中賣出。10 月初 CEO、GC、COO 與多位 Officer 幾乎同日同價（$24.19 或 $24.47）賣出，屬於有規律的重複性賣出。
- 最大單筆為 Lefebvre（Director，間接持股）於 2026-07-01 賣出 54,444 股，約 $1.64M。

**Derivative 行權 / 轉換（$2.50 行權價，非 open-market 買入，不計入淨買入）**：
- 2026-06-03 Calabria Carlo（Director）120,000 股，約 $0.30M 名目金額。
- 2026-06-05 Ritchie Garth（Director）73,562 股，約 $0.18M 名目金額。
- 2026-09-22 Lefebvre D'Ovidio Manfredi（Director，間接持股）4,600,000 股，約 $11.5M 名目金額。此為最大的潛在股權壓力來源：行權成本 $2.50 相對現價 $16 處於大幅價內，若後續出售將直接影響供給。目前尚未看到對應的 open-market 賣出紀錄。

**其他**：有數十筆無價格、無文字說明的 Form 4 紀錄（如 Leaver 5,208–5,209 股，多在 10 月初與 07-01 出現），性質不明（可能為 RSU 歸屬、扣繳或其他非市場交易），未計入淨買賣。

**淨額**：6 個月 open-market 淨額約為 **-$2.68M（純賣出）**。若把行權後的名目金額算入，數字會誤導，因此不納入。

## Ownership shifts

- 機構持股 82.6%，內部人持股 2.8%，機構數 94（來源：yf `major_holders`）。
- 前兩大持股高度集中：Defiance ETFs, LLC 32.6%（5.10M 股，2026-06-30，季度增加 2.5%）與 Penserra Capital Management 32.5%（5.08M 股，2026-06-30，季度增加 2.5%），兩者合計約 65%。
- 其他：UBS 3.3%（季度增加 5.1%）、Legal & General 1.8%（增加 4.2%）、National Bank of Canada 1.4%（增加約 193%，基數小）。Kessler Investment Group 0.9%（2026-09-30 資料）。
- 解讀：持股集中於兩家機構，且 Q2 皆為小幅加碼。這使得股權結構對單一機構的進出敏感，但目前沒有看到明確的減碼訊號。

## Net sentiment score

- **Composite：偏空（bearish），信心度低**。主要依據是內部人 6 個月持續 open-market 賣出（$2.68M，0 買入），以及 4.6M 股 $2.50 行權股份的潛在供給。分析師面與散戶面皆缺乏可靠的 2026 資料，無法納入加權。
- **Divergence flag：無法判定**。散戶面無資料，分析師面僅有 2025 年舊評級（Buy $60，明顯過時）。若以舊 Buy 評級與內部人賣出相比，形式上存在分歧，但因分析師資料已過時，不足以作為可靠訊號。
- **資料缺口清單**：
  1. recommendations / rec_summary 空回傳，需要替代來源（如 Benzinga、MarketBeat、TipRanks 的即時頁面）。
  2. Reddit、StockTwits 皆被封鎖（403 與 DNS 失敗）。
  3. 價格快取未確認當日收盤。
  4. 內部人 Form 4 中無價格紀錄的性質未核實。

SENTIMENT REPORT COMPLETE
