# Sentiment — MTSI (MACOM Technology Solutions) as of 2026-11-23

注意: 依系統指示, 本報告不寫入 daily/2026-11-23/MTSI/sentiment.md, 內容直接於此回傳。資料截止日以各來源實際時點為準, 最新可確認的內部人交易為 2026-11-13。

## Analyst consensus
yfinance rec_summary (0m): 14 buy (含 strong buy 4) / 2 hold / 0 sell。過去四個月趨勢: -3m 為 12 buy / 4 hold / 0 sell, 目前 hold 減少 2 檔、strong buy 增加 1 檔, 評等小幅上修。
WebSearch 聚合站 (Investing.com 類) 顯示 11 buy / 3 hold / 0 sell, 與 yf 數字不一致, 原因未知, 以 yf 為主, 聚合站僅作參考。

近期評等與目標價 (WebSearch 結果, 日期部分不完整):
- Raymond James: 升評 Outperform, 目標價 $300, 當日股價上漲約 6% (文章未註明日期, 疑為 2026-10 後)。
- BMO Capital: 升評 Buy, 目標價 $335, 2026-09-18。
- Northland: 目標價升至 $375, 2026-05-08。
- Jefferies: 目標價由 $295 升至 $450, 維持 Buy, 日期未確認 (文中提及 "breakout quarter", 疑為 2026 年 5 月財報後)。
- Fintel 平均一年期目標價 $391.26 (頁面日期 2026-09, 已過時)。
- 限制: yf 的 recommendations 欄位回傳的是 summary, 沒有逐筆升降評歷史, 因此無法列出完整升降評時間序列。

基本面背景 (WebSearch, Weiss Ratings 引用): 2026 財年第四季 adjusted EPS $2.09, 優於市場預期 $2.00; 營收 $424.8M, 年增 62.7%。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 軟失敗。WebFetch 無法連線 www.reddit.com, 無法取得貼文樣本、分數與留言數, 此項無資料。
- StockTwits: 軟失敗。api.stocktwits.com 無法解析 (DNS 失敗), 疑為 session 網路白名單未開放, 需由使用者於 session 設定允許此網域後才能重試。
- X / 新聞聊天 (WebSearch 代理指標, 無法取得原始貼文):
  - LunarCrush 主題頁: 社群熱度 (social dominance) 高於日均 118%, 互動量 22.3K, 高於日均 507%。時間點未明, 但顯示聲量明顯放大。
  - TipRanks: 散戶情緒為正向, 但持有比例低於 0.1%, 代表樣本代表性有限。
- 聲量: 相對於自身日均為明顯升高 (定性判斷, 缺乏可比的絕對 mention 數)。
- 散戶傾向: 依現有代理指標為偏多但信心低 (因 Reddit / StockTwits 皆無資料)。
- 主要主題 (由新聞與聚合站整理, 非原始貼文):
  1. AI 基礎建設與 CoreWeave 財報帶動的板塊反彈 (約 2026-11-10)。
  2. 估值爭議: Webull 指出本益比約 56.9x, 高於半導體產業 41.4x, 公允比率 37.5x。
  3. 10 月約 30% 回檔後, 分析師視為買點 (Raymond James 升評論調)。
  4. 股價高點與低點落差大: 52 週高點 $418.90 (2026-05-27), 2026-11-04 低點 $209.51。
- 引言: 本次無可安全引用的 Reddit / StockTwits 貼文原文, 不引用任何 quote。

## Insider activity
統計期間: 2026-05-23 至 2026-11-23 (6 個月)。統計口徑為 "Sale" 之公開市場賣出, 不含 "Stock Award(Grant)" 與 "Stock Gift"。
Net 6mo: $0 buys, 約 $16.6M sales (USD, 以 M 表示)。

