# News — CBRS as of 2026-11-09

## 資料核對說明
- CBRS 在 Yahoo 資料中解析為 **Cerebras Systems Inc.**（Nasdaq GS，產業 Semiconductors，sector Technology，2026-05-14 IPO，發行價 $185）。這與半導體板塊的定位相符，故本報告以 Cerebras 為分析對象。
- 使用者提到的 **Caris Life Sciences** 代號為 **CAI**（Nasdaq），並非 CBRS。本報告不涵蓋 Caris，避免混淆。
- `pipeline/tools/yf CBRS news` 因代理 403 無法取得新聞列表，新聞改以 WebSearch 彙整。yf `info` 可用，但其 `regularMarketTime` 時戳落在週六（2026-11-07），顯示為快取資料，價格與 MarketBeat 2026-11-06 報導的 +9.8% 漲幅一致，以 11/6 收盤為準。
- 所有資料截止 2026-11-09；之後的事件一律視為未知。來源日期互相矛盾之處已於內文標註。

## 基本面快照（yf info，快取）

| 指標 | 數值 | 單位 |
|---|---|---|
| 最新收盤價 | 89.68 | USD |
| 前收盤價 | 81.71 | USD |
| 單日漲跌 | +7.97（+9.75%） | USD / % |
| 市值（以 implied shares 237.6M 計） | 21.3 | B USD |
| 企業價值 EV | 14.9 | B USD |
| 現金及等價物 | 7.9 | B USD |
| TTM 總營收 | 0.68 | B USD |
| 52 週區間 | 77.84 – 386.34 | USD |
| 分析師平均目標價 / 中位數 | 275.3 / 290 | USD |
| 分析師評等 | 1.27（Strong Buy，11 家） | — |
| 空單佔流通股 | 17.7%（約 19.9M 股） | % |

核對：市值 21.3B USD ÷ 收盤價 89.68 ≈ 237.5M 股，與 implied shares 一致。但 yf 的 `sharesOutstanding` 為 112.2M，兩者差距約一倍，可能與股份類別或快取計算有關，使用市值時需留意。

## Top company-specific headlines (last 14d)
- 2026-10-28 — Short seller Culper Research 公開放空 CBRS，主張晶圓級晶片實際壽命僅約 1.5–2.5 年（18–30 個月），遠短於 IPO 文件所稱的 3–5 年；並指出散熱膨脹問題未解決、連接器材料來自外部供應商，部分證據來自匿名前員工與客戶（letsdatascience、DatacenterDynamics、technews.tw、TIKR 彙整）。Impact: **bearish**。這是本期最大的負面敘事，直接挑戰產品耐用性與 IPO 揭露。Culper 自稱可能隨時進出倉位。市場反應說法不一（約 -4% 至 -10%）。獨立佐證僅見 2026 年 4 月哈佛與 Meta FAIR 相關加速器研究，尚未被驗證。
- 2026-11-02 — 股價創下歷史新低，單日約 -11.7%；自 8/4 高點起算，至 11/2 累計跌約 57.6%，同期 S&P 500 約 -2.3%（Benzinga、Motley Fool 彙整）。Impact: **bearish**。反映放空報告與鎖定期壓力的集中釋放，技術面與情緒面皆轉弱。
- 2026-11-02 左右 — UBS 將目標價由 330 下調至 250，維持 Buy 評等（Startup Fortune、Trefis 彙整）。Impact: **bearish（偏弱）**。目標價大幅下修，但評等未降，屬於估值回調而非基本面否定。
- 2026-11-06 — 股價反彈 +9.75%（Morningstar 收 89.68；Yahoo 報 +10.12%；MarketBeat 報 +9.8%）。Impact: **neutral**。來源未指出明確催化劑，僅能視為超跌與空單回補的情緒性反彈，無法確認是否具持續性。
- 2026-11-09 左右 — 鎖定期解除（lockup）大批股份可交易，最終到期預估為 11/9 或 11/10（Benzinga、Startup Fortune 彙整）。Impact: **bearish**。供給壓力疊加於放空報告之上。來源對日期說法不一，見下方「未確認事項」。

