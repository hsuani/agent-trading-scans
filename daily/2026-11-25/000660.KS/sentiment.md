# Sentiment — 000660.KS (SK hynix) as of 2026-11-25

註: 任務指定分析日為 2026-11-25，系統當日為 2026-11-24。本報告的資料多數止於 2026-11 中旬，2026-11-25 當日的盤後投資人資料未取得。

## Analyst consensus
yf rec_summary (0m 快照): 12 strongBuy / 28 buy / 1 hold / 0 sell / 0 strongSell，合計 41 家，偏多度極高 (buy 類佔 97.6%)。

- 近 3 個月趨勢: strongBuy 由 11 增至 12，buy 由 27 增至 28，hold 維持 1，sell 始終為 0。
- 資料限制: yf recommendations 回傳內容與 rec_summary 完全相同，無逐筆升降評等紀錄，因此「近期 upgrade/downgrade 明細」為 DATA_UNAVAILABLE。
- 目標價 (WebSearch，來源不完整，需保留):
  - 2026-07 韓系券商下修: 神韓證券 (Shinhan) 目標價 420 萬元 → 270 萬元; 키움證券 260 萬元 → 220 萬元，但投資意見升為買進。
  - 2026-06 Mirae Asset 目標價 380 萬元 → 420 萬元; Hanwha 目標價 430 萬元。
  - 2026-10 國際券商 Rosenblatt 目標價上調 25%，隱含 ADR 約 175% 上檔空間; Wolfe 目標價 200 → 250 美元 (ADR SKHY 口徑); Cantor 維持 Overweight，目標 250 美元。
  - 上述 ADR 美元目標價與 KRX 韓元目標價口徑不同，不可直接比較。
- 結論: 外資 (international) 與部分韓系券商在 10 月後轉強; 韓系券商在 7 月出現目標價下修，顯示目標價分歧已擴大。

## Institutional and foreign flow (Korea)
- 11/2–11/6: 外資合計淨賣出 Samsung + SK hynix 約 7.6 兆韓元 (= 76,000 億韓元)，兩檔合計佔 KOSPI 淨賣出 10.4 兆韓元 (= 104,000 億) 的 73%。同期散戶合計淨買入約 4.1 兆韓元 (= 41,000 億)。注意: 上述為兩檔合計，無法拆分出 SK hynix 單獨金額。
- 外資持股比率: SK hynix 降至 48.27%，為 2021-11 以來約 5 年最低 (來源: kbmaeil)。
- 11/中: 有券商報告指出外資賣、股價靠公司 2026-10-28 決議的自家股票買回支撐 (買回期限至 2027-01-28，來源為二手轉述，待 DART 公告核實)。11/16 盤中快照收盤 1,120,000 韓元、單日 +7.90%，屬盤中資料，未核實。
- 機構: 無 11 月逐日機構淨買賣數字 (DATA_UNAVAILABLE)。
- yf major_holders (單一快照，無趨勢資料): 機構持股 40.1%，內部人持股 20.8%，機構家數 736，浮動股機構比例 50.7%。

## Retail social
- Reddit (r/stocks, r/wallstreetbets): 無法存取，WebFetch 回傳 blocked。DATA_UNAVAILABLE。
- StockTwits (api.stocktwits.com): DNS 無法解析，此網域不在允許清單內。DATA_UNAVAILABLE。需在 session 網路設定中允許此網域，才能重試。
- 韓國散戶 (WebSearch 新聞彙整，皆非 11 月資料):
  - 2026-06 報導標題: 外資賣出 10 兆、散戶買進 10 兆，顯示散戶承接外資賣壓的模式。
  - 2026-05 報導: 散戶擔心 190 層 NAND 技術進度，同時券商目標價仍維持高檔，散戶對此有焦慮。
  - 2026-09 報導: 批評券商目標價偏離度高，散戶對目標價的參考價值有疑慮。
- 散戶 tilt (11 月初): 偏多承接，即淨買入 SK hynix / Samsung。情緒主題包括「抄底」與「對目標價不信任」。
- Themes: (1) 外資撤出與散戶承接之對抗; (2) HBM 與 DRAM 供需缺口; (3) 公司自家股票買回; (4) 目標價分歧與券商可信度; (5) NAND 良率或層數技術風險。

## Insider activity
yf insider: 回傳空陣列 (DATA_UNAVAILABLE)。
- 內部人持股 20.8% 為 yf 快照，但不等於近 6 個月交易。
- 韓國 DART 大股東及高管持股變動 (임원·주요주주 특정증권등 소유상황보고서) 未查證，建議補查。
- 公司自家股票買回 (2026-10-28 決議) 屬公司端行為，本報告視為偏多訊號，但需以 DART 公告核實。
Net 6mo: DATA_UNAVAILABLE (無法判定買入或賣出淨額)。

## Net sentiment score
- 分析師: 偏多 (高信心，41 家中僅 1 家持有，0 家賣出); 但目標價於 7 月出現韓系券商下修，口徑分歧。
- 機構/外資流向: 偏空 (11 月初外資大幅淨賣，持股比率降至 5 年低點)，但 10 月後有公司買回支撐。
- 散戶: 偏多承接 (11 月初淨買入)，但情緒有焦慮成分，且 11 月後無資料。
- Composite: 中性偏多 (neutral-to-bullish)。信心: 中低。原因為 social 來源全數不可用、insider 無資料、外資流向只有 11 月初單一區間、以及 WebSearch 來源部分過期或口徑不一。

Divergence flag: **是**。分析師評等 (100% 非賣出) 與外資流向 (大幅淨賣) 方向相反。散戶承接則與分析師偏多方向一致，但與外資方向相反。此分歧常被視為資訊訊號，但本報告不作交易建議。

## Data quality notes
- Reddit/StockTwits: DATA_UNAVAILABLE (Reddit 被擋; StockTwits 網域未允許)
- insider: DATA_UNAVAILABLE (空陣列)
- recommendations 歷史: 與快照相同，無升降評等明細
- 韓國外資/散戶金額: 為兩檔合計，且多為 11 月初數字; 11 月中後無數據
- 網路搜尋結果中 ADR (SKHY, USD) 與 KRX (000660, KRW) 目標價混雜，已分開標示

SENTIMENT REPORT COMPLETE
