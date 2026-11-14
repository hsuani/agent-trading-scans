# Sentiment — 6830.TW (汎銓) as of 2026-11-15

注意: 系統日期為 2026-11-14，本報告以 2026-11-15 為 as-of，並只採用 11-15 之前的資料。目前可取得的最新新聞約到 2026-11-04，之後的行情未能確認。

## 資料可得性 (soft-fail 紀錄)
- Reddit (r/wallstreetbets、r/stocks): WebFetch 被拒絕 (無法連線 www.reddit.com)，無法取樣。
- StockTwits: api.stocktwits.com DNS 解析失敗，會話網路未允許，無法取得。
- Yahoo cookie/crumb 抓取失敗，yf 結果可能不完整。
- X、CMoney 筆記: cmoney.tw DNS 解析失敗，無法讀取。改以 WebSearch 新聞與法人網站搜尋結果替代。

## Analyst consensus
yf rec_summary 與 recommendations 皆只回傳一筆 (period 0m): 1 strongBuy / 0 buy / 0 hold / 0 sell，覆蓋度明顯不足，信心低。WebSearch 未找到任何券商目標價或評等變動的公開報導。一則 CMoney 新聞標題提到股價「突破法人目標價」，但日期與券商皆不明，無法採用。
Recent moves: 無可確認的升降評等或目標價變動。

## Retail social
- Reddit: 無法取得。
- StockTwits / X: StockTwits 無法取得。X 與社群討論無直接資料，僅能從新聞與論壇標題推估。
- 新聞熱度 (替代指標): 2026 年 3 月 (矽光子題材、連續漲停、創歷史新高) 與 9 月 (增資公告、股價上衝約 850 元) 為兩波高峰，10 月後熱度降低。以新聞篇數衡量屬於「高於一般、近期回落」，無法量化成 Reddit 式提及次數。
- 股價動能: 2026-02-25 收盤 259.5 元。3 月於展會展出 MSS HG 矽光子測試平台時一度觸及 620 元。高點約 850 元，之後回檔超過三成。2026-10-16 收盤 486.5 元 (約較高點回落 43%)。11-04 公司與安立知合作，早盤開高，目前行情未確認。
- Themes:
  - 矽光子設備能否從技術展示轉為付費訂單 (市場焦點為 11-05 第一批付費訂單)
  - 埃米世代材料分析與 AI 晶片檢測題材
  - 短線漲幅過大被列為注意股，追價風險
  - 9 月 500 元/股現金增資 (約 30 億 TWD，約 6,000 張) 的稀釋疑慮
  - 本業為半導體材料分析，並非直接生產矽光子晶片 (有人質疑題材純度)
- 代表性論述 (引述 ≤15 字，改寫為概述): 多數分析認為營收連創高有既有業務支撐，但評價能否跟上，取決於設備訂單落地。

## Insider activity
yf insider 回傳空清單 (該資料源未涵蓋台股董監申報)。WebSearch 未找到 2026 年董監持股增減的明細。
Net 6mo: 無法確認 (資料缺口，不應解讀為零交易)。
現金增資的董監認購情形亦未查到。

## Ownership shifts
yf major_holders: 內部人持股 21.21%、機構持股 8.62%、機構浮動股比例 10.94%、機構家數 10。
趨勢: 無時間序列資料，無法判斷集中度變化。券商分點買賣超資料顯示每日波動大 (例如高盛、元大買超，摩根士丹利、凱基賣超)，屬籌碼流向，不等同持股集中度趨勢。現金增資會稀釋既有比例，這是需要追蹤的變數。

## 財務背景 (用於校對情緒數字)
- 2025 年全年合併營收 21.8 億 TWD (歷史新高)
- 2026 年 1 月營收 2.02 億 TWD (年增 25.5%)
- 2026 年 3 月自結營收 2.24 億 TWD、稅後淨利 1,802 萬 TWD、EPS 0.35 元
- 2026 年 7 月營收 2.41 億 TWD (年增 26.15%)
- 2026 年 8 月營收 2.54 億 TWD (年增 31.95%，單月歷史新高)
- 9 月營收年增 36.7% (依新聞報導)
- 單位換算校驗: 3 月 1,802 萬 ÷ EPS 0.35 ≈ 5,150 萬股，與 6,000 張 × 500 元 = 30 億 TWD 的增資規模一致。
- 某估值網站顯示 P/E 約 1,944 倍，該數字源於單月 EPS 年化失真，不採用。

## Net sentiment score
Composite: **neutral** (信心: 低)
- 分析師面: 僅 1 筆 strongBuy，無法代表共識，偏多但樣本不足。
- 散戶/新聞面: 題材仍在，但自高點回落 43%，熱度降溫，情緒由亢奮轉向觀望，偏中性。
- 內部人面: 無資料，無法計入。
- 籌碼面: 增資稀釋與注意股狀態為負面因素。

Divergence flag: **無法判定 (no)** — 缺少可靠的散戶樣本 (Reddit、StockTwits 皆不可得)，也缺少券商評等，無法確認兩邊傾向是否相反。

## 資料缺口與後續建議
1. 需要 Reddit 或 StockTwits 可連線後補充散戶樣本 (需在會話網路設定允許 api.stocktwits.com 與 reddit.com)。
2. 需要取得 2026-11-05 之後的股價與「第一批付費訂單」公告結果，才能判斷矽光子題材是否兌現。
3. 需要公開資訊觀測站 (MOPS) 的董監持股申報與增資認購名單。
4. 券商目標價需人工查 MoneyDJ 或券商研究報告頁。

SENTIMENT REPORT COMPLETE

## Sources
- [汎銓(6830)布局矽光子設備，股價連三日漲停、創史上新高 (statementdog)](https://statementdog.com/news/15896)
- [汎銓擬現增募資30億元 每股定價500元 (uanalyze)](https://uanalyze.com.tw/articles/3017554970)
- [汎銓 3 月自結稅前淨利 2,264 萬元 EPS 0.35 元 (經濟日報/UDN)](https://money.udn.com/money/amp/story/5607/9434026)
- [汎銓 8 月營收 2.54 億元、年增 31.95% (WebSearch 摘要來源)](https://www.ctee.com.tw/news/20260805700612-430201)
- [汎銓 2026 年營收與增資公告 (Goodinfo 股權異動)](https://goodinfo.tw/tw/EquityTransfer.asp?STOCK_ID=6830)
- [汎銓 2026-11-04 與安立知合作 (工商時報/中時)](https://wantrich.chinatimes.com/news/20261104900113-420101)
- [汎銓 6830 收盤價 10/16 486.5 元 (statementdog)](https://statementdog.com/analysis/6830)
- [汎銓 2026 法說懶人包 (sinotrade)](https://www.sinotrade.com.tw/richclub/hotstock/汎銓-6830-法說懶人包-四大引擎全面啟動從埃米世代到矽光子設備商-股市話題-69e1e955a7d2270aedea14db)
- [Yahoo 股市 6830 法人買賣 (institutional trading)](https://tw.stock.yahoo.com/quote/6830.TW/institutional-trading)
