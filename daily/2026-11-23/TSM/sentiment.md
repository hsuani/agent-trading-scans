# Sentiment — TSM as of 2026-11-23

> 資料基準：yf 快取 `prices/yf/TSM.json`（refreshed 2026-11-22 14:32 UTC）與 WebSearch。Reddit / StockTwits 直接抓取未執行（依任務指示，reddit / stocktwits / nasdaq.com 以 WebSearch 間接取得）。股價與市值以 USD 計，市值以 B 為單位。

## Analyst consensus

rec_summary（yf 快取）：**6 Strong Buy / 14 Buy / 1 Hold / 0 Sell / 0 Strong Sell**，共 21 家。

| 期間 | Strong Buy | Buy | Hold | Sell |
|---|---|---|---|---|
| 0m（目前） | 6 | 14 | 1 | 0 |
| -1m | 6 | 14 | 1 | 0 |
| -2m | 6 | 14 | 1 | 0 |
| -3m | 6 | 12 | 1 | 0 |

- 近三個月的變化幾乎只有 Buy 家數增加 2 家（-3m 至 -2m 之間），沒有 Hold 或 Sell 的升降評等記錄，屬於評等穩定、偏多的狀態。
- 目標價（yf 快取 info，20 家）：平均 **586.7 USD**、中位數 560 USD、最高 1,000 USD、最低 440 USD。相對於快取現價 318.71 USD，平均目標價隱含約 +84% 上行空間。
- 不同來源數字不一致，需留意：WebSearch 結果提到 Benzinga 平均目標價約 521 USD（區間 210 至 670 USD），Barclays 目標 670 USD；BofA 於 11/17 重申 Buy、目標 390 USD。Barchart 計 19 家（16 Strong Buy / 2 Moderate Buy / 1 Hold），Stockchase 過去 12 個月計 38 筆（26 Buy / 7 Hold / 5 Sell）。彙整口徑不同，目前無法統一，以 yf 快取為主，其餘僅作交叉參考。
- 基本面錨點（快取）：EPS 最近一季 4.60 USD（對應預估 4.52，超出 1.67%）；下次財報 2027-01-14，EPS 預估 5.16 USD。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：本次未取得可用的直接貼文樣本。WebSearch 沒有找到該兩個版的近期 TSM 熱門主題，因此無法提供貼文級的語氣判讀，此項標記為**資料缺口**。
- **StockTwits / X / 新聞聚合**：
  - WebSearch 摘要（StockTwits 報導）指出 TSM 在半導體拋售期間登上 StockTwits 熱門榜（trending），散戶情緒曾上升至 bullish 區間，但同期股價在六個交易日中有五日以上下跌，累計跌約 11.5%。
  - Quiver Quantitative 的 AI 摘要語氣分歧：一則提及散戶慶祝市值突破 2,000B USD 與台灣政策放寬單一股票投資上限；另一則提到部分聲音認為是買點，其他人則擔心短線波動。這些摘要的日期不明，**可能不反映本週情況**，僅作背景。
  - 聲量（buzz volume）：定性判斷為**高於平常**（因為 trending 排名），但沒有可量化的提及次數。
- **Retail 偏向**：整體偏多（bullish-leaning），但信心中等，原因是樣本來自二手摘要，且日期不一。

## Themes

1. **AI 需求與營收成長**：Q3 營收約 46.72B USD（+41.2% YoY，TIKR 引用），管理層將成長展望上調至約 44%。這是多方論述的核心。
2. **回檔視為買點**：多篇文章認為股價相對五年平均 forward P/E 偏低，回檔後可加碼。
3. **估值與獲利了結**：一部分散戶與評論者認為「股價已反映大部分利多」，建議分批獲利。
4. **地緣政治與中國風險**：Stockchase 評論區提到半導體拋售與對中國的地緣政治風險。
5. **選擇權與做空部位轉趨防守**：Benzinga 顯示 put/call ratio 約 1.10，並提到 short interest 上升，這是本次最明確的偏空訊號。
6. **短期催化劑**：NVIDIA 11/17 財報（已發布，後續影響待觀察）、TSMC 11 月營收（12 月初公布）、2027 年展望（1 月中）。

