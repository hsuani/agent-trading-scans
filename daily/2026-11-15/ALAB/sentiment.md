# Sentiment — ALAB as of 2026-11-15

資料時點說明：分析師評等與內部人交易取自 pipeline/tools/yf（repo cache，屬正常）；股價參考值 $221.83 為 2026-11-14 快取報價，非 11-15 收盤。Reddit 與 StockTwits 直連主機被封鎖，改以 WebSearch 取得間接資料，未取得任何 11 月的直接貼文。2026-11-15 之後的資料一律視為未知，未採用。

## Analyst consensus

| 評等 | 家數 | 占比 |
|---|---|---|
| Strong Buy | 6 | 24% |
| Buy | 12 | 48% |
| Hold | 7 | 28% |
| Sell | 0 | 0% |
| Strong Sell | 0 | 0% |
| 合計 | 25 | 100% |

**BUY% = (Strong Buy + Buy) / 合計 = 18 / 25 = 72%**（上月 18/26 ≈ 69%，兩個月前 19/26 ≈ 73%，變動不大；無賣方評等）

近期動向（WebSearch 取得，部分來源日期不明，請留意）：
- 2026-11-04 前後，J.P. Morgan（Harlan Sur）維持 Overweight，目標價 $465；Morgan Stanley 維持 Overweight，目標價由 $382 調至 $389。兩家目標價隱含漲幅所對應的股價基準不一致（來源 TIKR 換算出約 $181 與約 $222），數字需以原始研究報告核對。
- MarketBeat 頁面（2026-07-24）列出共識目標價 $282.00（23 家），最高 $460、最低 $153；此為 7 月資料，已過時。
- Weiss Ratings 提及平均街頭目標價約 $204.47（無日期），與股價 $221.83 相比已接近或略高於共識。
- 未找到 11 月內的明確升評或降評紀錄。yf `recommendations` 只回傳彙總評等分布，不含個別券商的評等變動明細。

## Retail social

- **Reddit**：無法直接取得 r/wallstreetbets 或 r/stocks 的 11 月貼文（直連封鎖，WebSearch 未返回相關討論串）。第三方估計（AltIndex，資料約為 2026-09-08）：每日提及約 5 次，Reddit 單一情緒分數 66/100（中性），整體混合情緒 76/100（偏多，但較 30 日均值轉弱）。此為 9 月資料，不代表 11 月。
- **StockTwits / X**：StockTwits 直連封鎖，WebSearch 無 11 月資料。搜尋結果中的 StockTwits 文章多為 2024–2025 或 2026-09 以前的內容，不採用於當前判讀。
- **情緒來源（非論壇）**：Equibles 顯示整體情緒「中性」，聰明錢（smart money）偏多，機構資金呈累積；Earnings Whispers 描述情緒自「輕度負面」轉為「大致中性」。兩者均無明確日期。
- **Retail 聲量**：無 11 月可比的提及次數，無法與過去平均比較，聲量判讀為**資料不足**。
- **Retail 傾向**：中性偏混合。WebSearch 找不到 11 月內以散戶為主體的看多或看空論述樣本，因此無法引用直接貼文。

主要題材（依新聞與第三方文章歸納，非直接取自社群貼文）：
1. 11 月股價急跌約 26%（5 個交易日，自 $259 跌至 $191 附近），散戶關注是否屬板塊性拋售（AI 基礎建設估值疑慮）還是公司本身問題。
2. 財報 beat 但股價仍下跌，被視為「好報告、壞股價」的落差。
3. 估值爭論：有觀點認為急跌後具吸引力，也有人強調客戶集中度風險（TIKR 指出前三大客戶約占 2025 年營收 86%）。

**資料品質注意**：WebSearch 結果中的「11 月 3 日公布第三季營收 $585M、年增 153.7%」與公司 2025 年同期規模不易對齊（隱含基期約 $230M），此數字未經核對，不應作為基本面依據，需以財報原文確認。

## Insider activity

6 個月區間（2026-05-15 至 2026-11-15，USD）：
- **買進（open-market purchase）**：0 筆，$0M
- **賣出**：21 筆，合計約 **$484.1M**（已排除 Stock Award / Stock Gift）

依個人彙總（賣出金額）：
| 內部人 | 職位 | 6 個月賣出 |
|---|---|---|
| GAJENDRA SANJAY | President | 約 $238.2M |
| ALBA MANUEL | Director | 約 $132.5M |
| MOHAN JITENDRA | CEO | 約 $83.6M |
| DYCKERHOFF STEFAN A | Director | 約 $20.2M（定期小額賣出，多筆） |
| MAZZARA PHILIP | General Counsel | 約 $5.8M |
| LAZAR JACK R | Director | 約 $3.6M |
| MAYER BETHANY J | Director | 約 $0.3M |

Notable：
- 2026-11-05（股價急跌當日）DYCKERHOFF 以約 $211.41 賣出約 12,499 股，約 $2.6M。
- 2026-08-17 CEO MOHAN 與 President GAJENDRA 以約 $334–352 各賣出約 90,630 股（各約 $30.8M）。
- 2026-05-21 GAJENDRA 以約 $289–293 賣出 400,000 股（約 $116.1M），為單筆最大。
- 大量賣出是否來自 10b5-1 預定計畫，資料中未標示，無法判定。
- 無 CFO 大額交易（CFO LYNCH 僅有 2026-05-01 的股票授予）。

## Ownership shifts

- 內部人持股約 10.6%；機構持股約 72.9%（機構持股占流通股約 81.5%）；機構家數 1,351（yf `major_holders`，僅快照，無趨勢序列）。
- 最新 13F（2026-09-30）前十大機構變動：
  - FMR, LLC（第一大，約 9.0%）持股 **減少約 36.5%**
  - BlackRock（約 7.8%，06-30 資料）增加約 19.5%
  - T. Rowe Price（約 1.4%，06-30 資料）增加約 290%
  - Amundi（約 1.4%）增加約 54%
  - Vanguard 兩個單位（約 4.5% 與 3.9%）小幅增加約 6–8%
- **機構資金方向：分歧**。第一大持股者減碼，多家中小型與被動機構加碼；Equibles 另稱機構累積。淨流向難以定論，傾向「中性偏多（被動與部分主動加碼）」，但第一大機構減碼需留意。

## Net sentiment score

**綜合：中性（neutral），信心：低到中**

依據：
- 分析師：偏多（72% BUY，0% SELL），目標價仍高於股價。權重高，但僅反映券商觀點，且 11 月無明確調整。
- 內部人：明顯偏空（6 個月約 $484M 賣出，0 筆買進，且 11/05 急跌時仍在賣）。
- 散戶：無 11 月可靠數據，依第三方彙整屬中性。
- 機構：13F 混合，第一大機構減碼、多家加碼。
- 股價：近期跌幅約 26%，市場情緒明顯降溫。

**背離旗標：是**（有條件）。分析師整體偏多，與內部人大量淨賣出方向相反；散戶側因資料不足無法確認是否同向。內部人賣出可能含預定計畫，因此此背離的資訊量需保守看待。

本報告為情緒彙整，不含交易建議。

## Source notes

- yf：`rec_summary`、`recommendations`、`insider`、`major_holders`、`inst_holders`、`fast_info`（後三者部分為 repo cache，屬預期）
- WebSearch：TIKR、Trefis、MarketBeat、Equibles、Earnings Whispers、Weiss Ratings、AltIndex、Simply Wall St 等（多數非 11 月直接資料，已標註日期限制）

SENTIMENT REPORT COMPLETE
