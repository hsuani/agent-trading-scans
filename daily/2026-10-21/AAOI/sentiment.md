# Sentiment — AAOI as of 2026-10-21

資料可用性摘要：Reddit（r/wallstreetbets、r/stocks）與 StockTwits 抓取失敗，列為 DATA_UNAVAILABLE；WebSearch 最新可見內容僅到 2026 年 6 月，且多為單一選擇權分析網站，可信度低。分析師與內部人資料來自 yf 工具（cache），機構持股為 2026-06-30 季報資料。

## Analyst consensus
- yf rec_summary（當期 0m）：strongBuy 2 / buy 1 / hold 3 / sell 0 / strongSell 0，共 6 位分析師，買進比例約 50%，無賣出評等。
- 過去 3 個月（-1m、-2m）分布完全相同，yf 資料顯示無評等變動。
- yf `recommendations` 回傳與 rec_summary 相同的彙總結構，缺乏逐家券商的升降評等明細：升降評等明細 DATA_UNAVAILABLE。
- 目標價：yf 工具未提供，DATA_UNAVAILABLE。
- 外部來源（WebSearch，MarketBeat 等）描述較不一致，僅作參考：
  - MarketBeat 顯示 3 Buy / 2 Hold / 1 Sell，平均 12 個月目標價約 $141.80，區間 $54–$220，共識為 Hold。與 yf 的 6 位分析師分布不同，兩者來源與計算時點不一致。
  - Needham（Ryan Koontz）目標價由 $260 降至 $220（2026-07-22，MarketBeat 紀錄）；另有 Benzinga 條目顯示降至 $190（8 月），數字疑有誤植，需以原始紀錄核對。
  - Rosenblatt 維持 Buy，目標價 $220。
  - B. Riley 於 2026-02-27 由 Sell 上調至 Neutral，後目標價 $129（Hold，2026-05-08 更新）。
  - Northland 於 2026-02-27 由 Outperform 下調至 Market Perform。
  - Raymond James 目標價上調至 $178，維持 Outperform（日期不明）。
- 整體判讀：分析師評等偏中性，多數為 Hold，買方意見仍有一定比例，近三個月無 yf 可見的評等變動。

## Retail social
- Reddit（r/wallstreetbets）：DATA_UNAVAILABLE（WebFetch 無法連線 www.reddit.com，未取得貼文樣本）。
- Reddit（r/stocks）：DATA_UNAVAILABLE（同上）。
- StockTwits：DATA_UNAVAILABLE（api.stocktwits.com 無法解析網域，DNS 失敗）。
- X / 新聞輿情（WebSearch）：未找到 2026 年 10 月的相關討論。可見資料止於 2026 年 6 月：
  - 2026-06-08 一篇選擇權分析文稱 call 比例 86.2%，情緒偏多。
  - 2026-06-11 同系列文章判讀為中性（balanced）。
  - 2026-06-22 同系列文章稱情緒偏多，但 RSI 偏弱，價格貼近布林中軌，判讀為盤整。
  - 上述內容來源單一、部分數字在多個日期重複，可信度低，僅作背景參考。
- 聲量（mention volume）：DATA_UNAVAILABLE，無法與平常基準比較。
- 散戶情緒傾向：DATA_UNAVAILABLE（無有效樣本）。
- 主題（僅依據可見的 2026 年 4–6 月新聞）：
  - AI 光通訊需求與資料中心光模組成長預期，是主要多方論點（一篇 4 月文章指出，光元件族群的資金定位仍偏向 AI 硬體支出成長）。
  - 財報前後的獲利預期落差與股價劇烈波動，是 5 月的主要話題（一篇 5 月文章提到財測令人失望後股價大幅下跌）。
  - 估值與獲利：同一選擇權網站列出過去十二個月每股盈餘為 -$0.63，市值約 $32.29B（2026-06-22）。

## Insider activity
統計區間：2026-04-21 至 2026-10-21（近 6 個月）。

- 公開市場買進（Purchase）：0 筆，**淨買進 $0**。最近一次買進為 2025-08-14（董事 YEH WILLIAM H 及 CEO LIN CHIH-HSIANG THOMPSON 等，約 $0.6M 量級，已超出 6 個月窗口）。
- 公開市場賣出（Sale）：27 筆，合計約 **$94.6M**。
- 非市場交易（Stock Award / Gift）：多筆，不計入上述金額，包含 2026-05-15 與 2026-07-31 的大額股票獎勵（CEO 合計約 77 萬股）。
- 淨 6 個月：**$0 買進 / 約 $94.6M 賣出**。

