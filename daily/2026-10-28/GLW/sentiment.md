# Sentiment — GLW as of 2026-10-28

資料狀態: yf 工具因 Yahoo cookie/crumb 取得失敗,全部回傳快取資料 (recommendations / rec_summary 無日期戳記; insider 最新一筆為 2026-09-04)。Reddit 與 StockTwits 無法連線 (Reddit 回報 unable to fetch, StockTwits DNS 解析失敗),散戶 (retail) 資料不可用。單位: 美元 (USD), 以 M / B 表示。

## Analyst consensus

rec_summary (期間 0m) 共 18 位分析師: Strong Buy 1 / Buy 13 / Hold 4 / Sell 0 / Strong Sell 0。
- BUY 比例 (Strong Buy + Buy): 14 / 18 = **77.8%**
- HOLD 比例: 4 / 18 = 22.2%
- SELL 比例: 0%

趨勢 (BUY 比例, 由 yf 歷史快照計算):

| 期間 | Strong Buy | Buy | Hold | Sell | BUY 比例 |
|---|---|---|---|---|---|
| 0m (最新) | 1 | 13 | 4 | 0 | 77.8% |
| -1m | 0 | 13 | 5 | 0 | 72.2% |
| -2m | 0 | 12 | 4 | 0 | 75.0% |
| -3m | 0 | 11 | 5 | 0 | 68.8% |

近期動向: BUY 比例由 -3m 的 68.8% 升至最新 77.8%, 未出現賣出評等。Hold 數量在 4 至 5 之間小幅波動。

次級來源 (WebSearch 摘要, 未能直接驗證, 數字與 yf 不一致, 僅供參考):
- 某聚合站點稱 14 位分析師中 9 Strong Buy / 5 Hold, 評為 "Moderate Buy"。與 yf 數字不一致, 以 yf 為準。
- Truist 於 2026-10-02 目標價調至 182 美元, 維持 Buy (另一來源提及 Truist 自 Hold 升至 Buy, 時點不明)。
- MarketBeat 記載 Wall Street Zen 於 2026-10-10 升評為 buy。
- Morgan Stanley 於 2026-07-29 目標價由 180 降至 165 美元, 維持 Equal-Weight。
- Weiss Ratings 於 2026-08 降評為 hold (c+)。
- 目標價區間搜尋摘要提及高點約 270 美元、低點約 155 美元, 12 個月平均約 163 美元 (來源不一, 未核對)。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: 無法連線 (WebFetch 回報 unable to fetch)。無法取得討論串樣本、分數與留言數, tilt 無法判定。
- **StockTwits**: 無法連線 (DNS 解析失敗)。無法取得訊息數與 bullish/bearish 標籤分布。
- **X / 新聞聊天 (WebSearch)**: 未找到 r/wallstreetbets 或 Reddit 上關於 GLW 的討論串, 搜尋結果以財經文章與分析師評論為主。
- **聲量 (buzz volume)**: 無法量化, 無 retail 原始資料可比對歷史基準。
- **Tilt**: 無法判定 (資料缺失)。以媒體與分析師文章的語氣觀察, 多為「AI 光纖需求受惠 vs 估值偏高」的兩極辯論。
- **Themes (次級來源歸納)**:
  - AI 資料中心光纖需求: Meta 承諾至 2030 年採購最高 60 億美元光纖 (搜尋摘要, 未核對原始公告); 與 Amazon 的多年期光纖合作。
  - 光通訊 (Optical Communications) 業務年增 24% (Q4 摘要)。
  - 估值爭議: 有文章提及本益比約 73.9, 認為貴; 另有觀點認為回檔是買點。
  - 股價波動大: 摘要提及 2026-07 大幅回檔, 股價在 ~124 至 ~132 美元之間 (日期不一, 不宜當作現價)。
- 注意: 上述次級來源未經原文核對, 且與 yf 日期不一定對齊, 只作為主題歸納, 不作為量化依據。

## Insider activity

6 個月窗口 (2026-04-28 至 2026-10-28) 內, Sale 紀錄 14 筆, 合計約 **57.5M USD 賣出**; 公開市場買進 (Purchase) **0 筆 / 0 USD**。
- 淨流向: 淨賣出 約 57.5M USD, 無內部人買進。
- 注意: yf 最新交易日為 2026-09-04, 窗口後段 (2026-09 至 10) 可能缺漏, 實際淨賣出可能更大或更小, 需以 SEC Form 4 核對。

