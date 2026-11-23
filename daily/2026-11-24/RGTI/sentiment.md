# RGTI 情緒分析報告

- 標的：RGTI (Rigetti Computing)
- 報告日期：2026-11-24（資料截止約 2026-11-23）
- 資料來源：`pipeline/tools/yf.py`（rec_summary、recommendations、major_holders、inst_holders、insider；Yahoo cookie/crumb 取得失敗，資料為 cache）、WebSearch（Stocktwits、Investing.com、TIKR 等）

> 注意：部分新聞與價格資料僅到 2026-11-11 左右，且各來源股價互相衝突（Benzinga 與 Motley Fool 數字不一致），以下價格僅供參考，未經驗證。

---

## 1. Analyst Consensus（分析師共識）

### 1.1 評等分布（rec_summary，最近三期）

| Period | strongBuy | buy | hold | sell | strongSell | 總家數 | Weighted Rating Score (5=SB, 1=SS) |
|---|---|---|---|---|---|---|---|
| 0m（本月） | 1 | 8 | 4 | 1 | 0 | 14 | 3.64 |
| -1m | 1 | 8 | 4 | 0 | 0 | 13 | 3.77 |
| -2m | 1 | 8 | 4 | 0 | 0 | 13 | 3.77 |

觀察：
- 本月新增 1 家 sell，評級分數由 3.77 降至 3.64，評等偏向整體「Buy」但有退溫跡象。
- 與 `recommendations` 輸出一致（與 rec_summary 同源）。

### 1.2 目標價（WebSearch 彙整，2026-11-11 前後）

| 券商 | 評等 | 目標價 | 變動 |
|---|---|---|---|
| Needham | Buy | $15 | 由 $31 下調（-52%） |
| Mizuho | Outperform | $17 | 由 $22 下調 |
| Alliance Global Partners | Buy | $22 | 由 $37 下調 |
| StoneX | Buy | $20 | 由 $25 下調 |
| B. Riley | Buy | $23 | 由 $25 下調（11/9） |
| Jefferies | Hold | $12 | 下調 |

- 共識目標價約 **$26**（13 位分析師），較去年約 $34、2025 年 12 月約 $42 明顯下滑。
- Investing.com 另有平均目標價約 $29.65（12 位），但無日期，可能過時。
- 催化劑：Q3 營收低於預期，第四季指引低於共識（Mizuho 預估 $9.1M vs 共識 $9.7M）；C-DAC 系統是否於年底驗收為關鍵觀察點。

**評語**：評等結構仍偏多（約 9 成為 Buy 以上），但目標價連續下修，顯示分析師對短期營收時程與估值信心下降。

---

## 2. Institutional Holdings Trend（機構持股趨勢）

### 2.1 總體持股（inst_holders）

| Metric | Value |
|---|---|
| insidersPercentHeld | 1.69% |
| institutionsPercentHeld | 50.75% |
| institutionsFloatPercentHeld | 51.62% |
| institutionsCount | 636 |

### 2.2 前十大機構（major_holders，最新報告期多為 2026-09-30）

| Holder | pctHeld | Shares | pctChange（季度） |
|---|---|---|---|
| BlackRock Inc. | 7.95% | 27,239,052 | -4.54% |
| Vanguard Portfolio Mgmt | 5.98% | 20,511,108 | +3.06% |
| Vanguard Capital Mgmt | 4.38% | 15,002,227 | +3.98% |
| State Street Corp. | 3.74% | 12,821,240 | +8.41% |
| Geode Capital Mgmt | 2.52% | 8,646,880 | -0.31% |
| Morgan Stanley | 1.76% | 6,029,101 | +27.52% |
| Shaw D.E. & Co. | 1.17% | 4,021,708 | -25.03% |
| Unicom Systems | 1.03% | 3,521,935 | 0.00% |
| Penserra Capital Mgmt（6/30） | 1.00% | 3,420,579 | +110.36% |
| Van Eck Associates | 1.00% | 3,411,641 | +80.47% |

