# Sentiment — GOOGL as of 2026-11-16

資料狀態: Phase-1 部分完成。yf 分析師與內部人資料可用; Reddit 與 StockTwits 無法取得原始貼文 (見下方); 散戶情緒主要來自 WebSearch 彙整, 可信度低。

## Analyst consensus
58 家分析師: 10 Strong Buy / 43 Buy / 5 Hold / 0 Sell / 0 Strong Sell (即 買方 91.4%, 持有 8.6%, 賣方 0%)。

近 3 個月趨勢 (yf recommendations, 0m 對比 -3m):

| 評等 | -3m | 0m | 變化 |
|---|---|---|---|
| Strong Buy | 13 | 10 | -3 |
| Buy | 45 | 43 | -2 |
| Hold | 5 | 5 | 0 |
| Sell / Strong Sell | 0 | 0 | 0 |
| 合計 | 63 | 58 | -5 |

解讀: 評等總數減少 5 家, 但沒有出現賣出評等。買方比例仍高, 強力買進家數略減。yf 只提供計數, 沒有逐筆升降評等紀錄。

近期評等動態 (WebSearch, 單一來源, 未交叉驗證):
- Zacks Research 於 2026-08-13 將 GOOGL 降至 Hold (MarketBeat 標題)。
- 10 月 MarketBeat 文章指出分析師維持 Buy 但下調目標價, 理由是搜尋成長放緩與 YouTube 廣告營收低於預期。
- 聚合網站平均目標價約 400.37 美元, 標示隱含上漲約 37%。此數字未與 yf 核對, 且隱含現價 (約 291 美元) 與其他來源的 8 月價格 (約 356 美元 開盤) 不一致, 僅供參考。
- 其餘 WebSearch 提到的 Citi、Loop Capital、BNP Paribas、Mizuho 評等動態, 內容看來屬於 2025 年底, 非 2026 年 11 月, 不採計。

## Retail social
- Reddit: 無法取得。WebFetch 回傳 "unable to fetch www.reddit.com", 依規則軟失敗, 未擷取 r/wallstreetbets 與 r/stocks 的 25 篇貼文。
- StockTwits: 無法取得。api.stocktwits.com DNS 解析失敗, 屬於網路白名單問題。需在 session 網路設定中允許此網域後才能重試。
- X / 新聞 (WebSearch 彙整, 日期混雜, 多數非 11 月):
  - 10 月 8 日 r/wallstreetbets 一則看多貼文 (AI 軟體複製話題) 有約 501 讚與 178 則留言 (來源為 24/7 Wall St. 快照)。
  - Insider Monkey 將 GOOGL 列為 WSB 熱門、對沖基金也持有的股票之首, 但文章沒有日期。
  - 一則聚合頁面稱「86% 正面情緒」, 無法驗證, 不採用。
  - 其他 SEO 型頁面 (Brand Industry、Streets For All、Publisher Collective) 無實際情緒資料, 不採用。
- Buzz 量: 無法量化。沒有可靠的 2026 年 11 月提及數, 不宣稱有「高於平常」或「低於平常」。
- 散戶傾向: 偏多但證據薄弱。樣本以看多為主 (TPU 與 NVIDIA 競爭、雲端成長、AI 搜尋), 偶有中性與看空文字。

Themes (依來源出現頻率排序, 非量化):
1. 看多: 雲端 (Cloud) 成長、TPU 競爭力、企業 AI 合約。
2. 看空: 10 月 Q3 財報後自由現金流轉負 (資本支出增加), 搜尋成長放緩, YouTube 廣告不如預期。
3. 法律與題材: 集體訴訟調查形成法律風險; Golden Dome 國防合約傳聞 (11 月, 單一來源)。
4. 資金流: ARK Invest 於 11 月 6 日約買入 200 萬美元 (單一來源)。

## Insider activity
查詢區間: 2026-05-16 至 2026-11-16 (6 個月)。

| 日期 | 內部人 | 職位 | 交易類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-08-07 | Sergey Brin | 董事、>10% 實益持有人 | 贈與 (Gift) | 673,200 | 0 (無現金) |
| 2026-10-13 | Kavitark Ram Shriram | 董事 | 贈與 (Gift) | 396,700 | 0 (無現金) |

