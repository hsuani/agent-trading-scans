# News — MRVL as of 2026-10-12

資料說明：
- `pipeline/tools/yf MRVL news` 回傳 403（proxy CONNECT tunnel failed），本次新聞全部改用 WebSearch 補足。
- `pipeline/tools/yf MRVL info` 可用（cache，cached_at 2026-10-12 00:49 UTC）。最新價格快照為 2026-10-09 收盤 $275.28（prevClose $274.60），52 週高 $329.88。
- 多數新聞來源為二手（Stocktwits、Futurum、parameter.io、Admiral Markets 等），未取得 Marvell 官方 Investor Day 新聞稿或逐字稿，所有 Investor Day 數字需以 investor.marvell.com 核對。
- yf info 的 `nameChangeDate: 2026-10-11`、`prevName: Marvell Technology Group Ltd.` 疑為資料欄位殘留，未查到對應公司公告，不視為新聞。

## Top company-specific headlines (last 14d)

- 2026-10-06 — Investor Day：FY2031 營收目標 $70B–$90B（中點 $80B）；FY2028 營收展望上修至約 $20B（先前約 $18B）；FY2029 custom silicon 目標上修至 >$12B（先前 >$10B）；FY2031 custom 約 $30B、interconnect 約 $37.5B；可服務市場（TAM）上修至 CY2030 約 $400B；CFO Dan Durn 提出 FY2031 non-GAAP EPS >$30，gross margin 56%–59%（"$30 in '30"）。來源：Stocktwits、Futurum Group、parameter.io（二手報導）。Impact: bullish。長期目標大幅上修，若官方數字與二手報導一致，對估值中樞是實質利多；但數字未經官方文件核對，且 FY2031 為遠期假設。
- 2026-10-06 — Investor Day 當日股價反應：盤中上漲約 8%（單一來源，Stocktwits 類報導）。Impact: bullish。以 2026-10-09 收盤 $275.28 計，仍低於 52 週高 $329.88 約 16–17%；收盤幅度與是否延續未驗證。
- 2026-10-06 — CEO Matt Murphy 表示 $30B custom chip 目標 "not a stretch"，並提及有機會支撐約 $1T 估值（Stocktwits 報導）。Impact: neutral。屬管理層喊話，不是新事實，但會影響市場對 custom 業務的預期強度。
- 2026-10-02 — Piper Sandler（David O'Connor）維持 Buy，目標價 $270（來源：WebSearch 彙整之券商資料）。Impact: neutral。目標價低於當時股價（約 $271 附近），評等仍正面但上行空間有限。
- 2026-09-29 — Jefferies（Blayne Curtis）維持 Buy，目標價 $325。Impact: bullish，目標價高於現價約 18%。
- 分析師共識（yf info）：44 位分析師，recommendationMean 1.37（strong_buy），目標價均值 $337.99、中位 $350、高 $450、低 $210。Impact: bullish 偏多共識，但共識本身不構成新事件。
- 背景（14 日窗口外，供參考）：
  - 2026-08-27 — FQ2 FY27 財報：營收 $2.739B（YoY +37%，歷史新高）；FQ3 營收指引 $3.15B ±5%；FY27 營收約 $12B（二手）。Impact: bullish，是本次 Investor Day 上修的基礎。
  - 2026-07 — 與 Google 擴大 custom 半導體合作（TPU 生態系），Marvell 向 Google 發行最多約 5,900 萬股的 warrant。Impact: 中性偏空。warrant 若全數行使約占目前股本 877M 的 6.7%，屬稀釋風險；單一來源，需核對。
  - 2026-06-11 — CFO 異動：Dan Durn（前 Adobe CFO）自 2026-06-15 起接任，取代 Willem Meintjes（留任顧問至 2027-04）。Impact: neutral。Investor Day 由 Durn 主講，財務主導權已穩定。
  - 2026-02-02 — Celestial AI 收購完成：現金約 $1.3B（淨額約 $1.0B）加發行約 2,450 萬股，總對價約 $3.5B（10-Q）；另有 earnout 上限約 $5.5B，與累計營收 $2B（至 2029 年底）掛鉤；營收貢獻預計 FY28 下半年起。Impact: neutral to bullish，光學互連（optics）布局擴大，但 earnout 條款細節需以合約為準。

## Sector macro