按人彙總 (6mo 內賣出金額):

| 內部人 | 職稱 | 賣出金額 (M USD) |
|---|---|---|
| WEEKS WENDELL P. | CEO | 18.65 |
| STEVERSON LEWIS A | Officer | 7.42 |
| AMIN JAYMIN | CTO | 5.26 |
| ZHANG JOHN Z | Officer | 4.75 |
| SCHLESINGER EDWARD A | CFO | 4.20 |
| SEETHARAM SOUMYA | CTO | 4.12 |
| BECKER STEFAN | Officer | 3.95 |
| NELSON AVERY H III | COO | 3.92 |
| GULLO MICHELLE L | Officer | 2.51 |
| VERKLEEREN RONALD L | Officer | 2.08 |
| TILLMAN MICHAUNE D. | General Counsel | 0.67 |

Notable:
- **CEO Wendell P. Weeks**, 2026-06-09, 以 186.46 美元賣出 100,000 股, 約 18.65M USD; 同日行使衍生性證券 (option conversion) 100,000 股, 行使價 27.03 美元。手法為「行使後賣出」, 是窗口內最大單筆。驗算: 100,000 股 × 186.46 美元 = 18,646,000 美元, 與 yf Value (18,646,070) 吻合。
- **CFO Edward A. Schlesinger**, 2026-04-15 有大量 (63,069 股) 紀錄 (無價格欄位, 性質不明, 可能為歸屬或稅務扣繳), 2026-05-07 以 186.08 美元賣出 22,562 股。
- **CTO Jaymin Amin**, 2026-05-22 以 192.14 美元賣出 27,395 股 (約 5.26M USD)。
- **COO Avery H. Nelson III**, 2026-05-15 以 195.93 美元賣出 20,000 股。
- 窗口前 (2025-10 至 2026-02) 亦有多筆賣出, 價格區間 89 至 133 美元, 顯示內部人在股價上升過程中持續減持。
- 附註: 多數賣出出現在 2026-05 股價 180 至 210 美元高檔區間, 之後 2026-08 至 09 價格 150 美元上下仍有賣出。多數內部人同時有大量「Stock Award/Grant」或衍生性證券行使紀錄, 屬例行薪酬相關性質, 不應全部解讀為看空訊號。是否屬於 10b5-1 預定交易計畫, yf 資料無法判定。

## Ownership shifts

yf major_holders 快照 (無歷史序列, 無法計算趨勢):
- 內部人持股 (insidersPercentHeld): 8.07%
- 機構持股 (institutionsPercentHeld): 74.67%
- 機構持股 (以流通股計, institutionsFloatPercentHeld): 81.23%
- 機構家數 (institutionsCount): 3,154

結論: 機構集中度高, 但無季度變化資料, 無法判斷近期是增持或減持。建議以 13F 季報補充。

## Net sentiment score

- **分析師**: 偏多 (BUY 77.8%, 無 Sell, 近 3 個月 BUY 比例回升)。信心: 中高 (樣本 18 位, 但資料為快照, 日期未標示)。
- **內部人**: 偏空 / 淨賣出 (6mo 約 57.5M USD 賣出, 0 買進, 含 CEO 大單)。信心: 中 (需排除例行薪酬與衍生性行使的影響, 且資料可能缺後段)。
- **Retail 散戶**: 無資料 (Reddit / StockTwits 皆不可用)。信心: 無。
- **機構持股**: 高度集中 (74.7%), 趨勢不明。

**綜合判斷: 中性偏多 (neutral-to-bullish), 信心中低。** 分析師共識明確偏多, 但內部人持續淨賣出抵銷了部分正面訊號。散戶端無法評估。

Divergence flag: **部分是 (分析師 vs 內部人)**。分析師偏多而內部人淨賣出, 方向相反; 但這不是散戶 vs 分析師的背離, 因散戶資料缺失, 無法判定 retail 與 analyst 是否背離。若後續取得 Reddit/StockTwits 資料, 再重新評估。

## 資料缺口與後續建議
1. Reddit / StockTwits 連線失敗, 散戶情緒為空白, 建議於可連線時重跑 (或改用其他來源)。
2. yf cookie/crumb 失敗, 所有資料為快照, 建議確認 insider 最新交易 (2026-09 之後) 與分析師評等日期。
3. 次級來源的分析師數字與 yf 不一致, 以 yf 為準。
4. 機構持股無趨勢, 建議補 13F 資料。

SENTIMENT REPORT COMPLETE
