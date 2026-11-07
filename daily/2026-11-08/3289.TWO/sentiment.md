# Sentiment — 3289.TWO (宜特) as of 2026-11-08

注意：本次資料嚴重不足。yf 的 recommendations、rec_summary、insider、inst_holders 全部回傳空值，Reddit 與 StockTwits 無法取得，WebSearch 也找不到 2026 年 10 月以後的散戶討論或券商評等。綜合評級只能視為「資料不足、信心低」，不可作為市場情緒判斷的依據。

## 來源狀態

| 來源 | 狀態 | 說明 |
|---|---|---|
| yf recommendations | 失敗 (空值) | Yahoo cookie/crumb 取得失敗，無歷史評等變動 |
| yf rec_summary | 失敗 (空值) | 同上，無 buy/hold/sell 分布 |
| yf insider | 失敗 (空值) | 無內部人交易資料 |
| yf inst_holders | 失敗 (空值) | 無機構持股明細 |
| yf major_holders | 部分成功 | 見「Ownership shifts」 |
| yf news | 失敗 | CONNECT tunnel 403 |
| Reddit r/wallstreetbets / r/stocks | 未取得 | 本次依指示以 WebSearch 代替，搜尋無 3289 相關貼文 |
| StockTwits | 未取得 | 本次依指示未直接連線，WebSearch 無相關資料 |
| WebSearch 中文社群 (PTT / Dcard / CMoney) | 無有效貼文 | 僅抓到 CMoney 股市討論區入口頁，無可計量的貼文內容 |
| WebSearch 券商評等 / 目標價 | 無 2026 年資料 | 僅找到非券商來源的估值快照 |

## 公司辨識

3289 為宜特科技 (Integrated Service Technology)，櫃買中心上櫃。WebSearch 結果中有一處英文頁面標示為 Waffer Technology Corp.，與其他來源衝突，本報告以宜特為準。

## Analyst consensus

0 buy / 0 hold / 0 sell（資料缺失，無法取得）。

Recent moves：無法確認。WebSearch 找到的券商相關頁面皆為舊資料或聚合站快照，未出現 2026 年的評等調升、調降或目標價變動，不能當作現行共識。

## Retail social

- Reddit：未取得。WebSearch 未找到 r/wallstreetbets 或 r/stocks 中與宜特相關的貼文。
- StockTwits / X：未取得。WebSearch 未找到 2026 年 10 月以後的 X 貼文或情緒摘要。
- PTT / Dcard / CMoney：WebSearch 僅回傳 CMoney 股市討論區與 Yahoo 股市新聞頁面的入口，無法統計聲量，也無法抽樣貼文。因此本節不提供散戶多空比例。
- 聲量 (qualitative)：無法判定相對於過去的高低。
- Themes（僅從媒體與聚合站摘要歸納，非散戶原文，信心低）：
  - 2 奈米製程材料驗證 (ALD 新材料、立體電晶體架構)，屬於成長敘事的主軸。
  - AI 高速運算、ASIC、HBM 硬體平台測試委案。
  - 矽光子 (CPO)，與光焱科技合作切入。
  - 估值偏高：StatementDog 快照顯示本益比約 29.7 倍，殖利率約 4.1%，日期不明。
  - 營收年減：2026 年 8 月營收約 3.71 億 TWD，年減約 7.9%；StatementDog 另列 9 月營收年增約 -21.5%。

## Insider activity

Net 6mo：無資料（yf insider 回傳空值）。

本次未能確認 CEO / CFO 或其他內部人近 6 個月的買賣申報。需要改查公開資訊觀測站的內部人持股申報後才能補足。

## Ownership shifts

yf major_holders 單一快照：
- 內部人持股約 17.55%
- 機構持股約 2.77%，佔流通股約 3.36%
- 機構家數約 8 家

解讀：流通股中機構比例偏低，內部人持股比例高。這是單點數據，無歷史趨勢可比，無法判斷機構是增持還是減持。

## 股價與事件（非情緒資料，供背景參考）

- 價格快照並不一致：2026/09/18 收 136.50 元；10/16 收 135.5 元（StatementDog）；另一頁面標示 147.5 元，日期不明。本報告未取得 2026-11-07 的收盤價。
- 除權息：10 月的 Win 投資預告為 11/05 除權、每股現金股利 1.6 元、11/27 發放。前一份 11/01 報告則記載 8 月除息後很快填息。兩者時點不一致，本報告未能確認實際除權息日，需以公開資訊觀測站為準。
- 財務：2025 年全年營收約 48.43 億 TWD，年增約 11.4%。稅後淨利的來源數字有出入（一處為 3.35 億 TWD，前一報告為 3.66 億 TWD），EPS 約 4.81 元，本報告未重新核對。
- 2026 年 2Q EPS 約 1.03 元，年減約 31%（WebSearch 聚合站）。
- 新聞風險：時報報導宜特在 2026 年 5 月 13 日澄清媒體報導，指特定員工疑涉採購弊案，目前由法務部調查局介入。此為負面事件，後續進展未查到。

## Net sentiment score

綜合判斷：中性偏弱 (neutral, low confidence)。

理由：
- 無分析師評等、無內部人申報、無散戶量化資料，無法形成可靠的雙方對照。
- 可用的正面訊號僅有 2nm 驗證、AI 與矽光子等成長敘事，來源為媒體與聚合站，不是散戶情緒樣本。
- 負面訊號包括 2026 年營收與 EPS 年減、8 月與 9 月營收年減、估值偏高，以及採購弊案的調查新聞。
- 整體偏中性，略偏保守，但信心低，不足以判定方向。

Divergence flag：無法判定。缺少分析師與散戶雙方資料，不能判斷兩者是否背離。

## 建議後續補足

1. 允許 Yahoo Finance 與 api.stocktwits.com、reddit.com 連線後重試 yf 與社群來源。
2. 以 MoneyDJ 或 Yahoo 股市「分析師評等」頁人工確認 2026 年最新目標價與評等。
3. 以公開資訊觀測站確認近 6 個月內部人申報、除權息實際日期，以及 5 月採購弊案調查的後續進展。
4. 在 CMoney 股市討論區或 PTT 股版人工抽樣近 30 天貼文，以補足散戶 tilt。

SENTIMENT REPORT COMPLETE
