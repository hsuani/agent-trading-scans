# Sentiment — AMT as of 2026-11-21

資料說明：`yf.py` 無 `ratings` / `holders` 子命令，改用 `rec_summary`、`recommendations`、`major_holders`、`inst_holders`。Reddit 直接抓取被擋（WebFetch 回傳無法存取），改以 WebSearch 補充。StockTwits 與 X 無可用的當期資料。所有數字以工具輸出或來源頁面為準，來源日期晚於 2026-11-21 的資料一律不採用。

## Analyst consensus

結構化資料（`rec_summary` / `recommendations`，截至 0m 期）：Strong Buy 7 / Buy 16 / Hold 3 / Sell 0 / Strong Sell 0，合計 26 家。近四個月分布幾乎不變（-1m 至 -3m 為 7 SB / 15 B / 3 H / 0 S），沒有評級下修紀錄。

目標價（WebSearch 彙整，來源日期不一）：平均目標價約 $215.8 至 $217.5，高點 $260、低點 $185。來源之間的數字有差異，應以當期 tracker 為準。

近期評級動作（依 WebSearch 結果，未能確認 2026-11 當月的評級變動）：
- Bernstein 於 2026-05-19 由 Market Perform 升至 Outperform，目標價 $207。
- Mizuho 由 Neutral 升至 Outperform，目標價由 $189 調至 $205（日期未明，應為 2026 年中後）。
- TD Cowen 於 2026-07-29 維持 Buy，目標價 $227。
- BMO Capital 於 2026-07-29 維持 Market Perform，目標價 $195。
- RBC 於 2026-04-30 維持 Hold，目標價 $195。

未發現 2026-11 的降評或目標價大幅修改的紀錄。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: DATA_UNAVAILABLE。直接抓取被擋；WebSearch 也找不到 2026 年 AMT 相關的 WSB 或 r/stocks 討論串。沒有迷因式或爆量討論的跡象，但這不能代表討論量很低，只是查不到。
- **LunarCrush 主題頁（間接資料）**: 頁面提到 Reddit 上對 AMT 投資 AST SpaceMobile（ASTS）的討論整體偏正面。頁面資料為佔位資料，可信度低。
- **StockTwits**: DATA_UNAVAILABLE（當期情緒儀表讀數）。可查到的 StockTwits 相關頁面都是 2025 年的新聞，其中 2025 年 4 月 Morgan Stanley 升評後情緒由偏空轉為中性。AltIndex 在 2026-07 統計訂閱者約 6,871 人，近三個月持平。
- **X / 網路聊天**: 查無 2026-11 的可靠貼文樣本，DATA_UNAVAILABLE。
- **Seeking Alpha 留言（約 2026-04）**: 偏空。留言者把塔類 REIT 的弱勢歸因於利率上升，以及衛星寬頻（Musk 相關計畫）的競爭。這是單頁、時間較早的少量樣本，證據力弱。
  - 引述（短句）：「$CCI $AMT collapsing」，取自 2026-04 的留言。
- **Retail buzz volume**: 無量化數字可用。定性判斷為低至中等，沒有可見的爆量現象。

- **Retail tilt**: 偏中性至偏空，但證據薄弱，信心低。
- **主要主題**:
  1. 利率環境對 REIT 估值的壓力。
  2. 衛星寬頻與 5G 相關的競爭疑慮。
  3. 數據中心業務與 AST SpaceMobile 的策略投資（偏正面）。
  4. 相對 SBAC、CCI 等同業的表現比較。

## Insider activity

以 2026-05-21 至 2026-11-21 為 6 個月窗口，只計公開市場買賣（不含 Stock Award 與 Stock Gift）：

| 日期 | 內部人 | 職稱 | 方向 | 股數 | 金額 (USD M) | 備註 |
|---|---|---|---|---|---|---|
| 2026-08-21 | Rajesh Kalathur | Director | 買入 | 2,829 | 0.50 | 每股 $177.00 |
| 2026-07-29 | Robert Joseph Meyer Jr. | Officer | 賣出 | 5,000 | 0.89 | 每股 $178.89 |
| 2026-07-29 | Ruth T. Dowling | General Counsel | 賣出 | 1,791 | 0.31 | 每股約 $169.5 至 $175.0 |
| 2026-10-30 | Juan Hernandez Font | Officer | 賣出 | 592 | 0.11 | 每股 $189.63 |

