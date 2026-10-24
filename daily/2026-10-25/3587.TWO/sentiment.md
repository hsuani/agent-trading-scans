# Sentiment — 3587.TWO (閎康科技 Materials Analysis Technology) as of 2026-10-25

**注意:** 本報告大部分來源失效,無法完成完整覆蓋。結論信心偏低。要求的 as-of 日期 2026-10-25 晚於今日 (2026-10-24),所有資料以抓取當下可得者為準。

## 資料來源狀態

| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary | 回傳空陣列,無評等歷史與買/持/賣分布 |
| yf insider | 回傳空陣列,無內部人交易資料 |
| yf major_holders | 有資料(見下方持股) |
| Reddit r/wallstreetbets、r/stocks | 代理層封鎖 (Claude Code 無法存取 reddit.com),無法取得貼文 |
| StockTwits | DNS 解析失敗 (api.stocktwits.com),無法取得 |
| 網路搜尋 (X / 新聞) | 僅找到一筆 Investing.com 日文頁面,無日期,數字可能過時 |

## Analyst consensus
唯一可用來源為 Investing.com 日文版 Materials Analysis Technology (3587) 頁面,該頁未標示更新日期,且 yf 工具未能驗證:
- 評等分布: 3 buy / 0 hold / 0 sell (共 3 位分析師)
- 12 個月平均目標價: 約 365.67 元,頁面示意上行空間約 48%(對照頁面股價約 246.50 元)
- 近期財報 (2026-05-19 公布): EPS 2.17,低於預估 2.22;營收約 14.2 億(NT$),高於預估 13.9 億
- 近期評等升降級與目標價變動: 無法取得歷史紀錄,無法判斷近期方向

## Retail social
- Reddit: 無法取得 (封鎖)。無法提供樣本貼文或語氣比例。
- StockTwits / X: StockTwits 無法連線;X 無可用搜尋結果。
- 討論量: 無法量化,無法與平常水準比較。
- 主題: 無資料可歸納。

## Insider activity
Net 6mo: 無資料 (yf insider 回傳空)。無法判斷 CEO/CFO 或其他內部人的買賣方向,不可解讀為中性或無交易。

## Ownership shifts
- 內部人持股比例: 約 28.1%
- 機構持股比例: 約 8.8%(流通股中約 12.2%),機構數 16 家
- 機構持股趨勢 (季度變化): 無資料,無法判斷集中度變化方向
- 註: 內部人持股高、機構持股低,流通股本相對少,這是結構特徵,不是情緒訊號。

## Net sentiment score
**Composite: 中性 (neutral),信心: 低。**
- 分析師面: 偏多(3 買、0 賣),但來源未標日期且無法核對,權重低。
- 散戶面: 無資料,無法評估。
- 內部人面: 無資料,無法評估。

**Divergence flag: 無法判定。** 缺少散戶語氣資料,無法比較散戶與分析師方向是否相反。

## 缺口與後續建議
1. 重新抓取 yf recommendations / rec_summary,確認分析師分布與日期。
2. 以台灣證交所 / 櫃買中心 (TPEx) 公告、券商研究報告核實目標價與評等。
3. Reddit 或 StockTwits 封鎖時,改用可用的替代來源(例如 PTT 股板、Threads 或中文財經論壇),並註明來源限制。
4. 補抓 insider 交易(公開資訊觀測站董監持股申報)以確認 6 個月淨買賣金額。

SENTIMENT REPORT COMPLETE
