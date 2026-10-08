# Sentiment — PANW as of 2026-10-09

環境日期為 2026-10-08，任務指定 as-of 為 2026-10-09，以下以任務日期為準；最新內部人交易日為 2026-10-01。

## Analyst consensus
yf rec_summary 目前 55 家：10 strong buy / 32 buy / 11 hold / 1 sell / 1 strong sell。買方合計 42 家（約 76%），持有 11 家（約 20%），賣方 2 家（約 4%）。

三個月前（-3m）為 11 / 34 / 9 / 1 / 0，買方 45 家（約 82%），持有 9 家。近三個月買方家數減 3、持有增 2、賣方增 1，屬於輕微降溫，尚非方向翻轉。

Benzinga 2026-09-04 快照（33 家，來源不同、計數口徑不同）：28 buy / 1 strong buy / 4 hold，平均目標價 $377，當時股價約 $330.5。
近期目標價異動：
- Citi 2026-09-02 由 $400 上調至 $410。
- Argus 2026-09-03 維持 Buy，目標 $425。

注意：內部人 2026-09-24 至 10-01 的成交價約 $388–396，已高於 Benzinga 平均目標價 $377。目標價可能落後股價，此為事實觀察，不構成結論。

資料缺口：
- yf 的 recommendations 只提供計數快照，沒有逐筆升降評等事件。
- 目前最新平均目標價無法從資料確認。
- 4 月 WSJ 調查（55 家，41 buy / 5 overweight / 8 hold / 1 sell，平均目標 $207.75）已過時，不可作現況依據。
- TipRanks 上 Citi 調至 $432（自 $395）的消息無日期，與 9/2 的 Citi 動作不符，未採用。

## Retail social
- Reddit (r/wallstreetbets, r/stocks)：無法取得。WebFetch 回報 unable to fetch；直接 curl 經 proxy 回 403 CONNECT tunnel failed。依規定 soft-fail，未嘗試繞過。
- StockTwits：無法取得。WebFetch 回報 ENOTFOUND；直接 curl 回 403 CONNECT tunnel failed。
- X / 新聞：WebSearch 未找到 2026 年 10 月的散戶討論。找到的文章多為 4–5 月與 7 月資料，不能代表當前情緒。
- 討論量：無法量化，無 buzz 基準比較。
- 散戶傾向：無法判定（資料缺口）。
- 主題（僅來自新聞，非散戶貼文）：
  - AI 威脅被視為提升資安支出的催化劑，而非對資安廠商的風險（Blockonomi 文章，無日期，聲稱 6/10 起上漲約 32%）。
  - 9/1 Console 收購案（單一聚合站資料）。
  - 股價由 4 月約 $180 上漲至 10 月約 $390，屬於大幅上漲後的市場討論。

## Insider activity
區間：2026-04-09 至 2026-10-08（6 個月）。
- 公開市場買入：0 筆。
- 公開市場賣出：22 筆，總金額約 $49.1M（以 yf Value 欄加總）。
- 排除 Form 4 授予與贈與，不計入淨額。

主要賣方（依金額）：
- Lee Klarich（Officer and Director，CTO 身分）：2026-05-22，62,904 股，約 $16.27M，價格 $250–261。
- James Joseph Goetz（Director）：2026-09-17，20,000 股，約 $7.53M；2026-06-12，20,000 股，約 $5.60M。
- Dipak Golechha（CFO）：2026-09-24，27,500 股，約 $10.77M，價格 $388.69–396.21；另有 6/23 約 $1.45M、4/01 約 $0.80M。
- John Phillip Key（Director）：6/12 約 $2.09M、9/14 約 $0.94M。
- Joshua D. Paul（Officer）：7 筆，多為 900–1,100 股，約 $1.7M 合計，最新 10/01 400 股。此模式接近定期賣出，但資料未標註 10b5-1 計畫，無法確認。

CEO Nikesh Arora 最近一次買入：2026-03-27，68,085 股，約 $10.0M，價格約 $147。此筆在 6 個月區間之外，但屬於年內最大的內部人買入訊號，與近期的大量賣出形成對比。

結論：6 個月內以淨賣出為主（約 $49M，0 筆買入）。CFO 與多位董事的大額賣出集中在 6–9 月，股價上漲期間同步出現。資料無法判斷是否屬計畫性出售。

## Ownership shifts
- 機構持股：84.35%（institutionsPercentHeld），float 持有 84.99%，機構數 3,849。
- 內部人持股：0.75%。
- 趨勢：yf major_holders 僅為單一快照，無歷史比較，無法判定集中度變化方向。

## Net sentiment score
- 分析師面：偏多（買方約 76%，較 3 個月前小幅降溫）。信心：中高。但目標價資料過時，方向可信度受限。
- 內部人面：淨賣出（6 個月 0 筆買入、約 $49M 賣出）。信心：中。多數賣出可能屬計畫性，無法確認。
- 散戶面：無資料。信心：無。
- 綜合：中性（信心：低–中）。分析師端偏多，內部人端淨賣出，散戶端缺資料，無法做完整交叉確認。

Divergence flag：是。分析師多數評等為買進，同期內部人為淨賣出，方向相反。散戶端無資料，無法比較。

本報告不含交易建議。

Sources:
- [Benzinga PANW price targets](https://www.benzinga.com/quote/panw/price-targets)
- [TipRanks / TheFly: Citi PT $432 (undated)](https://www.tipranks.com/news/the-fly/palo-alto-networks-price-target-raised-to-432-from-395-at-citi)
- [TipRanks / TheFly: Bernstein PT $207 (undated)](https://www.tipranks.com/news/the-fly/palo-alto-networks-price-target-raised-to-207-from-204-at-bernstein-thefly)
- [SentiSense: PTs raised to $290 (2026-05-27)](https://app.sentisense.ai/stories/palo-alto-networks-price-targets-raised-to-290-despite-different-analysts-05272026)
- [Blockonomi: PANW new peak on AI security (undated)](https://blockonomi.com/palo-alto-networks-panw-stock-surges-to-new-peak-as-ai-security-concerns-drive-growth/)

SENTIMENT REPORT COMPLETE
