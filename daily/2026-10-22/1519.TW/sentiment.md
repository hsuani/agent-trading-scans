# Sentiment — 1519.TW (華城 Fortune Electric) as of 2026-10-22

資料狀態註記: Yahoo 即時 API 在本環境被封鎖 (ConnectionError)，`yf.py` 全部回落至 repo 快取 `prices/yf/1519.TW.json`（`_refreshed_at` 2026-10-22T11:37 UTC，`_misses` 為空）。`ratings` 與 `holders` 不是 yf.py 合法子命令，實際使用 `recommendations` 與 `major_holders`。Reddit 與 StockTwits 未抓取（任務指定廣泛搜尋改用 WebSearch；且 r/wallstreetbets、r/stocks 對台股覆蓋極低）。PTT / Dcard 搜尋無可用討論串。

## Analyst consensus
快取 `rec_summary` / `recommendations`（0m）: **8 家 — 3 strong buy / 5 buy / 0 hold / 0 sell**，無賣出或中性評等。
- 近 3 個月趨勢: -3m 為 2 SB + 4 B（共 6 家），目前增至 8 家，評等全部維持正向，無降評紀錄。
- 目標價（Yahoo 快取 info）: 平均 873.3、最高 970.0、最低 727.3（TWD）。
- 外部來源（WebSearch，日期不一，口徑不同）:
  - Citi 於 2026-04-20 由持有升為買進，目標價 1150（前次 2025-12-16 持有 850）。
  - 本土金控投顧 2026-03 維持買進，目標價由 1000 上調至 1050，依 2026、2027 年平均 40 倍本益比估算。
  - Investing.com 共識頁面一處 avg 963.6（約 2026-08 資料）、另一處 avg 856.99（未註明日期）。
- 近期盈餘: 快取 `earnings_dates` 近 4 次公告中 3 次 EPS 低於預估（2025-11 -19.4%、2026-05 -12.8%、2026-08 -6.6%），2026-03 持平。2026-08 實際 EPS 3.23 vs 預估 3.46。
- 解讀: 評等面高度一致偏多，但盈餘連續未達預估，分析師仍維持買進，表示市場接受對 AIDC 訂單能見度的長線論述。

## Retail social
- **Reddit**: 未抓取。
- **PTT / Dcard**: WebSearch 未找到可引用的 2026-10 討論串。無法量化提及數。
- **StockTwits / X**: 未取得。
- **新聞層級散戶敘事（WebSearch）**: 一篇報導（2026-04-04）描述早盤大漲 7% 後震盪收低、震幅 9.3%，業內人士歸因於散戶與當沖客比重高、主力高檔反向洗盤；屬單一媒體觀點，非共識。
- **聲量（定性）**: 無法與歷史基準比較。新聞曝光集中於 AIDC 訂單與月營收，散戶論壇聲量無可用資料，判定為「資料不足」。
- **Retail tilt**: 無法定論。新聞與券商口徑偏多；論壇口徑缺失。
- **Themes（從新聞與公司說法歸納）**:
  - AIDC（AI 資料中心）訂單: 公司稱接單逾 120 億元，外部報導在手訂單逾 300 億、能見度看至 2028（數字來源不一）。
  - 高毛利專案與美國外銷變壓器訂單，2026Q1 毛利率報導為 43.61%。
  - 產能擴充: 觀音 3B 廠預計 2026 年底完工、2027 Q1 投產，台中廠 2027 Q2 投產。
  - 估值爭議: 本益比約 44 至 50 倍（快取 trailingPE 44.3；Statementdog 約 49.8），散戶對高估值的看法未能觀察到。

## Insider activity
- **Yahoo 快取 `insider`**: 空陣列（live 與快取皆無資料）。6 個月淨買賣金額: **無法計算（DATA_UNAVAILABLE）**。
- **Wantgoo 股東結構（WebSearch）**: 董監持股比例 2026-09 底為 13.02%，2026-10-02 顯示 0.00%。此跳動極可能是資料揭露缺漏而非實際出售，需以 MOPS 申報核實，不可直接解讀為內部人賣出。
- **Poorstock（無日期）**: 單一高層質押比例約 37%，日期不明，僅供風險提示。
- 結論: 內部人交易面無法判定。

## Ownership shifts
- Yahoo 快取 `major_holders`: insidersPercentHeld 46.37%（TW 市場此欄位口徑可能包含大股東與關係人，不宜直接等同董監持股）、institutionsPercentHeld 13.09%、institutionsFloatPercentHeld 24.40%、機構數 173。
- 外資持股比例（Wantgoo，WebSearch）: 2026-10-02 為 17.96%，較 8 月略降。同期外資單日淨賣超（10-01、10-02）。
- 趨勢: 缺乏多期歷史序列，僅能指出 8 月至 10 月外資持股小幅下降，無法確認方向性轉折。

## Net sentiment score
- **Composite: 偏多 (bullish)，信心: 中低 (low-moderate)**
  - 分析師面（信心高）: 偏多。8 家全數買進、無降評、目標價中位數高於快取現價。
  - 盈餘面（信心中）: 偏空訊號。近 4 次公告 3 次未達預估，但分析師未因此降評。
  - 內部人面（信心低）: 無資料，不計分。
  - 散戶面（信心低）: 無可用資料，不計分。
  - 籌碼面（信心中低）: 外資小幅減碼，中性偏空。
- 價格參考: 快取現價 615 TWD；WebSearch 片段顯示 10/08 收盤約 692 TWD、9 月底約 699 TWD。快取與外部片段相差約 11%，需以快取時點與來源時間核對，本報告不據此判斷趨勢。

**Divergence flag: 無法判定（no）** — 分析師偏多，但散戶口徑缺乏可引用資料，無法比對是否背離。若後續取得 PTT / Dcard 或 StockTwits 資料，可重新評估。

## 資料缺口
1. Yahoo 即時 API 被封鎖，所有數據為快取（cached_at 2026-10-22 11:37 UTC）。
2. `insider` 無資料，淨買賣金額 DATA_UNAVAILABLE。
3. 目標價來源口徑不一（Yahoo 平均 873 vs Investing 963.6 vs 856.99 vs 投顧 1050），採用快取值並標示來源差異。
4. 無 PTT / Dcard / Reddit / StockTwits 可用資料。
5. 2026-10 的券商目標價調整未在搜尋中找到。

SENTIMENT REPORT COMPLETE