### 背景事件（超出 14 天或日期不明，僅供參考，未計入 14 天統計）
- Q2 財報（2026-08-12）：GAAP 營收 180M USD（+74% YoY），core 營收 210M USD（+103%）；FY2026 core 營收指引由 855–865M USD 上調至 880–890M USD；core 毛利率指引 41–43%；RPO 逾 25B USD。雖然指引上調，股價仍下跌。core 與 GAAP 差異主要來自 pass-through 收入與股票報酬等非核心項目。
- OpenAI 合作：Wedbush 指出 OpenAI 於超快速模型層使用 Cerebras 晶片，視為既有合作進展，約 750MW 產能承諾至 2028 年，並有延長至 2030 年的空間（個股大漲約 15%）。**發布日期無法確認**，未計入 14 天統計。合約金額說法不一（10B 至 20B USD 等版本）。
- Oracle：有報導稱雙方宣布將 Cerebras 推論能力整合進 OCI，預計 2027 年可用；另一來源描述為 Oracle 成為客戶，兩者關係描述不一，**日期與性質均未確認**。

## Sector macro
- 2026-12-08～09 — FOMC 會議（Fed 官網行事曆），Dec 9 決議，為年內最後一次會議。位於 14 天窗口之外，列入遠期背景。Impact on 半導體 / AI 基礎建設：利率路徑影響高估值成長股的折現率，對 CBRS 這類 EV 為 14.9B USD、仍為虧損的標的敏感度高。當前政策利率來源不一（3.50–3.75%），未經 Fed 原始資料核實。
- AI 資本支出情緒：本期 AI 晶片股整體偏弱，有 AI 族群拋售報導（德文來源，日期不明）。Impact on 半導體：情緒面為主要壓力，但未能取得可驗證的具體總經數據。
- 供應鏈與客戶集中：CBRS 的 backlog 高度集中於 OpenAI（約 80%），屬於單一客戶風險；Impact on 半導體：若 OpenAI 相關支出或時程變動，會直接影響營收可見度。

## Peer signals
- AMD — 2026-11-03 盤後財報（預期營收約 13.1B USD，EPS 公告結果未取得）。本次未能確認結果與股價反應，無法評估對 CBRS 的外溢效果。
- NVDA — 財報日期未確定（Earnings Whispers 列 11/25；ChartRow、The Right Trader 列 11/18，後者稱未經公司確認）。Nvidia 財報將是 AI 晶片族群的重要情緒事件，需待 IR 網站確認。
- Culper Research 同時有報導對 NVDA 建立空單（以中國市場關聯為理由），日期不明，僅作為空方對 AI 晶片標的的集中關注參考。

## Forward calendar (next 14d, 至 2026-11-23)
- 2026-11-09 ~ 11-10 — 鎖定期大批解除（來源日期互相矛盾，見未確認事項）。Expected impact: **bearish**，供給壓力與短線波動放大。
- 2026-11-12（週四）盤後 — Cerebras 2026 Q3 財報與電話會議（PT 下午 2 點，ET 下午 5 點；公司官方新聞稿）。Expected impact: **高度不確定，兩向皆可能**。Q3 core 營收指引 214–216M USD，core 毛利率指引 38–40%，core 營業利益率指引 -25% 至 -23%；CFO 表示 Q3 為毛利率低點。市場關注毛利率是否觸底、FY 指引能否維持，以及 Culper 報告的回應。
- 2026-11-13 — 財報後的首個交易日，波動性預期較高（依 Q1 與 Q2 財報後股價皆下跌的歷史，風險偏向負面）。
- 2026-11-18 或 11-25 — NVDA 財報（日期未確認），AI 晶片族群情緒催化劑。
- 窗口內無已確認的 FOMC 會議（下次為 12/8–9，超出窗口）。

## 未確認事項（需於下次更新時核實）
- 鎖定期日期：Benzinga 與 Startup Fortune 說 11/9 至 11/10；另有說法稱 10/1 已到期並伴隨約 84M USD 內部人出售；另有說法稱 180 天鎖定約在 2026 年 11 月中旬。建議以 SEC 文件（招股說明書或 Form 4）核實。
- Culper 放空的具體股價反應（-4% 或 -10%）以及 Cerebras 是否已正式回應，未在來源中確認。
- OpenAI 合約金額（10B / 20B / 30B 版本）與 Wedbush 的 +15% 事件日期。
- Oracle 合作性質與時程。
- SEC 文件中 Q3 財報的指引標籤有誤（"Third Quarter 2026 Financial Outlook" 列 880–890M USD，實為 FY 數字），以公司新聞稿的 Q3 數字為準。

