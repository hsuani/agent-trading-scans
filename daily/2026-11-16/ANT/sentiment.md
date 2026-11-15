# Sentiment — ANT as of 2026-11-16

**狀態: 資料不足, 低信心. ANT 目前尚未上市交易.** 以下各區塊的結論主要是「無資料」, 不是「中性」.

## 重要前提: ANT 為待上市代號
- ANT 是 Anthropic 規劃中的 Nasdaq Class A 股票代號 (Nasdaq Global Select Market), 不是 Ant Group, 也不是 ANTA / ANTE.
- 依 2026-11-10 修訂版 S-1 與媒體報導 (CNBC 援引知情人士): 定價預計 2026-11-18, 2026-11-19 開始 Nasdaq 交易. 價格區間約 $70–$78/股, 發行約 825M Class A 股 (其中 801M 為新股, 約 24M 為既有股東出售). 另有 $26.0B Class N 私募配售.
- 日期與價格仍可能變動, 尚未定價. 本報告以 2026-11-16 為基準, 此時點仍無交易價格.
- 參考來源: thenextweb.com (Anthropic's IPO seeks up to $64.4B at a $1.4 trillion valuation), letsdatascience.com (Anthropic Sets IPO Range and Adds $26 Billion Private Placement), letsdatascience.com (Anthropic files for Nasdaq IPO under ticker ANT), bitmex.com/blog (Anthropic IPO Date, Price, and Valuation)

## 資料來源可用性
| 來源 | 狀態 | 說明 |
|---|---|---|
| yf recommendations / rec_summary | 不可用 | `pipeline/tools/yf` 四項查詢皆回傳空陣列, Yahoo cookie/crumb 取得失敗. 代理日誌顯示 query2.finance.yahoo.com 遭 403 政策拒絕 (CONNECT). 未嘗試繞過. |
| yf insider | 不可用 | 同上. 且 ANT 尚未為上市公司, 理論上無 Form 4 內部人交易. |
| yf major_holders | 不可用 | 同上. 尚無公開持股資料. |
| Reddit r/wallstreetbets, r/stocks | 不可用 | WebFetch 回報無法連線 www.reddit.com. 未重試. |
| StockTwits API | 不可用 | api.stocktwits.com 與 stocktwits.com DNS 解析失敗 (網路未允許). 未重試. 需於 session 網路設定允許後才能再查. |
| WebSearch | 可用 | 僅得到二手摘要與新聞, 見下文. |

## Analyst consensus
0 buy / 0 hold / 0 sell. 目前無可查證的分析師評等, 目標價或評等變動 (WebSearch 未找到 ANT 之券商評等). 上市前尚無 sell-side 覆蓋. 此區塊無法計算共識, 不應解讀為「分析師中性」.

## Retail social
- Reddit: 不可用 (連線遭拒, 未取得樣本貼文).
- StockTwits / X: StockTwits 直連不可用. 搜尋摘要引用一則 2026-11-11 StockTwits 新聞, 稱 ANT 零售情緒在前一日由 bearish 轉為 bullish, 討論量由 low 升至 extremely high. 此為二手摘要, 未能直接核對原始訊息與樣本數, 且樣本僅一個時點.
- 聲量 (相對基準): 無可量化的 mention 計數. 摘要所述「extremely high」為定性描述, 相對 Anthropic IPO 話題熱度而非 ANT 交易代號本身.
- Themes (依可得新聞標題歸納): Anthropic IPO 被視為 AI 族群走勢的定調事件; 估值 (約 $1.4T 量級) 與私募配售規模受關注; 上市時程與定價變動風險.
- Tilt: 零售整體偏多 (低信心, 單一來源, 時點為 11-11).

## Insider activity
Net 6mo: 無資料 (yf insider 不可用; 且 ANT 於評估時點尚未上市, 不適用 6 個月內部人交易統計). 無可引用的 CEO/CFO 交易紀錄. 此區塊不得視為內部人中性.

## Ownership shifts
無資料. yf major_holders 不可用; 上市前無 13F 或持股變化數據. 私募配售 (Class N, $26.0B) 的投資人結構尚未公開, 無法評估集中度.

## Net sentiment score
Composite: **neutral (資料不足, 信心低)**.
- 唯一可用訊號為單一時點的零售偏多 (二手來源), 分析師與內部人面皆無資料, 因此不能形成可靠的綜合偏向.
- 不得將「neutral」解讀為正面或負面建議. 本報告不含交易建議.

Divergence flag: **no** (無分析師評等可比較, 無法判定零售與分析師是否背離).

## 後續待辦
1. 定價後 (2026-11-18 起) 重新確認 ANT 是否開始交易, 並重跑 yf recommendations / rec_summary / insider / major_holders.
2. 於 session 網路設定允許 www.reddit.com, api.stocktwits.com, stocktwits.com 後再補零售情緒樣本.
3. 上市後 30 日內可望出現首批分析師覆蓋與 Form 4 內部人交易, 屆時更新本報告.

## Process notes
- 本次未引用任何過去 daily/<date>/ 報告的數字.

SENTIMENT REPORT COMPLETE
