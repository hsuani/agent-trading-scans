# News — 2408.TW (南亞科 Nanya Technology) as of 2026-11-23

**資料品質警示（先看這段）**
- yfinance 新聞工具 (`pipeline/tools/yf 2408.TW news`) 失敗：CONNECT tunnel 被代理 403 拒絕，屬於政策阻擋的主機，依規定不重試、不繞過。本報告的公司新聞全部來自 WebSearch，深度不足。
- WebFetch 的 money.udn.com、wantrich.chinatimes.com 因 DNS 無法解析（session 網路未開放）而失敗。下列來自這兩站的內容只取自搜尋摘要，未能讀原文，需由使用者在 session 網路設定中開放後再核對。
- 價格與營收數據彼此矛盾，請勿直接引用：
  - yfinance info 顯示 2026-11-23 盤中成交價 263.0 TWD（前收 264.5，日內區間 255.5–281.0），52 週高點 569.0。
  - 搜尋摘要顯示 11/17 收 325、11/18 收 328（-0.30%）。若兩者皆正確，11/18 至 11/23 約有 -20% 跌幅，但查無對應的單日重挫新聞。日內區間 255.5–281 與 -0.57% 的漲跌也不一致。
  - 營收數字亦衝突：一則稱 Q3 2026 營收 1336.5 億 TWD，另一則稱 10 月營收 464.76 億 TWD，另一則稱 10 月營收 79.08 億 TWD。尚未取得可靠的交易所或公司公告原文。
  - 本報告採用的價格只以 yfinance 為準，且標示為待核對。

**Money units**: 本報告 TWD 金額統一以 億 表示（1 億 = 1e8 TWD）。Micron 僅列每股美元價格，不使用 B。

**Company data 核對（yfinance info, TWD）**
- 市值 9,074 億 TWD（263.0 × 3.4502 十億股 ≈ 9,074 億，核對通過）
- TTM 營收 2,953.8 億 TWD；TTM 淨利 1,749.7 億 TWD；TTM EPS 50.82 × 股本 3.4502 十億股 ≈ 1,753 億，與淨利一致，核對通過
- 因此 trailing P/E 約 5.2、forward P/E 約 2.1（EPS forward 125.7）。數字符合 yfinance 內部一致性，但受上述價格不確定性影響。

## Top company-specific headlines (last 14d)
- 2026-11-16 — 南亞科受邀參加 Macquarie Taiwan Conference 2026（公司公告，經 Goodinfo 頁面快照，Goodinfo 為二手聚合）。Impact: neutral。一般性投資人接觸活動，無財務資訊。
- 2026-11-18 — 記憶體類股指數當日下跌 3.89%；南亞科收 328 元（-0.30%）。外資報告（摘要稱為 BofA、Morgan Stanley）指出消費型 NAND 率先轉弱，成為獲利了結的導火線（來源：wantrich 摘要，未能讀原文）。Impact: bearish。板塊級賣壓，但南亞科當日跌幅有限。
- 2026-11 上旬 — 現貨 NAND 價格自 10 月中下旬起下跌約 14% 至 20%（Micron 相關報導引用 TrendForce 512Gb TLC NAND 晶圓現貨 10 月初至 11 月初跌 14.2%）。Impact: bearish（現貨領先合約價）。
- 2026-11 上旬 — 市場擔心中國 CXMT 的記憶體設計與產能擴張，最快 2026–2027 全面開出（外資看法，來源：多篇搜尋摘要）。Impact: bearish，對 DRAM 漲價循環的終點有疑慮。
- 2026-11-05 — Micron 單日下跌 17.5%，收 656.39 美元，月內跌約 40%（Motley Fool 與 Trefis 摘要，兩者日期與價位不完全一致）。Impact: bearish（同業情緒傳導）。
- 近期（日期不明，疑為 2026 年內）— 台塑集團（台塑、台化、台塑化）第三波合計出脫約 5.69 萬張，套現約 96.52 億 TWD（來源：搜尋摘要）。Impact: bearish（籌碼面賣壓）。
- 2026-10-12 — 南亞科公布 2026 Q3 財報，單季稅後淨利 876.3 億 TWD，毛利率 85.7%（較上季 79.5% 續升）（technews 2026-10-25 報導）。Impact: bullish，但已超出 14 天窗口，列為背景。Q3 營收數字與其他來源衝突，需核對。
- 2026 年資本支出預算由 520 億 TWD 上修至 697 億 TWD；Fab 5A 2026–2029 計畫上限 3,466 億 TWD（TrendForce / Taipei Times 2026-08-06 報導）。管理層預期 2027 年資本支出續增。Impact: 中性偏空（供給擴張風險），屬於背景，超出 14 天窗口。

## Sector macro
- 2026-11-11 — TrendForce 更新 PC DRAM 4Q26 合約價預估：季增 13%–18%，低於 3Q26 的 18%–23%。Impact on 記憶體 / 半導體: 合約價仍漲，但漲幅遞減，屬於二次微分轉弱。mixed。
- 2026-11-18 — TrendForce DRAM Market Bulletin：合約價續漲但每季增幅縮小；點名三項觀察指標：LTA 價格條款、擴產時點、2028 年需求。一般 DRAM 4Q26 季增約 10%–15%（較 9/30 預估的最高 20% 下修）。Impact: mixed，對 Q4 獲利有利，對 2027 年定價斜率偏空。
- 2026 年內 — 行動 DRAM 合約談判停滯，品牌方持續壓低採購；消費端需求（PC、手機）因記憶體漲價減少單機容量或延後拉貨（搜尋摘要）。Impact: bearish，需求端邊際轉弱。
- 2026-11 — 有報導指 AI 伺服器需求排擠產能，2027 年 PC DRAM 供給可能下降（TrendForce 觀點，來源：搜尋摘要）。Impact: bullish 長期，但時點不明。
- 政治面 — 有標題稱「政治利空恐衝擊 AI 算力！台美日韓記憶體股重挫，南亞科、華邦電大跌」（udn，日期與細節未能讀取）。Impact: bearish，但無法核對具體政策內容，僅列為待查。

