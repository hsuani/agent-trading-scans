# Sentiment — 8021.TW（尖點科技 Topoint Technology）as of 2026-10-26

資料時點說明：yf 快取的報價快照時間約為 2026-10-23 收盤前後（收盤參考價 479 TWD，前收 506 TWD，單日跌幅約 -5.3%），非 10-26 當日資料。10-26 之後的事件（例如現增繳款截止 10-30）一律視為未知或僅為排程。

## Analyst consensus
- 分析師家數、買進／持有／賣出分布：**DATA_UNAVAILABLE**（`rec_summary` 與 `recommendations` 皆為空，全部計數為 0，代表無資料而非真的沒有評等）。
- 目標價（平均／最高／最低／中位數）：**DATA_UNAVAILABLE**（yf 欄位皆為 None，`numberOfAnalystOpinions` 無值，`recommendationKey` = none）。
- 唯一可見的法人觀點來自新聞轉述：7 月下旬一份法人報告維持「買進」，目標價 600 TWD（券商名稱未在來源中揭露，且日期為 7 月，非近期）。此為二手轉述，未經 yf 驗證，權重低。
- 近期評等變化：無可得資料，**DATA_UNAVAILABLE**。
- 新聞報導指出，法人態度近期轉趨保守，原因是鎢粉現貨價格自 2026 年第一季高點回落約五成，市場擔心鑽針漲價動能放緩；報導同時認為公司議價與成本轉嫁能力較強，中長期成長趨勢不變。

## Institutional / insider flow
- 機構持股比例：約 20.7%（`major_holders` 顯示 institutionsPercentHeld 0.20727，機構家數 29）。
- 機構持股變化趨勢（季度對比）：**DATA_UNAVAILABLE**（`inst_holders` 回傳空清單，無法比較前後期）。
- 內部人持股比例：約 10.1%（insidersPercentHeld 0.10132）。
- 內部人交易（近 6 個月淨買賣金額）：**DATA_UNAVAILABLE**（`insider` 回傳空清單；這不等於「無交易」，只能確認工具未取得資料）。
- 三大法人買賣方向：網路搜尋摘要提到外資近期連續賣超、投信連續買超，但該數據來自 8 月的 Yahoo 股市頁面，已過時，僅供參考，無法代表 10 月方向。
- 管理層薪酬（yf 所列，FY2025）：President & Director Ruo-Ping Lin 總薪酬約 885.8 萬 TWD（約 0.09 億 TWD）。薪酬資料不構成交易情緒訊號。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：**DATA_UNAVAILABLE**。依任務規定，沒有直接抓取 Reddit；本次未驗證 Reddit 覆蓋程度。
- StockTwits：**DATA_UNAVAILABLE**（未使用，該平台對此標的覆蓋極少）。
- PTT 股票板、Dcard 理財版、股吧：網路搜尋未找到 10 月份的討論串內容，**DATA_UNAVAILABLE**。
- 散戶討論量（相對常態）：無法量化，**DATA_UNAVAILABLE**。
- 散戶語氣：**無法判定**。新聞與財經網站的報導語氣偏正面（營收創高、獲利大增），但這是媒體立場，不是散戶討論。
- 主要話題（由新聞代理，非散戶貼文）：
  - 營收創高：9 月營收約 8.3 億 TWD，年增約 98%；第三季營收約 23.31 億 TWD；1 至 9 月累計營收已超過 2025 全年。
  - 獲利大增：上半年稅後純益約 4.7 億 TWD，每股純益 3.25 元，第二季毛利率約 41.8%。
  - 籌資案：現金增資約 15.52 億 TWD（每股 388 TWD，原股東與特定人認購，繳款截止 10-30），另發行 4.8 億 TWD 無擔保可轉債（轉換價 528 TWD）。
  - 產能擴充：鑽針月產能預計年底達 4,500 萬支，2027 規劃 7,000 萬支。
  - 估值爭議：trailing P/E 約 97 倍，forward P/E 約 25.7 倍（yf）；股價自 52 週高點 627 TWD 回落至約 479 TWD。
- 代表性引述（新聞）：「中長期成長趨勢不變，維持「買進」評等」（法人報告轉述，非散戶）。

## 數據一致性檢核
- 市值：479 TWD × 148.3M 股 ≈ 710.3 億 TWD（yf marketCap 710.35 億 TWD，吻合）。
- 非稀釋市值 468.5 億 TWD，隱含股數約 97.8M，與上述不一致，推測與現增前後的股本定義有關，本報告以 148.3M 股為準。
- 每股純益與淨利：上半年純益 4.7 億 TWD ÷ EPS 3.25 ≈ 1.45 億股，與 148.3M 股大致吻合。
- 收盤價來源衝突：網路資料中 9-29 收盤約 480、10-06 收盤約 580、10-19 收盤約 520，三者與 yf 快照（10-23 附近 479）時序不一致，未採用任何單點價格作為結論依據。

## Net sentiment score
- 綜合判斷：**中性（信心：低）**
- 理由：
  - 基本面與營運面新聞偏多（營收、獲利、產能），但這些多為財報與媒體報導，不是市場情緒指標。
  - 唯一法人評等為 7 月的「買進」二手轉述，且附帶「態度轉保守」描述，近期評等資料缺失。
  - 內部人與機構流向資料缺失或過時，無法確認方向。
  - 散戶社群聲量與語氣完全無法取得。
- 背離旗標（retail vs analyst）：**無法判定**。因缺少近期分析師評等與散戶資料，無法判斷是否背離。
- 覆蓋度提醒：此標的分析師覆蓋極少，評級類訊號本身稀薄；本報告不提供交易建議。

## 資料缺口清單
| 項目 | 狀態 |
|---|---|
| 分析師評等分布 | DATA_UNAVAILABLE |
| 目標價 | DATA_UNAVAILABLE（僅有 7 月新聞轉述 600 TWD） |
| 內部人交易 6 個月 | DATA_UNAVAILABLE |
| 機構持股趨勢 | DATA_UNAVAILABLE |
| Reddit / StockTwits / PTT / Dcard | DATA_UNAVAILABLE |
| 散戶討論量 | DATA_UNAVAILABLE |

## 來源
- 新聞（營收、現增、法人觀點）：搜尋結果中 udn、uanalyze、ltn、ctee、cnyes 等財經媒體的 2026 年報導（轉述自公司公告與法人報告）。
- yf 快照：`pipeline/tools/yf.py 8021.TW` 之 info、major_holders、rec_summary、recommendations、inst_holders、insider（快取回退，實際抓取受限）。

SENTIMENT REPORT COMPLETE