## Net read
本期 CBRS 的新聞流以負面為主，淨傾向為**偏空（bearish），強度中高**。主要負面包括 10/28 Culper 對產品壽命的放空報告、11/2 歷史新低與 UBS 目標價下修、以及 11/9 前後的大批鎖定期解除，三者同時壓在股價上。加上 17.7% 的高空單比例，短線波動性會被放大。相對正面的因素有：8 月上調的 FY2026 core 營收指引（880–890M USD）、Strong Buy 的分析師共識（平均目標價 275 USD、收盤價折價約 67%）、現金 7.9B USD 足以支撐營運、以及 11/6 單日 +9.75% 的反彈，但該反彈未有可確認的基本面催化劑。接下來 14 天最重要的事件是 11/12 Q3 財報，它將決定 Culper 報告與毛利率疑慮能否被數字化解。未來的風險要點包括：毛利率是否觸底、OpenAI 集中度、以及鎖定期解除後的籌碼消化。

## Sources
- [Cerebras Systems Q3 2026 earnings date (investors.cerebras.ai press release, via finviz)](https://www.cerebras.ai/press-release/cerebras-systems-announces-date-of-third-quarter-2026-financial-results-3384934)
- [Why Cerebras Systems Stock Is Plummeting Today (Motley Fool, 2026-11-02)](https://www.fool.com/investing/2026/11/02/why-cerebras-systems-stock-is-plummeting-today/)
- [Cerebras Stock Hits All-Time Low (Benzinga)](https://www.benzinga.com/trading-ideas/movers/26/11/62794514/cerebras-stock-hits-all-time-low-whats-happening)
- [Cerebras Systems Stock Price Up 9.8% (MarketBeat, 2026-11-06)](https://www.marketbeat.com/instant-alerts/price-cerebras-systems-nasdaq-cbrs-stock-price-up-98-heres-why-2026-11-06/)
- [Cerebras stock has fallen 39% from its peak as lockup and earnings collide (Startup Fortune)](https://startupfortune.com/cerebras-stock-has-fallen-39-from-its-peak-as-lockup-and-earnings-collide/)
- [Did The Market Read Cerebras Stock Right? (Trefis, 2026-11-03)](https://www.trefis.com/stock/cbrs/articles/622303/did-the-market-read-cerebras-stock-right/2026-11-03)
- [Short Seller Culper Research Alleges Cerebras Wafer Chips Last Only 1.5 to 2.5 Years (letsdatascience)](https://letsdatascience.com/news/short-seller-culper-research-alleges-cerebras-wafer-chips-la-e92b69e1)
- [Cerebras chips have shorter lifespans than statements suggest (DatacenterDynamics)](https://datacenterdynamics.com/en/news/cerebras-chips-have-shorter-lifespans-than-statements-suggest-short-seller-report-claims)
- [Cerebras Sinks 10% as Short Seller Culper Claims (TIKR)](https://www.tikr.com/blog/cerebras-sinks-10-as-short-seller-culper-claims-its-wafers-break-down-after-just-2-years)
- [Cerebras Raises 2026 Outlook as Q2 Core Revenue Doubles (letsdatascience)](https://letsdatascience.com/news/cerebras-raises-2026-outlook-as-q2-core-revenue-doubles-899f6a8c)
- [Cerebras Systems Q2 earnings call highlights (MarketBeat, 2026-08-12)](https://www.marketbeat.com/instant-alerts/cerebras-systems-q2-earnings-call-highlights-2026-08-12/)
- [Cerebras Shares Jump 15% as Wedbush Flags Bigger OpenAI Deal Opportunity (GuruFocus)](https://www.gurufocus.com/news/9038597/cerebras-shares-jump-15-as-wedbush-flags-bigger-openai-deal-opportunity)
- [Cerebras Faces Fast IPO Lockup Release (letsdatascience)](https://letsdatascience.com/news/cerebras-faces-fast-ipo-lockup-release-8d4f562d)
- [Nvidia earnings date (Earnings Whispers)](https://beta.earningswhispers.com/go/x/NVDA)
- [FOMC Meeting Schedule — December 2026 (fedratecalc)](https://fedratecalc.com/fomc-meeting-schedule/december-2026/)
- [December 2026 FOMC (Federal Reserve)](https://www.federalreserve.gov/newsevents/2026-december.htm)

NEWS REPORT COMPLETE
