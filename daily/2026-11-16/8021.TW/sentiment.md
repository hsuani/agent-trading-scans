# Sentiment — 8021.TW (尖點 Topoint Technology) as of 2026-11-16

資料品質警示: 本次 yfinance 類工具（rec_summary / recommendations / insider / inst_holders）因 fc.yahoo.com cookie/crumb 連線失敗，回傳空值或全 0。這代表「查無資料」，不代表「分析師人數為 0」或「無內部人交易」。下列判讀大量依賴 WebSearch 的間接資料，信心偏低。另外，系統日期為 2026-11-15，報告 as-of 日期為 2026-11-16，最新可取得的資料點是 2026-11-10 前後的新聞。

## Analyst consensus
單位: 分析師家數（無資料）

| 評等 | 家數 |
|---|---|
| Strong Buy / Buy | 無資料 |
| Hold | 無資料 |
| Sell / Strong Sell | 無資料 |

- 工具 rec_summary 與 recommendations 回傳全 0 / 空陣列，屬取數失敗，不可解讀為無券商覆蓋。
- WebSearch 未找到 2026 年 11 月任何券商評等或目標價。Investing.com 的 "Analyst Targets" 數字（65 與 627）實際對應 52 週區間，不是目標價。
- 基本面事件（非評等）: 11/06 法說會公布前三季稅後純益 8.99億 TWD（年增 2.75 倍，EPS 6.18 TWD）；公司表示 2026 與 2027 年資本支出各至少 36億 TWD，並擴充 PCB 鑽針產能。
- 估值參考（不同日期快照）: 本益比約 87（10/28 Goodinfo）至 113（8/10 Yahoo 股市，同業平均約 45）；PBR 約 10.25。

換算核對: 前三季稅後純益 8.99億 TWD ÷ EPS 6.18 ≈ 1.46 億股，與現增 4,000 張（400 萬股）的規模一致；4,000 張 × 388 TWD = 15.52億 TWD，與報導相符。

## Retail social
- Reddit: 本次未取得。使用者指定直接社群站點受限，且 r/wallstreetbets、r/stocks 對台股個股討論量本身極低，預期無有效樣本。
- StockTwits / X: 未取得有效樣本。WebSearch 無 2026 年 11 月的 X 貼文。
- PTT Stock 板: 唯一可定日期的文章為 2026-07-22 轉貼的 6 月自結獲利新聞，回文極少，無法反映情緒。
- CMoney 股市爆料同學（時間不明）: 多空交錯。一端為「回檔風險、賣壓」的悲觀留言，另一端為「可能反彈」的樂觀留言。另有摘要提到盤後走弱、跌停收盤的描述，顯示買盤轉弱。
- 報導中提及的 11/05 跌停與 11/06 新股上市，兩則來源日期描述不一致，未能交叉確認，僅作背景。

**Retail 聲量**: 無法量化。以台股個股而言，討論熱度主要集中在 CMoney、PTT 與 Dcard 等平台，本次資料無法取得可比較的月度提及數。

**Retail tilt**: 混合偏空（信心低）。依據是 CMoney 留言對回檔與賣壓的描述，以及 11 月現增、CB 發行後的股價壓力敘述。

**主要主題（Themes）**:
- AI PCB 鑽針需求與 ABF／高階封裝題材（長期故事，較受關注）
- 獲利爆發（前三季 EPS 6.18 TWD）與高估值之間的拉扯
- 現金增資（388 TWD 溢價發行，募資 15.52億 TWD）與可轉債（募資約 6.52億 TWD）造成的稀釋與籌碼壓力
- 籌碼面: 外資 8 月初連續賣超（8/7 單日賣超 1,449 張），投信同期小幅買超（253 張）

## Insider activity
工具 insider 回傳空值，無法取得 6 個月內董監事實際申報交易的美元／台幣金額。以下為間接資料:

- 董監持股比例（HiStock 籌碼資料）: 2026/05/22 至 2026/07/09 各週皆為 9.69%，期間無明顯變動。
- 較早數字: Yahoo 2025/12/05 為 8.36%。兩站統計口徑不同，不可直接比較。
- 工具 major_holders 回傳 insidersPercentHeld = 10.1%，與上述數字大致一致。
- 未找到 2026 年 11 月的董監事轉讓或質押公告。官方紀錄應查公開資訊觀測站「董監持股申報」與「內部人持股轉讓事前申報」。

Net 6mo: 資料不足，無法計算淨買賣金額（不可視為零）。Notable: 無可確認之 CEO／CFO 交易紀錄。

## Ownership shifts
- 機構持股（工具 major_holders）: institutionsPercentHeld = 18.4%；institutionsFloatPercentHeld = 20.5%；機構家數 29。
- 機構持股趨勢: 無歷史序列，無法判定增減方向。inst_holders 工具回傳空值。
- 法人買賣超（WebSearch，最近可得資料為 2026 年 8 月）: 外資 8/7 賣超 1,449 張，投信 8/7 買超 253 張；8/4 外資賣超 201 張。11 月法人數據未取得。
- 現增與 CB 發行後的股本擴大，會稀釋既有持股比例，需在後續報告中以新股本重算。

## Net sentiment score
**Composite: neutral（信心：低）**

理由:
- 基本面正向: 獲利大幅成長、毛利率創高（Q2 毛利率 41.8%，Q2 營收約 18.26億 TWD，年增 80%）、8 月營收 7.71億 TWD 創高。
- 估值與籌碼偏負: 本益比偏高、外資 8 月連續賣超、11 月現增與 CB 帶來稀釋與賣壓敘述、零售留言偏向回檔風險。
- 分析師端無有效資料，無法判斷共識方向。

**Divergence flag: 無法判定（分析師端無資料）**
- 若日後取得分析師資料，且其偏多而零售偏空，可視為值得注意的背離訊號。目前不能下此結論。

**需補件（下次更新）**:
1. 修復 yfinance 工具的 cookie/crumb 連線，重跑 rec_summary、recommendations、insider、inst_holders
2. 取得 11 月三大法人買賣超日報
3. 取得公開資訊觀測站董監事申報
4. 取得 CMoney／PTT 2026 年 11 月的可定日期留言樣本

來源（WebSearch 間接資料）: Yahoo 股市 8021 頁面（major-holders、institutional-trading、announcement）、HiStock 籌碼資料、Goodinfo 8021 頁面、uanalyze 與 udn 財報新聞、CMoney 8021 論壇、PTT Stock 板。

SENTIMENT REPORT COMPLETE
