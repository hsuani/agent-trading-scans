# Sentiment — HON as of 2026-10-13

資料截止: 2026-10-13。晚於此日期之資料視為未知，不納入判斷。

## Analyst consensus
24 位分析師: 14 buy (3 strong buy + 11 buy) / 9 hold / 1 sell (strong sell)。Buy 佔比約 58%。
近三個月趨勢: 期初 (-3m) 為 15 buy / 8 hold / 1 sell，目前為 14 buy / 9 hold / 1 sell，屬於輕微降溫，一檔 buy 轉 hold 發生於約 -2m 至 -1m 之間。整體仍偏多，但評等傾向有小幅往中性移動。
近期評等變動 (個別 upgrade/downgrade 明細): DATA_UNAVAILABLE。`pipeline/tools/yf HON recommendations` 本次僅回傳彙總計數，未回傳逐筆評等變動。
目標價 (第三方彙整，日期不一，未直接核對 Yahoo 原始資料):
- 平均 12 個月目標價約 258.83 USD (高 303 / 低 186)。
- Bank of America 維持 Buy，目標價由 275 下修至 265 (反映 Solstice 拆分)。
- JPMorgan 維持 Hold，目標價由 222 下修至 212。
- 來源: WebSearch 彙整，為外部聚合站資料，非一手來源。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE。WebFetch 無法連線 reddit.com，無法取得貼文樣本、分數與留言數。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com 無法解析網域 (DNS 失敗)，本次無資料。
- X / 新聞輿情: WebSearch 兩次查詢均未找到具體散戶討論串，結果以財經新聞與股價聚合頁為主。搜尋結果明確指出找不到 Reddit 討論，因此無法評估散戶語氣。
- 聲量相對基準 (buzz volume): DATA_UNAVAILABLE。
- 散戶傾向: 無法判定 (bullish / bearish / mixed 皆無可靠樣本)。
- 主要主題 (由新聞推斷，非散戶貼文): (1) 航太業務拆分 (Honeywell Aerospace 以 HONA 獨立掛牌)、(2) 拆分後 1-for-2 反向股票分割、(3) 激進投資人施壓 (Elliott 約 50 億美元持股、Third Point 公開主張拆分)、(4) Q2 2026 EPS 1.95 優於預期並上修全年 EPS 指引至 8.20 (中位數)。
- 股價語境 (WebSearch 單一快照，未核對原始來源): 2026-10-02 約 213.80 USD，52 週區間 195.77 至 260.15 USD；拆分後航太部門疲弱被提及為情緒壓力來源。

## Insider activity
統計區間: 2026-04-13 至 2026-10-13 (6 個月)。
Net 6mo: 公開市場買進 $0 / 公開市場賣出約 $4.23M。
- 主要賣出: WEST KENNETH J (Officer) 2026-07-27 賣出 17,032 股，約 $4.15M (價格 243.77)，同日有 17,032 股衍生性證券轉換 (約 $3.31M 行權價值，屬行權而非市場買進)；2026-08-03 再賣出 316 股，約 $77.6K (價格 245.47)。
- 其他 CEO/CFO/GC 申報列 (VIMAL KAPUR, CEO; MICHAL STEPNIAK, CFO; SU PING LU, GC 等) 多數為無金額欄位的申報，性質推定為 RSU/績效股歸屬或稅款代扣，無法確認是否為市場交易，本報告未將其計入淨賣出。
- 董事 (FLINT, WATSON, STEINBERG, BURKE, NOOYI, AYER 等) 於 2026-04-15 有一批 625 股等級的申報，無金額，推定為年度董事股權授予。
- 沒有發現 CEO / CFO 於本區間內的公開市場買進。
- 注意: 前幾個月 (2026-03-02 WEST 與 CURRIER 賣出，約 $0.76M) 落在 6 個月窗口之外，未計入。
- 註: yfinance 資料中職稱欄位不一致 (例如 WEST 於 2025-07 被列為 CEO，之後列為 Officer)，以申報當時職稱為準。

Notable: WEST KENNETH J (Officer), 2026-07-27 與 2026-08-03 賣出，合計約 $4.23M，為本區間內最大的公開市場賣出。

## Ownership shifts
- 機構持股比例 84.4% (2,775 家機構)，內部人持股約 0.08%。
- 機構持股趨勢 (多期比較): DATA_UNAVAILABLE，本次僅取得單一快照。

## Net sentiment score
Composite: neutral (信心: 低至中)。
- 分析師: 偏多 (58% buy，但 buy 家數近三個月微降，hold 增加)。
- 內部人: 偏空 (6 個月內約 $4.23M 公開市場賣出，無買進)。但賣出集中於單一 Officer，且可能屬行權後例行出售，解讀權重不高。
- 散戶: 無資料，無法納入評分。
- 綜合: 分析師偏多與內部人淨賣出抵銷，散戶資料缺失使整體信心降低。

Divergence flag: 無法判定。散戶資料缺失，無法比較散戶傾向與分析師傾向是否相反。

## 其他注意事項
- 板塊標籤: 本次任務標註 sector 為 quantum，但 HON 主業為工業與自動化，本報告以 HON 公司層級資料為準，未對 quantum 相關曝險做獨立查證。
- 近期催化劑: Q3 2026 財報預計 2026-10-22 (WebSearch 所列日期，尚未正式確認)。此日期落在本報告資料截止日之後，屬於未知事件，僅作為觀察點。
- 拆分與反向分割: 拆分後的 HON 股價、歷史價格與內部人交易價格 (約 240 至 245) 可能不可直接比較，解讀時需留意調整基準。
- 第三方數據 (目標價、股價快照) 來源與日期不一，未與一手來源逐項核對。

## Metrics

| 指標 | 數值 | 備註 |
|---|---|---|
| 分析師總數 | 24 | 3 SB / 11 B / 9 H / 0 S / 1 SS |
| Buy 佔比 | 58.3% | (SB + B) / 總數 |
| Hold 佔比 | 37.5% | |
| Sell 佔比 | 4.2% | |
| 近三月 buy 家數變化 | 15 → 14 | -3m 對比 0m |
| 近三月 hold 家數變化 | 8 → 9 | |
| 平均目標價 (第三方) | 258.83 USD | 日期不明，未核對 |
| 6mo 公開市場買進 | $0 | 未發現 |
| 6mo 公開市場賣出 | ~$4.23M | 主要為 WEST KENNETH J |
| 6mo 淨內部人交易 | ~-$4.23M | 不含衍生性證券轉換與無金額申報 |
| 機構持股比例 | 84.4% | 單一快照 |
| 內部人持股比例 | 0.08% | |
| 機構家數 | 2,775 | |
| Reddit 樣本數 | DATA_UNAVAILABLE | |
| StockTwits 樣本數 | DATA_UNAVAILABLE | |
| 綜合情緒 | Neutral | 信心: 低至中 |
| 背離旗標 | 無法判定 | 散戶資料缺失 |

SENTIMENT REPORT COMPLETE
