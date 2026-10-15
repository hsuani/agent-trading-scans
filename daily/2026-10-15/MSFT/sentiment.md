# Sentiment — MSFT as of 2026-10-15

資料說明：`pipeline/tools/yf MSFT` 的 `rec_summary`、`recommendations`、`insider`、`major_holders` 四個端點皆回傳 ConnectionError (curl 7, CONNECT tunnel failed, response 403)。`/root/.ccr/README.md` 狀態端點記錄為 Yahoo 相關主機 (query2.finance.yahoo.com、guce.yahoo.com) 遭 proxy 政策拒絕, 屬 policy denial, 依規定不重試、不繞過。`prices/yf/MSFT.json` 快取亦不存在。Reddit 與 StockTwits 未取得當期內容。以下各節僅使用 WebSearch 找到的內容, 並標註日期, 不以舊資料冒充當期數字。

## Analyst consensus
DATA_UNAVAILABLE。yf 分析師評級、評級變動與目標價端點皆失敗, 無當期 buy / hold / sell 分布, 不提供當期共識。

僅供參考的過期第三方摘要 (非 2026-10-15, 未納入判斷):
- Benzinga 快照 (約 2026-08-11): 32 位分析師, 1 Strong Buy / 29 Buy / 2 Hold, 平均目標價約 555 美元。
- StreetInsider 評級歷史 (約 2026-08 前後的 12 個月視窗): 平均目標價約 550 美元, 區間約 400 (Melius) 至 690 (Tigress Financial)。Morgan Stanley 2026-07 首次給予 Overweight, 目標價 600; CLSA 2026-07 首次給予 Outperform, 目標價 535。
- Bernstein 2026-07-30 目標價上調至 647; Tigress 2026-08-05 上調至 690。

上述數字日期早於當期 6 週以上, 且來源為聚合站, 下游不應把它們當作 10-15 的共識。

## Retail social
- Reddit: DATA_UNAVAILABLE。WebSearch 未回傳 r/wallstreetbets 或 r/stocks 的 MSFT 近期討論串, 無法評估討論量與多空傾向。Reddit JSON 端點屬於受阻主機, 本次未以 WebFetch 嘗試。
- StockTwits / X: 僅有過期資料, 無當期數據。
  - StockTwits (2026-06-25 前後): 報導指 MSFT 情緒由 bullish 轉為 bearish, 當時股價年初至今跌約 24%。交易者把跌幅歸因於晶片 supercycle 的資金輪動, 有評論指記憶體晶片股走強、雲端客戶股價走弱。
  - SentiSense (2026-08-09 前後): 30 日情緒分數為 bullish, 但當日讀數轉為 bearish; Reddit 聲量占比約 33%, News 占比約 51%。
  - X: 2026-08 底的摘要頁顯示 "bullish" 但同頁股價為 517.28 美元, 日期與價格不一致, 不採用。
- 聲量 (buzz volume): 無法量化。WebSearch 結果中 MSFT 的社群討論以 6 月與 8 月為主, 未見 10 月的聲量訊號。
- 主題 (以過期資料為限):
  - 資本支出與 AI 投資回報: 市場等待龐大 AI 投入轉為實際報酬, 2026 資本支出指引約 1,900 億美元 (另一來源 1,750 億美元, 數字不一致)。
  - 毛利率下滑: 報導指毛利率降至 67.6%, 為 2022 年以來最低。
  - 估值面: 報導指 forward P/E 約 20.2 倍, 為 2016 年底以來最低 (Koyfin 數據, 日期為 6 月前後)。
  - 晶片 supercycle 輪動: 散戶把 MSFT 弱勢歸因於資金流向半導體。

## Insider activity
DATA_UNAVAILABLE。yf insider 端點失敗, 無法計算近 6 個月淨買賣金額, 亦無法確認 CEO / CFO 或其他內部人的交易紀錄。

Net 6mo: DATA_UNAVAILABLE。

## Ownership shifts
DATA_UNAVAILABLE。yf major_holders 與 inst_holders 皆無法取得, 無機構持股集中度趨勢。

## Net sentiment score
- Composite: 中性 (低信心)。分析師面與內部人面無當期資料; 散戶面僅有 6 至 8 月的過期訊號, 且偏空 (bearish flip) 與分析師偏多 (舊資料) 的對比無法在 10-15 驗證。此分數僅反映資料缺口, 不構成方向性判斷。
- Confidence: 低。有效當期樣本為 0 (analyst、insider、holders、Reddit 皆缺)。
- Divergence flag: 無法判斷。過期資料顯示散戶偏空與分析師偏多的對比, 但兩者日期不同, 不能當作 10-15 的背離訊號。

## Data gaps and next steps
- yf 端點恢復後重跑: `pipeline/tools/yf MSFT rec_summary`、`recommendations`、`insider`、`major_holders`。
- 若 yf 持續受阻, 可依 `daily/2026-10-15/MSFT/fundamentals.md` 的建議, 由 GitHub Actions `yf.py refresh-cache` 產生快取後重跑。
- 2026-10-27 MSFT FQ1 FY2027 財報 (依 `news.md` 所列日期, 待 IR 確認) 前後, 分析師評級與目標價通常會大幅調整, 建議屆時重新抓取。

SENTIMENT REPORT COMPLETE
