# Sentiment — 5455.TWO 英特磊 as of 2026-11-22

> 資料完整度: 低。多數來源無法取得 (Yahoo 經 proxy 回 403 / 空陣列、Reddit 與 StockTwits 無法連線)，本報告無法給出可靠的分析師共識或散戶情緒數字。
> 代號確認: 搜尋結果顯示「英特磊」為 **4971 (IET-KY)**，並非 5455。目前無法確認 5455.TWO 是否對應英特磊，請先核對代號與公司名稱。

## Analyst consensus
無資料。`rec_summary` 與 `recommendations` 皆回傳空陣列，無法得知 buy / hold / sell 家數，也沒有目標價變動紀錄。
- 補充搜尋 (鉅亨、工商時報、Wantrich 等) 未找到 4971 或 5455 在 2026 年的券商評等或目標價。搜尋結果中唯一的 FactSet 目標價資料屬於 ENTG (Entegris)，與本標的無關，不採用。
- 因此「分析師偏多/偏空」無法判定。

## Retail social
- Reddit (r/wallstreetbets、r/stocks): 無法取得。WebFetch 回報 www.reddit.com 不在允許的網域內，未重試。
- StockTwits / X: StockTwits 的 api.stocktwits.com 解析失敗 (不在本 session 允許網域)，需在 session 網路設定中加入後才能重試。X 以 WebSearch 查詢，未找到與 5455 相關的 2026-11 貼文。
- 討論量: 無法量化。WebSearch 結果全部指向 4971，沒有 5455 的散戶討論串。
- 情緒傾向: 無法判定 (bullish / bearish / mixed 皆無樣本)。
- 主題: 無可靠樣本。以下為搜尋中出現、屬於 4971 的背景資訊，**不能直接套用到 5455**:
  - 2026-02 自結: 稅前盈餘 3,600 萬元 (年增 126.67%)，稅後 2,700 萬元 (年增 120.15%)。
  - 2026 年 InP 訂單量 "較去年翻倍" 的說法來自一篇推薦性文章，不是正式券商報告。
  - 美國德州二廠與聯邦晶片法案現金補助的簽約進度 (預計 2026 年完成)。

## Insider activity
Net 6mo: 無資料 (`insider` 回傳空陣列，無法區分是「無交易」或「連線失敗」)。無法列出 CEO / CFO 或其他人員的買賣。

## Ownership shifts
`major_holders` 有回傳部分資料:
- insidersPercentHeld: 70.34%
- institutionsPercentHeld / institutionsCount: 0.0

注意: 機構持股為 0 很可能是資料缺漏，不代表沒有機構持股。內部人持股 70% 偏高，可能包含控股股東或關係人持股，但資料未說明結構，也無法比較前後期趨勢。機構持股集中度的變化: 無法判定。

## Net sentiment score
Composite: **neutral (信心: 低)**。原因是分析師與散戶兩側皆無有效樣本，內部人交易無資料，僅能給出中性的預設值，不代表市場情緒真的中性。

Divergence flag: **無法判定 (no)**。缺乏散戶與分析師任一側的傾向數據，無法比較兩者是否背離。

## 資料來源狀態
| 來源 | 狀態 | 說明 |
|---|---|---|
| yf recommendations | 空陣列 | 無資料 |
| yf rec_summary | 空陣列 | 無資料 |
| yf insider | 空陣列 | 無資料 (與連線失敗無法區分) |
| yf major_holders | 部分成功 | 內部人 70.34%，機構欄位為 0 (疑似缺漏) |
| 另一代號 yf 測試 (4971) | 失敗 | proxy 回 403 CONNECT tunnel failed，屬政策拒絕，未繞過 |
| Reddit (wallstreetbets / stocks) | 失敗 | 網域無法存取 |
| StockTwits | 失敗 | api.stocktwits.com 解析失敗，需加入允許網域 |
| WebSearch (散戶/新聞) | 部分 | 僅找到 4971 相關資料，無 5455 內容 |

## 後續建議
1. 核對 5455.TWO 的正式公司名稱與代號，確認是否為英特磊 (目前證據指向 4971)。
2. 將 api.stocktwits.com 與 www.reddit.com 加入 session 允許網域後重跑社群部分。
3. 確認 Yahoo Finance 網域是否可經 proxy 存取，以重取分析師評等與內部人交易。

SENTIMENT REPORT COMPLETE
