# Sentiment — AMT as of 2026-11-28

資料時點說明：本報告只採用 2026-11-28 當日或之前可取得的資料。搜尋結果中未發現 2026-11-28 之後的資料。多數社群與評等頁面未標註日期，已於各段註明。未找到的資料一律標示 DATA_UNAVAILABLE。

## Analyst consensus

yf `rec_summary`（當期 0m 快照，未附抓取日期，視為當期）：23 buy（含 7 strongBuy、16 buy）/ 3 hold / 0 sell，共 26 家。
- 與 -1m、-2m、-3m 比較：buy 由 22 增至 23，hold 維持 3，sell 維持 0。strongBuy 歷來維持 7。
- 搜尋結果中一則未標註日期的聚合頁面（Nov 2026 相關頁）：22 家分析師，14 Strong Buy / 1 Moderate Buy / 7 Hold，共識由 Strong Buy 轉弱。此頁與 yf 的 hold 數（3）不一致，日期也無法確認，故以 yf 為主、此頁僅作為「分歧存在」的註記。

近期評等變動（以搜尋結果為準，最新一筆為 2026-05-19，2026 年 11 月未找到評等變動）：
- Mizuho：2026-04-15 由 Neutral 升至 Outperform，目標價由 189 升至 205 USD。
- Bernstein：2026-05-19 由 Market Perform 升至 Outperform，目標價 207 USD。
- BMO Capital：2026-01-09 由 Outperform 降至 Market Perform，目標價由 210 降至 185 USD，理由為 DISH 相關議題。
- UBS：2026-01-20 目標價由 260 降至 254 USD，維持 Buy。
- Barclays：2026-04 維持 Equal-Weight，目標價 195 USD。
- RBC：2026-04-30 維持 Hold，目標價 195 USD（來源為 Yahoo/Barchart 轉載）。
- 2026-11 的評等與目標價變動：DATA_UNAVAILABLE。

價格參考：搜尋結果顯示 2026-11-17 收盤約 183.18 USD，單日下跌約 3.96%。此數字來自單一聚合頁，未與交易所資料交叉確認。

## Retail social

- Reddit：WebSearch 未找到 r/wallstreetbets 或 r/stocks 上近期的 AMT 專屬討論串。已知的間接資料只有 Insider Monkey 的「Reddit 推薦倫理投資標的」清單（AMT 排第 4，日期不明）。WebFetch Reddit JSON 依任務指示未使用。Reddit 專屬 tilt：DATA_UNAVAILABLE。
- Seeking Alpha 留言（2026-03，非 Reddit）：看法分歧。一派提到 DISH 合約付款違約相關訴訟是塔類股的風險；另一派認為股價已進入約五年的下跌趨勢。引述：「the stock has been in a downtrend for going on 5yrs」。
- StockTwits：未取得資料，DATA_UNAVAILABLE（任務限定以 WebSearch 取得，未直接呼叫 API）。
- X / 新聞型討論：未找到 2026-11 的 X 貼文。一則聚合摘要提到「交易者談論 AMT 突破與 REIT 復甦」，但無日期且為摘要性質，不列為直接證據。
- LunarCrush：頁面情緒百分比為占位值，不採用。
- 聲量（buzz volume）：無法量化，定性判斷為低。搜尋索引中沒有專屬討論串，這本身即為低聲量的訊號，但信心低。
- 主題（themes）：(1) 資料中心成長與塔類資產估值；(2) DISH 合約與訴訟風險；(3) AST SpaceMobile 相關合作（來自 LunarCrush 摘要的描述，未證實）；(4) 長期下跌趨勢與估值偏高的爭議。
- 零售傾向：DATA_UNAVAILABLE（資料不足，無法判定偏多或偏空）。

## Insider activity

以 2026-05-28 至 2026-11-28 為 6 個月窗口，依 yf insider 資料計算（USD）：

| 日期 | 人員 | 職稱 | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-05-28 | Pamela Reeve | Director | 贈與（Gift） | 810 | 0 |
| 2026-07-29 | Ruth Dowling | General Counsel | 賣出 | 1,791 | 0.31 |
| 2026-07-29 | Robert Meyer Jr. | Officer | 賣出（178.89/股） | 5,000 | 0.89 |
| 2026-08-21 | Rajesh Kalathur | Director | 公開市場買入（177.00/股） | 2,829 | 0.50 |
| 2026-10-01 | Paul Blanchett | Officer | 股票獎勵 | 16,299 | 0 |
| 2026-10-30 | Juan Hernandez Font | Officer | 賣出（189.63/股） | 592 | 0.11 |

