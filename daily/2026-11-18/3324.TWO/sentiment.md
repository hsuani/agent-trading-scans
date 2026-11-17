# Sentiment — 3324.TWO (雙鴻 Auras Technology) as of 2026-11-18

資料狀態總覽: 分析師評等 (yf rec_summary) 可用; 個別升降評事件 (yf recommendations) 與內部人交易 (yf insider) 無有效資料; Reddit 與 StockTwits 無法取得; 網路搜尋可取得部分新聞型目標價但未能二次驗證。

## Analyst consensus

共 17 位分析師: 13 buy (含 strongBuy 4 / buy 9) / 4 hold / 0 sell。最近 4 個月 (0m 至 -3m) 買方家數持平在 13, hold 維持 4, sell 維持 0; 僅 strongBuy 由 3 增至 4 (-3m → 0m)。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m (本期) | 4 | 9 | 4 | 0 | 0 |
| -1m | 4 | 9 | 4 | 0 | 0 |
| -2m | 4 | 9 | 4 | 0 | 0 |
| -3m | 3 | 9 | 4 | 0 | 0 |

- 個別升降評事件: DATA_UNAVAILABLE。yf recommendations 回傳內容與 rec_summary 相同的彙總結構, 沒有券商別的升降評紀錄, 無法列出 upgrade/downgrade 明細。
- 目標價 (網路搜尋彙整, 未經原始報告驗證): 美系外資與花旗於 2026-09 將目標價由 1,550 元上調至 1,800 元, 維持「買進」; 日系外資於 2026-07 維持「買進」, 目標價 1,640 元; 本土投顧凱基與第一金目標價分別為 1,950 元與 1,880 元 (2027 EPS 預估分別為 99.35 元與 94 元)。搜尋結果中也夾雜 2025 年的 1,000 元、1,200 元舊目標價, 已不代表目前觀點, 不納入計算。
- 股價參照 (同一搜尋來源, 報導日 2026-11-11): 收盤 1,235 元, 盤中 1,295 元。來源描述的單日漲跌幅前後不一致 (4.86% 與 7.39%), 此處僅作區間參考。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE。WebFetch 回傳 "unable to fetch from www.reddit.com", 本次無法取得貼文數、分數與多空傾向。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com 解析失敗 (ENOTFOUND), 本 session 網路白名單未包含該網域, 需由使用者於 session 設定開放後才能重試。
- X / 新聞與論壇 (WebSearch): 未找到 2026-11 的散戶留言或社群討論。可得內容以財經新聞與券商評等為主, 屬機構與媒體觀點, 不能當作散戶情緒。
- 聲量 (buzz volume) 相對基準: DATA_UNAVAILABLE, 無可靠計數。
- 主題 (僅依新聞標題歸納, 非社群原文): (1) 水冷 (液冷) 散熱營收占比提升, 中信投顧預估 2027 年水冷營收占比 70% 至 75%; (2) 2026-10 營收 33.72 億元, 年增 44.75%, 部分專案出貨遞延至 11 月; (3) 2026-09 上修目標價的券商調整, 強化多方敘事。
- 散戶傾向: DATA_UNAVAILABLE (無可靠樣本, 不做多空判斷)。

## Insider activity

Net 6mo: DATA_UNAVAILABLE。yf insider 回傳空清單 []; 無法區分「期間內無申報」與「資料來源暫時缺漏」, 因此不以零計算。Cookie/crumb 取得失敗 (fc.yahoo.com ConnectionError), 其他欄位仍正常回傳, 故此項應視為待確認。Notable: 無。

## Ownership shifts

單一快照 (yf major_holders, 無時間序列, 無法判斷趨勢):
- 內部人持股 28.92%
- 機構持股 (占總股本) 11.61%; 機構占流通股 16.33%
- 機構家數 56
- 集中度趨勢: DATA_UNAVAILABLE (只有單期, 無法比較前期)。內部人持股比例高, 流通股比例相對有限, 對波動放大效果值得留意, 但這只是結構描述, 不構成方向判斷。

## Net sentiment score

- 分析師面: 偏多 (信心: 中高)。13/17 為買方評等, 0 家賣出, 近四個月評等結構穩定。
- 散戶面: 無法判定 (信心: 無)。Reddit、StockTwits 皆不可用, 網路搜尋未取得 2026-11 社群樣本。
- 內部人面: 無法判定 (DATA_UNAVAILABLE)。
- Composite: 偏多 (信心: 低到中)。綜合結論僅反映分析師面, 散戶與內部人面缺口大, 不應視為完整的情緒判讀。

Divergence flag: 無法判定 (no)。散戶樣本缺失, 無法確認散戶傾向是否與分析師傾向相反。

資料缺口清單 (供下游參考):
1. Reddit 讀取被拒 (fetch 失敗)
2. StockTwits 網域未在 session 白名單內
3. yf recommendations 無個別券商升降評紀錄
4. yf insider 回傳空清單, 需人工或其他來源確認
5. 網路搜尋的目標價數據未經原始報告驗證, 且部分日期與漲跌幅前後矛盾

SENTIMENT REPORT COMPLETE
