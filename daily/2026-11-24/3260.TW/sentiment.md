# Sentiment — 3260.TW (威剛) as of 2026-11-24

**注意：本次資料大幅不足，多數區塊無法取得，結論信心低。**

## 資料來源狀態

| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary / insider / major_holders | 全部回傳空清單，Yahoo cookie/crumb 取得失敗（ConnectionError），無法使用 |
| Reddit r/wallstreetbets、r/stocks | 無法連線（WebFetch 被拒），未取得任何貼文 |
| StockTwits | DNS 解析失敗（api.stocktwits.com 不在允許網域內），未取得資料 |
| WebSearch（新聞與券商報導） | 可用，作為唯一資料來源，多為二手報導 |

## Analyst consensus

Buy / Hold / Sell 分布：**無法取得**（yf rec_summary 空白）。

已知的個別券商動作（來自新聞搜尋，非完整統計）：
- 玉山投顧：維持「增持」，目標價 420 元，認為毛利率回落至約 28.64%（來源為近期新聞，發布日期未在搜尋結果中確認）。
- 2025-11：一家投顧將評等由 BUY 降為 Trading BUY，目標價由 297.5 元下調至 200 元，理由為記憶體短線漲價趨緩（屬一年前資料，已過時）。
- 2026-01：一家美系外資預估 2026 年 NAND 混合 ASP 全年成長約 40%，認為威剛低價庫存會轉為跌價回升利益（觀點偏多，非評等變動）。
- 華南投顧看好威剛在貨源與庫存上的優勢（無目標價細節）。

目標價變動：近期僅能確認玉山 420 元一筆。另有一個估值網站顯示分析師平均目標價 455 元，但其股價與日期與其他來源不一致，可信度低，不採用。

## Retail social

- Reddit：無法取得（r/wallstreetbets、r/stocks 皆連線失敗），無樣本、無傾向判斷。
- StockTwits：無法取得（DNS 失敗），需於 session 網路設定允許 api.stocktwits.com 後才能補抓。
- PTT / X：搜尋未找到論壇討論串，結果幾乎全為新聞媒體報導。X 未能查到相關貼文。
- 聲量（buzz volume）：無法量化，無法與常態比較。
- 傾向：無法判斷。
- 主要主題（來自新聞而非散戶，僅供參考）：
  - 記憶體缺貨 / 超級週期：董事長陳立白表示 DRAM 缺貨到 2027 年且更嚴重，NAND 下半年缺口比 DRAM 更大。
  - 毛利率承壓：第三季毛利率 35.88% 被法人認為低於預期，推估成本上升壓縮毛利。
  - Q4 營收季減：11/6 法說表示第四季受年底客戶庫存結算影響，營收將較第三季略降。
  - 庫存優勢：在手庫存突破 400 億元，被視為低價庫存的利益來源。

## Insider activity

Net 6mo：**無法取得**（yf insider 空白；WebSearch 未找到 2026 年董監持股申報的個股資料）。
建議直接查詢公開資訊觀測站（mops.twse.com.tw）的「董事、監察人持股變動」與「內部人股權申報」。

## Ownership shifts

major_holders 無資料，機構持股趨勢無法判斷。

## Fundamental context（判讀用，非情緒來源）

以下數字已依序驗證：
- 2026 年 10 月營收 170.63 億 TWD，月增 8.5%，年增 282.3%。
- 2026 年 1-10 月累計營收 1,343.69 億 TWD，年增 222.7%。
- 2026 年第二季稅後淨利 107.7 億 TWD，EPS 32.39 元。以此反推股數：107.7 億 ÷ 32.39 元 ≈ 3.33 億股，與威剛約 33 億 TWD 股本（面額 10 元）相符，單位換算正確。
- 2025 全年 EPS 23.18 元（來源報導）。2026 前三季 EPS 報導為 101.47 元，此數字未經完整驗證，僅列為來源宣稱值。
- 2026 年 10/30 收盤 346.5 元，當日下跌 4.28%（來源：新聞）。

## Net sentiment score

- **Composite：neutral（信心：低）**
  - 理由：基本面與產業敘事偏多（記憶體缺貨、營收年增超過 200%、玉山維持增持），但第四季營收季減與毛利率下滑的疑慮存在，且可用的情緒資料僅來自新聞與券商，缺少散戶與內部人數據。
- **Divergence flag：無法判定**。缺少散戶傾向與 rec_summary 完整統計，無法比較散戶與分析師方向是否相反。

## 後續補抓建議
1. 網路設定允許 api.stocktwits.com 後，重試 StockTwits。
2. 修復 Yahoo cookie/crumb 連線（fc.yahoo.com）後，重跑 yf recommendations、rec_summary、insider、major_holders。
3. Reddit 需能連線 reddit.com 的 JSON 端點，目前被擋。
4. 由 mops.twse.com.tw 手動確認董監持股申報。

SENTIMENT REPORT COMPLETE