**趨勢判讀**：
- 被動型基金（Vanguard、State Street、Geode）多持平或小幅加碼，屬指數資金的被動配置，對情緒訊號有限。
- 主動型機構動向分歧：Morgan Stanley、Van Eck、Penserra 明顯加碼；Shaw D.E. 減持 25%；BlackRock 減持約 4.5%。
- 整體屬「機構持股約半數、主動資金小幅淨加碼但分歧」，無明顯一面倒的撤離或建倉。

---

## 3. Insider Transactions（內部人交易）

### 3.1 近期交易（約 2026-08-20 至 2026-11-23）

| 日期 | 內部人 | 職位 | 類型 | 股數 | 價格 | 金額（USD） |
|---|---|---|---|---|---|---|
| 2026-11-20 | Bertelsen Jeffrey A | CFO | Sale | 3,979 | $7.79 | 30,996 |
| 2026-11-20 | Rivas David | COO | Sale | 9,277 | $7.78 | 72,148 |
| 2026-09-09 | Kulkarni Subodh K | CEO | Sale | 120,000 | $15.68 | 1,882,104 |
| 2026-09-09 | Kulkarni Subodh K | CEO | Option exercise | 150,000 | $0.96 | 144,570 |
| 2026-09-03 | Bertelsen Jeffrey A | CFO | Sale | 25,000 | $15.00 | 375,010 |
| 2026-09-03 | Bertelsen Jeffrey A | CFO | Option exercise | 25,000 | $0.60 | 15,000 |
| 2026-08-20 | Bertelsen Jeffrey A | CFO | Sale | 3,860 | $16.89 | 65,187 |
| 2026-08-20 | Rivas David | COO | Sale | 9,038 | $16.79 | 151,734 |

- 約 3 個月內，**公開市場賣出合計約 $2.58M**（不含選擇權行使），全部為 CEO / CFO / COO 等高階主管，**未見公開市場買入**。
- 11/20 的小額賣出價格約 $7.8，為近期低點區間，屬於低價位仍賣出。
- 部分小額賣出與選擇權行使成對出現，可能屬於行權後賣出或稅務性質，需與 SEC Form 4 原文核對，此處未確認。

### 3.2 較早期交易（參考）

- 2026 年 6 月：Johnson Ray O（董事）賣出約 $4.3M（6/8 與 6/22）；Kulkarni 於 6/1 賣出約 $2.6M；Rivas 於 5/29 賣出約 $12.7M。
- 2025 年下半：Clifton、Iannotti、Sandford 等董事持續減持，Rivas、Bertelsen 亦有定期出售。
- 整體 12 個月以上趨勢為**持續性淨賣出**，且賣出價格高於現價。

**評語**：內部人淨賣出為持續性模式，近期賣價隨股價下滑而降低，不見逢低承接的買入訊號。

---

## 4. Retail / Social Sentiment（散戶與社群情緒）

| 面向 | 觀察 | 來源與時間 |
|---|---|---|
| Stocktwits 情緒 | 財報前後由「bullish」轉為「neutral」，財報後出現「extremely bullish」描述，訊息量大增（單日 +444%） | Stocktwits，約 11/11 前後 |
| 散戶論點 | 有散戶認為「有更好的量子股」，對估值與營收不滿；另有逢低買入聲音 | Stocktwits |
| 空頭部位 | 做空股數 71.04M，占流通股約 21.65%，屬極高空單比例 | Finviz（財報前，日期未明） |
| 選擇權 | 50 日 call/put 成交量比 3.58，選擇權端偏多 | Finviz（財報前） |
| 價格敘事 | 年初至今跌幅超過 48%（截至 11/11）；散戶情緒受量子計算題材與營收時程影響 | 多來源 |
| Reddit | 未找到可用的 2026-11 資料 | — |
| X / 其他 | 未找到可用資料 | — |

