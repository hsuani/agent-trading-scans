# Sentiment — LIN as of 2026-11-20

資料說明：Reddit (r/wallstreetbets, r/stocks) 與 StockTwits 皆無法連線（Reddit 回傳無法存取；api.stocktwits.com DNS 解析失敗，需於 session 網路設定允許該網域）。散戶情緒部分僅能以網路搜尋的次級資料補充，無法量化提及次數。

## Analyst consensus

截至 2026-11-20 (yfinance rec_summary, 0m)：**29 家券商，23 buy（strong buy 6 + buy 17）/ 5 hold / 1 sell（strong sell 0）**。買進比例約 79%。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m（當前） | 6 | 17 | 5 | 1 | 0 | 29 |
| -1m | 6 | 17 | 5 | 1 | 0 | 29 |
| -2m | 5 | 17 | 5 | 1 | 0 | 28 |
| -3m | 5 | 16 | 5 | 1 | 0 | 27 |

近三個月買進評等 +2（21 → 23），hold 與 sell 數量持平，評等結構偏多且略有上修趨勢。

Recent moves（次級來源，日期與數字需人工核對）：
- UBS (Joshua Spector) 2026-10-30 維持 Buy，目標價 $574 → $585（搜尋結果引用 Benzinga 彙整資料）。
- Citigroup 同期維持 Buy，目標價約 $580（同上來源）。
- Seaport Research 曾因 Q3 結果升級至 Buy（日期未確認）。
- Simply Wall St 共識估值 fair value 約 $544.40，對比其引用之收盤價 $515.25（日期未明）；該站亦提及 LIN 曾自部分 top ideas 名單移除，顯示近期相對同業超額報酬的信心偏保守。
- Barchart 估計 FY2026 調整後 EPS 約 $17.78（年增約 8%），並提到過去四季皆優於共識。

Rating-level 歷史變動（個別券商 upgrade/downgrade 逐筆紀錄）在 yfinance `recommendations` 中無法取得，僅有彙總計數。

## Retail social

- Reddit: 無法取得（r/wallstreetbets、r/stocks 搜尋皆回傳無法存取）。無法評估討論量與多空傾向。
- StockTwits / X: StockTwits 無法連線。X 與新聞端搜尋結果多為分析師評等與估值文章，未見可靠的近期散戶貼文樣本，故不引用個別發文。
- 量化提及次數：無資料，無法與常態比較。
- 散戶傾向：**無法判定**（資料缺口）。
- Themes（僅依次級搜尋所見，屬推估）：估值偏高（P/E 約 33.8x，Simply Wall St 稱為「較吃力」）、EPS 穩健成長、工業氣體定價與資本支出循環。

## Insider activity

以 2026-05-20 至 2026-11-20 為 6 個月窗口，依 yfinance insider 原始資料計算（單位 USD，以 M 表示）：

- **Buys（公開市場買進）**：約 $0.05M（1 筆，Paula Reynolds 董事，2026-08-18，100 股 @ $479.12）。
- **Sells（公開市場賣出）**：約 $4.85M（1 筆，Guillermo Bichara，Officer，2026-11-02，9,350 股 @ $518.91）。
- **選擇權行權（非現金買進）**：Bichara 同日以 @ $173.13 行權 26,155 股（名目約 $4.53M，與 9,350 股賣出同日發生，多為行權後出售）。
- 其他：Innocenzi Stefanos 2026-06-08 4,035 股（無價格資料，性質未確認，可能為獎酬配發）。
- 6 個月淨額：**賣出約 $4.85M，買進約 $0.05M，淨賣出約 $4.8M**（不計行權）。

Notable：
- CEO Sanjiv Lamba 於 2025-12-08 以 @ $396.68 公開買進 2,520 股（約 $1.0M），為 12 個月內較具代表性的高階主管買進，但超出 6 個月窗口。
- 過去 12 個月內 Bichara 多次賣出（2026-03-10 @ $480.79、2026-02-17 @ $480.45，及 2026-11-02）並伴隨選擇權行權，屬行權後出售模式，訊號強度有限。
- 董事 Stephen Angel 於 2025-08-07 賣出約 $23.8M，為 2025 年下半年規模最大的單筆賣出，已超出 6 個月窗口。
- 2026-03-09 多位高階主管與董事的無價格紀錄多為年度獎酬配發，不計入買賣。
- 內部人持股僅 0.25%，持股比例低，內部人交易對整體籌碼的影響有限。

## Ownership shifts

- 機構持股比例 90.3%（float 內 90.5%），機構數 3,395 家。
- yfinance 僅提供當前快照，無歷史季度變化，無法判定機構集中度趨勢。

## Net sentiment score

**Composite：偏多（bullish），信心中等（medium-low）。**

- 分析師面：偏多，信心高（23/29 buy，近三個月小幅上修）。
- 內部人面：小幅偏空至中性（6 個月淨賣出約 $4.8M，但多與選擇權行權同步，且 CEO 於 2025-12 有公開買進）。
- 散戶面：無資料，不計入評分。
- 扣分因子：估值偏高（P/E 約 33.8x），以及散戶資料缺口使整體信心降低。

**Divergence flag：無法判定。** 因散戶傾向資料缺失，無法確認是否與分析師傾向相反。待 Reddit 或 StockTwits 可連線後應重新評估。

SENTIMENT REPORT COMPLETE
