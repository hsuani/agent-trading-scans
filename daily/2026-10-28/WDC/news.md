# News — WDC as of 2026-10-28

資料來源與限制：
- `pipeline/tools/yf WDC news` 因 sandbox proxy 封鎖，無法取得 yfinance 新聞清單；本報告新聞全部以 WebSearch 補足。
- `pipeline/tools/yf WDC info` 可用（Cookie/crumb 失敗不影響欄位），價格、市值、EPS、目標價以此為準。
- WebFetch 無法解析 www.sec.gov（DNS 失敗），因此 FQ1 FY27 數字取自 WebSearch 摘要所引用的 WD 新聞稿（westerndigital.com 新聞室與 SEC 8-K 附件），未與原文逐字核對，標註為「新聞稿摘要」。
- 多個來源之間的股價、市值、Fed 利率水準互相矛盾，已於各段標註。
- 報告截止 2026-10-28 開盤前；10/28 14:00 ET FOMC 結果視為未來事件。

## 公司基本面與價格快照（供對照，非新聞）

| 指標 | 數值 | 備註 |
|---|---|---|
| 最近價格（regularMarketPrice） | 356.13 USD | 前收 343.67，日漲 +3.6%（yf 快照時間未提供） |
| 52 週區間 | 121.85 – 799.87 USD | 現價距 52 週高點約 -55% |
| 50 日均 / 200 日均 | 429.95 / 415.50 USD | 現價低於兩條均線 |
| 市值 | 133.3B USD | 374.3M 股 × 356.13 驗算一致 |
| 企業價值（EV） | 132.9B USD | |
| TTM 營收 | 14.48B USD | 年增 55.5%；與 Q2 FY26（推算約 3.0B）+ Q3 3.34B + Q4 3.75B + Q1 FY27 4.38B 加總約 14.5B 相符 |
| TTM EPS / Forward EPS | 28.43 / 40.40 USD | 以 yf 欄位推算 Trailing P/E 約 12.5x、Forward P/E 約 8.8x |
| 淨利（netIncomeToCommon）/ FCF | 9.91B USD / 2.73B USD | EPS × 股數約 10.6B，與淨利差約 7%，屬 TTM EPS 與股數口徑差異 |
| 分析師共識 | buy，24 家，目標價均值 610.04 USD（區間 405–900） | yf 快照 |
| 空單占浮動股 | 4.9% | |
| Beta | 2.17 | |

## Top company-specific headlines (last 14d)

- 2026-10-22 — WD 公布 FQ1 FY27（季末 2026-10-02）：營收 4.38B USD（年增約 55%）、non-GAAP EPS 4.64 USD、GAAP EPS 4.63 USD、non-GAAP 毛利率 58.1%。全面高於 8 月指引（營收 4.0–4.2B USD、EPS 3.85–4.15 USD）（WD 新聞稿摘要，westerndigital.com 新聞室／SEC 8-K 附件）。Impact: bullish。1 行理由：營收與 EPS 雙雙超越指引，毛利率回到 58% 以上，基本面證據強。
- 2026-10-22 — FQ2 FY27 指引：營收 5.1B ±0.1B USD（年增約 66–72%）、non-GAAP 毛利率 60–61%、non-GAAP EPS 5.80 ±0.20 USD，稀釋股數約 380M（WD 新聞稿摘要，英文與西班牙語站）。Impact: bullish。1 行理由：指引明顯高於共識（asktraders 引用營收 4.57B、EPS 4.82 USD，單一來源，待確認）。
- 2026-10-22 — 季股息上調 17% 至 0.175 USD，2026-12-17 發放（WD 新聞稿摘要）。Impact: bullish（小幅）。1 行理由：管理層對現金流有信心，但對價格影響有限。
- 2026-10-22（財報當日常規盤，日期為推斷）— 股價反應：asktraders 稱常規盤收 354.18 USD、-6.4%（財報於盤後公布前），盤後 +2.1%。yf 快照顯示前收 343.67、現價 356.13。財報後次日的實際收盤價與分析師調整目標價「未找到」。Impact: neutral（待確認）。1 行理由：正面財報未轉成明確價格反應，市場似乎仍在定價週期高點與競爭疑慮。
- 2026-10-02 — Toshiba 宣布擴建菲律賓 Laguna HDD 產線，投資約 60B 日圓（約 0.38B USD），目標於 FY2027 將 AI 資料中心用 HDD 產能較 2025 年翻倍（evertiq 2026-10-20、blocksandfiles 2026-10-06 轉載）。當日 WD 約 -7%、STX 約 -10%（247wallst 2026-10-02）。Impact: bearish（情緒與中期份額）。1 行理由：新增供給是市場對 HDD 定價權的主要疑慮。
- 2026-10-05 — 研究部門反駁 Toshiba 供給擔憂，Citi 認為產業仍在供不應求，Toshiba 的增量對整體可用供給影響有限（法文二手來源，原始 Citi 報告待確認）。WD 當日約 +7%、STX 約 +5%（247wallst 2026-10-05）。Impact: neutral（修復）。1 行理由：賣壓快速反彈，市場未採納供給過剩論點。
- 2026-10-05 — WD 提交 proxy statement，列出股東投票與治理事項（WebSearch 摘要）。Impact: neutral。1 行理由：例行文件，未涉及財務內容。
- 分析師目標價（財報前，確切日期未確認，可能早於 14 天窗口）— BofA 由 720 上調至 800 USD 維持 Buy；Cantor 由 660 上調至 900 USD；Rosenblatt 於 8/6 由 900 下調至 800 USD（MarketBeat、TipRanks 等摘要）。Impact: neutral to bullish。1 行理由：多數目標價高於現價，但都是財報前數字，財報後未見更新。

