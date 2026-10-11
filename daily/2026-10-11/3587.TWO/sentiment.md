# Sentiment — 3587.TWO (閎康) as of 2026-10-11

資料完整度低。Reddit 與 StockTwits 無法取得，yf 分析師評級與內部人交易回傳空資料，目前只能依 WebSearch 的新聞與聚合頁面做低信心判讀。

## Analyst consensus
DATA_UNAVAILABLE（yf `rec_summary` 與 `recommendations` 皆回傳空陣列，無法取得 buy/hold/sell 分布與升降評等紀錄）。

WebSearch 可見的零散數據，時間與樣本皆不一致，僅供參考：
- FactSet 彙整（鉅亨網報導，日期不明）：6 位分析師，目標價中位數由 264 元下修至 250 元，區間約 210 至 320 元，5 位偏正面、1 位中立。該報導收盤價為 175 元。
- Investing.com 頁面（標示為過去 3 個月）：僅 3 位分析師，12 個月平均目標價約 365.67 元，最高 450 元、最低 300 元，共識為「買入」。該頁股價顯示 251.50 元。
- 上述兩者股價差距大（175 元與 251.50 元），應屬不同時點，無法直接比較。
- 2025 年 3 月研究文章目標價 290 至 340 元，屬舊資料，不採用。

Recent moves: 無法確認 2026 年內的評等升降紀錄。

## Retail social
- Reddit: DATA_UNAVAILABLE。WebFetch 無法連線 r/wallstreetbets 與 r/stocks 的 search.json（回報 unable to fetch）。
- StockTwits / X: StockTwits 回報 DNS 解析失敗（api.stocktwits.com 無法解析），DATA_UNAVAILABLE。X 未取得可用貼文。
- PTT / CMoney: 未找到 PTT Stock 板閎康相關討論串。CMoney 股市社群頁有 3587 討論區入口，但抓到的內容以其他個股為主，與閎康直接相關的留言很少。
- 聲量（mention volume）: DATA_UNAVAILABLE，無法與平常基準比較。
- Retail tilt: DATA_UNAVAILABLE（無法判定）。
- Themes（僅從新聞與公司動態歸納，非社群原文）:
  - 日本與美國市場成長：董事長表示日本營收比重今年有機會達 20%。
  - 矽光子（silicon photonics）布局：2026 年 6 月股東會上董事長看好。
  - 大陸子公司 80% 股權出售：2026 年 7 月 31 日董事會通過，預計 2026 年底前交割，需股東會同意與主管機關核准。
  - 股利：2026 年 6 月股東會通過每股現金股利 4.5 元（另有媒體引用 2025Q4 配發 4.21 元，兩者口徑待核）。
  - 營收動能：2026 年 7 月合併營收 5.63 億元，年增 18.56%，報導稱連續五個月創歷史新高。
  - 法人觀點：大來投顧於 2026 年 8 月初將閎康納入投組，認為第二季季報是扭轉盤勢的催化劑。

## Insider activity
DATA_UNAVAILABLE。yf `insider` 回傳空陣列，無法確認近 6 個月內部人買賣淨額。空陣列可能代表無申報，也可能是資料源缺漏，目前無法區分。

Ownership（yf `major_holders`，有資料）:
- insidersPercentHeld: 28.13%
- institutionsPercentHeld: 8.80%
- institutionsFloatPercentHeld: 12.25%
- institutionsCount: 16

Ownership shifts: DATA_UNAVAILABLE（只有當前快照，無歷史趨勢）。

## Net sentiment score
Composite: neutral，信心低（low）。

判讀依據:
- 分析師面（有限樣本）偏多，但目標價中位數 250 元與多數報價落差不一，且樣本僅 3 至 6 位，不足以代表共識。
- 基本面新聞偏正面（營收年增、獲利年增、日本與矽光子題材），但多來自公司或媒體報導，非獨立情緒指標。
- 散戶面完全缺資料，無法做 crowd mood 判讀。
- 內部人面缺資料，無法作為佐證。

Divergence flag: 無法判定（散戶與分析師兩側皆缺乏可用的直接資料）。

## 資料缺口與待補項目
- Reddit、StockTwits 連線失敗，需改用代理或其他來源重試。
- yf `rec_summary`、`recommendations`、`insider` 回傳空值，需確認 `3587.TWO` 在 Yahoo 端的對應是否正確，或改用其他來源。
- WebSearch 的 2026 年 9 月營收（5.69 億，年增 12.31%）與第二季 EPS 0.75 元（年減 46%）來自搜尋摘要，未經原始財報核對。
- 股價來源不一（175、251.50、276.5 元），需以同一時點的收盤價重新校正後再使用目標價比較。

## 來源（WebSearch，未逐一驗證原文）
- 鉅亨速報 FactSet 調查報導（Yahoo 財經）
- Investing.com 閎康 consensus 頁面
- 大來投顧 / 中時財經 (wantrich.chinatimes.com) 2026 年 7 至 8 月報導
- nStock 閎康介紹頁
- CMoney 股市社群 3587 頁

SENTIMENT REPORT COMPLETE
