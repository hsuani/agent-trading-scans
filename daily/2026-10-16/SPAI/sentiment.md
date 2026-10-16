# 情緒分析 (Sentiment) — SPAI 截至 2026-10-16

## 分析師共識

**評級分佈 (rec_summary, 0m 期)**: 3 位 Buy / 0 位 Hold / 0 位 Sell / 0 位 Strong Buy / 0 位 Strong Sell。
**買入比例 (% BUY): 100% (3/3)**。樣本只有 3 位, 統計意義很低。

**近期動態**:
- yf `recommendations` 回傳的內容與 `rec_summary` 相同, 沒有逐筆升降評等紀錄, 因此無法確認近期 upgrade / downgrade 事件。
- 0m、-1m、-2m 三期皆為 3 Buy, 過去三個月評級分佈沒有變動。
- 目標價: yf 工具沒有提供 price target 欄位。第三方 Benzinga 頁面 (經 WebSearch 取得摘要) 顯示平均目標價 $10, 當時股價約 $4.51 (引用日期 2026-10-08)。此數字未經 yf 交叉驗證, 僅作參考。
- 最近的分析師動作 (據 Benzinga 摘要) 為 2025 年底 Lake Street 首次給予 Buy、Northland 給予 Outperform, 未見 2026 年下半年的評級異動。

## 散戶社群 (Retail social)

- **Reddit (r/wallstreetbets, r/stocks)**: DATA_UNAVAILABLE。沙箱封鎖 Reddit 直連, 本次未使用 WebFetch 取樣, 無法估計提及次數或看多/看空比例。
- **StockTwits**: DATA_UNAVAILABLE。同樣因沙箱封鎖。
- **X / 新聞與意見網站 (WebSearch)**: 2026-10 期間沒有找到針對 SPAI 的公開散戶意見。搜尋結果多為自動生成、品質低的頁面 (日期多為 2026-04), 已排除。
  - Investing.com 的使用者喊單紀錄顯示結果分歧: 2026 年 6 月數筆喊單虧損約 20% 至 36%, 7 月一筆於 8 月中旬上漲約 65%。這屬於個別樣本, 不代表整體散戶情緒。
  - Benzinga 情緒頁面標示 short interest 3.9% 並註記為上升 (偏空訊號), 30 天內內部人淨賣出。
- **聲量 (buzz volume)**: 無可靠量化數據。依據 2026-06-24 的歷史報告, SPAI 當時未進入熱門股清單, 本次無法更新此判斷, 暫列為低聲量 (低信心)。
- **主題 (依現有可取得的資料)**:
  1. 股價由約 $6.22 (2026-06) 回落至約 $4.5 (2026-10 初) 的走勢, 是市場注意的焦點之一。
  2. CEO 於 9 月出售 100 萬股, 成為近期最明顯的負面話題來源。
  3. 政府與國防合約 (如 2026-06 前後的陸軍合約) 為正面敘事, 但本次未取得新的合約資訊可驗證。

## 內部人活動 (Insider activity)

- **淨 6 個月 (2026-04-16 至 2026-10-16)**: 公開市場買入 $0; 公開市場賣出約 $4.0M (1,000,000 股 @ $4.00)。
- **主要交易**:
  - CEO Daniyel Erdberg, 2026-09-09, Sale 1,000,000 股 @ $4.00, 約 $4.0M, 直接持有 (D)。yf 的 Transaction 欄位為空, 交易代碼無法從工具確認, 但敘述欄位標示為 Sale。
  - Officer Brian William Mack, 2026-05-01, Stock Award (Grant) 300,000 股, 價值 $0 (非市場交易)。
  - 其餘在 6 個月窗口內的紀錄皆為 Grant 或 Gift, 不計入買賣。
- **解讀**: 在窗口內唯一的市場交易是 CEO 的大額賣出。沒有任何董事或高階主管的公開市場買入紀錄。CEO 的持股基數在 2026-06 歷史報告中記為約 514 萬股, 若該數字仍正確, 此次賣出約為其直接持股的五分之一左右, 但這是推估, yf 未直接提供持股數。
- 內部人合計持股 (insidersPercentHeld) 45.47%, 股權結構集中。

## 機構持股 (Ownership)

- **機構持股比例**: institutionsPercentHeld 12.06%; 以浮動股計 institutionsFloatPercentHeld 22.13%; 持有機構數 31 家。
- **前 10 大機構 (13F 報告日 2026-06-30, 資料較舊)**:
  - 增持 4 家: Vanguard Capital Management (+24.5%, 約 56.4 萬股)、Jane Street (+100%, 約 14 萬股)、BlackRock (+21.6%)、Vanguard Fiduciary Trust (+15.7%)。
  - 減持 3 家: Tudor Investment (-42.6%)、Geode Capital (-2.0%)、Perkins Capital (-0.3%)。
  - 持平 3 家: Cresset Asset Management、Thompson Siegel & Walmsley、State Street。
  - 依前 10 大的股數變動推算, 合計淨增約 10 萬股 (約佔流通股約 0.5%, 以 Vanguard 的持股比例推估流通股約 2,040 萬股)。
- **趨勢判讀**: 機構淨流向為小幅流入, 主要來自指數型與部分量化機構。規模小, 且資料已延遲約 3.5 個月, 無法反映 2026 年第三季的變化。

## 綜合情緒評分 (Net sentiment score)

- **綜合判定: 中性 (信心: 低)**, 略偏空的情緒訊號集中在內部人與股價走勢, 機構與分析師則偏正面。
  - 分析師: 偏多 (3/3 Buy, 信心低, 樣本少)
  - 內部人: 偏空 (單一大額 CEO 賣出, 無買入)
  - 機構: 小幅偏多 (前 10 大淨增, 資料延遲)
  - 散戶: 無法判定 (Reddit / StockTwits 不可用, 其餘來源零散)
- **背離旗標 (Divergence flag): 是 (分析師與內部人方向相反)**。分析師全部 Buy, 而 CEO 在 9 月賣出 100 萬股。散戶與分析師之間的背離無法確認, 因為散戶資料不可用。

## 資料可用性

| 項目 | 狀態 |
|---|---|
| yf rec_summary / recommendations | 可用 (來源為快取, 屬正常) |
| yf insider | 可用 (最新交易 2026-09-09) |
| yf major_holders / inst_holders | 可用 (13F 日期 2026-06-30) |
| Reddit (WSB, r/stocks) | DATA_UNAVAILABLE (沙箱封鎖) |
| StockTwits | DATA_UNAVAILABLE (沙箱封鎖) |
| 分析師目標價 | 僅第三方來源, 未經 yf 驗證 |

## 摘要

- 分析師共識: **100% BUY** (3/3), 無評等變動紀錄。
- 機構資金流向: **小幅淨流入** (前 10 大淨增約 10 萬股, 資料截至 2026-06-30)。

SENTIMENT REPORT COMPLETE
