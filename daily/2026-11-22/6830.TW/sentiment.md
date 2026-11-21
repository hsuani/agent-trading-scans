# Sentiment — 6830.TW (汎銓科技) as of 2026-11-22

資料時點說明: 2026-11-22 之後的資料一律視為未知。Reddit 與 StockTwits 本次無法取得 (見下方資料缺口)。

## Analyst consensus
Yahoo 來源僅有 1 家覆蓋機構 (strongBuy 1 / buy 0 / hold 0 / sell 0 / strongSell 0)。覆蓋家數極少, 不足以判斷市場共識。近期評等升降級與目標價異動: 未取得資料。

## Retail social
- Reddit: 無法取得 (r/stocks 與 r/wallstreetbets 搜尋皆被擋, 回傳 "unable to fetch")。
- StockTwits: 無法取得 (api.stocktwits.com 無法解析, 需於 session 網路設定允許該網域後再試)。
- PTT / Dcard / X: 以 WebSearch 查詢, 結果皆為新聞與分析文章, 未找到 PTT Stock 版或其他社群的具體討論串, 無法量測討論量與多空比例。
- 新聞端語氣 (作為代理指標, 非社群原始資料): 偏多敘述為主, 圍繞「矽光子 (Silicon Photonics) / CPO」題材; 同時有多篇報導提醒估值與出貨時程風險。
  - 偏多引述: 「董事長對 2027 年抱持樂觀看法, 獲利有機會較今年數倍成長」 (依新聞轉述)。
  - 保留引述: 「實機展示不等於已取得正式訂單」 (分析文章提醒語)。
- 討論量 (相對常態): 無法量化。
- Themes:
  1. 矽光子量測設備 MSS HG: 2026-11-05 實機發表, 公司表示 2026 年底有望交付三台, 最晚延至 2027 年第一季。
  2. CPO 良率與 Debug 平台題材, 與安立知、旺矽、FormFactor 合作。
  3. 股價波動: 曾衝上約 850 元, 之後明顯回檔, 距高點仍逾三成 (新聞時點)。
  4. 基本面: 2026 年上半年仍為稅後淨損; 2027 年才是放量預期年。
  5. 籌資: 現金增資, 每股 500 元, 募資 30 億元。

## Insider activity
Net 6mo: 資料為空 (yf insider 回傳空陣列)。這可能代表該期間無申報, 也可能是台股內部人申報未被 Yahoo 收錄, 不應直接解讀為「無內部人交易」。台灣內部人持股申報需以公開資訊觀測站為準, 本次未查核。
Notable: 無可引用項目。
Ownership: insidersPercentHeld 約 21.2%; institutionsPercentHeld 約 9.3%; institutionsFloatPercentHeld 約 11.8%; institutionsCount 10。機構持股比例偏低, 歷史趨勢資料未取得, 無法判斷近期集中度變化方向。

## Net sentiment score
Composite: 中性偏多 (信心: 低)。
依據: 分析師端只有 1 家且為 strongBuy, 樣本太少; 社群端無可用原始資料, 僅能以新聞敘述代理; 新聞敘述偏多 (矽光子題材、營收創高), 但同時出現股價大幅回檔、2026 年仍為淨損、出貨量未放大等保留訊號。

Divergence flag: 無法判定。分析師端樣本不足, 社群端無原始資料, 無法確認零售與分析師傾向是否相反。

## 資料缺口與可信度
- Reddit (r/stocks, r/wallstreetbets): 被擋, 未取得。
- StockTwits: DNS 解析失敗, 未取得。
- Yahoo cookie/crumb 取得失敗, 部分 yf 輸出可能不完整 (recommendations 與 rec_summary 僅回 1 家覆蓋機構)。
- 未取得任何台股價格與市值資料, 本報告未引用市值數字。
- 新聞來源數字 (營收、募資) 以新聞所載單位「億元」呈現, 未另行換算。

## 主要參考 (WebSearch 摘要)
- 汎銓 MSS HG 發表與出貨時程 (2026-11 相關報導)
- 汎銓 2026 年 9 月與第三季營收創高: 單月 2.65 億元; 第三季 7.59 億元 (季增 19.56%, 年增 31.63%)
- 2025 年全年合併營收 21.79 億元 (年增 10.78%), 全年稅後淨損 3,667 萬元
- 2026 年前 5 月營收累計 10.08 億元 (年增 22.49%)

SENTIMENT REPORT COMPLETE