**評語**：散戶情緒高度波動、以題材與短線交易為主；極高空單比例（約 21.65% 流通股）加上選擇權偏多，可能形成反彈時的軋空風險，但基本面（營收時程）未改善前，多頭敘事缺乏支撐。缺少 11/18–11/23 的情緒讀數。

---

## 5. Composite Judgment（綜合判斷）

評分範圍：-2（極度偏空）至 +2（極度偏多）。

| 構面 | 指標 | 判讀 | 分數 | 權重 | 加權 |
|---|---|---|---|---|---|
| Analyst Consensus | Weighted Rating Score 3.64；共識 PT $26，連續下修 | 評等仍偏多，但 PT 下修、本月出現 sell | +0.5 | 30% | +0.15 |
| Institutional Holdings | 機構持股 50.75%；前十大淨變動分歧 | 主動與被動分化，無明顯方向 | 0 | 20% | 0.00 |
| Insider Transactions | 近 3 個月公開市場賣出約 $2.58M，無買入 | 持續性淨賣出，低價位仍賣 | -1.5 | 25% | -0.375 |
| Retail / Social | 情緒波動、空單 21.65%、call/put 3.58 | 高波動、方向不明，軋空與追高風險並存 | 0 | 25% | 0.00 |
| **綜合** | | | | 100% | **-0.23** |

### 結論

- **綜合判斷：偏中性略偏空（Neutral to Slightly Bearish）**，綜合分數 -0.23。
- 主要支撐：分析師評等仍以 Buy 為主，極高空單比例具反彈的軋空潛力。
- 主要壓力：目標價連續下修、Q3 營收與第四季指引低於預期、內部人持續賣出（含近期低點賣出）。
- 關鍵觀察點：
  1. C-DAC 系統驗收是否於年底完成；
  2. 第四季財報（預計明年初）的營收與指引；
  3. 內部人是否出現公開市場買入（目前為零）；
  4. 空單比例變化與 Stocktwits 情緒是否延續極端值。
- 資料限制：新聞與價格資料截至約 11/11–11/18，11/18–11/23 的情緒與價格變化未能完全覆蓋；Yahoo cookie/crumb 失敗，yf 資料為 cache。

---

## 來源

- Stocktwits：RGTI Stock Falls Premarket On Weak Q3, Outlook（https://stocktwits.com/news-articles/markets/equity/rgti-stock-rigetti-earnings-miss-estimates-outlook-quantum-computing-commercialization/cNGDk2OR9B4）
- Stocktwits：Rigetti Attracts Strong Retail Buzz（https://stocktwits.com/news-articles/markets/equity/rigetti-attracts-retail-buzz-as-260-ytd-rally-stirs-valuation-concerns/ch6mXGDR3lk）
- Stocktwits：RGTI price target cut up to 52%（https://stocktwits.com/news-articles/markets/equity/rgti-stock-sees-its-price-target-cut-by-up-to-52-despite-quantum-fidelity-gains-company-sets-sights-on-1-000-qubit-system/cNGDAZ4R9Bq）
- TIKR：Alliance Global Cut Rigetti's Target（https://www.tikr.com/blog/alliance-global-cut-rigettis-target-from-37-to-22-it-still-sees-90-upside）
- TIKR：B. Riley 77% upside（https://www.tikr.com/blog/77-upside-for-rigetti-computing-b-riley-thinks-so-and-heres-how）
- Investing.com：Rigetti Computing consensus（https://au.investing.com/equities/rigetti-computing-inc-consensus-estimates）
- Nasdaq / Motley Fool：Rigetti 股價走勢（https://www.nasdaq.com/articles/rigetti-computing-stock-plunged-42-last-month-heres-why，https://www.fool.com/investing/2026/11/07/where-will-rigetti-computing-stock-be-in-3-years/）
- Finviz：Bulls pile on Rigetti ahead of earnings（https://finviz.com/news/419369/bulls-pile-on-rigetti-computing-stock-ahead-of-earnings）
- 本地資料：`pipeline/tools/yf.py`（RGTI rec_summary、recommendations、major_holders、inst_holders、insider）
