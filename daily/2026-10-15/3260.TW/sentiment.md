# Sentiment — 3260.TW 威剛科技 (ADATA Technology) as of 2026-10-15

> 資料狀態: 大部分來源 DATA_UNAVAILABLE。本報告只能提供有限的基本面與舊的分析師資訊, 不足以判定 2026-10-15 當下的散戶情緒。信心度低。

## Analyst consensus
- 本次 `yf 3260.TW rec_summary` 與 `recommendations` 回傳空陣列 (Yahoo cookie/crumb 取得失敗, 連線遭 proxy 拒絕), 視為 DATA_UNAVAILABLE。
- 網路搜尋結果 (investing.com / Simply Wall St, 資料日期約 2026 年 3 至 4 月): 共識評等 "Buy", 僅 1 位分析師, 平均 12 個月目標價 455 TWD。此資料已過時, 且樣本僅 1 家, 不具代表性。
- 近期評等升降級 (upgrade / downgrade) 與目標價調整: DATA_UNAVAILABLE。
- 目前 buy / hold / sell 分布: DATA_UNAVAILABLE (無法取得 2026-10 的數字)。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE。WebFetch 回應 "unable to fetch from www.reddit.com", 無法取樣討論串或計算提及量。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com 無法解析 (DNS 失敗), 無法取得 bullish / bearish 標籤。
- PTT (Stock 版): DATA_UNAVAILABLE。www.ptt.cc 連線遭 egress proxy 拒絕, 搜尋結果也找不到 PTT 上的 3260 討論串。
- CMoney 股市爆料同學會 / X 與新聞輿情: DATA_UNAVAILABLE (cmoney.tw 連線遭拒絕)。一般網路搜尋只找到零散的新聞摘要與股價頁, 沒有可計量的散戶語氣樣本。
- 提及量 (buzz volume) 相對平常水準: 無法判定。
- 散戶 tilt: 無法判定。
- 主要主題 (themes): 無可靠樣本。搜尋結果中有少數與產業背景相關的敘述, 不能當作散戶情緒。以下為間接資訊, 非散戶貼文:
  - 記憶體缺貨與報價上漲推升獲利, 威剛董事長表示供需缺口可能延續一整年 (來源為新聞摘要, 日期約 2026 年初)。
  - 外資曾提示 DDR4 需求可能在 2026 年下半年轉弱, 記憶體股曾因此下跌 (日期不明, 屬於警示性敘述)。
  - 有一則未標日期的新聞指稱威剛與創見單日跌幅超過 5%, 同一搜尋結果另提到法人在前五日買超逾 1,000 張。兩則日期皆無法確認。

## Insider activity
Net 6mo: DATA_UNAVAILABLE。`yf 3260.TW insider` 回傳空陣列, 無法計算淨買賣金額, 也無法辨識 CEO / CFO 等人的交易。

## Ownership shifts
- `yf 3260.TW major_holders` 回傳空陣列, 持股集中度與機構持股變化: DATA_UNAVAILABLE。

## Background (非情緒資料, 僅供參考)
以下數字來自 nStock 摘要 (搜尋結果, 日期約 2026 年 9 月中), 尚未交叉驗證:
- 2026 年 8 月營收約 189.25 億元, 年增約 280%, 為單月歷史新高。
- 2026 年 Q2 EPS 32.39 元, 毛利率約 42%。
- 股價約 402.5 元, 近一週均價約 410 元, 近一年均價約 323.8 元。
- 2026 年 Q2 現金股利 18.01 元, 除息日 2026-09-21, 現金殖利率約 4.5%。
- 2026-08-03 盤中價約 393.5 元 (MONEY LINK 頁面)。
- 不同來源的股價與日期互相不一致, 使用前應以交易所或券商報價為準。

## Net sentiment score
- Composite: **neutral (信心度低)**。
  - 分析師面: 唯一可得資料為 1 位分析師的 Buy 評等, 但日期約為 2026 年 3 至 4 月, 已過時, 不足以代表 10 月的共識。
  - 散戶面: 無資料。
  - 內部人面: 無資料。
  - 基本面背景正向 (營收與 EPS 年增幅度大), 但股價與產業景氣循環相關, 且有 DDR4 需求轉弱的警示, 方向不明。
- Divergence flag: **無法判定**。散戶資料全部缺失, 不能比較散戶與分析師的傾向。

## 資料缺口與後續建議
1. Yahoo Finance (query2.finance.yahoo.com) 遭 proxy 拒絕, 需由 pipeline 維護者確認該主機是否允許於本 session 使用, 才能重跑 `yf` 的 rec_summary / recommendations / insider / major_holders。
2. Reddit、StockTwits、PTT、CMoney 均無法存取。若要取得散戶情緒, 需開放對應網域, 或改用其他已授權的資料來源。
3. 建議重新執行本任務, 以取得 2026-10-15 當日的分析師與內部人資料。

SENTIMENT REPORT COMPLETE