| 日期 | 內部人 | 職位 | 股數 | 金額 (USD M) | 備註 |
|---|---|---|---|---|---|
| 2026-05-29 | DALY STEPHEN G | CEO | 15,828 | 5.79 | 價區 $358–391 |
| 2026-06-25 | HWANG DONGHYUN THOMAS | Officer | 2,620 | 1.01 | 價區 $367–392 |
| 2026-08-17 | KOBER JOHN F. III | CFO | 7,389 | 2.41 | 價區 $321–331 |
| 2026-08-28 | DENNEHY ROBERT B | COO | 252 | 0.07 | 價 $275.20 |
| 2026-10-01 | ROTH AMBRA R | General Counsel | 653 | 0.20 | 價 $300.00 |
| 2026-10-26 | KOBER JOHN F. III | CFO | 1,027 | 0.24 | 價 $236.60 |
| 2026-11-09 | KOBER JOHN F. III | CFO | 22,009 | 4.56 | 價區 $196–212 |
| 2026-11-09 | ROTH AMBRA R | General Counsel | 9,497 | 2.15 | 價區 $212–230 |
| 2026-11-12 | ROTH AMBRA R | General Counsel | 552 | 0.14 | 價 $250.00 |

重新驗算: KOBER 2026-11-09 股數 22,009 × 區間中價約 $204.3 ≈ $4.50M, 與來源 $4.56M 誤差約 1%, 金額數量級正確。
9 筆合計 $16.56M, 與逐筆加總一致。

- 賣出集中於 CFO 與 GC 於 2026-11-09 至 11-12 之間 (約 $6.9M), 落在財報後。是否屬 10b5-1 計畫或稅務相關賣出, 資料中無法確認。
- 賣出價格自 $358–392 (2026 年 5–6 月) 降至 $196–250 (2026 年 11 月), 內部人在股價大幅下跌後仍持續賣出, 偏負面訊號, 但稅務或分散投資的解釋也常見。
- 2026-10 與 2026-11 有 CEO / CFO / 董事等 "Stock Award(Grant)" (例如 CEO 2026-11-05 授予 107,710 股), 屬薪酬性質, 未計入淨額。
- 未見 10%+ 持股人於統計期間賣出 (Susan Ocampo 最後一筆賣出為 2026-02-25)。
- 無任何公開市場買進紀錄。

## Ownership shifts
- 機構持股比例約 98.8%, 機構數 871 (yf major_holders 當前快照)。
- 內部人持股比例約 6.6%。
- 趨勢資料不足: yf 僅提供目前快照, 無歷史機構持股變化可比較。
- 10%+ 持股人 Susan Ocampo 於 2025-09 至 2026-02 期間有大量賣出與贈與 (單日數十萬股量級), 2026-02-25 後無紀錄, 屬於大股東減持已告一段落的跡象 (此為觀察, 非結論)。

## Net sentiment score
- 分析師: 偏多 (14 buy / 2 hold / 0 sell, 評等近四個月小幅上修)。信心: 中高 (資料來源單一, 且與聚合站數字不一致)。
- 內部人: 偏空 (6 個月 $16.6M 賣出, 零買進, 賣出集中於財報後)。信心: 中。
- 散戶: 偏多但信心低 (僅有 LunarCrush / TipRanks 代理指標與新聞; Reddit / StockTwits 無資料)。
- 綜合評分: 中性 (分析師偏多與內部人偏空相抵, 散戶資料不足)。綜合信心: 中低。

Divergence flag:
- 內部人 vs 分析師: 是。分析師評等偏多, 內部人淨賣出, 方向相反。
- 散戶 vs 分析師: 否 (或無法判定)。兩者目前皆偏多, 但散戶端資料不足, 無法確認。

## 資料缺口與限制
1. 目前股價未能於本次工具中確認。新聞與聚合站的價格快照分散於 $137–390, 多為過時資料。內部人交易價 (2026-11 為 $196–250) 與 StockTwits 無日期快照 ($287.57) 不一致, 請以即時報價校正估值與 "價格相對目標價" 的判讀。
2. Reddit 與 StockTwits 無資料 (軟失敗)。api.stocktwits.com 需於 session 網路設定允許後才能重試; Reddit 同樣無法連線。
3. analyst 評等數字 yf (14/2/0) 與聚合站 (11/3/0) 不一致, 未能解釋差異來源。
4. 升降評歷史缺失 (yf recommendations 回傳 summary), 只能以 WebSearch 片段拼湊近期事件, 日期多半不完整。
5. 日期紀律: 本報告以 2026-11-23 為基準, 但執行當下系統日期為 2026-11-22, 最新已知內部人交易為 2026-11-13, 其餘新聞與聚合站日期多為 2026-05 至 2026-10 之間。本報告未引用任何歷史 daily/ 報告的數字。

SENTIMENT REPORT COMPLETE
