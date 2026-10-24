# Sentiment — POET as of 2026-10-25

**資料完整度:** 分析師評等資料缺失；Reddit 與 StockTwits 無法存取；零售情緒僅能由次級搜尋摘要推估。整體信心偏低。

## Analyst consensus
- 資料缺失: `yf POET rec_summary` 與 `yf POET recommendations` 皆回傳 period 0m 且各評等數全為 0。Yahoo 來源因 cookie/crumb 連線失敗（fc.yahoo.com 被代理拒絕），此為資料不可得，不代表無分析師覆蓋。
- 第三方次級來源（Tradestie，搜尋摘要，更新於 2026-10-15）: 平均目標價 $14.75，評等 "WAIT" 低信心；當時股價 $5.43，5 日約跌 22%，30 日約跌 28%，技術面為強勢下跌。此來源未提供分布，僅可作參考。
- Stockscan 預估 2027 目標價約 $6.37，但基於較早股價，時效性不足，權重低。
- 近期評等調整（upgrade/downgrade、目標價變動）: 無法取得。

## Retail social
- Reddit (r/wallstreetbets、r/stocks): 無法存取。代理回報 CONNECT 403（政策拒絕），依規則軟失敗，未嘗試繞過。無討論串可引用，無法判定 tilt。
- StockTwits: 無法存取。`api.stocktwits.com` 同樣被代理以 403 拒絕，軟失敗。
- X / 新聞: 僅有一則搜尋摘要（Seeking Alpha 一篇文章，發表日期不明）描述情緒「由興奮轉為失望，再度興奮後又因回檔進入新一波失望」。此為單一作者觀點，權重低。
- 聲量（buzz volume）: 無法量化，無法與常態比較。
- Tilt: 無法判定。唯一可得訊號偏空（股價大幅回檔後的失望情緒）。
- 主要主題: 無足夠樣本可歸納。搜尋摘要提及的 Lumilens 進展（SA 文章標題）與股價回檔為可見議題，但未經 Reddit 或 StockTwits 佐證。
- 代表性引述: 無可引用之原始貼文。

## Insider activity
統計區間: 2026-04-25 至 2026-10-25（6 個月）。單位: USD M。

| 項目 | 金額 (USD M) | 備註 |
|---|---|---|
| 公開市場買入 | 0.00 | 區間內無任何 open-market 買入 |
| 公開市場賣出（已計價） | 5.10 | 共 18 筆，皆 Disposition in the public market |
| 選擇權行使（已計價，非買入） | 約 0.40 | 多數隨後同日賣出（exercise-and-sell） |
| 淨額（買入 − 賣出） | **約 −5.10** | 不含選擇權行使 |

按人員彙總賣出（USD M，依 Yahoo 欄位，職稱為該來源之泛稱，未能確認 CEO/CFO）:
- Barnes (Kevin), Senior Officer: 約 1.94（2026-05-20 大額賣出 1.23；06-05 0.57；08-10 0.13）
- Jinyu (Mo), Senior Officer: 約 1.09（06-05 0.65；06-03 0.44）
- James (Lee), Director or Senior Officer: 約 1.07（06-01 至 06-12 多筆）
- Mika (Thomas R), Senior Officer: 約 0.41（08-07）
- Kankipati (Venkata Rama Raju), Senior Officer: 約 0.29（06-16、08-07）
- Riley (Glen), Director: 約 0.15（06-30、08-19）
- Khan (Sohail A), Director: 約 0.06（07-08）
- Ende (Theresa Lan), Director: 約 0.05（06-30）
- Tirva (Robert Linas), Director: 約 0.04（06-30）

值得注意:
- 2026-05-20 至 06-05 密集賣出，Barnes 與 Jinyu 單筆賣出股價約 $10.8–$14.7，為區間內金額最大的事件。
- 2026-08-07 出現 Mika、Kankipati、Venkatesan 等多人同日大量「無價格」Form 4 紀錄（Venkatesan 合計 539,077 股，Mika 123,001 股，Barnes 30,750 股等）。性質不明（可能為歸屬、授予或稅款扣繳），未計入金額，需人工核對 SEC Form 4。
- 2026-06-30 與 08-19 之部分董事紀錄同樣無價格，性質同上。
- 交易價格趨勢: 6 月約 $14.2–14.7，8 月約 $8.9–9.5，與第三方所示 10 月中約 $5.43 一致，股價區間跌幅約 63%。內部人於高位與回落途中持續賣出，無買入紀錄。
- 2025-10-25 之 James 紀錄超出區間，已排除。

## Ownership shifts
- 機構持股: 20.3%（institutionsPercentHeld 0.20335），機構數 185。
- 內部人持股: 約 0.07%（insidersPercentHeld 0.00068）。
- 趨勢: 僅有單一時點快照，無歷史比較，無法判定增減。

## Net sentiment score
- **內部人訊號**: 偏空。6 個月內零公開市場買入、約 $5.1M 公開市場賣出，且賣出跨越多名高階人員與董事，信心中等。部分賣出可能與選擇權行使後的例行變現有關，故非純粹看空訊號。
- **分析師訊號**: 無法判定。Yahoo 來源缺資料；第三方目標價 $14.75 遠高於股價，但來源不可靠，且無分布。
- **零售訊號**: 無法判定。Reddit 與 StockTwits 皆不可達，僅一則弱證據偏空。
- **綜合評分: 偏空（neutral-to-bearish 傾向）；信心: 低。**

**分歧旗標 (Divergence flag): 無法判定（否）。** 因分析師與零售端皆缺資料，無法確認二者方向是否相反。

## 資料來源與缺口
- 成功: `yf POET insider`、`yf POET major_holders`（部分成功，回傳資料）
- 失敗（資料缺失）: `yf POET rec_summary`、`yf POET recommendations`（Yahoo cookie/crumb 失敗，回傳全零）
- 失敗（代理拒絕）: Reddit r/wallstreetbets、r/stocks（CONNECT 403）；StockTwits（403）
- 次級: WebSearch 摘要（Tradestie、Stockscan、Seeking Alpha），時效不一，權重低
- 下次財報日: 搜尋摘要稱為 2026-11-12，未經官方來源核實

SENTIMENT REPORT COMPLETE
