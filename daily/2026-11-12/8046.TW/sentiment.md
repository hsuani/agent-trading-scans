# Sentiment — 8046.TW (南電) as of 2026-11-12

資料完整度警示: Reddit 與 StockTwits 本次皆無法取得 (見下方), yfinance 的 cookie/crumb 連線失敗, 分析師與內部人資料可能非最新。整體結論信心偏低。

## Analyst consensus
14 家: 3 strong buy / 10 buy / 1 hold / 0 sell (rec_summary, 0m 期)。近四個月 (0m, -1m, -2m, -3m) 分布完全相同, 代表 yf 資料可能未更新, 或期間內無評等變動, 無法區分。

近期目標價動向 (取自媒體轉述券商報告, 非原始報告):
- 高盛 (7 月中): 由 1,115 元升至 2,310 元, 維持買進並列首選。理由為 ABF 載板缺貨可能超過 30 個月。
- 大和資本: 合理股價拉升至 2,444 元 (市場最高)。
- 本土法人 (7 月 27 日): 維持買進, 目標價由 1,100 元上調至 1,500 元, 評價基礎為 2027 年預估 EPS 之 45 倍。
- 花旗、摩根士丹利 (7 月中): 同步調升目標價, 文中未列具體數字。

注意: 最新一筆可查到的目標價報導為 2026 年 7 月 27 日, 距報告日超過三個月。目標價區間 1,500 元至 2,444 元, 分歧極大。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 本次無法取得 (WebFetch 無法連線 www.reddit.com), 無聲量與情緒數據。
- StockTwits / X: StockTwits 因 api.stocktwits.com 無法解析 (DNS 失敗) 而略過。X 無直接資料, 改以新聞搜尋替代。
- 新聞與討論區替代來源: 搜尋結果以法人報導與財經媒體為主, 未見有效的散戶討論樣本。近期股價曾出現 2 成左右回檔 (南電、景碩、欣興自前波高點起算), 屬媒體描述。
- 聲量: 無法量化, 無法與平常基準比較。
- Themes (由新聞與法人報告歸納, 非散戶原文):
  1. ABF 載板缺貨與長約 (LTA) 價格上漲 (高盛預估 2026 下半年至 2028 年缺貨率 14% / 34% / 51%)
  2. 估值偏高 (媒體提及本益比約 173 倍, 日期不明, 殖利率約 0.14%)
  3. 風險面: T-glass 供應變化, ABF 與 BT 載板價格走勢, 籌碼面波動
  4. 第三季營收預估季增 18.5% (法人預估, 媒體轉述)
  5. 第四季營收預估持平, PCB 受淡季影響可能季減近 2 成 (較早期的法人看法)

## Insider activity
Net 6mo: 無資料。yf insider 回傳空清單, 但 yfinance 連線失敗, 無法確認是真的沒有交易, 或是抓取失敗。本次不做「無內部人交易」的結論。
ownership 參考 (major_holders): 內部人持股 61.36%, 機構持股 14.49% (佔流通股 37.50%), 機構數 138 家。

## Ownership shifts
- 目前只有單一時點的快照 (major_holders), 無歷史比較, 無法判斷機構集中度趨勢。
- 內部人持股比例高 (約六成一), 流通股多數不在機構手中, 股價易受籌碼波動影響 (與新聞所提「籌碼面波動」一致)。

## Net sentiment score
Composite: **偏多 (bullish), 信心低**。
- 分析師端: 偏多 (14 家中 13 家買進以上, 0 家賣出, 目標價持續上調)。
- 散戶端: 無資料, 無法判定。
- 內部人端: 無資料。
- 信心低的原因: 單一來源 (分析師), 且資料為 2026 年 7 月前後, 距報告日已有數月。

Divergence flag: **無法判定 (no)**。缺少散戶資料, 無法比較與分析師方向是否相反。若後續取得 Reddit 或 StockTwits 資料, 再行重算。

## 資料來源與限制
- yf (recommendations, rec_summary, insider, major_holders): 部分成功, cookie/crumb 失敗。
- Reddit (r/wallstreetbets, r/stocks): 失敗, 無法連線。
- StockTwits: 失敗, DNS 無法解析 (api.stocktwits.com 需在 session 網路設定中允許)。
- 新聞搜尋: 成功, 但多為 2025 年底至 2026 年 7 月的報導。
  - [南電 11 月營收符合預期 法人估第 4 季 EPS 為 1.3 元](https://money.udn.com/money/story/5607/9187590) (日期偏早, 2025 年底前後推估)
  - [南電 (8046) 股價 1415 元還能買? 最新目標價曝光](https://www.businesstoday.com.tw/article/category/183008/post/202607150049/)
  - [ABF 四強目標價 調高](https://money.udn.com/money/amp/story/5607/9625332)
  - [mirrormedia 2026.07.27 報導](https://www.mirrormedia.mg/external/setn_1879204)

## 單位
本報告無 TWD 總額數字 (無營收、市值、淨利), 價格與目標價為每股 元 (TWD/股), 未換算為 億。