## Insider activity

6 個月窗口：2026-05-23 至 2026-11-23。依 yf 快取 insider 紀錄（Value 欄位為 USD，與 shares × price 核對一致，例如 1,375 股 × 363.66 ≈ 500,032 USD，與 500,039 相符）。

- **6 個月淨買入**：約 **0.82M USD**（816,537 USD），全部為買進，**無賣出紀錄**。
- 明細（窗口內）：
  - 2026-11-17：Ursula M. Burns（Director），買進 1,375 股，約 0.50M USD，均價 363.66 USD
  - 2026-11-05：Michael R. Splinter（Director），買進 840 股，約 0.30M USD，均價 357.00 USD
  - 2026-07-28、07-20、05-20：Bor-Zen Tien（Officer），小額買進，合計約 0.017M USD（5,850 + 4,050 + 6,718 USD）
- 窗口外（不計入）：2026-04-28 Tien 買進 7,760 USD；2026-03-31 Burns 買進 1,000 股，約 0.32M USD。
- **觀察**：董事層級在近期股價下跌時出手，買進價格 357 至 364 USD，高於快取現價 318.71 USD，屬於逢回加碼。Insider 持股比例僅 0.022%（快取 major_holders），買進金額絕對值小，訊號強度有限，主要價值在方向性。
- 注意：買入皆為小額，且主要來自董事而非 CEO / CFO，不應解讀為管理層的強烈信心表態。

## Ownership shifts

- 機構持股比例約 **15.42%**（快取 major_holders），機構數 4,761 家；內部人持股 0.022%。
- 2026-09-30 季報前十大機構（inst_holders）變動：
  - FMR 增持約 +10.9%（持股約 6,537 萬股）
  - Bank of America 增持約 +9.5%
  - T. Rowe Price 增持約 +9.3%
  - Capital World Investors 減持約 -1.7%
  - Sanders Capital 減持約 -6.5%
  - JPMorgan 減持約 -25.6%
  - BlackRock 減持約 -2.9%
- 前十大中淨增持家數多於減持，但數字僅反映 9 月底資料，尚無 Q3 之後的最新 13F。整體解讀為機構配置未出現明顯撤出。

## Net sentiment score

**綜合：偏多（bullish），信心中等。**

- 分析師：強烈偏多（21 家中 20 家 Buy 以上，0 家 Sell，目標價平均顯著高於現價）。
- 內部人：偏多（近 6 個月全為買進，近期買入集中於董事層級）。
- 散戶：偏多但不穩（StockTwits 轉向 bullish，但價格同期下跌，且資料多為二手摘要）。
- 期權與做空：偏空（put/call 約 1.10，short interest 上升）。
- 扣分因素：資料來源不一致（目標價與股價），Reddit 缺口，社群樣本日期不明，且 11/10 至 11/22 股價由約 396 USD 下跌至約 319 USD，走勢與基本面樂觀不完全同步。

**Divergence flag：否（主要）。** 分析師與散戶社群整體同向偏多，因此不構成典型的反向訊號。唯一的局部分歧是期權部位（put/call 1.10）偏防守，與分析師的偏多看法不同，屬於需要留意但不足以改變綜合判斷的訊號。

**資料注意事項**
- 快取現價 318.71 USD（11/22），而 WebSearch 摘要提到 11/10 收盤約 396.48 USD、11/13 收盤約 398.73 USD。兩者之間的約 20% 跌幅與 StockTwits 摘要的「11.5% 累計跌幅」不一致，應由 pricing 模組核對，本報告未自行調整。
- 快取 `recommendations` 與 `rec_summary` 內容完全相同，視為同一來源，未重複計算。
- 本報告僅呈現情緒面，不包含交易建議。

SENTIMENT REPORT COMPLETE