- **6 個月淨額**: 買入 $0.50M（1 筆，Director），賣出 $1.32M（3 筆，含 General Counsel 與 Officer），淨賣出約 $0.82M。
- **CEO / CFO**: 窗口內無 CEO（Steven Vondran）或 CFO（Rodney Smith）的公開市場交易。
- **窗口外的重要紀錄（僅供背景）**:
  - CEO Vondran 於 2026-03-04 賣出 33,482 股，約 $6.31M，同日有 $94.71 的選擇權行權轉換。
  - CFO Smith 於 2026-02-17 賣出 34,341 股，約 $6.60M，同樣伴隨選擇權行權。
  - COO Eugene Noel 於 2026-03-02 賣出 41,209 股，約 $7.87M，同樣伴隨選擇權行權。
  - Director Kalathur 於 2026-03-10 買入 2,671 股，約 $0.49M，每股 $185.30。
- 2025-10-31 Director Eugene Reilly 買入約 $0.99M，屬窗口外。

整體解讀：近六個月內部人以賣出為主，但金額遠小於 2026 年 2 月至 3 月的大額賣出，且多為行權後賣出，性質偏向資產配置。唯一的公開市場買入來自獨立董事。

## Ownership shifts

- 內部人持股約 0.1%（`major_holders`）。
- 機構持股約 98.1%，機構數 2,410 家。
- 13F 報告期為 2026-09-30，前十大持股合計約 42.0%。

| 機構 | 持股比 | 股數 (M) | 季度股數變化 |
|---|---|---|---|
| BlackRock | 9.79% | 45.40 | -0.86% |
| Vanguard Capital Mgmt | 6.58% | 30.50 | +0.21% |
| Vanguard Portfolio Mgmt | 6.01% | 27.86 | +0.04% |
| State Street | 4.79% | 22.19 | +0.58% |
| Geode Capital | 3.07% | 14.24 | +2.92% |
| Cohen & Steers | 2.62% | 12.15 | -11.79% |
| FMR | 2.55% | 11.85 | +4.13% |
| Lazard Asset Mgmt | 2.36% | 10.92 | +29.98% |
| JPMorgan Chase | 2.28% | 10.58 | +19.45% |
| Invesco | 1.97% | 9.14 | +29.31% |

趨勢：主動型基金多數加碼（Lazard、Invesco、JPMorgan、FMR），被動型持股幾乎持平，Cohen & Steers 明顯減碼約 11.8%。機構面整體偏中性偏多，沒有集中式的撤退跡象。

## Net sentiment score

**綜合判斷：中性偏多（信心：中低）**

- 分析師面：偏多。26 家中 23 家為 Buy 或 Strong Buy，無賣出評級，平均目標價高於 2026-11 的股價區間（約 $183 至 $188）。
- 內部人面：小幅偏空。6 個月淨賣出約 $0.82M，且無 CEO / CFO 的公開市場交易。
- 機構面：中性偏多。前十大持股多數加碼，無大規模撤出。
- 散戶面：中性偏空，但證據薄弱。Seeking Alpha 留言偏空，LunarCrush 偏正面，WSB、StockTwits、X 皆無可用資料。
- 價格背景：WebSearch 顯示 AMT 於 2026-11-17 單日下跌約 4%，收在約 $183.18，盤中區間 $182.92 至 $190.74。下跌原因在本次搜尋中未查到。

**Divergence flag: 是（弱）**。分析師與機構的傾向偏多，而可查到的散戶與內部人賣出傾向偏中性至偏空。但散戶端樣本太少，這個背離訊號的參考價值有限。

## 限制與缺口

- Reddit、StockTwits、X 的當期情緒與聲量數據無法取得，均標註為 DATA_UNAVAILABLE。
- 分析師目標價與股價在不同來源間有差異，部分來源未標註日期。
- 2026-11-17 的單日下跌原因未查到，可能影響後續情緒判讀。
- 任務指定的 as-of 日期為 2026-11-21，本報告使用的最新價格資料為 2026-11-17，無晚於 2026-11-21 的資料被採用。

SENTIMENT REPORT COMPLETE
