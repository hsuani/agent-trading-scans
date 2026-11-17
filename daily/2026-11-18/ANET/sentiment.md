# Sentiment — ANET as of 2026-11-18

> 資料時效注意: 系統當日為 2026-11-17, 本報告依任務指定之 2026-11-18 作為 as-of 日期。內部交易資料最新至 2026-11-06; 分析師評等為無日期快照; 散戶資料來源多為未標註日期之搜尋摘要。未取得 Q3 2026 財報後的實際分析師調整紀錄。

## Analyst consensus

| 評等 | 家數 |
|---|---|
| Strong Buy | 9 |
| Buy | 21 |
| Hold | 0 |
| Sell | 0 |
| Strong Sell | 0 |
| **合計** | **30 (Buy 系 30 / Hold 0 / Sell 0)** |

- 30 家中 100% 為 Buy 系, 無 Hold 或 Sell。
- 與 1 個月前快照比較: Strong Buy 由 7 增至 9, Buy 由 24 降至 21, Hold 由 1 歸零, 總家數由 32 降至 30。方向為評等集中於買進, 但總覆蓋家數略減。
- 與 3 個月前快照比較: Strong Buy 8 → 9, Buy 23 → 21, Hold 0 → 0, 合計 31 → 30, 結構穩定。
- 個別升降評等 (upgrade/downgrade) 明細: DATA_UNAVAILABLE (yf recommendations 工具僅回傳彙總快照, 未提供逐筆變動紀錄)。
- 目標價變動: DATA_UNAVAILABLE (工具未提供)。搜尋摘要提及平均目標價約 $180 至 $188、Street high 約 $200 至 $220, 但來源日期不明, 不採計為當期數據。

## Retail social

- **Reddit**: 直接抓取 r/wallstreetbets 與 r/stocks 的 public JSON 被阻擋 (依任務說明改以 WebSearch 替代), 未取得個別貼文樣本。搜尋摘要中的 AltIndex 聚合頁 (最後更新 2026-10-16) 顯示 Reddit 討論量低於近期平均, 情緒分數 88/100 (偏多)。此為單一聚合來源, 無法核對原文。
- **StockTwits**: 未直接取得 (任務指定之 API 端點未嘗試或不可用, 標記為 soft-fail)。
- **X / 新聞論壇**: 搜尋結果多為 Seeking Alpha、Barchart、Simply Wall St 等媒體觀點, 並非散戶貼文。
- **聲量 (buzz volume)**: 定性判斷為低於平常水準 (依 AltIndex 聚合)。無精確提及次數, 數值為 DATA_UNAVAILABLE。
- **散戶傾向**: 偏多但力道不強, 信心低 (來源單一且日期不明)。
- **代表性論點 (摘要, 非原文)**:
  - 財報後股價大幅回檔 (搜尋摘要稱約 18%), 社群爭論是否為買點。
  - 估值偏高: 來源指出 EV/EBITDA 約 40 倍以上, 高於同業, 成長需要持續兌現。
  - AI 網路需求為主要多方敘事, Q1 2026 營收年增約 35% 被引用。
  - 內部人大額賣出被視為空方論點。
- **Themes**: AI 網路需求 (多)、估值過高 (空)、財報後回檔是否為買點 (中性)、內部人減持 (空)。

## Insider activity

視窗: 2026-05-18 至 2026-11-18 (6 個月)。

| 類別 | 金額 (USD M) | 備註 |
|---|---|---|
| 公開市場買進 (Purchase) | 0.0 | 無 |
| 公開市場賣出 (Sale) | 1,296.3 | 約 1.30 B USD, 共 65 筆申報列 (含選擇權行使後賣出與股票獎勵列) |

賣出金額依申報人分列 (USD M):

| 申報人 | 職稱 | 賣出金額 (USD M) |
|---|---|---|
| Andreas Bechtolsheim | 持股 >10% 股東 (非經理人) | 677.4 |
| Jayshree Ullal | CEO | 580.2 |
| Kenneth Duda | President | 32.1 |
| Mark Templeton | Director | 2.8 |
| Charles Giancarlo | Director | 2.7 |
| Chantelle Breithaupt | CFO | 0.8 |
| 其他獨立董事 (Battles, Wassenaar) | Director | 0.2 |

- **Notable**:
  - Bechtolsheim 於 2026-10-30 至 2026-11-06 連續多筆賣出, 價格區間約 $159 至 $174, 為視窗內最近期的大額賣出。
  - Ullal 於 2026-10-06 與 10-09 賣出, 價格約 $211 至 $217, 為較高價位區段的大額減持。
  - Duda 以選擇權行使後賣出的方式定期減持, 屬例行模式。
  - Templeton 與 Giancarlo 每月或每季有小額固定賣出。
- 大部分賣出似為定期或計畫性交易 (部分重複的固定股數模式), 但無法從工具資料確認是否屬 10b5-1 計畫, 此點標記為 DATA_UNAVAILABLE。
- 無任何內部人公開市場買進紀錄。

## Ownership shifts

- 內部人持股 (insidersPercentHeld): 17.2%
- 機構持股 (institutionsPercentHeld): 73.0%
- 流通股中機構持股 (institutionsFloatPercentHeld): 88.3%
- 機構持股家數: 3,299
- 持股變動趨勢 (季度對比): DATA_UNAVAILABLE (工具僅回傳單期快照)。

## Net sentiment score

- **分析師 (bullish)**: 30 / 0 / 0, 一致偏多; 1 個月內 Hold 歸零, 方向穩定。信心: 高 (對方向), 但目標價與逐筆評等變動缺漏。
- **散戶 (mildly bullish)**: 單一聚合來源顯示偏多、聲量偏低。信心: 低。
- **內部人 (bearish tilt)**: 6 個月約 $1.30 B 賣出, 零買進, 近期 (10 月底至 11 月初) 有高價區以外的大額減持。信心: 中 (賣出多為例行模式, 但規模大)。
- **綜合**: **中性偏多 (neutral-to-bullish)**, 信心 **中低**。分析師與散戶方向一致偏多, 內部人為明顯淨賣出, 拉低綜合分數。

**Divergence flag: 是 (內部結構層面)**
- 散戶與分析師方向相同 (皆偏多), 無散戶對立分析師的跨群體背離。
- 但內部人淨賣出與分析師全數買進方向相反, 屬於值得注意的內部背離。
- 外部背離判讀受限於: 散戶資料來源單一、日期不明, 且未取得 Q3 2026 財報後之分析師調整紀錄。

## Data gaps (DATA_UNAVAILABLE 彙整)

- 分析師逐筆升降評等與目標價變動 (yf recommendations 僅回傳快照)
- Reddit 個別貼文與 r/stocks 資料 (直接抓取受阻)
- StockTwits 訊息流 (未取得)
- 散戶提及次數的精確數值
- 機構持股季度變動趨勢
- 內部人賣出是否屬 10b5-1 計畫
- Q3 2026 財報後實際股價走勢與分析師反應 (僅有未標註日期之搜尋摘要)

SENTIMENT REPORT COMPLETE
