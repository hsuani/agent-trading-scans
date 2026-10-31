# Sentiment — 3163.TWO (光普 Browave) as of 2026-11-01

資料完整度很低，本報告大多數欄位無法實際取得。以下結論僅反映「資料缺口本身」，不代表市場情緒偏多或偏空。

## Analyst consensus
無法取得。`yf 3163.TWO recommendations` 與 `rec_summary` 皆回傳空陣列（使用 3163.TW 重試亦為空）。yfinance cookie/crumb 取得失敗，可能影響覆蓋率。無法給出 buy/hold/sell 分布、近期升降評等或目標價變動。

## Retail social
- Reddit (r/wallstreetbets, r/stocks)：WebFetch 被拒絕存取，本次未取得任何貼文，無樣本、無語氣判斷。
- StockTwits：`api.stocktwits.com` DNS 解析失敗（ENOTFOUND），疑為 session 網路白名單未允許該網域。
- X / 新聞搜尋：兩次 WebSearch（英文與中文）皆未找到與光普（3163）直接相關的券商評論、法人目標價或投資人討論。結果多為大立光、聯一光、台光電等同類或無關個股。
- 聲量：無法量化，判定為「無法評估」，不是「低聲量」。
- 主題：無可引用的散戶觀點。

## Insider activity
`yf 3163.TWO insider` 回傳空陣列，無法確認近 6 個月內部人申報買賣。空陣列可能代表「無申報」，也可能是資料源缺漏，兩者無法從本次資料區分。淨買賣金額：無法提供。

## Ownership shifts
- 內部人持股比例：約 11.26%
- 機構持股比例：約 10.50%（流通股口徑約 11.84%）
- 機構家數：23
- 僅有單一時點快照，無法判斷持股集中度的趨勢方向。

## 公司概況（供背景參考，非情緒來源）
依 yfinance info：光普為新竹科學園區光通訊元件廠（產品含 WDM、分光器、MPO/MTP 連接器、光纖陣列等，應用於 CATV/FTTH、5G、資料中心），產業為 Communication Equipment。

## Net sentiment score
Composite：**無法判定（insufficient data，信心：低）**。
- 分析師面：無資料
- 散戶面：無資料（Reddit 被擋、StockTwits 網域無法解析）
- 內部人面：無資料（空陣列）
- 機構持股：僅快照，無趨勢

Divergence flag：**無法判定**。分析師與散戶皆無可比較的語氣，無法判斷是否背離。

## 資料缺口
1. api.stocktwits.com 未開放。
2. Reddit 需另尋可用來源，目前 WebFetch 路徑不可用。
3. 內部人交易需從公開資訊觀測站或 TPEx 申報資料補上空缺。
4. 券商目標價與評等明細需個別券商報告或付費資料。
