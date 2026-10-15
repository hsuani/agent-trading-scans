# Sentiment — ARQQ as of 2026-10-15

## 資料品質總覽
- 分析師評級（recommendations / rec_summary）：即時與 repo cache 皆為空，**DATA_UNAVAILABLE**。
- Reddit（r/wallstreetbets、r/stocks）：直接抓取於本環境受限，WebSearch 亦未找到相關討論串，**DATA_UNAVAILABLE**。
- StockTwits：僅有一份無日期的 symbol 頁快照，無貼文級情緒資料，**DATA_UNAVAILABLE**（部分）。
- 內部交易（insider）與持股（major_holders / inst_holders）：可用，來源為 yf 即時 + cache。
- **價格資料衝突（需優先核對）**：Form 4 顯示 2026-10-02 至 10-06 成交價約 $23.78–$24.47，但 repo cache 的 currentPrice 為 $15.37（refreshed 2026-10-15），previousClose 為 $16.84。若兩者皆正確，代表 10 月初至 10 月中約 -36% 的跌幅，但 WebSearch 未找到相關新聞。在核對前，本報告不以任一價格作為結論依據。

## Analyst consensus
- 目前無可用的 buy / hold / sell 分布（live 與 cache 皆為空，info 中 numberOfAnalystOpinions、targetMeanPrice 均為 None）。
- 第三方聚合站說法不一致（僅供參考，未能於官方來源驗證）：
  - 一個來源列出 H.C. Wainwright 於 2025-10-13 與 2025-12-18 維持 Buy、目標價 $60。
  - Investing.com 顯示 1 buy、平均目標 $60。
  - Alpha Spread 平均目標 $61.20（區間 $60.60–$63）。
  - MarketBeat 顯示 Hold 共識（1 buy、1 sell），目標 $60。
- 近期升降評等：未找到 2026 年內的評等變動。最近可查到的目標價更新停留在 2025 年底。
- 結論：分析師面無法在當日確認，且所有已知訊號都來自 2025 年底，參考價值低。

## Retail social
- Reddit：未找到 r/wallstreetbets 或 r/stocks 的 ARQQ 討論串（WebSearch 結果以自動生成的價格頁為主）。**DATA_UNAVAILABLE**。
- StockTwits / X：
  - StockTwits symbol 頁有一份快照（無日期）顯示市值約 $290M、股價約 $16.65，並有趨勢標題「ARQQ Stock On Track For A Four-Month High」。標題本身無法確認日期與情緒內容。
  - 未取得可引用的貼文或 X 討論。
- 聲量（相對於平常）：無法量化。10 日平均成交量約 307,000 股（cache），僅能視為普通到偏低的散戶熱度，屬定性推論。
- 主題（可見的幾條線索，均為間接來源）：
  - 量子加密（post-quantum cryptography）政府標案與英國 NCSC PQC pilot 的正面敘事（來自 TipRanks 摘要頁，多為被動引用）。
  - 合約落地時程的疑慮（TipRanks 的 bear case：新客戶收入可能延後）。
  - 無具體可引用的散戶原文，因此無法列出代表性引言。
- 散戶傾向：無法判定（DATA_UNAVAILABLE）。

## Insider activity
統計區間：2026-04-15 至 2026-10-15（6 個月）。

- **公開市場買進（Buy）：0 筆**。
- **公開市場賣出（Sale，有價格）：約 $2.65M**（含 Lefebvre D'Ovidio 間接持有之賣出 $1.64M；扣除後約 $1.01M 來自直接持有人）。
- **衍生性證券行使（Conversion，行權價 $2.50，非市場買進）**：
  - Calabria Carlo（Director）2026-06-03：120,000 股，名目 $300K。
  - Ritchie Garth（Director）2026-06-05：73,562 股，名目 $184K。
  - Lefebvre D'Ovidio Manfredi（Director，間接持有）2026-09-22：4,600,000 股，名目 $11.5M。
  - 行權後是否立即出售未知，需與賣出紀錄分開看待。
- **無價格列（Value 為空）**：多筆列於 Oct 1–5、Jul 1、Apr 1 等日期，且與賣出同日出現（例如 Leaver 5,208–5,209 股重複列出），性質（歸屬、配股、稅務扣繳或其他代碼）無法從資料判定，未計入金額。

