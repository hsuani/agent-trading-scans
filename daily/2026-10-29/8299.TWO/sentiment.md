# Sentiment — 8299.TWO (群聯 Phison Electronics) as of 2026-10-29

資料完整度: 分析師評等 (有,但目前一期為 10/29 前後的 Yahoo 快照,個別券商目標價日期為 3–5 月)、零售社群 (無法取得)、內部人交易 (資料源缺漏,非確定為零)、股權結構 (單一快照,無趨勢)。

## Analyst consensus

| 項目 | 數值 | 來源 |
|---|---|---|
| 評等分布 (yf 快照) | Strong Buy 4 / Buy 7 / Hold 1 / Sell 1 / Strong Sell 0 (共 13 家) | yf rec_summary |
| 評等分布 (Investing.com 近 3 月) | Buy 10 / Hold 1 / Sell 0 (共 11 家) | 搜尋結果彙整 |
| 近 4 期趨勢 | 0m 與 -1m、-2m 相同 (4/7/1/1);-3m 為 4/6/1/0 | yf recommendations |
| 平均目標價 (彙整網站) | 約 NT$2,942–2,977 | Investing.com 彙整 |
| 個別券商目標價 | CLSA Buy NT$3,000 (5/11,前值 2,600);Macquarie Buy NT$2,654 (3/9);Nomura/Instinet Buy NT$2,240 (3/9) | Investing.com |
| 參考股價 | NT$1,890 (10/16 收盤,+3.3%) | statementdog / nStock |

**近期動態**: 過去約 3 個月評等結構略微轉弱但仍以買進為主。-3m 時無賣出評等,之後出現 1 家 Sell,同時 Buy 由 6 增為 7 (總家數由 11 增為 13)。搜尋未發現 2026 年有明確降評的券商報告,也未找到 10 月的新目標價調整。目前目標價約 NT$2,240–3,000,相對 10/16 參考股價 NT$1,890 仍有上行空間,但目標價日期多在 3–5 月,可能已落後於股價與基本面更新。

**資料衝突**: yf 為 13 家分析師、Investing.com 為 11 家,家數與分布不一致,以 yf 為主、Investing.com 為輔。

## Retail social

- **Reddit (r/wallstreetbets、r/stocks)**: 無法取得。Proxy 對 reddit.com 回傳 CONNECT 403,WebFetch 亦被拒。無貼文樣本,無法判斷語氣。
- **StockTwits**: 無法取得。api.stocktwits.com 無法解析 (未列入 session 允許網域),需由使用者在 session 網路設定中允許後才能重試。
- **X / PTT / Dcard**: 搜尋 PTT、Dcard 相關討論未找到 2026 年 10 月的串文,僅有財經數據頁面。X 未搜尋到可辨識的近期討論。
- **Buzz 量**: 無法量化,無法與平常基準比較。
- **Retail tilt**: 無法判定 (bullish / bearish / mixed 皆不下結論)。
- **投資人敘事 (Simply Wall St 社群)**: 此為彙整型投資人敘事,非社群貼文,僅作為間接參考。正面敘事集中於「下一代控制器與儲存擴張」與「全球資料需求爆發帶動先進 SSD 控制器」;負面敘事集中於「競爭加劇與本益比偏高」。兩者並存,未見明確一面倒。

**Themes (由新聞與基本面報導歸納,非社群)**:
1. 營收爆發: 9 月合併營收 NT$306.39億,年增 370.3%、月增 8.4%;前 9 月累計 NT$1,949.32億,年增 290.9%。
2. 獲利能力: 2026 Q1 EPS NT$68.8,毛利率 61.82%。
3. 估值爭論: 本益比約 8.66 倍 (10/16),但股價 52 週區間 NT$406–2,465,一年報酬約 +238%,波動大 (beta 約 1.68)。
4. AI 儲存題材: aiDAPTIV 與 7nm 控制器被視為新產品延伸。

## Insider activity

Net 6mo: **無法確認** (資料缺漏,非確定為 0)。

- yf insider 回傳空陣列。同時 Yahoo cookie/crumb 取得失敗 (guce.yahoo.com 遭 proxy 403),空陣列可能是資料源問題而非確實無交易。
- 公開資訊觀測站 (MOPS) 董監持股申報未能透過搜尋取得。
- 目前可得資訊: 內部人持股比例約 15.9% (yf major_holders),僅為持股結構,不代表近 6 個月買賣方向。
- Notable: 無可確認之 CEO / CFO 或其他董監事交易紀錄。

## Ownership shifts

- 機構持股約 19.3%,流通股內機構持股約 22.9%,機構家數 172 家 (yf major_holders 單一快照)。
- 無季度趨勢資料,無法判斷機構集中度增減。

## Net sentiment score

**Composite: bullish (信心: 中低)**

- 分析師面: 偏多。13 家中 11 家買進 (含 4 家強力買進),僅 1 家持有與 1 家賣出;目標價均高於 10/16 參考股價。信心中等,因目標價日期偏舊。
- 零售面: 無資料,不納入權重。
- 內部人面: 無資料,不納入權重。
- 基本面敘事 (新聞): 偏多,營收與 EPS 成長強勁,但估值與波動風險被投資人提出。

**Divergence flag: 無法判定** — 因零售語氣無法取得,無法比較零售與分析師方向是否相反。若後續取得 Reddit/StockTwits 資料,應重新評估此旗標。

**資料缺口與後續建議**:
- 允許 api.stocktwits.com 網域後重試 StockTwits。
- Reddit 目前由 proxy 阻擋,需另行處理或改用其他來源。
- 取得 MOPS 董監持股申報以補足內部人面。
- 更新券商目標價 (目前最新為 5/11)。

SENTIMENT REPORT COMPLETE
