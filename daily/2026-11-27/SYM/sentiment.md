# Sentiment — SYM (Symbotic) as of 2026-11-27

資料時點說明: yf 工具走 pricefeed cache (source: cache 為本環境常態)。Yahoo cookie/crumb 與 `actions` 端點因 CONNECT 403 失敗, 標示 DATA_UNAVAILABLE。Reddit / StockTwits 直連本環境被封鎖, 改以 WebSearch 取得的摘要判讀, 多數來源日期不明或為 2025 年舊文, 可信度低。

## Analyst consensus

rec_summary (期間 0m, 最新快照): **9 buy / 6 hold / 2 sell / 1 strongSell (strongBuy 0)**, 共 18 家。買方佔 50%, 持有 33%, 賣方 17%。

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 |
|---|---|---|---|---|---|---|
| 0m (最新) | 0 | 9 | 6 | 2 | 1 | 18 |
| -1m | 1 | 9 | 5 | 2 | 1 | 18 |
| -2m | 1 | 8 | 5 | 2 | 1 | 17 |
| -3m | 1 | 9 | 5 | 2 | 1 | 18 |

- 近三個月評級分布穩定, 最新一期 strongBuy 由 1 降至 0, hold 增 1 家。
- 交易評級變動 (recommendations 僅回傳月度彙總, 無個別券商 upgrade/downgrade 明細): DATA_UNAVAILABLE。
- WebSearch 另見一份 11/13 摘要, 稱 19 家覆蓋為 9 buy / 7 hold / 3 sell, 與 yf 快照略有出入, 以 yf 為準。
- 目標價: 當前共識目標價 DATA_UNAVAILABLE。搜尋所得數字 ($54.75、$55.36 (2026-03-03 快照)、$48.6) 日期不一且互相矛盾, 不採用。
- 個別券商動作 (WebSearch 所見, 日期多不明, 未經原始來源核實):
  - KeyBanc Hold → Buy, PT $70 (標示 2026-02-19)
  - Barclays Underweight 維持, PT $44 → $38 (標示 2026-09-08)
  - DA Davidson 降至 Neutral, PT $47 (標示 2025-08-25)
  - Goldman Sachs Sell, PT $47 (日期 DATA_UNAVAILABLE)
  - Craig-Hallum 降至 Hold, PT $25; Arete 降至 Neutral, PT $50 (日期 DATA_UNAVAILABLE)
- 11 月內未找到可驗證的評級變動 (AAII 11/16 摘要稱過去一個月無券商改評等)。

## Retail social

- **Reddit**: 直連封鎖, 以 WebSearch 替代。r/wallstreetbets 搜尋未找到 SYM 相關討論串, 提及次數與情緒 DATA_UNAVAILABLE。r/stocks 有一篇看多論述 (作者 snem420), 日期不明。r/ValueInvesting 亦有一篇看多文章 (日期不明)。以上只是少數樣本, 不足以代表整體散戶傾向。
- **StockTwits**: 直連受限。AltIndex 頁面顯示 SYM 情緒 94/100 (看多), 日均約 56 則訊息 (較三個月前 +24%), 但無時間戳記, 可信度低。StockTwits 新聞標題多為歷史事件 (Q1 盤前重挫後 "Retail Eyes Bottom Fishing Opportunity"; 收入認列錯誤揭露後 "Retail Sentiment At 2-Month Lows"), 顯示散戶情緒隨事件大幅擺盪。
- **X / 新聞**: AAII 動能分數 22 (弱); 11/17 股價約 $32.78, 當月跌約 13.6%。Benzinga 指出 SYM 選擇權交易近期偏負面。TipRanks 情緒模型為負面, 但指出 2026-05-06 財報電話會議情緒為正面。
- **聲量**: 相對典型水準 DATA_UNAVAILABLE (無可靠的 mention count 基準)。StockTwits 日均約 56 則為唯一量化數字, 且未標日期。
- **Themes (反覆出現的論點)**:
  - 看多: 股價回檔即買點 (bottom fishing); 機器人與 Walmart 合作前景; 長期目標 (長線持有論點)。
  - 看空: 客戶集中度 (約 84% 營收來自 Walmart, 來源為 WebSearch 摘要); 收入認列與財報品質疑慮; 估值與高 beta (約 2.85, 摘要所述); 股價動能轉弱。

## Insider activity

