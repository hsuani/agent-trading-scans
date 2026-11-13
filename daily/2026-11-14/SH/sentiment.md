# Sentiment — SH as of 2026-11-14

資料說明: SH 為 ProShares Short S&P 500 (inverse ETF)，不適用 insider / major_holders 章節，已略過。SH 的方向性判讀以「美股大盤情緒」反推: 大盤情緒偏空 = 對 SH 偏多。資料截至 2026-11-14 前可取得的最新公開數據 (多為 11/2 至 11/9 週)。

## Analyst consensus
- yf 工具 (rec_summary / recommendations) 兩次呼叫皆回傳空值 (Yahoo cookie/crumb 取得失敗)。SH 為 ETF，通常無個股式分析師評等，故無 buy / hold / sell 分布可用。
- 改以大型券商對 S&P 500 的策略師觀點代理 (非 SH 本身評等):
  - Goldman Sachs Research 維持 2026 年底 S&P 500 目標 8,000。
  - JPMorgan earlier in 2026 上修目標至 8,000，理由為獲利成長與 AI 投資。
  - Morgan Stanley Michael Wilson 於 11/2 報告認為期中選舉可移除一大不確定因素，偏好品質型景氣循環股。
  - 11/4 S&P 500 收 7,698.80 (+1.72%)，媒體報導為選後反彈。
  - 風險提示: 殖利率上升可能壓縮本益比，即使獲利持續成長。
- 結論: 策略師陣營整體偏多 (目標價集中於 8,000 附近)，對 SH 構成逆風。
- 注意: 部分來源為聚合站或自動生成內容 (如 allmind.ai)，未能逐一對照原始券商報告。Oppenheimer 11/9 市場策略報告僅見標題，內容無法讀取。

## Retail social
- Reddit (r/wallstreetbets、r/stocks): 本次 WebFetch 遭拒 (Claude Code 無法存取 www.reddit.com)，無法取得貼文樣本。以 WebSearch 補查亦未找到該兩個版塊於 11/2026 的相關討論。Reddit 部分為資料缺口，不列入計分。
- StockTwits: api.stocktwits.com 解析失敗 (DNS 不通，session 網路未允許)，無法取得訊息流與 Bullish / Bearish 標籤統計。需於 session 網路設定中允許該網域後才能重試。
- X / 新聞輿情: 網路搜尋可見的 11/2026 相關內容多為策略師與媒體觀點，未見可量化的散戶留言樣本。
- 相關市場情緒 (非 Reddit / StockTwits):
  - 密西根大學消費者信心初值 11/2026 為 51.0，為 8 月以來高點，顯示消費者情緒回升。
  - 一則 11/2026 報導引述約 40% 散戶預期年底報酬持平或為負。
  - 搜尋結果出現 CBOE 11/2 週市場週報，標題為「Tech Rout, Muted Vol: Bullish Positioning Unwinds」(科技股重挫、波動率低迷、多方部位撤出)，但內文未能讀取。
- 相關度低的過期資料 (2025 年底至 3 月) 未納入本次判讀。

- 量化 buzz: 無法取得 Reddit / StockTwits 提及次數，無法與歷史基準比較。

- 主要主題 (由可得來源歸納):
  1. 科技股近期回檔，多方部位撤出。
  2. 選後政治不確定性下降的反彈論述 (Morgan Stanley 觀點)。
  3. 殖利率上升對估值的壓力。
  4. 地緣政治 (伊朗相關) 的尾部風險 (DailyForex 11 月技術預測引用，屬零售導向內容)。

## Positioning
- AAII 散戶調查 (週末 11/4):
  - 看空 48.4%、看多 34.1%、中性 17.5%。
  - 看空高於長期平均 31.5% 約 17 個百分點；看多 34.1% 低於長期平均 37.5%。
  - 前一週 (10/28) 看空為 41.4%、看多 37.8%，看空情緒一週內明顯升溫。
  - AAII 本身將此指標視為反向指標；歷史上極度看空後平均報酬偏高。
  - 未找到 11/11 週的數據，本報告以 11/4 為最新讀數。
  - 來源對 1 年期看空高點記載不一 (52.0% 於 3/18 與 53.3% 於 3/4)，與本次判讀無直接關係。
- Put/call ratio:
  - 無可靠的 11/2026 CBOE equity put/call 讀數。
  - 一筆 OptionCharts 數據顯示 11/4 put/call volume 2.04，但該數字對應 Cboe 公司股票而非市場 put/call，且數值異常高，未採用。
  - 較早期數據: 6 月底 equity put/call 0.85；4 月 0.52；長期 200 日均值約 0.61 (來源為早期頁面，僅供參考)。
- CFTC S&P 500 E-mini 投機部位:
  - 無 11/2026 數據。可得資料為 2026 年 3 月至 6 月的非商業淨部位，數值來源彼此不一致，無法採用。
  - 需直接查閱 CFTC Commitments of Traders 報告以取得最新值。
- 選擇權大單: 10/20 有 SPY 11/20 到期的 put spread 交易，解讀為溫和回檔對沖，非崩盤押注；單筆交易不代表市場整體。

## Insider activity
不適用 (ETF)，略過。

## Ownership shifts
不適用 (ETF)，略過。

## Net sentiment score
- 策略師 (對大盤): 偏多 (目標價 8,000 附近，多家強調獲利與選後利多)。對 SH 為負面。
- 散戶問卷 (AAII): 明顯偏空，且週內升溫。以反向指標解讀，對 SH 為正面 (反向訊號)；以順勢解讀則對 SH 為正面 (市場情緒偏空)。
- 社群 (Reddit / StockTwits): 無資料，不納入。
- 消費者信心: 回升，偏多，對 SH 為負面。
- 綜合: **中性 (neutral)，信心低**。策略師與消費者信心偏多，散戶問卷偏空，三者方向不一致，且社群與持倉資料缺漏多，綜合分數不具高信心。

Divergence flag: **是** — 散戶 / AAII 偏空，與策略師偏多方向相反。此類分歧在歷史上常具參考價值 (但需注意樣本僅一週)，應由後續報告持續追蹤。

## 資料缺口與限制
- yf rec_summary / recommendations: 空值 (Yahoo cookie / crumb 取得失敗；ETF 亦無個股評等)。
- Reddit (r/wallstreetbets、r/stocks): 存取遭拒。
- StockTwits: DNS 解析失敗，需於 session 網路設定允許 api.stocktwits.com。
- CFTC 與 CBOE put/call: 無 11/2026 可靠數據。
- 報告日 2026-11-14 與系統日 2026-11-13 不一致，本報告依指定日期標示，實際資料多止於 11/4 至 11/9 週。

SENTIMENT REPORT COMPLETE
