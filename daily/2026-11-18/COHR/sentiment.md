# Sentiment — COHR as of 2026-11-18

資料來源說明: 分析師評級、內部人交易、持股結構取自 `pipeline/tools/yf.py` (yfinance 快取回退; Yahoo cookie/crumb 連線失敗)。散戶情緒因 Reddit/StockTwits 直接抓取受阻, 改以 WebSearch 彙整二手報導, 可信度較低。未引用任何舊日期報告的內容。

## Analyst consensus

| 評級分布 (本期) | 家數 |
|---|---|
| Strong Buy | 4 |
| Buy | 17 |
| Hold | 5 |
| Sell | 0 |
| Strong Sell | 0 |
| 合計 | 26 |

- 共識: 買進 (yfinance `recommendationKey` = buy, `recommendationMean` = 1.54, 1 為最強買進)。含 Strong Buy 在內, 買進類占約 81%, 無賣出評級。
- 近 4 個月評級趨勢: 買進加強買 家數由 -3m 的 18 增至本期 21; Hold 由 5 → 6 → 5, 波動不大; Sell 始終為 0。
- 目標價 (USD, 股價 $201.7): 平均 $371.9 / 中位數 $380.0 / 最高 $525.0 / 最低 $228.0。以平均目標價計算, 隱含上行空間約 84%。
- 近期評等變動: 個別升降評等明細 DATA_UNAVAILABLE (yfinance `actions` 本次回傳空值)。WebSearch 提到 Citi 將目標價上調至 $440 (TIKR 報導, 約 11 月初), 以及 BofA 由 $400 下調至 $240 (TIKR 另一篇), 兩者日期與來源未獨立核實, 僅供參考。
- 注意: `rec_summary` 合計 26 家, `info` 的 `numberOfAnalystOpinions` 為 25, 為快照時點差異。

## Retail social

- Reddit: r/wallstreetbets 與 r/stocks 直接 JSON 抓取受阻 (依任務指示改用 WebSearch)。WebSearch 未找到 COHR 相關 wallstreetbets 討論串; 僅有 r/stockstobuytoday 於 2026-08 的一則低互動貼文, 把 COHR 列為當日隨晶片股盤前走弱的標的。散戶傾向: DATA_UNAVAILABLE (直接討論串樣本不足)。
- StockTwits / X: 
  - 一篇 TIKR 轉載的 StockTwits 報導指出, 截至 11 月 2 日散戶情緒仍處於 "bearish" 區間 (時點與原始頁面不易獨立確認)。
  - 較早的 StockTwits 報導 (財報後) 曾描述散戶情緒 "extremely bullish", 但該篇屬前一財報季, 不代表本期。
  - 2026-08 的 247wallst 報導指出, 社群 "optics vs. memory" 之爭使 COHR 單日下跌約 11.6%, 顯示社群多空辯論對股價敏感。
  - Quiver 之 AI 摘要 (非原始貼文) 描述: 多數貼文認為估值相對網通大廠有吸引力, 但同時有重大看跌選擇權部位, 整體偏謹慎但看好 AI 長期機會。
- 討論量: 無可靠提及次數, 與平常比較 DATA_UNAVAILABLE; 以定性判斷為中等, 集中於財報前後。
- 代表性觀點 (摘錄, 非完整轉載):
  - 看空: "$COHR operating cash flow is a big concern - big decrease." (經 Quiver 轉述之 StockTwits 貼文)
  - 看多: 社群多數圍繞 "AI 由銅纜轉向光學" 的長期論述。
- 主要主題:
  1. AI 光通訊需求與 Nvidia 相關投資 (正面)
  2. 營運現金流與估值壓力 (負面)
  3. 光學與記憶體 (memory) 資本支出之爭 (分歧)
  4. 內部人大量賣出 (負面)

## Insider activity

視窗: 2026-05-18 至 2026-11-18 (6 個月)。金額以 USD M 計, 僅計公開市場買賣 (Purchase / Sale), 不含 Stock Award 與 Stock Gift。

