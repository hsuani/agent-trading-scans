# Sentiment — 5455.TWO as of 2026-10-11

**警示：代號與公司名稱不一致，本檔資料不可用於英特磊判讀。** 本地 yfinance 快取 `prices/yf/5455.TWO.json` 的 longName 為 Sheng Yi Development Co.,Ltd（盛益開發，產業 Real Estate - Development，市值約 TWD 2.0B）。依 cnyes 與 wantgoo 公開資料，英特磊科技（IntelliEPI，GaAs 磊晶片）為 **4971.TWO（IET-KY）**，上櫃日 2013/07/24。需由使用者確認應分析的代號（5455.TWO 或 4971.TWO）。

## Analyst consensus
DATA_UNAVAILABLE. yf `recommendations` 與 `rec_summary` 皆為空陣列（即時 Yahoo 連線失敗，快取內亦為空）。WebSearch 未找到 5455.TWO 的券商評等或目標價；搜尋結果僅有 3455.TWO 的 Stock Alarm 頁面（無目標價），其餘為美國 INTC 資料，不可引用。

## Retail social
- Reddit: DATA_UNAVAILABLE（r/stocks 搜尋端點無法存取，錯誤為 "Claude Code is unable to fetch from www.reddit.com"；r/wallstreetbets 未嘗試，同一網域）。
- StockTwits / X: DATA_UNAVAILABLE（api.stocktwits.com 無法解析 DNS，ENOTFOUND）。X 端未找到與 5455.TWO 相關的近期討論。
- Themes: DATA_UNAVAILABLE。
- 散戶聲量 (buzz volume): DATA_UNAVAILABLE。

## Insider activity
DATA_UNAVAILABLE. yf `insider` 為空陣列，快取同樣為空，無法計算 6 個月淨買賣金額。

## Ownership shifts
- insidersPercentHeld: 70.34%（yf major_holders，來源為快取，`_refreshed_at` 2026-10-11）。此數字與一般台股公開發行公司的持股結構差異很大，需與 Sheng Yi 身分一併核對後才能採信。
- institutionsPercentHeld / institutionsCount: 回傳 0.0，視為 DATA_UNAVAILABLE，不代表機構持股為零。
- inst_holders: DATA_UNAVAILABLE。
- 趨勢: DATA_UNAVAILABLE（僅單一時點快照，無歷史比較）。

## Net sentiment score
Composite: **DATA_UNAVAILABLE**（無 confidence 評分）。五大來源中，analyst、Reddit、StockTwits/X、insider、機構持股全部缺漏，無足夠樣本支撐方向判斷。

Divergence flag: **DATA_UNAVAILABLE**（無法比較散戶與分析師傾向）。

## 資料來源狀態
| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary | 空（Yahoo 即時連線失敗，快取為空） |
| yf insider | 空 |
| yf major_holders | 僅 insider % 有值，機構欄位為 0 |
| yf inst_holders | 空 |
| Reddit r/stocks | 無法存取 |
| StockTwits | DNS 解析失敗 |
| WebSearch | 無相關結果 |

## 後續建議
1. 確認目標代號：5455.TWO（盛益開發）或 4971.TWO（英特磊）。確認後重跑本報告。4971.TWO 目前在本地快取中不存在，需以 `yf.py refresh-cache` 或即時連線補抓。
2. 待 Yahoo 連線恢復後重新抓 recommendations、rec_summary、insider。
3. 若需 Reddit / StockTwits 資料，需改用可連線的代理或其他來源。

SENTIMENT REPORT COMPLETE
