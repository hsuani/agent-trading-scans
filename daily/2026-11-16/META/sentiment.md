# Sentiment — META as of 2026-11-16

注意: 系統日期為 2026-11-15, 本報告依指示以 2026-11-16 為 as-of。最新內部人交易為 2026-11-09, 最新股價參考來自次級報導 (2026-11-10 收盤約 $641), 非 yf 工具直接輸出。

## Analyst consensus

yf `rec_summary` (0m, 共 61 家評等, 數據來源: yf CLI 於 2026-11-16 查詢):

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 當前 (0m) | 9 | 45 | 6 | 1 | 0 |
| -1m | 9 | 46 | 6 | 1 | 0 |
| -2m | 8 | 47 | 7 | 1 | 0 |
| -3m | 8 | 47 | 7 | 0 | 0 |

當前合計: 54 buy (含 strong buy) / 6 hold / 1 sell, 買進比例約 89%。三個月來 buy 家數略降 (55→54), hold 由 7 降為 6, sell 由 0 升為 1, 整體仍偏多但邊際略轉保守。

Recent moves: yf `recommendations` 工具只回傳彙總分佈, 沒有個別券商升降評等明細, 因此無法列出個別 upgrade/downgrade。次級新聞 (WebSearch, 日期混雜, 未經原始來源核對) 提到:
- JPMorgan 將 META 納入 Analyst Focus List, 維持 Overweight, 目標價 $940 (報導日期約 2026-11-09)。
- Cantor Fitzgerald 將目標價由 $830 下調至 $720, 維持 Overweight。
- RBC 下調目標價, 理由為 2026 opex/capex 指引上修。
- Roth Capital 稱資本支出引發的下跌為 "sentiment air-pocket", 建議逢低買進。

另一篇次級報導提到 "62 of 67 analysts buy, 共識目標價 $859.85", 與 yf 的 61 家計數口徑不同, 本報告以 yf 為準。

## Retail social

- **Reddit**: 不可用。`www.reddit.com` 無法連線 (WebFetch 回報 "unable to fetch"), 未重試。以下僅為次級報導引述之定性描述, 非本次直接抓取:
  - 報導稱 META 在 Reddit 的提及量於財報後明顯上升, 討論偏向質疑 AI 支出回報。
  - 代表性看法 (次級引述): 「dead money」直到資本支出停止為止; Reality Labs 虧損為常見抱怨。
  - 傾向: 偏空 / 懷疑 (定性, 信心低)。
- **StockTwits / X**: StockTwits 不可用 (`api.stocktwits.com` 與 `stocktwits.com` 皆無法解析, 需於 session 網路設定中允許)。未重試。
  - 次級報導稱 StockTwits 散戶情緒標示為 "neutral", 且 RSI 顯示超賣; 另有散戶將下跌稱為 "overreaction to a transparent tax error" (次級引述)。
  - 傾向: 分歧, 略偏中性 (信心低)。
- **聲量**: 無法直接量化 mention count。次級來源僅定性描述「財報後提及量明顯上升」, 無基準比較數字。
- **Themes (次級來源歸納)**:
  1. 資本支出爆增 (2026 capex 指引約 $135–145B) 與 AI 報酬質疑。
  2. 融資與信評壓力 (報導提及約 $25–35B 股權或債券募資, 及 S&P 信評展望負面的說法), 屬次級資訊, 未經核實。
  3. 財報後股價回檔 (一則報導提到單月跌幅約 16.7%, 與法律費用與稅務準備有關), 同樣屬次級資訊。
  4. 長線持有論 (「2030 年前最佳 buy and hold」之類文章)。

## Insider activity

6 個月窗口 (2026-05-16 至 2026-11-16, yf `insider` 工具):

Net 6mo: **$0 buys, $141.5M sells** (不含無金額列與 7/31 贈與列)。買進為 0, 全為賣出。

| 內部人 | 職稱 | 6mo 賣出 (USD M) | 筆數 | 備註 |
|---|---|---|---|---|
| COX CHRISTOPHER K | Officer | 55.0 | 3 | 單筆最大, 2026-09 集中出售 (2026-09-21 40,000 股, 約 $28.5M) |
| OLIVAN JAVIER | COO | 23.9 | 19 | 多為每週約 1,400–1,700 股的規律賣出, 疑似排程性 |
| ZUCKERBERG MARK | CEO | 21.4 | 1 | 2026-09-24 賣出 27,474 股, 約 $21.4M。另 2026-07-31 有 591,690 股贈與 (非現金, 未計入) |
| LI SUSAN J. | CFO | 13.4 | 3 | 2026-08-18 等 |
| ANDREESSEN MARC L | Director | 13.0 | 2 | 2026-11-02 出售 20,951 股, 約 $12.8M |
| BOSWORTH ANDREW | CTO | 9.1 | 2 | 2026-08-18 等 |
| 其他 (MAHONEY, ANDERSON, KIMMITT, ALFORD) | 董事/官員 | 5.5 | 8 | 金額小 |

Notable: 最近一筆為 2026-11-09 COO Olivan 出售 1,575 股, 約 $0.99M (以 631.03 計, 1,575 × 631.03 ≈ $0.99M, 與工具輸出一致)。CEO 的 $21.4M 單筆出售為本窗口內最大 C-suite 單筆之一。

Interpretation: 內部人全為賣出, 無公開市場買進。大量 COO 規律小額賣出可能反映既定交易計畫, 單看金額意義有限; Cox 與 Zuckerberg 的集中出售訊號較值得注意, 但無法從工具判斷是否屬於計畫性交易。

## Ownership shifts

yf `major_holders` (單一快照, 無歷史趨勢):
- 機構持股比例: 78.0% (institutionsFloatPercentHeld 78.3%)
- 機構數: 6,737
- 內部人持股: 0.27%

趨勢: 無歷史時序資料, 無法判斷機構集中度為增加或減少。

## Net sentiment score

**Composite: 中性偏多 (信心中等偏低)**

- 分析師面: 偏多 (54/61 buy, 信心高, 但邊際轉保守)。
- 內部人面: 偏空 (6mo 全為賣出 $141.5M, 0 買進; 部分為規律性計畫交易, 信心中)。
- 散戶面: 分歧至偏空 (主要依據次級報導, Reddit / StockTwits 直接資料不可用, 信心低)。
- 機構面: 持股集中、無趨勢數據, 中性。

**Divergence flag: yes** — 散戶與次級媒體偏懷疑 (主要針對資本支出), 與分析師偏多方向相反。內部人賣出亦與分析師偏多不一致。此分歧值得後續 bull/bear 辯論納入考量。

Data gaps: Reddit、StockTwits 不可用; 分析師個別升降評等明細不可得; 機構持股無時序; WebSearch 結果日期混雜 (2025–2026), 已盡量以 yf 工具數字為準, 次級數字僅作定性參考。

SENTIMENT REPORT COMPLETE