6 個月窗口 2026-05-27 至 2026-11-27 (含 2026-05-27 邊界日):
- **買入: $0 (0 筆)**
- **賣出: $288.1M (26 筆公開市場賣出)**
  - SoftBank Group (10% 以上大股東) 於 2026-05-27 以約 $50.42 賣出 5.59M 股, 約 $281.8M (5,590,000 × 50.42 ≈ 281.9M, 與工具值相符)。此筆佔窗口賣出總額約 98%。
  - 扣除 SoftBank, 高管與董事賣出約 $6.3M。
- 排除邊界日 (2026-05-27) 後, SoftBank 一筆不計, 窗口賣出總額約 $6.3M; 結論方向不變。

| 內部人 | 職位 | 6 個月賣出 (M USD) | 近期交易 |
|---|---|---|---|
| SoftBank Group | 10% 以上大股東 | 281.8 | 2026-05-27 賣 5.59M 股 @ $50.42 |
| James J. Kuffner Jr. | CTO | 1.80 | 2026-11-24 賣 3,627 股 @ $36.99 |
| Izilda P. Martins | CFO | 1.40 | 2026-10-28 賣 7,224 股 @ $38.93 |
| William M. Boyd III | 高管 | 0.97 | 2026-10-27 賣 9,194 股 @ $38.34–39.14 |
| Brian D. Alexander | 高管 | 0.72 | 2026-10-27 賣 9,314 股 @ $38.26–38.28 |
| Todd J. Krasnow | 董事 (部分間接持有) | 0.69 | 2026-11-02 賣 2,000 股 @ $37.53–39.67 |
| Charles F. Kane | 董事 | 0.51 | 2026-11-02 賣 2,000 股 @ $37.46–39.68 |
| Maria G. Freve | 高管 | 0.18 | 2026-10-27 賣 2,288 股 @ $38.25–38.34 |

- 另有 13 筆無金額紀錄 (多為選擇權行使、稅務代扣或配發性質), 無法量化: 其中多筆為 CTO/CFO/高管同日成對出現, 屬例行性質, 以 DATA_UNAVAILABLE 處理。
- 賣價趨勢: 2026-04 至 05 高管賣出價約 $52–60; 2026-07 至 08 約 $40–46; 2026-10 至 11 約 $37–39。賣出價隨股價回落, 但內部人仍持續出售。
- 董事 Ford Rollin L. 於 2026-02-11 賣 60,000 股 (約 $3.45M), 不在 6 個月窗口內, 僅列為背景。

## Ownership shifts

- 機構持股 81.6%, 機構數 547 家; 內部人持股 13.6%; 機構流通股持有比例 94.4%。
- 前十大持股合計約 68.7% (以 2026-09-30 數據計):
  - SoftBank 30.45% (39.8M 股), 較大
  - Walmart 11.47%
  - Baillie Gifford 9.32% (季減 -0.64%)
  - Vanguard (兩實體合計) 約 6%, 季增約 11–21%
  - Morgan Stanley 3.63% (季增 22.9%)
  - JPMorgan 2.97% (季增 34.4%)
- 趨勢: 指數與大型銀行持股季增, Baillie Gifford 小幅減碼, SoftBank 為主要集中來源。SoftBank 2026-05 的大額賣出與其 30% 持股相比, 屬於需追蹤的集中度變化 (是否續減持未知)。

## Net sentiment score

**Composite: neutral (信心: 低至中)**

| 維度 | 傾向 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 偏多 (中性偏多) | 中 | 買方 50%, 賣方 17%; 評級結構穩定 |
| 散戶 | 不明 / 混合 | 低 | 情緒 94/100 (無日期) 與 TipRanks 負面並列; Reddit 無有效樣本 |
| 內部人 | 偏空 | 中 | 6 個月零買入, 賣出 $288.1M (扣 SoftBank 約 $6.3M); 賣價隨股價下跌仍持續 |
| 價格動能 | 偏弱 | 中 | AAII 動能 22, 11 月跌約 13.6%, 選擇權情緒偏負 |

**Divergence flag: 部分存在 (partial)**
- 分析師評級整體偏多, 但內部人持續淨賣出且股價動能轉弱, 方向不一致。
- 散戶傾向無法以可靠資料判定, 故無法確認 retail 與 analyst 是否相反 (資料不足)。
- 若後續取得有日期的 StockTwits 或 Reddit 數據, 應重新檢查此旗標。

SENTIMENT REPORT COMPLETE