## Peer signals
- Micron (MU) — 11/05 單日 -17.5%，收 656.39 美元；11/13 前後約 760 美元（摘要報價不一致）。月跌約 20%–40%。52 週收盤高點 1,213.56 美元（2026-06-25）。Bearish 情緒傳導。
- 華邦電 (2344) / 旺宏 (2337) / 力積電 (6770) — 11/18 記憶體族群同跌（摘要引用），個股數據未核對。
- CXMT（中國） — 新一代記憶體設計與擴產消息，為板塊情緒主要利空來源。Impact: bearish。
- Korean memory peers — 6 月底 Seoul 同業重挫時，台股記憶體同步承壓（2026-06-23 報導摘要）。歷史事件，僅為背景參考。

## Forward calendar (next 14d, 2026-11-23 至 2026-12-07)
- 約 2026-12-05 至 12-10 — 南亞科 11 月自結營收公布（台灣規定每月 10 日前）。Expected impact: 關鍵，可驗證 Q4 合約價上漲是否轉化為營收；若 10 月營收數字真的是 464.76 億，月增 3.1% 將顯示增速放緩。
- 2026-12 月中（待確認） — Micron FQ1 2027 財報（secondary 來源指 12 月，日期未定，多數可能落在窗口之外）。Expected impact: 高，直接影響 DRAM 定價判斷。
- 2026-12 初（待確認） — FOMC 12 月會議（日期未核對，常見為 12 月上旬）。Expected impact: 中性偏大，影響高 beta 股（yfinance beta 2.08）。
- 日期未定 — Macquarie Taiwan Conference 2026（南亞科參加，具體日期未確認）。Expected impact: 中性，管理層可能釋出資本支出與定價口徑。
- 不在窗口內 — 南亞科 Q4 2026 財報預期 2027 年 1 月（yfinance earningsTimestamp 為 2026-10-12，屬已過期日期）。

## Net read
整體頭條傾向為 mixed 偏空，幅度中等。基本面面向：DRAM 合約價仍在上漲（PC DRAM 4Q26 季增 13%–18%，一般 DRAM 季增 10%–15%），南亞科 Q3 毛利率 85.7% 為歷史紀錄，yfinance 顯示 trailing P/E 約 5.2、分析師評級 1.71（Buy）且目標均價 654.9 TWD（13 位分析師）。但價格與情緒面全部偏空：NAND 現貨領先回檔 14%–20%、CXMT 擴產疑慮、Micron 單月大跌、台塑集團減持約 96.52 億 TWD、11/18 板塊級重挫。外資內部也出現「高點可能已過」的保守看法。屬於基本面仍強、但市場正在折價 2027 年定價斜率與產能增加的局面。最關鍵的不確定性是 263 TWD 與 325–328 TWD 的價格衝突，以及營收數字矛盾，這些需要在用於任何決策前由交易所或公司公告核對。

Sources:
- yfinance info (tool output, 2408.TW, cached 2026-11-23T02:01 UTC)
- [technews 2026-10-25 南亞科 Q3 2026](https://technews.tw/2026/10/25/nanya-2028/)
- [technews 2026-11-03 南亞科 10 月營收](https://finance.technews.tw/2026/11/03/ntc-2408-202610-financial-report/)
- [Goodinfo 2408 快照](https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID=2408)
- [TrendForce DRAM Market Bulletin 2026-11-18](https://www.trendforce.com/research/download/RP261118PS)
- [iconnect007 4Q26 memory price article](https://iconnect007.com/article/151792/ai-server-demand-drives-4q26-memory-price-increases-consumer-pressure-persists/151789/smt)
- [Trefis Micron 2026-11-10](https://www.trefis.com/stock/mu/articles2/623897/micron-stock-at-733-why-did-memory-stocks-crash/2026-11-10)
- [Motley Fool Micron 2026-11-09](https://fool.com/investing/2026/11/09/why-micron-stock-fell-17-last-month)
- [247wallst Micron 2026-11-13](https://247wallst.com/investing/2026/11/13/micron-is-down-20-in-a-month-what-will-it-take-to-get-mu-stock-back-to-1000/)
- [Taipei Times 2026-08-06 Nanya Fab 5A](https://www.taipeitimes.com/News/biz/archives/2026/08/06/2003862002)
- [TrendForce 2026-08 Nanya Fab 5A](https://www.trendforce.com/news/2026/08/06/news-nanya-unveils-up-to-us10-7b-fab-5a-investment-plan-through-2029-targets-10nm-class-dram-with-euv/)
- [udn 政治利空 headline](https://money.udn.com/money/amp/story/5607/9858751) (headline only, not read; site unreachable)
- [wantrich 2026-11-18 sell-off](https://wantrich.chinatimes.com/news/20261118900236-420101) (search summary only; site unreachable)

NEWS REPORT COMPLETE
