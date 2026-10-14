# Sentiment — 000660.KS (SK hynix) as of 2026-10-14

資料可信度聲明：Reddit（r/stocks、r/wallstreetbets）與 StockTwits 本次皆無法取得（Reddit 拒絕連線；StockTwits 域名解析失敗）。散戶情緒部分僅能以新聞與搜尋摘要替代，且多數搜尋來源日期停留在 2026-07 至 2026-08，數字互相矛盾。yf 工具回報 Yahoo cookie/crumb 取得失敗，資料可能來自快取，未能確認時間戳。以下結論信心偏低，僅供參考。

## Analyst consensus
yf rec_summary（0m）：11 strongBuy / 27 buy / 1 hold / 0 sell / 0 strongSell，共 39 家。
近四個月（-1m、-2m、-3m）無明顯變化：-2m 時 buy 為 26，-3m 時為 25，近期略增。yf recommendations 歷史資料沒有出現降評紀錄，僅見 buy 數目逐步增加。
Recent moves（新聞來源，未經 yf 核實）：
- Eugene Investment & Securities 於 2026-10-08 給予 Strong Buy，目標價 370 萬韓元，預估 2026 營業利益 263.4 兆韓元、2027 年 454.1 兆韓元。
- Shinhan Investment 於 2026-07 下旬維持 Buy，但目標價由 300 萬下調至 270 萬韓元，理由為對記憶體價格較保守，長期觀點不變。
- 某聚合頁面顯示 42 Strong Buy / 103 Buy / 5 Hold / 1 Sell，但頁面標示最後更新於 2026-08，且與 yf 的 39 家分布差異很大，不採用。
- Parameter.io 提及 Barclays 目標價 300 美元（ADR SKHY 口徑），來源單一，未核實。

## Retail social
- Reddit：本次無法取得（r/stocks 與 r/wallstreetbets 查詢皆被拒）。無法判斷 tilt 與樣本。
- StockTwits / X：StockTwits 無法連線（域名解析失敗），本次略過。X 無獨立可用資料。
- 新聞端替代觀察：搜尋摘要描述投資人情緒「熱烈」，焦點集中於 HBM4 量產與 AI 記憶體需求；另有出口管制風險與「政策折價」的提醒。這些為媒體敘述，不等於散戶情緒。
- 散戶通路：摘要指出散戶多半透過 OTC 或 EWY 等韓股相關 ETF 間接接觸，直接買入韓股的門檻較高。
- 聲量（qualitative）：無法量化，本次不以聲量作為判斷依據。
- Themes（來自新聞，非散戶原文）：HBM4 量產進度、2026 獲利預估上修、記憶體定價與 2027 展望、出口管制、Q3 財報前的股價波動。
- 財報日期：來源各異，Parameter.io 為 10-27，Earnings Whispers 為 10-28，Yahoo 為 10-27，需以公司公告為準。

## Insider activity
yf insider 回傳空陣列（Yahoo 連線失敗或此標的無資料），無法由 yf 取得 6 個月淨額。以下為新聞來源整理，未經 DART 核實：
- 2026-04：CEO Kwak No-jeong 等高管行使股票選擇權，約 62 億韓元（KRW 6.2B），媒體解讀為信心訊號。
- 2026-05-29：AI Infrastructure 部門社長 Kim Ju-sun 賣出 1,000 股，約 23.3 億韓元，持股剩餘 2,881 股。公司回應稱屬個人安排。
- 2026-07 下旬：SK 集團會長 Chey Tae-won 於公開市場買入約 48 億韓元，因超過 50 億韓元門檻前需提前 30 天揭露，此金額接近上限。
- 淨額（估）：買入約 110 億韓元以上（含選擇權行使與會長買入）、賣出約 23 億韓元，6 個月淨買入方向。金額為新聞加總估算，不能視為精確值。
- 揭露管道：SK hynix 屬 Section 16 豁免，不走 Form 4，而是韓國 DART 系統。
- 未見監管調查或違規指控的紀錄。

Notable: Chey Tae-won（SK 集團會長，非公司內部職務）、CEO Kwak No-jeong（買入選擇權行使）、Kim Ju-sun（社長，賣出）。

## Ownership shifts
yf major_holders（時間點未確認）：
- insidersPercentHeld：20.17%
- institutionsPercentHeld：39.31%
- institutionsFloatPercentHeld：49.24%
- institutionsCount：727
機構持股趨勢無歷史對比資料，無法判斷是增持或減持。內部人持股比例偏高（SK 集團為主要股東），屬結構性特徵，不宜直接解讀為賣壓或買壓。

## Net sentiment score
Composite: **bullish（偏多）**，信心 **低-中**。
- 分析師面：強烈偏多（39 家中 38 家 Buy 以上，0 賣出評等，目標價近期上修為主）。權重高。
- 內部人面：偏多（選擇權行使與會長買入為主，單筆賣出金額較小）。權重中。
- 散戶面：無資料。權重無法計入，這是信心偏低的主因。
- 新聞敘述：偏多但含出口管制與估值風險提醒。

Divergence flag: **無法判定**。本次取不到散戶語調，無法確認散戶是否與分析師相反。待 Reddit/StockTwits 恢復後再重跑。
注意：分析師高度一致偏多，可能已反映於股價；Q3 財報前股價波動大（ADR beta 約 2.3），情緒面需與價格面一起看。

## 指標表
| 指標 | 數值 | 來源 | 備註 |
|---|---|---|---|
| 分析師評等（strongBuy / buy / hold / sell / strongSell） | 11 / 27 / 1 / 0 / 0 | yf rec_summary (0m) | 共 39 家，時間點未確認 |
| 分析師買進比例（strongBuy + buy） | 97.4% | 由 yf 計算 | 38/39 |
| 近 3 個月 buy 數變化 | 25 → 27（-3m 至 0m） | yf rec_summary | 小幅增加 |
| 近期目標價調整 | Eugene 370 萬韓元（10-08）；Shinhan 270 萬韓元（07 下旬，由 300 萬下調） | 新聞 | 未經 yf 核實 |
| 6 個月內部人淨額（估） | 約淨買入 80 至 90 億韓元 | 新聞加總估算 | 非 DART 核實 |
| 內部人持股比例 | 20.17% | yf major_holders | |
| 機構持股比例 | 39.31%（流通股 49.24%） | yf major_holders | |
| 機構家數 | 727 | yf major_holders | |
| Reddit 樣本數 / 語調 | 無資料 | — | 連線被拒 |
| StockTwits 語調 | 無資料 | — | 域名解析失敗 |
| 散戶 vs 分析師背離 | 無法判定 | — | 缺散戶資料 |
| 綜合情緒 | 偏多，信心低-中 | 本報告 | |

SENTIMENT REPORT COMPLETE
