# Sentiment — 3260.TW 威剛科技 as of 2026-11-28

## 資料可得性

- `pipeline/tools/yf 3260.TW` 的 rec_summary、recommendations、insider、major_holders 四項即時查詢皆回傳空陣列 (Yahoo cookie/crumb 連線失敗)。
- 回退快取 `prices/yf/3260.TW.json` 所有欄位皆為空 (`recommendations`、`rec_summary`、`insider`、`major_holders`、`inst_holders` 均為 `[]`，`_misses` 為空)。快取更新時間為 2026-11-28T03:33 UTC，內容為空，不是過期資料，因此未以舊報告回填。
- Reddit、StockTwits 依指示略過。PTT 股板、Dcard 本次 WebSearch 未找到相關討論串。

## Analyst consensus

- **買賣持有分布: DATA_UNAVAILABLE** (yf 快取與即時皆無 rec_summary)。
- Investing.com 共識頁顯示 "Buy"，但僅依據 1 位分析師，且該頁的目標價為 455 TWD (單一來源，日期不明)。
- 近期個別券商動向 (來源為 WebSearch 媒體報導):
  - 2026-05: 一家投顧給予買進，目標價 556 元，以今年 EPS 與 4 倍本淨比推算。這是本次搜尋中最新的目標價。
  - 2026-04: 一家美系外資預估今年 NAND 混合平均售價年增 40%，認為威剛持有的低價庫存可轉為跌價回升與毛利擴張。未提供明確目標價。
  - 玉山: 增持，目標價 420 元，認為毛利率向上空間有限。
  - 國票等機構: 下修明年獲利預估 (未列出具體數字)。
  - 2025-11: 一家法人由 BUY 降為 Trading BUY，目標價由 297.5 元降至 200 元 (舊事件，僅供背景參考)。
- 目標價離散度極大 (200 元至 556 元)，且覆蓋家數少，代表性有限。

## Retail social

- **Reddit / StockTwits: DATA_UNAVAILABLE** (依指示不抓取)。
- **PTT / Dcard: 未找到** 相關討論串。
- **新聞與 X 類訊息:** 搜尋結果以媒體與公司說法為主，較少散戶意見。
- **Buzz 量級:** 無法量化，定性判斷為中等偏高。記憶體題材本身受關注，但本次未取得可比對的提及次數。
- **Retail tilt:** 無法直接判定。間接來看，媒體與公司敘事偏多 (DRAM 缺貨、價格續漲)，但市場反應偏弱 (見下)。
- **主要主題 (依媒體報導):**
  1. DRAM/NAND 缺貨與漲價，多家報導指 2027 年缺貨可能更嚴重。
  2. 營收高成長: 10 月營收 170.63 億 TWD，年增 282.3%；前 10 月累計 1,343.69 億 TWD，年增 222.7%。
  3. 股價落後基本面: 2 月報導指出營收暴增但股價由高點 390 附近跌至 306 元；Q3 EPS 達 101.47 元創新高，但股價仍跌逾 4%，法人認為 Q3 低於預期，成本上升壓縮毛利。
  4. 毛利率擔憂: 法人認為上行空間受限，成本端壓力是焦點。
  5. Q4 展望偏保守: 公司預估 Q4 營收較 Q3 略減，理由為年底客戶庫存結算。
- 可引用的代表性文字 (媒體敘述，非散戶貼文): 「DRAM明年缺貨可能比今年更嚴重」。

## Insider activity

- **DATA_UNAVAILABLE** (yf insider 即時與快取皆為空)。無法判定近 6 個月 CEO/CFO 或其他董監事買賣淨額。

## Ownership shifts

- **DATA_UNAVAILABLE** (major_holders 與 inst_holders 皆為空)。無法判定法人持股集中度趨勢。

## 價格資料一致性 (供上層留意)

- 2026-10-30 收盤 346.5 元，單日跌 4.28% (nStock 來源)。
- 2026-10-17 約 360 元 (Investing.com)。
- 另有 383、457.5 元等無日期數字，來源互相矛盾，未採用。
- 2026-03-05 收盤 285 元。
- 本報告不以上述價格作為結論依據。

## 財務與事件時點

- 2026-11-06 線上法說會: 預估 Q4 營收較 Q3 略減。
- Investing.com 列出下次財報日為 2026-11-18，與法說日期不一致，未能確認。
- 法說後股價反應: 未找到資料。

## 淨情緒評分

- **綜合: 偏多 (信心低)。**
  - 偏多因素: 營收年增約 3 倍、DRAM/NAND 供需敘事強、部分投顧目標價高 (556 元)。
  - 偏空或保留因素: 股價對利多反應偏弱、Q4 指引季減、分析師目標價離散、覆蓋家數少。
  - 信心低的原因: 散戶情緒與分析師評等分布皆缺資料，不能做完整加權。
- **背離旗標: 無法判定。** 散戶面無資料，無法與分析師傾向比較。若以媒體與法人傾向看，兩者大致同向偏多，但市場價格反應偏弱，這是一種價格與敘事之間的背離，不是散戶與法人之間的背離。

## 資料缺口與來源

- 缺口: rec_summary、recommendations、insider、major_holders、inst_holders、Reddit、StockTwits、PTT/Dcard。
- 來源 (WebSearch 摘要所引用的媒體):
  - uanalyze.com.tw (Q4 營收展望)
  - wantrich.chinatimes.com (2026-11-06 法說報導)
  - finance.technews.tw (2026-11-06 10 月營收)
  - udn.com (外資 NAND 報導、董座陳立白談缺貨)
  - ctee.com.tw (2025-11 法人降評)
  - investing.com 共識頁
  - nasdaq.com / Fintel (2025-11 目標價，已過時)