主要個人與事件：
- **Andrew Leaver（CEO）**：6 個月內公開市場賣出約 $437K（2026-07-02 9,893 股 @ $25.20，$249K；10-02 2,818 股 @ $24.47，$69K；10-05 2,535 股 @ $23.78，$60K；10-06 2,398 股 @ $24.19，$58K）。
- **Patrick Willcocks（General Counsel）**：2026-06-30 4,000 股 @ $29.48（$118K）；07-02 2,009 股 @ $25.20；10-02、10-05、10-06 亦有小額賣出。
- **Jennifer Bers（Officer）**：2026-06-22 8,288 股 @ $21.42（$178K）。
- **Pointon Nicholas（CFO）**：2026-04-20 435 股 @ $15.87（$7K）；4 月初另有較大賣出（4/2 約 $23K，超出 6 個月窗口）。
- **Oct 2–6 群體賣出**：Leaver、Willcocks、Feenan、Wilder、Nilan、Ritchie 幾乎在三個交易日連續以 $23.78–$24.47 出售，每次金額多為 $3K–$68K。此一集中且規律的模式可能屬於預先排程或稅務相關，但資料中未註明 10b5-1，無法確認。
- Director 群體（Ritchie、Calabria、Lefebvre）同時有行權與部分賣出紀錄。

整體解讀：6 個月內無內部人買進，且高階主管與董事在 2026 年 7 月與 10 月連續賣出，屬偏空訊號。但賣出規模相對 ~267M 市值仍小，且多數為小額，若為排程或稅務性質，偏空強度應打折。

## Ownership shifts
- 機構持股約 82.6%（institutionsPercentHeld），內部人持股約 2.7%，機構數量約 94 家。
- 集中度高：前兩大持有人合計約 65%。
  - Defiance ETFs, LLC：約 32.6%，5.10M 股，2026-06-30 較前期 +2.5%。
  - Penserra Capital Management LLC：約 32.5%，5.08M 股，2026-06-30 較前期 +2.5%。
- 其他顯著變動（2026-06-30）：UBS +5.1%（522,874 股）、Legal & General +4.2%、National Bank of Canada 大幅增持至 212,000 股（+193%）。
- Kessler Investment Group（2026-09-30）小幅減持 -0.1%。
- 趨勢判斷：前兩大持有人在 6 月小幅加碼，其餘機構小幅混合。資料最新僅到 2026-09-30，且 13F 有時間差，無法判定 10 月的機構動向。
- 空方部位：short interest 約佔流通股 17.8%（約 2.6M 股），偏高，代表空方仍有相當部位。

## Net sentiment score
**綜合：偏空（bearish-leaning），信心：低。**

理由：
- 內部人面（唯一可用的有效訊號）：偏空。0 筆公開市場買進，CEO 與多位高階主管在 7 月與 10 月持續賣出。
- 分析師面：DATA_UNAVAILABLE，不計入分數。
- 散戶面：DATA_UNAVAILABLE，不計入分數。
- 空方部位：17.8% 流通股 short interest，偏空。
- 信心下調原因：(1) 價格資料衝突，無法確認 10 月的股價走勢；(2) 分析師與散戶兩大面向都缺資料；(3) 唯一可用的內部人訊號可能含排程或稅務性質賣出。

**Divergence flag：無法判定**（缺乏分析師與散戶其中一方的傾向，無法比較是否反向）。

## 後續核對建議
1. 核對 ARQQ 的 2026-10-06 至 10-15 收盤價（cache $15.37 與 Form 4 $24 不一致），確認是否為真實下跌或資料錯誤。
2. 以 SEC EDGAR 核對 Form 4 的交易代碼（P / S / M / F / A），確認賣出是否屬 10b5-1 排程或稅務扣繳。
3. 取得即時 analyst tab（或 Benzinga / MarketBeat 完整頁面）確認現行評等分布與目標價。
4. 直接查閱 r/wallstreetbets 與 r/stocks 的 ARQQ 搜尋結果，或於可連線環境重試 StockTwits API。

SENTIMENT REPORT COMPLETE
