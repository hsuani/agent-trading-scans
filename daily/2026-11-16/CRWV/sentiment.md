# Sentiment — CRWV as of 2026-11-16

資料來源狀態: Reddit 與 StockTwits 直接存取皆失敗 (Reddit 被拒絕, api.stocktwits.com 無法解析), 散戶部分僅能依次級新聞搜尋結果推估, 信心低。yf 工具的 Yahoo cookie/crumb 取得失敗但仍回傳資料, 數值可用。

## Analyst consensus

| 評級 | 家數 (最新, period 0m) | 三個月前 (-3m) | 變化 |
|---|---|---|---|
| Strong Buy | 7 | 5 | +2 |
| Buy | 24 | 21 | +3 |
| Hold | 7 | 10 | -3 |
| Sell | 2 | 1 | +1 |
| Strong Sell | 1 | 1 | 0 |
| 合計 | 41 | 38 | |

目前 41 家中 31 家 Buy 系 (約 76%), 7 家 Hold (約 17%), 3 家 Sell 系 (約 7%)。三個月內 Buy 比例由約 68% 升至約 76%, Hold 減少。

最近動作 (WebSearch 次級報導, 未逐一核對原始研報):
- Stifel 目標價由 $120 降至 $60 並維持 Hold, 時間點為公司上修 2026 年營收指引之後。
- Citi 認為股價有大幅上行空間 (報導標題指 "over 200% upside"), 屬偏多。
- Jim Cramer 給予 BUY (此為媒體人評論, 不計入 sell-side 共識)。
- 另一來源 Stockchase 統計過去 12 個月 12 筆評級 (5 Buy / 2 Hold / 5 Sell), 與 yf 的 41 家口徑不同, 不宜混用。

## Retail social

- Reddit: 無法取得 (WebFetch 遭拒絕)。r/wallstreetbets 與 r/stocks 的 CRWV 搜尋未能讀取, 散戶取向無法直接判斷。
- StockTwits: 無法取得 (api.stocktwits.com 在本工作階段無法解析, 需於網路設定允許該網域後重試)。
- X / 新聞: 次級報導 (StockTwits 新聞文章) 描述 Q3 財報後散戶情緒轉強、留言量偏高, 但未附具體貼文數量, 無法核對。此為間接描述, 不當作直接證據。
- 聲量 (buzz volume): 無法量化相對於平時的倍數, 定性判斷為 "財報前後偏高, 日常水準無資料"。
- 散戶取向: 無法可靠判定。次級來源同時出現偏多 (財報後反彈、Citi 上行目標) 與偏空 (債務與資本支出疑慮) 兩種敘述, 目前標示為 "混合, 信心低"。
- 主要議題 (依次級報導彙整):
  - 債務與再融資風險: 報導提到公司債價格明顯走弱, 引發違約與再融資疑慮。
  - 資本支出與股權稀釋: 財經評論持續關注資本支出壓力與稀釋風險。
  - 股東訴訟: 有律師事務所表示正在調查公司高階主管與董事的潛在責任。
  - 同業聯動: 新雲端 (neocloud) 同業財報會帶動 CRWV 股價, 被視為 "槓桿化 AI 交易"。
  - 財報日期不一: 不同來源分別寫 11/10 已公布與 11/16 預期公布, 散戶討論可能因此混亂, 需以公司公告為準。

## Insider activity

資料區間: yf insider 回傳 150 筆, 最早一筆為 2026-06-17, 最新為 2026-11-09。6 個月窗口 (2026-05-16 起) 的前段可能未完整涵蓋, 數字為 "回傳期間內的合計"。

Net 6mo (可見期間): 買入 $0 (無公開市場買入)。賣出約 $1.23B (USD B), 共 79 筆賣出交易。

| 人員 | 身分 | 賣出金額 (USD B) | 備註 |
|---|---|---|---|
| Magnetar Financial | 10% 以上持股人 | 0.51 | 8 月集中出售, 單日最高約 $0.23B (8/12) |
| Michael N. Intrator | CEO | 0.42 | 每週固定 307,692 股, 週期性出售, 疑似預定計畫 (10b5-1 未經核實) |
| Brannin McBee | Officer | 0.23 | 6–8 月多次出售, 單筆最大約 $0.02B |
| Kristen J. McVeety | General Counsel | 0.02 | 含選擇權行使後賣出 |
| Brian M. Venturo | Officer & Director | 0.02 | 6 月與 9 月出售, 9/18 另有股票贈與 |
| Nitin Agrawal | CFO | 0.02 | 8–9 月多筆出售 |
| 其他 (Goldberg, Jones, Jain, Baker) | Officer / COO | 0.01 | 小額 |

其他非市場交易: 董事 (Hutchins, Whitman, Boone) 有股票授予 (grant), 金額極小, 屬例行薪酬性質, 不列為看多訊號。

價格脈絡: 6 月至 10 月內部人賣出價格區間約 $66–$111, 11/09 COO Jain 於 $46.23 賣出 13,611 股, 顯示股價在 11 月初已大幅下跌。

## Ownership shifts

- 內部人持股 (insidersPercentHeld): 約 20.0%。
- 機構持股 (institutionsPercentHeld): 約 77.3%; 持股機構家數 1,371 家。
- 機構占流通股比例: 約 96.6%。
- 前十大持股 (最近申報):
  - Magnetar Financial: 11.35% (6/30 申報, 較前期減持約 24%)。
  - Nvidia: 10.29% (6/30 申報, 持平)。
  - BlackRock: 5.25% (較前期增持約 157%)。
  - Goldman Sachs: 3.95%。
  - Vanguard (兩個實體合計): 約 7.1%。
  - Invesco: 2.76% (9/30 申報)。
  - Alyeska Investment Group: 2.37% (增持約 56%)。
  - Value Aligned Research Advisors: 2.37%。
  - Bank of America: 1.80%。
- 趨勢判讀: 機構持股集中度高, 大型被動基金與策略型持股者 (Nvidia) 持股穩定; Magnetar 持股同時出現在 13F 減持與 Form 4 大額賣出, 方向一致。注意: 13F 資料截至 6/30 與 9/30, 距 2026-11-16 有一段時間差。

## Net sentiment score

- 分析師: 偏多 (Buy 系占約 76%, 買入比例三個月內上升), 但目標價下修 (Stifel) 顯示估值分歧。信心: 中高。
- 內部人: 偏空 (可見期間約 $1.23B 賣出、零公開市場買入; 主要賣方為 10% 持股人與 CEO)。信心: 高 (交易記錄直接可查), 但需注意部分賣出可能屬預定計畫, 不必然代表對前景的判斷。
- 散戶: 無法可靠判定, 次級來源呈現混合 (財報後偏多、債務與稀釋疑慮偏空)。信心: 低。
- 綜合: 中性 (信心低)。分析師與內部人方向相反, 散戶資料缺口使整體判斷受限。

Divergence flag: 是 (分析師偏多 vs 內部人大額賣出偏空, 方向相反)。散戶與分析師之間的分歧無法判定, 因 Reddit 與 StockTwits 皆無法取得。
注意: 本報告為 Phase-1 情緒盤點, 不含交易建議。

SENTIMENT REPORT COMPLETE