- 6 個月淨額：買入 0.50M USD（僅 1 筆，董事 Kalathur）；賣出約 1.32M USD（3 筆，含 General Counsel 與 Officer）；淨賣出約 0.82M USD。
- 驗算：Kalathur 2,829 × 177.00 ≈ 500,733 USD；Meyer 5,000 × 178.89 ≈ 894,450 USD。
- 解讀：買入金額小且僅一人，賣出金額也屬中小規模，未見 CEO 或 CFO 在窗口內交易。CEO（Vondran）與 CFO（Smith）在 2026-03 之後無公開市場交易紀錄。2026-03 之前有較大規模的 CEO/COO/CFO 賣出，但不在窗口內。
- 注意：窗口內 Dowling 另有 2026-04-29 賣出（不在本窗口，已排除）。

## Ownership shifts

- 機構持股比例約 97.9%，機構數 2,414 家；內部人持股約 0.1%（yf major_holders 當期快照）。
- 趨勢（季度間比較）：DATA_UNAVAILABLE（僅有當期快照，無前期比較）。

## Fundamental context (sentiment-related only)

- Q3 2026（2026-10-27 公布）：營收約 27.85 億 USD（+2.5%）；AFFO/股約 2.87 USD（去年同期 2.78 USD）；全年 AFFO/股指引收窄為 11.04–11.16 USD。
- 資本配置：Q3 回購 3.15 億 USD；董事會另授權 20 億 USD 回購額度。搜尋結果提到加拿大塔業務出售約 20 億 USD（單一摘要，未交叉確認）。
- 投資人情緒分數（EarningsWhispers，方法不明）：財報前 -0.23 轉為財報後 +0.19。

## Net sentiment score

- 分析師面：偏多（bullish）。yf 顯示 23 buy / 3 hold / 0 sell，無賣出評等。近期上調與下調並存。信心：中高。
- 零售面：DATA_UNAVAILABLE，無法有效判定。搜尋中找不到專屬討論串。信心：低。
- 內部人面：小幅淨賣出（約 0.82M USD），無 CEO/CFO 公開市場交易。信心：中。
- 綜合：中性偏多（neutral-to-bullish），信心中低。主要依據是分析師評等結構，零售面資料缺失拉低整體信心。
- 股價與評等的背離：搜尋結果顯示 11 月中股價單日下跌 3.96%，而一則未註明日期的聚合頁提到共識「比一個月前更保守」。此類訊號可能暗示分析師端的實際動向與 yf 的計數不一致，但證據不足，僅作為待查項目。

Divergence flag: 無法判定（DATA_UNAVAILABLE）。原因是缺少可靠的零售情緒資料，無法確認零售與分析師傾向是否相反。若要判定，需補取 Reddit、StockTwits 的當日資料。

## Data gaps

- Reddit 專屬討論串：DATA_UNAVAILABLE（WebSearch 未索引）
- StockTwits：DATA_UNAVAILABLE（任務限定以 WebSearch 取得）
- X 貼文（2026-11）：DATA_UNAVAILABLE
- 2026-11 的分析師評等與目標價變動：DATA_UNAVAILABLE
- 機構持股季度趨勢：DATA_UNAVAILABLE

## Metrics table

| 指標 | 數值 | 單位 / 備註 |
|---|---|---|
| 買進評等（yf 當期） | 23 | 家（7 strongBuy + 16 buy） |
| 持有評等（yf 當期） | 3 | 家 |
| 賣出評等（yf 當期） | 0 | 家 |
| 分析師總數（yf） | 26 | 家 |
| 買進評等 -1m 對照 | 22 | 家 |
| 未註明日期聚合頁共識 | 22 家（14 SB / 1 MB / 7 Hold） | 與 yf 不一致，僅註記 |
| 近期最高目標價變動 | Bernstein 207 USD（2026-05-19） | USD |
| 近期下調目標價 | UBS 254 USD（2026-01-20） | USD |
| 2026-11-17 收盤參考價 | 約 183.18 USD | USD，單日 -3.96% |
| 6 個月內部人買入 | 0.50 | M USD（1 筆，董事） |
| 6 個月內部人賣出 | 1.32 | M USD（3 筆） |
| 6 個月內部人淨額 | -0.82 | M USD（淨賣出） |
| CEO/CFO 窗口內公開市場交易 | 0 | 筆 |
| 機構持股比例 | 97.9 | % |
| 機構持有家數 | 2,414 | 家 |
| 內部人持股比例 | 0.1 | % |
| Reddit 聲量 | DATA_UNAVAILABLE | 定性：低 |
| StockTwits 情緒 | DATA_UNAVAILABLE | — |
| X 情緒 | DATA_UNAVAILABLE | — |
| 零售傾向 | DATA_UNAVAILABLE | — |
| 綜合情緒 | 中性偏多 | 信心：中低 |
| 分歧旗標 | 無法判定 | DATA_UNAVAILABLE |

SENTIMENT REPORT COMPLETE
