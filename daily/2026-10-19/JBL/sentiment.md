# Sentiment — JBL as of 2026-10-19

## Analyst consensus
yf rec_summary（目前）：2 Strong Buy / 7 Buy / 1 Hold / 0 Sell / 0 Strong Sell（共 10 家）。綜合 9 買 / 1 持有 / 0 賣。
三個月前為 2 Strong Buy / 6 Buy / 2 Hold，表示一家 Hold 轉為 Buy，評級結構小幅改善，無任何 Sell。

近期動向：
- **Zacks Research 降評**：Strong Buy 降為 Hold，MarketBeat 報導日期為 2026-08-19。這是目前可找到最近的負面評級變動，但 Zacks 為量化評級機構，不一定計入 yf 的分析師計數。
- **Weiss Ratings**：2026-07-01 由 Buy (B-) 升至 Buy (B)，2026-08-12 又降回 Buy (B-)，屬小幅來回。
- **Wall Street Zen**：2026-04-11 由 Strong Buy 降為 Buy。
- **UBS**：有聚合站提到 UBS 因 AI 需求升評，但未找到可驗證日期，不採信為近期事件。
- **目標價**：各來源不一致，屬不同時點的數字。MarketBeat 2026-08 平均目標價 $453.67；另一來源平均 $447.73，Fintel 為 $435.07；Street high 約 $482，Benzinga 列出最低 $160 應為舊資料。Stifel 由 $290 升至 $430（Buy），BofA 由 $354 升至 $410（Buy）。TipRanks 報導 Barclays 升至 $267（Overweight），與另一來源 Barclays $426 相互矛盾，需以原始報告確認。
- 公司近期基本面：FQ3 2026 上修 adjusted EPS 指引至 $12.70、營收指引至 $35B，AI 相關營收預估 $13.6B。FQ4 財報（9/25）營收與 EPS 優於預期，但股價當日下跌約 6.7%。
- 注意：目標價隱含上行空間需以當日實際股價計算，本次未取得可驗證的 2026-10-19 收盤價，故不計算上行幅度。

## Retail social
- **Reddit（r/wallstreetbets、r/stocks）**：本次以 WebSearch 嘗試查詢，未能取得任何 2026 年 JBL 相關 Reddit 串文。直接 Reddit JSON 端點未依規定使用（規範要求社群類以 WebSearch 進行）。**無法判定 tilt，資料缺失。**
- **StockTwits**：可取得的最強讀數為 2026-03-05 文章，情緒 95/100（"extremely bullish"），起因為 FQ4 財報優於預期與 $1B 買回授權。**此為 2026-03 舊資料**，未找到 2026-10 的即時讀數。StockTwits 直接 API 本次未呼叫（依規範以 WebSearch 為主），soft-fail。
- **X / 聚合情緒站**（非原始貼文，時點不一）：
  - LunarCrush：正向情緒 100%，但僅基於 41 則貼文（24 小時），樣本量極小，且快照日期不明。
  - SentiSense：30 日視角偏多，但標示「降溫中」。
  - Equibles：整體情緒中性，機構資金流入、內部人資金流出。
  - Benzinga（2026-08 快照）：分析師共識 Buy（12 家）、選擇權 Put/Call 0.39 偏多、Short interest 3.9% 且標示為上升。
- **聲量（buzz volume）**：無可靠的量化提及數。LunarCrush 的 41 則貼文顯示聲量偏低，但該數字來源時點不明，只能定性判斷為**低至中等，信心低**。
- **Themes（從新聞與聚合站反覆出現的敘事）**：
  - AI 資料中心與雲端基礎建設需求推動的成長敘事（多源重複）
  - 估值擔憂：股價大幅上漲後，市場期待過高，即使 beat-and-raise 也可能失望（"not entirely satisfied"）
  - 技術面：價格位於 MA-20 / MA-50 / MA-200 之上，但多項指標顯示超買
  - 空單比例上升（3.9% short float）需留意

## Insider activity
統計區間：2026-04-19 至 2026-10-19（6 個月）。

- 6 個月內賣出（不含 grant / gift）：約 **$1.74M**
  - 2026-04-20 COO Andrew Priestley 賣出 3,169 股，約 $1.05M（$330）
  - 2026-04-30 Officer Gary K. Schick 賣出 1,000 股，$340,000（$340）
  - 2026-07-06 Officer Matthew Crowley 賣出 94 股，$32,430（$345）
  - 2026-07-15 Officer Gary K. Schick 賣出 1,000 股，約 $320K（$315–330）
- 6 個月內買入：約 **$0.15M**
  - 2026-07-17 Director Tyagarajan Nallicheri Vydianathan 買入 500 股，$149,815（$299.63）。這是區間內唯一的公開市場買入，且為董事而非高管。
- **淨額：約 -$1.59M（淨賣出）**

Notable：
- CEO Michael Dastoor 最近一次賣出為 2026-04-08（9,467 股，約 $2.71M），在區間起點之前；區間內 CEO 無交易。
- 2026-04-17 Officer Steven Borges 賣出約 $1.63M，亦在區間起點之前。
- 本區間內 yf 最新交易為 2026-07-17，7 月中之後到 10-19 之間無任何申報資料。可能是申報延遲或資料源落後，**需以 SEC Form 4 核對**。
- 較長期來看（2025-06 起），Mark Mondello（Officer and Director）持續定期賣出，為主要的賣方來源。

## Ownership shifts
- 機構持股：99.76%（yf major_holders）；機構數 1,536 家。
- 內部人持股：1.19%。
- 趨勢：yf 只提供當下快照，無時間序列，**無法判定持股集中度變化**。MarketBeat 2026-08-01 報導 Access Investment Management 為其最大持倉之一，但僅為標題層級資訊，未驗證持倉比例。

## Net sentiment score
**Composite：偏多（bullish-leaning neutral），信心中低。**

分項判斷：
| 面向 | 判斷 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 偏多 | 高 | 9 買 / 1 持有 / 0 賣，目標價多在 $410–$450 區間 |
| 散戶社群 | 無法可靠判定（推估偏多） | 低 | StockTwits 為 2026-03 舊資料，Reddit 無資料，X 聚合樣本極小 |
| 內部人 | 偏空（溫和） | 中 | 6 個月淨賣約 $1.59M，唯一買入為董事 |
| 評級動向 | 中性偏多 | 中 | 三個月內 Hold 減少，但 2026-08 Zacks 降為 Hold |
| 空單 / 選擇權 | 混合 | 低 | Put/Call 0.39 偏多，但 short interest 上升 |

**Divergence flag：無法判定（資料不足）。**
- 分析師偏多與內部人淨賣出之間存在結構性分歧，但這屬於「專業人士內部」的分歧，不是散戶與分析師之間的分歧。
- 散戶 tilt 無法取得當期可靠資料，因此無法確認是否與分析師方向相反。若之後補到當期 Reddit / StockTwits 資料，需重新評估。

## 資料限制與可信度
- Reddit：WebSearch 未回傳任何 2026 年 JBL 相關串文，無法採樣代表性貼文，故不引用任何 Reddit 原文。
- StockTwits：僅有 2026-03 的舊讀數；直接 API 未呼叫。
- 價格資料：各來源價格不一致（$320–$380 區間），本報告未依賴特定價格。
- Barclays、UBS 目標價存在來源衝突。
- 內部人交易以 yf 為準，最新紀錄為 2026-07-17。
- 本報告僅為情緒觀察，不構成交易建議。

SENTIMENT REPORT COMPLETE