- 2026-09-16 — FOMC 升息 25bp，目標區間升至 3.75%–4.00%，12-0 全票通過，為 2023 年 7 月後首次升息；9 月 SEP 2026 年底中位數 4.1%，隱含再升息一次。Impact on 半導體 / 高估值成長股：偏空。MRVL 目前 forwardPE 約 37.8x、beta 2.26，對利率與風險偏好變化敏感。來源：Admiral Markets、advisorperspectives 利率日曆等二手，未直接核對 federalreserve.gov。
- 2026-10-14（週三，08:30 ET）— 9 月 CPI 預計公布；預覽預估 headline YoY 約 3.6%–3.7%（前值 3.4%），core CPI 約 2.4%。Impact on 半導體: 若 CPI 高於預期，升息預期上升，對高 beta 半導體股是負面衝擊。日期來自多個二手日曆，建議到 bls.gov 核對。
- 2026-10-15（週四，08:30 ET）— 9 月 PPI 預計公布。Impact: 次要，與 CPI 同週放大利率波動。
- 2026-01-14 / 01-15 — 美國出口管制與關稅：Section 232 對一小部分晶片加徵 25% 關稅，與 H200 對中國銷售安排（政府抽成 25%）掛鉤；BIS 1/15 生效之規則將先進 AI 晶片對中國及澳門的審查由推定拒絕改為個案審查並附條件。Impact on MRVL: 中性偏空的尾部風險。來源非 10 月新聞，MRVL 對中國營收暴露在本次搜尋中未量化。
- 2026-11-10 — 依 2025 年末美中貿易協議，部分 Section 301 關稅豁免到期日延至此日。Impact: 若不再延長，會影響進口成本與供應鏈，屬需追蹤的政策節點（位於 14 日窗口外）。來源為二手摘要，需核對。
- 2026 年 7 月 — SOX 指數單月下跌 21%，為 2008 年 10 月以來最差月份；7/29 低點後反彈 21.3%（WTOP，8 月報導）。Impact: 板塊波動極高，對持有部位的風險管理是重要背景。
- 2026 年 Q2 — 全球半導體銷售創紀錄 $403.3B（Zacks，10 月前後文章）。Impact: bullish，支撐 AI 資本支出需求假說。
- 2026 年整體 — Bank of America 預估全球半導體銷售 2026 年年增約 30%、突破 $1T（較早預測，非近期更新）。Impact: bullish，屬背景。

## Peer signals

- AVGO — 10/06 已列為 catalyst 事件（akrostec 日曆，內容未驗證）。custom ASIC 為 Marvell 的直接競爭對手，9 月 7 日摘要指出 Broadcom 的 hyperscaler custom 晶片可能壓縮 AMD 市占，對 MRVL custom 業務亦構成同類競爭。AI 半導體營收數字來源衝突（$10.8B、+143% 對比 $16.7B、+221%），未能確定。Impact on MRVL: 競爭性利空，需持續追蹤 hyperscaler 設計案分配。
- NVDA — 最近一季營收約 $81.6B，YoY +85%；data center 約 $89B，+117%（二手，日期未確認）。Impact: 板塊基本面偏多，對 AI capex 需求為正面訊號。2026-06-02 Jensen Huang 在 Computex 稱 Marvell 為 "next trillion-dollar company"，MRVL 單日上漲約 18%（SentiSense 報導），為先前大幅事件驅動的參照。
- AMD / INTC — 2026 年 YTD 分別約 +195% 與 +230%（Motley Fool，日期含糊）。Impact: 資金輪動與估值擁擠的風險訊號，非 MRVL 直接事件。
- TSMC — 9 月合併營收於 10/08 公布（日曆列示，未核對數字）。Impact: 上游訂單的景氣溫度計，本次未取得具體數字，中性。

## Forward calendar (next 14d)

- 2026-10-14（週三）— 美國 9 月 CPI，預期對利率路徑與高 beta 半導體股有明顯影響（見 Sector macro）。
- 2026-10-15（週四）— 美國 9 月 PPI。
- 2026-10-12 至 10-26 窗口內：未查到 MRVL 公司層級的已確認事件（無確認之財報、Investor Day 已於 10/06 舉行、無已公告之 conference 或產品發表）。
- 2026-10-27–28 — FOMC 會議（多數日曆來源列示，但有來源質疑會議是否存在，需到 federalreserve.gov 核對）；預期維持利率不變，升息較可能落在 12 月或之後。位於 14 日窗口外的邊緣。
- 2026-11-10 — Section 301 關稅豁免到期日（見 Sector macro），窗口外。
- Q3 FY27 財報：日期未確認。yf `isEarningsDateEstimate: true`，估計值約 2026-12-01，需以 investor.marvell.com 公告為準；屬窗口外。
- 股息：yf 顯示 $0.06/股，除息日 2026-10-09（已過），付息日約 2026-10-29（估計）。Impact: 無實質影響。

## Net read

整體新聞傾向偏多，強度中高。核心驅動是 2026-10-06 Investor Day 大幅上修 FY2028 至 FY2031 的營收與 custom silicon 目標，以及 FQ2 FY27 營收年增 37%、FQ3 指引 $3.15B 的基本面延續性；分析師評等維持 Buy 且共識目標價約 $338，較 10/09 收盤價 $275.28 仍有約 23% 上行空間。但有三點需要保留：(1) Investor Day 數字多來自二手報導，未經官方新聞稿與逐字稿核對；(2) 總經層面，9 月升息後市場預期仍有再升息的可能，CPI（10/14）與 FOMC（10/27–28，存在日期爭議）是近期最大的利率風險事件，而 MRVL beta 約 2.26、forward PE 約 37.8x，對利率衝擊敏感；(3) custom silicon 面臨 Broadcom 的直接競爭，且 Google warrant 約 6.7% 的潛在稀釋尚未被市場完全定價（需核對）。綜合而言，公司面的 headline tilt 為偏多（中高強度），總經面則為偏空中性，兩者在近期窗口內呈現拉扯。本報告不含交易建議。

NEWS REPORT COMPLETE