雜訊已排除：
- 無日期的「WD 股價因 AI 資料儲存競爭加劇單日跌超 11%」報導，無法定位日期，不採信。
- 單日漲跌、第三方「股價 X 元」排名文章、估值摘要網站的內容。
- 8 月指引本身（已在 10/22 財報中被超越，列為背景）。

## Sector macro

- 2026-10-28 14:00 ET — FOMC 利率決議（非 SEP 會議）。利率水準來源衝突（3.50–3.75% 或 3.75–4.00%），各快照的市場隱含機率也不一致（hold 約 53–80%）。Impact on HDD / 資料中心儲存：利率影響 hyperscaler 資本支出與高 beta 股票估值；WD beta 2.17，對鷹派意外敏感。結果未知。
- 2026 年 10 月 — HDD 供給緊：Seagate 表示 2026 年 nearline 產能已售罄，長期供貨協議延伸至 2027–2028；WD 2026 年產能據稱也已售罄（單一來源）。Impact: bullish，是本季指引高於共識的基礎。
- 2026-10（TrendForce 研究摘要，約 10/07）— 份額預測：Toshiba 2028 年市占回到約 12%，Seagate 升至約 45%，WD 降至約 43%。Impact: bearish（中期份額，但屬預測而非事件）。
- HAMR 技術轉換 — Seagate 表示 HAMR 產品約占 nearline exabyte run rate 的 40%（Seagate FY26 財報電話會議摘要，日期不完全清楚）。Impact: neutral；WD 的 HAMR 時程本次未查證，屬資料缺口。
- 關稅與出口管制 — 本次搜尋未找到 WD 特定的關稅、出口管制或 USMCA 新聞，屬資料缺口，本報告不做判斷。
- NAND 同業 — Sandisk 可查最近報告為 FQ3 2026（4/30），資料中心營收 1.467B USD、季增 233%；未找到 10 月的新數據，已過時。Impact: neutral（資料中心儲存預算同時流向 NAND 與 HDD）。

## Peer signals

- STX（Seagate）— FY26 出貨 789 EB、營收約 12.2B USD、毛利率 46%、淨利 3.2B USD；nearline EB 由 497 升至 695。最新電話會議摘要稱大部分 nearline 產能已分配至 CY2028（來源日期不完全清楚，待確認）。FQ1 FY27 財報日期未找到官方公告，歷史上於 10 月下旬發布（2023 年 10/26、2024 年 10/22）。Impact: 需求與供給面同向利多，但 10/2 與 WD 同步大跌，股價相關性高。
- Toshiba（非本 pipeline 標的）— HDD 第三大廠，見 Top headlines 與 Sector macro 的擴產與份額預測。Impact: bearish（中期）。
- SNDK（Sandisk）— 見 Sector macro 的 NAND 段落，數據已過時。

## Forward calendar (next 14d)

- 2026-10-28 14:00 ET — FOMC 利率決議，結果未知。預期影響：中（高 beta 成長股的估值敏感度）。
- 2026-10-28 之後，日期未確認 — Seagate FQ1 FY27 財報。歷史上 10 月下旬發布，若落在窗口內，將是 HDD 族群的最大催化劑。預期影響：高（WD 與 STX 同步波動的紀錄）。
- 2026-11 上旬，日期未確認 — WD 年度股東大會（proxy 已於 10/5 提交，會議日期本次未查證）。預期影響：低。
- 2026-12-17 — WD 股息發放日（窗口外；登記日未查證）。
- 窗口內無 WD 自身的財報或法說會。

## Net read

以新聞口徑看，WDC 的基本面訊號明確偏多，價格反應偏弱，整體 headline 傾向為 bullish，幅度中等偏強，但受股價與族群情緒的牽制。FQ1 FY27 營收 4.38B USD、non-GAAP EPS 4.64 USD 皆超越 8 月指引，FQ2 指引營收 5.1B USD 與 EPS 5.80 USD 明顯高於 asktraders 引用的共識，毛利率目標升至 60–61%，股息上調 17%，產能與長期供貨協議延伸至 2027–2028，這些都是正面證據。另一方面，股價 356.13 USD 仍較 52 週高點 799.87 USD 低約 55%，低於 50 日與 200 日均線，財報後的正面數字未見有效的價格修復，Toshiba 擴產、HAMR 帶來的 Seagate 份額優勢，以及 TrendForce 的中期份額預測，構成市場的主要疑慮。報告內有數個關鍵資料衝突：現價與 8 月的 469.05 USD 差距很大，財報當日的實際價格反應與財報後分析師目標價調整均未查證，Fed 利率水準與 Seagate 財報日期也未確認。窗口內最大的 HDD 族群變數是 10/28 FOMC 結果與尚未確認日期的 Seagate 財報。本段僅描述新聞傾向，不構成交易建議。

NEWS REPORT COMPLETE