| 日期 | 內部人 | 職務 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-11-10 | Enrico DiGirolamo | Director | 買進 @ $222.88 | 1,000 | 0.22 |
| 2026-11-09 | James R. Anderson | CEO | 買進 @ $199.48 | 5,000 | 1.00 |
| 2026-09-11 | Enrico DiGirolamo | Director | 賣出 @ $305.98 | 5,315 | 1.63 |
| 2026-09-09 | Robert P. Beard | Officer | 賣出 @ $309.32 | 500 | 0.15 |
| 2026-09-02 | Lisa Neal-Graves | Director | 賣出 @ $268.42 | 2,200 | 0.59 |
| 2026-09-01 | Julie Sheridan Eng | CTO | 賣出 @ $270.69–276.83 | 13,077 | 3.58 |
| 2026-08-31 | Enrico DiGirolamo | Director | 賣出 @ $276.85 | 2,272 | 0.63 |
| 2026-08-31 | Stephen A. Skaggs | Director | 賣出 @ $276.88 | 2,272 | 0.63 |
| 2026-08-18 | Sherri R. Luther | CFO | 賣出 @ $324.00 | 3,000 | 0.97 |
| 2026-07-22 | Sherri R. Luther | CFO | 賣出 @ $306.68 | 1,000 | 0.31 |

- 6 個月買進: 約 USD 1.22M (CEO Anderson 1.00M; 董事 DiGirolamo 0.22M), 共 2 筆。
- 6 個月賣出: 約 USD 8.49M, 共 8 筆 (CTO Eng 最大, 3.58M; CFO Luther 合計 1.28M; 董事 DiGirolamo 合計 2.25M)。
- 淨額: 約 USD -7.27M (淨賣出)。
- 手算核對: 1,000 股 × $222.88 ≈ $0.22M; 5,315 股 × $305.98 ≈ $1.63M, 與工具回報值一致。
- 值得注意: 7–9 月賣出價位集中於 $268–324, 11 月則由 CEO 以 $199 附近買進 5,000 股, 為本視窗內最大單筆公開市場交易之一 (買方)。CEO 與董事於股價回落後出手買進, 與先前的賣出形成對比。
- 持股類 (Stock Award / Stock Gift) 不計入淨額。

## Ownership shifts

- 機構持股比例 87.6%, 內部人持股 4.4%, 機構家數 1,769 (yfinance `major_holders`/`info`)。空頭占浮動股比例 5.1%。
- 前十大機構 (最新 13F, 多為 2026-09-30):

| 機構 | 持股比例 | 股數變化 (%) |
|---|---|---|
| BlackRock | 8.68% | +2.95 |
| Vanguard Capital Mgmt | 6.50% | +0.31 |
| Vanguard Portfolio Mgmt | 5.13% | +0.96 |
| State Street | 4.37% | +0.07 |
| FMR (Fidelity) | 4.16% | -25.65 |
| NVIDIA (2026-06-30) | 3.95% | 0.00 |
| Invesco | 3.02% | -20.01 |
| Capital International | 2.77% | +51.32 |
| Geode Capital | 2.71% | +1.36 |
| T. Rowe Price (2026-06-30) | 1.56% | +99.80 |

- 趨勢: 指數型與被動資金持續穩定或小增; 主動型中 FMR、Invesco 減持, Capital International、T. Rowe 加碼。整體為機構結構分歧, 不構成明顯集中或撤離。

## Net sentiment score

- 分析師: 偏多 (高)。買進類約 81%, 零賣出, 目標價隱含大幅上行。
- 內部人: 6 個月淨賣出 (USD -7.27M), 但 11 月出現 CEO 與董事買進, 近期訊號轉為偏多。
- 散戶: 偏空至中性 (低可信度)。僅一篇 StockTwits 轉載提及 11 月初偏空區間; 直接 Reddit 樣本不足。
- 機構持股: 中性, 主動型資金分歧。

**綜合: 中性偏多 (信心: 中低)**。分析師與近期內部人買進方向一致, 但 6 個月內部人淨賣出與散戶情緒資料薄弱, 拉低信心。

**分歧旗標: 是 (低信心)**。散戶 (偏空, 低可信度) 與分析師 (強烈偏多) 方向相反, 屬於經常具參考價值的分歧, 但因散戶資料來源為二手報導, 不宜作為強訊號。

## Data gaps

- 個別評級升降明細 (yfinance `actions` 空值): DATA_UNAVAILABLE
- Reddit 直接抓取: 受阻, 改用 WebSearch
- 社群提及次數: DATA_UNAVAILABLE
- Citi / BofA 目標價變動: 來源日期與數字互相矛盾, 未獨立驗證
- 本報告以 2026-11-18 為基準日; 系統當日日期記錄為 2026-11-17, 報告依任務指定之 2026-11-18 撰寫, 實際股價快照時點未由工具明示。

SENTIMENT REPORT COMPLETE