Net 6mo: 買入 0 USD M / 賣出 0 USD M (公開市場)。非現金贈與合計 1,069,900 股。

區間外參考 (近 12 個月):
- John L. Hennessy (董事) 於 2026-01-13 與 2026-02-13 各賣出 600 股 (約 20.3 萬與 18.4 萬美元), 為小額。
- Kavitark Ram Shriram 最後一次公開市場賣出為 2025-08-15, 26,000 股, 約 533 萬美元。
- 2026 年 2 月 Brin 亦有一筆 437,500 股贈與 (非現金)。

解讀: 6 個月內無公開市場買賣。主要為創辦人與董事的贈與, 屬於資產規劃性質, 不宜直接解讀為看空或看多。沒有 CEO 或 CFO 的交易紀錄。內部人情緒中性。

資料注意: 此工具輸出的 Brin 8 月那一列有重複 (一列有金額 0、一列金額空白), 已合併計算。

## Ownership shifts
- 內部人持股: 1.73%。
- 機構持股: 80.5%, 機構家數 7,483。
- 前十大機構合計約 33.8% (以下為各機構報告的持股比例與報告區間內的變動):

| 機構 | 持股比例 | 持股 (M 股) | 報告期 | 區間變動 |
|---|---|---|---|---|
| BlackRock | 7.83% | 461.0 | 2026-06-30 | +3.1% |
| Vanguard Capital Mgmt | 6.50% | 383.0 | 2026-06-30 | +1.2% |
| FMR (Fidelity) | 4.21% | 247.7 | 2026-09-30 | -1.2% |
| State Street | 4.11% | 242.3 | 2026-09-30 | +1.4% |
| Geode | 2.58% | 151.9 | 2026-09-30 | +1.2% |
| Morgan Stanley | 2.05% | 120.5 | 2026-06-30 | -0.4% |
| T. Rowe Price | 1.72% | 101.3 | 2026-06-30 | +25.9% |
| Vanguard Portfolio Mgmt | 1.68% | 98.9 | 2026-06-30 | +2.4% |
| JPMorgan | 1.60% | 94.1 | 2026-09-30 | +2.4% |
| Invesco | 1.55% | 91.4 | 2026-09-30 | +0.1% |

趨勢: 前十大中 8 家增持、2 家減持 (FMR、Morgan Stanley)。T. Rowe Price 增幅最大。整體傾向機構淨增持, 但增幅多為個位數百分比。

單位交叉檢查: BlackRock 持股 4.61 億股 ÷ 7.83% ≈ 總股數 58.9 億股。持倉市值 1,363.4 億美元 ÷ 4.61 億股 ≈ 每股 295.8 美元 (2026-06-30 參考價)。以此推算市值約 1.74 兆美元 (約 1,740 B USD)。此為推算值, 非 yf 直接提供。

## Net sentiment score
Composite: **偏多 (bullish), 信心中低**

- 分析師: 偏多, 信心高 (91% 買方、0 賣出評等), 但評等總數減少 5 家、強力買進減少 3 家, 且 8 月 Zacks 降為 Hold。
- 散戶: 偏多但證據薄弱。Reddit 與 StockTwits 皆無資料, 只能依 WebSearch 彙整, 且日期多非 11 月。
- 內部人: 中性。無公開市場買賣, 僅為贈與。
- 機構: 偏多。前十大多數增持。

信心偏低的主因: (1) 散戶資料缺失 (2 個主要來源皆失敗); (2) 分析師評等數量下降; (3) 基本面論述 (FCF 轉負、搜尋放緩) 與評等的正面論述並存, 散戶與基本面看法分歧。

Divergence flag: **否**。散戶 (弱偏多) 與分析師 (偏多) 方向一致, 沒有出現相反傾向。但需注意散戶資料不足, 此判定可能因資料不完整而失準。

Data gaps (待補):
- Reddit r/wallstreetbets 與 r/stocks 原始貼文與提及數 (WebFetch 被擋)。
- StockTwits 訊息流與多空標籤 (DNS 失敗; 需允許 api.stocktwits.com)。
- 逐筆評等升降紀錄 (yf recommendations 僅有計數)。
- 目前股價 (本次未取得, 目標價隱含漲幅未驗證)。

SENTIMENT REPORT COMPLETE
