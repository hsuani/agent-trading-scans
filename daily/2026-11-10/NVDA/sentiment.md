# Sentiment — NVDA as of 2026-11-10

> 資料狀態：yf 工具走 cache fallback（Yahoo cookie/crumb 連線失敗，屬預期情況）。Reddit / StockTwits 直接抓取未執行，社群聲量數字標記 DATA_UNAVAILABLE；社群判斷以 WebSearch 結果為主，多數來源日期不明或屬 2025 年，可信度低。

## Analyst consensus

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m（當前） | 10 | 48 | 3 | 1 | 0 | 62 |
| -1m | 10 | 49 | 2 | 1 | 0 | 62 |
| -2m | 10 | 49 | 2 | 1 | 0 | 62 |
| -3m | 9 | 48 | 2 | 1 | 0 | 60 |

目前分布：58 buy（含 strong buy）/ 3 hold / 1 sell，買方比例約 94%。近四個月評等幾乎沒有變化，hold 由 2–3 家維持，無明顯降評趨勢。

Recent moves（WebSearch 所得，未經 yf 驗證，請以原始研報為準）：
- Melius Research 於 2026-11-02 把目標價由 $420 下修至 $315（來源說明為「較參考股價仍高約 54%」，但同一批資料的 NVDA 股價約 $181.6，兩者隱含的參考價不一致，數字需再核對）。
- Oppenheimer 維持 Outperform，目標價上調至 $265（來源為德文站，日期不明）。
- Susquehanna 目標價由 $210 上調至 $230（同上，日期不明）。
- Weiss Ratings 評等 B+（Buy）。
- 一篇 Seeking Alpha 文章提到評等下調（"Pressure Builds Diamonds"），但文中提及的 11/19 財報日對應 2025 年，時間不符，不採計。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。WebSearch 無法取得 2026-11 的可讀貼文樣本與帖數。一則日期不明的報導指出 WSB 與 r/options 版面近期多為市場焦慮與虧損貼文，而非 NVDA 個股論述；另一則 2026-03 的報導提到 Reddit 情緒在 30 天內下降 17 點。以上皆非 11 月資料，僅供參考。
- StockTwits / X：
  - 最近一筆可查到的 StockTwits 情緒讀數為 2026-10-16，標示 "bearish"，當時散戶多把看空理由歸於 Alphabet 競爭與中國市場阻力；有人留言 "buy the dip" 但屬少數。
  - 2026-08 曾短暫降至 "extremely bearish"（財報前）。
  - 2026-11-05 大跌後的 StockTwits 情緒未查到，視為 DATA_UNAVAILABLE。
  - X 平台貼文：DATA_UNAVAILABLE。
- 聲量（相對水準）：無可靠量化數字。WebSearch 結果顯示 11/05 前後的新聞報導量明顯增加（股價單日 -9.26%，同期 S&P 500 -4.4%，據報導為 AI 晶片族群拋售），但這是新聞量而非社群聲量。
- 主要話題（由可取得的報導歸納）：
  1. AI 泡沫疑慮與高點回落：近一個月股價自 10/07 至 11/05 下跌約 23.5%，部分報導引用 Michael Burry 看空部位。
  2. 競爭與毛利：Alphabet 競爭、中國市場阻力是 StockTwits 看空留言的主要理由。
  3. 政策風險：一則報導指稱 2026 中期選舉後，市場擔心 AI 資料中心的監管趨嚴。
  4. 財報催化劑：多份來源指向 2026-11-17 的 FQ3 FY2027 財報，市場關注是否達到約 $108B 的營收指引（來源僅 Trefis 與一則新聞摘要，日期未完全確認）。
  5. 散戶「逢低買進」論述：仍有少數留言認為 AI 需求未減。

代表性言論（僅為 WebSearch 摘要中的語句，非原貼文）：
- "Time to buy the dip?"（StockTwits 文章標題式提問，2026-11 前後）
- "Retail bulls shrug off AI bubble worries"（StockTwits 文章標題，日期不明，疑為 2025 年）

## Insider activity

資料區間：2026-05-10 至 2026-11-10（yf cache 最後一筆交易日期為 2026-09-21，9/21 之後到 11/10 之間的申報可能缺漏）。

Net 6mo：$0 buys（無公開市場買入）/ 約 $1.37B sells（以 Value 欄位加總，僅計 "Sale" 類）。

Notable：
- Mark A. Stevens（Director）：區間內為最大賣方，合計約 $0.98B（含 6/18 $186M、6/04 $221M、9/02 $411M、9/04 $236M、9/18 $300M 等多筆）。
- Timothy S. Teter（General Counsel）：8/31 約 $6.5M、9/21 約 $6.8M 賣出。
- Jen-Hsun Huang（CEO）：2026-06-16 贈與 400,000 股（Stock Gift，無現金價值），區間內無 CEO 賣出紀錄。
- Tench C. Coxe（Director）：多筆 500,000 股 Stock Gift（非買賣）。
- Nicholas P. Parker（Officer）、Scott Gawel（Officer）：股票獎勵（Grant），非市場交易。
- 其餘董事多為年度股票獎勵（2026-06-25，每人 1,211 股）。

注意：Stock Gift 與 Stock Award 不計入買賣金額；賣出是否屬 10b5-1 計畫，工具資料未提供，無法判斷。

## Ownership shifts

- 機構持股比例：71.6%（institutionsPercentHeld = 0.7157）；浮動股比例：74.6%；機構數：7,752 家。
- 內部人持股：4.0%（insidersPercentHeld = 0.0401）。
- 趨勢：工具僅提供單一時點快照，無法判斷機構持股趨勢。標記為「快照可用、趨勢 DATA_UNAVAILABLE」。

## Net sentiment score

- 分析師面：偏多（bullish），信心高。58/62 評等為買入，評等近四個月幾乎穩定，但目標價在 11 月出現分歧（Melius 下修、Oppenheimer/Susquehanna 上修）。
- 散戶面：偏空（bearish）至中性，信心低。可取得的 StockTwits 讀數多為 bearish（最新為 10/16），11/05 之後無有效讀數，Reddit 完全無資料。
- 內部人面：偏空（bearish），信心中。區間內約 $1.37B 賣出、零公開市場買入，但多為既有持股的出售，且 CEO 無賣出紀錄。
- 綜合：中性偏空（neutral-to-bearish），信心低。主要受社群與內部人賣壓拖累，分析師評等支撐。

Divergence flag: **yes**。分析師評等偏多（94% buy），散戶情緒偏空，且兩者方向相反。此類分歧在過去資料中常見，但本次散戶端證據年代不一、覆蓋不完整，解讀時應保守。

資料缺口與後續建議：
1. Reddit 2026-11 資料缺失，需於可連線環境補抓 r/wallstreetbets 與 r/stocks 搜尋結果（limit=25，sort=new）。
2. StockTwits 2026-11-05 之後的情緒讀數缺失。
3. yf insider 資料在 2026-09-21 後無紀錄，需確認是否為 cache 過期。
4. 目標價數字（Melius、Oppenheimer、Susquehanna）未經 yf 驗證，且 Melius 隱含參考價與當前股價不一致。

SENTIMENT REPORT COMPLETE