依職位（賣出金額，近似值）：
| 職位 | 人員 | 賣出金額（近 6 個月） | 主要時點 |
|---|---|---|---|
| CEO | LIN CHIH-HSIANG THOMPSON | 約 $19.9M | 2026-05-19（$173.26）、2026-06-12（$166.53） |
| Officer | CHANG HUNG-LUN FRED | 約 $22.7M | 2026-05-19、2026-06-12、2026-06-17（$170.60）、2026-09-08（$110.21） |
| Officer | YEH SHU-HUA JOSHUA | 約 $17.0M | 2026-05-19、2026-06-12、2026-06-04（$204.75–205.39）、2026-08-18（$147.73）、2026-10-05（$120.03） |
| CFO | MURRY STEFAN J | 約 $14.4M | 2026-05-19、2026-06-12、2026-07-10、2026-08-10、2026-09-10、2026-10-12（$102.87） |
| Director | DELANEY CYNTHIA | 約 $10.7M | 2026-05-26（$189.23） |
| Officer | KUO DAVID C. | 約 $8.2M | 2026-05-19、2026-06-12 |
| Director | CHEN MIN-CHU MIKE | 約 $1.7M | 2026-06-02（$201.00） |

重點觀察：
- 高階主管與董事在 2026-05-19 與 2026-06-12 出現兩次集中賣出，同日多人以相近價位成交（2026-06-12 共五人皆以約 $166.53 成交），疑似預定交易計畫或同步執行，需以 Form 4 的 10b5-1 註記確認，本報告無法判定。
- 賣出價位由 6 月約 $166–205 下滑至 10 月約 $103–120，顯示內部人在股價約回落一半後仍有持續賣出（9 月、10 月仍有 CFO、Officer 賣出）。
- 近期無任何董事或高階主管公開市場買進，與 2025 年 8 月的買進形成對比。
- CEO 本期未在公開市場買進，主要動作為賣出與獎勵股。

## Ownership shifts
- 內部人持股比例：9.78%。
- 機構持股比例：63.71%（流通股比例 70.62%），機構家數 634。
- 前十大機構合計持股約 32.5%（資料日期 2026-06-30）。前十大機構中 8 家增持、2 家減持：
  - BlackRock：7.63%，持股數較上季減少 10.3%（減持）。
  - Invesco：4.04%，增加約 69%。
  - Vanguard Capital Management：3.98%，增加約 9.9%。
  - Marex Group：3.35%，增加約 879%（變動幅度異常，疑為建倉或資料口徑差異，需核對）。
  - Vanguard Portfolio Management：3.14%，增加約 47%。
  - UBS Group：2.50%，增加約 118%。
  - Oberweis Asset Management：2.12%，減少約 24%（減持）。
  - Geode Capital：1.98%，增加約 3%。
  - Value Aligned Research Advisors：1.89%，增加約 26%。
  - Goldman Sachs：1.88%，增加約 46%。
- 趨勢判讀：2026 年 6 月底季報顯示機構小幅淨加碼的跡象，但持股資料已落後約 3.5 個月，Q3 13F（預計 11 月中旬前後公布）尚未納入。

## Net sentiment score
- 分析師面（中性）：6 位分析師，買進約 50%，無賣出評等，近三個月無 yf 可見評等變動。信心：中。
- 散戶面：DATA_UNAVAILABLE（Reddit、StockTwits 無資料；X/新聞僅有 6 月前的低可信度資料）。
- 內部人面（偏空）：近 6 個月 0 筆公開市場買進、約 $94.6M 賣出，主要為高階主管與董事，賣出價位隨股價下跌仍持續。信心：中（需確認是否為預定交易計畫，若屬 10b5-1 則偏空訊號強度應下調）。
- 機構面（偏中性至偏多）：前十大中 8 家增持，但資料為 6 月底，時效性不足。信心：低至中。
- **綜合判斷：中性偏空（bearish-leaning neutral），信心：低。** 理由：內部人賣出規模大且持續，分析師仍偏中性，機構小幅加碼，散戶面無資料無法納入。綜合信心受限於 Reddit、StockTwits 失敗與資料時效。

**Divergence flag：是（部分）。** 分析師評等偏中性且半數為買進，與內部人的持續賣出方向不一致；散戶面因無資料無法判定是否與分析師背離。內部人與分析師背離的訊號價值，需在取得 Form 4 交易計畫註記與散戶資料後再確認。

## 資料缺口與後續需求
- Reddit（r/wallstreetbets、r/stocks）與 StockTwits 需要可用的抓取路徑，目前皆失敗。
- 逐家券商的升降評等歷史與目標價，yf 工具未提供，需補充來源。
- 2026 年 8 月至 10 月的財報後分析師動態與輿情，WebSearch 未能取得，建議再補查。
- Q3 2026 13F 持股資料，待公布後更新機構趨勢。

SENTIMENT REPORT COMPLETE
