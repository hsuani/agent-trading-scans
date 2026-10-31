# Sentiment — ISRG as of 2026-10-31

## Analyst consensus
目前 34 位分析師：26 buy（含 7 strong buy）/ 6 hold / 2 sell（含 1 strong sell）。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 | 買方合計 (SB+B) |
|------|-----------|-----|------|------|-------------|------|----------------|
| 0m (現在) | 7 | 19 | 6 | 1 | 1 | 34 | 26 |
| -1m | 7 | 17 | 7 | 1 | 0 | 32 | 24 |
| -2m | 7 | 17 | 8 | 1 | 0 | 33 | 24 |
| -3m | 7 | 16 | 9 | 1 | 0 | 33 | 23 |

近三個月趨勢：買方家數由 23 增至 26，hold 由 9 降至 6，sell 由 1 增至 2（其中一家為 strong sell）。整體偏向正面但並非一面倒。

最近動態：yf 工具的 `recommendations` 回傳的是各期評等分布快照，不是逐筆升降評等紀錄，因此無法確認具體哪家券商在何時升評或降評。web 搜尋中有一則低品質聚合站提及某家機構（Wall Street Zen）降評，但無法從主要來源核實，僅列為待確認。目標價（price target）變動工具未提供，本報告無法評估。

## Retail social
- Reddit：r/wallstreetbets 與 r/stocks 搜尋請求均遭封鎖（WebFetch 無法連線 www.reddit.com），本次無樣本，無法判定散戶討論量與傾向。
- StockTwits：api.stocktwits.com 無法解析（DNS 失敗），需於 session 網路設定中允許該網域後才能取得。本次未取得資料。
- X / 新聞 web 搜尋：結果多為低品質聚合頁，缺乏可靠的散戶原始貼文。可用的語意如下：
  - 整體描述為「情緒分歧、偏中性偏謹慎」。
  - Equibles 綜合評等為 neutral，動能偏弱，機構資金呈現流出跡象，6 個月相對 S&P 500 強弱約 -37%（聚合站數據，未經核實）。
  - 10/23 有報導指 ISRG 當日表現優於同業（MarketWatch 類型來源）。
  - 一則 8/10 的文章指年初至該日股價跌幅約 30%，但同時指近期反彈為情緒改善訊號。
- 聲量（buzz volume）：無可靠數據，無法與歷史基準比較。

- Themes（自 web 搜尋歸納，樣本有限）：
  1. 美國手術量成長放緩的疑慮，是偏空論點的主要來源。
  2. 季報發布日期與結果在各來源間不一致（10/19 與 10/20 皆有出現），本報告無法確認 Q3 實際財報內容，此點需由一手來源核對。
  3. 股價自 8 月低點反彈至 10 月下旬，市場在 10 月底對短線趨勢的看法分歧。
  4. 多數「目標價預測」頁面數字差距極大（約 $325 至 $685），多為自動生成內容，不可作為情緒依據。

## Insider activity
Net 6mo（2026-05-01 至 2026-10-31）：$0 買入（未見公開市場買進紀錄）/ 約 $19.8M 賣出（約 22 筆 open-market sale；不含 option 行權 conversion 與無金額的 gift/授予紀錄）。

依金額排序的主要賣方：

| 日期 | 姓名 | 職位 | 交易 | 股數 | 金額 (USD M) |
|------|------|------|------|------|-------------|
| 2026-10-23 | GUTHART GARY S | Director（間接持有）| 賣出 @ 451.61 | 20,095 | 9.08 |
| 2026-08-11 | GUTHART GARY S | Director（間接持有）| 賣出 @ 400.00 | 10,000 | 4.00 |
| 2026-06-01 | JEDDI IMAN | Officer | 賣出 @ 420.55（另有 derivative 行權）| 5,625 | 2.37 |
| 2026-10-23 | WIDMAN FREDRIK | Officer | 賣出 @ 453.21（另有 derivative 行權）| 4,047 | 1.83 |
| 2026-10-23 | WADORS PATRICIA L. | Officer | 賣出 @ 443.80 | 1,078 | 0.48 |
| 2026-10-23 | BARRATT CRAIG H | Director | 賣出 @ 443.80（另有 derivative 行權）| 1,150 | 0.51 |

其餘小額賣出：BROSIUS MARK PRESTON（Officer，累計約 $0.41M，多筆每月小量）、LOEB GARY（Officer，3 筆合計約 $0.50M）、LADD AMY L（Director，8/11 賣出 $0.18M）、WIDMAN（9/15 賣出 $0.41M）。

CEO DAVID J. ROSA 於 6/10 與 7/10 有兩筆無金額紀錄（推測為 RSU 歸屬或稅務扣繳，非公開市場賣出），本報告不計入買賣金額。

觀察：
- 大宗賣出集中於 10/23 前後股價約 $440–$453 區間，且 Guthart 與多位 officer 同日成交，時點與股價高點重合。
- 過去六個月未見高階主管公開市場買進，只見賣出，屬偏空訊號；但多筆為小量定期性賣出（如 Brosius），可能為 10b5-1 計畫或稅務相關，無法由資料確認。
- 股價自 7 月約 $345 上漲至 10 月底約 $440–$450，部分賣出可能屬獲利了結，需與公司公告（Form 4 附註）交叉確認。

## Ownership shifts
- 機構持股：91.4%（float 口徑 91.9%），機構家數 3,136。
- 內部人持股：0.52%。
- 限制：`major_holders` 僅提供單一時點快照，無法判斷 13F 歷史趨勢，因此無法確認機構集中度是增加或減少。

## Net sentiment score
**Composite：中性偏多（confidence：低）**

分項判讀：
- 分析師共識：偏多（中等信心）。買方 26 / 34，買方家數三個月上升，hold 下降。
- 內部人：偏空（中等信心）。六個月約 $19.8M 公開市場賣出、零買進；但多為小量與可能的計畫性交易，偏空力道需保留解讀空間。
- 散戶：無法判定（無 Reddit、StockTwits 資料；web 搜尋結果品質不足）。
- 新聞與 web 聚合：中性偏謹慎（低信心，來源多為低品質聚合站）。

信心偏低的主因是散戶資料完全缺失，加上 Q3 財報細節無法確認。

Divergence flag：無法判定（no）。散戶傾向無有效樣本，無法與分析師傾向比較。若後續補上 Reddit 或 StockTwits 資料，應重新評估是否出現「分析師偏多、散戶偏空」的背離。

資料缺口與建議補強：
1. 允許 api.stocktwits.com 網域後重抓 StockTwits 串流。
2. Reddit 封鎖需另找可用端點（如 pushshift 替代或授權 API）後重試。
3. `recommendations` 工具僅回傳計數快照，建議補充逐筆 upgrade/downgrade 與 price target 來源。
4. 機構持股需補 13F 歷史資料以判斷集中度趨勢。

SENTIMENT REPORT COMPLETE
