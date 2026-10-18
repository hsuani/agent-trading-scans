# Sentiment — 3443.TW (創意電子) as of 2026-10-19

資料截止：2026-10-19（台北時間）。之後的資料視為未知。部分來源的日期無法確認，已在內文標註。

## Analyst consensus
Yahoo 快取（yf 0m）：6 Strong Buy + 13 Buy / 0 Hold / 0 Sell，**BUY 佔比 100%（19 家）**。
Yahoo 即時抓取失敗（ConnectionError），此數字來自 repo 快取，快取日期不明。

近幾期變化（yf 快取）：
- -3m：4 Strong Buy + 8 Buy + 4 Hold = 16 家，BUY 佔比 75%
- -2m：6 Strong Buy + 12 Buy = 18 家，BUY 佔比 100%
- -1m 與 0m：19 家，BUY 佔比 100%
- 趨勢：Hold 評等全部消失，BUY 家數由 12 增至 19。無 Sell 評等。

第三方彙整（WebSearch，標示為 2026 年中）：16 家，12 Buy / 4 Hold / 0 Sell，**BUY 佔比 75%**。平均目標價約 5,454 TWD，最高 7,500、最低 2,500。與 yf 快取在家數上不一致，應視為區間，不宜精確解讀。

近期個別券商動向（日期不一，需留意）：
- 里昂：目標價由 3,600 上調至 6,000，維持「優於大盤」，理由是 CPU 與 ADAS 動能擴大、首季 EPS 12.28 元高於預期。
- 大和資本：目標價由 2,450 上調至 2,920，維持「買進」，理由是 AI 客戶基礎擴大。
- 摩根士丹利：「優於大盤」，目標價 3,288（較早報告）；另一彙整來源列為 5,688，兩者不一致。
- 花旗：Buy，目標價 6,000（彙整來源）。花旗引用管理層說法，上半年營收偏低、下半年明顯提升。
- 野村 5,800、摩根大通 5,500：皆為 2026 年 3 月資料，可能已過時。

股價與估值（資料衝突）：
- MONEY LINK 顯示 8/12 收盤 5,130 元。其他快照出現 2,175、2,475、3,805 等價位。
- 10/19 收盤價未能確認，無法計算目標價上行空間。若以 8/12 價位對照，平均目標價 5,454 略高於現價，上行空間有限。
- Simply Wall St DCF 公允價值 NT$590.7，遠低於市價，屬少數派估值觀點。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：WebFetch 被阻擋（Claude Code 無法存取 www.reddit.com）。soft-fail，無資料。
- StockTwits：DNS 解析失敗（api.stocktwits.com），soft-fail，無資料。
- PTT 股票板、Dcard：無法直接存取，僅能經搜尋引擎取得。搜尋未找到近期討論串。
- 替代來源：CMoney 股市爆料同學（cmoney.tw/forum/stock/3443）與 Mobile01 標籤頁（mobile01.com/tag.php?tag=3443）有討論串，但多為 2025 年以前的舊文。例：2025-01-30 技術面文章標題「月線來看頸線位置是0.5 不構成M頭型態空頭走勢」，屬偏多，但已過時約一年半，不代表近期散戶情緒。
- X 與新聞評論：未取得可靠的近期貼文樣本。

Retail buzz volume：無法量化。新聞覆蓋在 8 月至 9 月明顯增加（8/3 盤中大漲近 10%、9/24 列為處置股、期交所調高保證金），顯示市場關注度高，但未取得 10 月的聲量數據。

Retail tilt：無法判定。可觀察到的媒體與論壇內容偏多，但多數為舊文，不足以代表 10 月的散戶看法。

Themes（從新聞與論壇歸納）：
- 雲端服務商（CSP）自研晶片與 ASIC 題材，CPU 與加速器出貨放量
- ADAS 與車用晶片需求
- 台積電持股約 35%，「台積電親兒子」相關題材
- 波動風險：處置股、保證金調高、短線漲幅過快
- 基本面：2026 年 1 至 5 月營收 204.16 億元，年增 90.6%；5 月營收 46.74 億元，年增 132.1%
- 指數納入：富時羅素自 2026 年 6 月起納入台灣 50 指數

## Insider activity
Net 6mo：**無法確認**。yf insider 回傳空陣列，本次未取得買賣明細。

- Yahoo 持股資料：內部人持股比例 36.68%（與台積電約 35% 持股大致相符，但兩者口徑未核對）。
- 未找到 2026 年董監持股申報（MOPS）的資料。
- 無法判定 CEO、CFO 或其他董監是否有買進或賣出。

## Ownership shifts（機構持股）
- 機構持股比例 33.52%，流通股中機構持股 52.93%，機構家數 223。
- 快照僅有單期，無時間序列，無法判斷集中度趨勢。
- 三大法人買賣超：未取得 2026 年資料。已有資料皆為 2025 年（9/23 外資賣超 378 張、投信賣超 27 張；2025 年 10 月外資買超 925 張、投信買超 691 張），時間過舊，不作為當前流向依據。
- **機構流向方向：未驗證。**

## Net sentiment score
Composite：**偏多（bullish），信心中低**

依據與權重：
- 分析師（高權重）：偏多。yf 快取 100% BUY、彙整來源 75% BUY，目標價多數上調，Hold 評等減少。信心高，但快取日期不明，且 Yahoo 即時資料抓取失敗。
- 散輿論（中權重）：無法量化。新聞語氣偏多但伴隨高波動警訊。信心低。
- 內部人（中權重）：無資料，記為中性（未知）。
- 機構流向（中權重）：無當期資料，記為中性（未知）。

Divergence flag：**無法判定**。缺乏當期散戶樣本，無法與分析師傾向比較。若後續取得 10 月的 PTT 或 Dcard 資料，應重新評估。

## 資料缺口與限制
1. Yahoo 即時抓取失敗，analyst 數字來自 repo 快取，快取日期不明。
2. 收盤價與目標價來源衝突，10/19 價位未確認。
3. Reddit、StockTwits 無法存取，PTT、Dcard 無近期樣本。
4. 內部人交易與三大法人買賣超無 2026 年資料。
5. 以上內容為資訊整理，不構成投資建議。

## 參考來源
- yf 工具輸出：recommendations、rec_summary、insider、major_holders（3443.TW）
- [MONEY LINK 創意股價與技術頁](https://ww2.money-link.com.tw/TWStock/StockChart.aspx?SymId=3443)
- [鉅亨網 創意營收速報](https://news.cnyes.com/news/id/6219545)
- [工商時報 / 經濟日報 創意 Q1 CSP 出貨相關報導](https://www.ctee.com.tw/news/20260409700295-430203)
- [UDN 創意題材護體 外資按讚](https://money.udn.com/money/amp/story/5607/9304556)
- [UDN 創意早盤攻上漲停 本月飆逾65%](https://money.udn.com/money/amp/story/5607/9452393)
- [CMoney 股市爆料同學 3443 討論區](https://www.cmoney.tw/forum/stock/3443)
- [Mobile01 3443 標籤頁](https://www.mobile01.com/tag.php?tag=3443)
- [Simply Wall St 3443 估值頁](https://simplywall.st/stocks/tw/semiconductors/twse-3443/global-unichip-shares/valuation)
- [MarketScreener 3443 consensus](https://ca.marketscreener.com/quote/stock/GLOBAL-UNICHIP-CORP-6498981/consensus/)

SENTIMENT REPORT COMPLETE
