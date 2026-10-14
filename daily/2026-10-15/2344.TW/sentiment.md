# Sentiment — 2344.TW (華邦電 Winbond Electronics) as of 2026-10-15

資料狀態摘要：Reddit、StockTwits、PTT 三個社群來源皆 DATA_UNAVAILABLE；內部人交易（yf insider）回傳空陣列，無法判定是真的無交易或抓取失敗。分析師評等來自 yf rec_summary（可用），但與網路搜尋結果數字不一致，需留意。

## Analyst consensus
yf rec_summary（0m 期）：8 buy（含 strongBuy 4）/ 0 hold / 0 sell。
- 與 -3m 期相比：總家數 6 → 8，hold 1 → 0，buy 增加，無 sell。
- yf recommendations 的歷史表與 rec_summary 相同，未提供個別券商的評等變動明細，因此無法逐家列出升降評。

網路搜尋的補充資訊（日期分散，數字不一致）：
- Investing.com 共識：Buy，6 位分析師（5 buy / 1 hold / 0 sell），平均 12 個月目標價約 234 TWD（高 360 / 低 121）。
- JPMorgan：目標價由 70 調至 83（較早報告），另有 Investing.com 資料顯示 2026/07/15 調升至 360，兩者時間與數字未能對齊。
- Morgan Stanley：Hold，目標價 100（2026/05 報告）；另有 Investing.com 顯示 2026/03/19 下調評等、目標價 140，兩者不一致。
- 國內券商（時間未明確標示，推測為 2026 Q3 財報後）：玉山 Buy 72、凱基 65 → 69、中信 63（調升至增加持股）、福邦 Buy 65。

目標價離散度極大（約 60 至 360 TWD），顯示各來源資料的更新時間差異很大，不宜直接取平均作為決策依據。

## Retail social
- Reddit：DATA_UNAVAILABLE。WebFetch 無法存取 www.reddit.com（r/wallstreetbets 與 r/stocks 皆失敗），未取得任何貼文、分數或留言數。
- StockTwits / X：DATA_UNAVAILABLE。api.stocktwits.com 無法解析（DNS 失敗），未取得訊息數與多空標籤比例。
- PTT Stock 板：DATA_UNAVAILABLE。www.ptt.cc 無法解析，WebSearch 也未回傳任何 PTT 討論串。
- 替代觀察（非社群原文，僅供參考）：Investing.com 使用者喊單表（2026/06–07）顯示多數短線喊單虧損，短線情緒偏空；CMoney 股票討論區的意見則是長期看好車用與利基型記憶體需求，但認為股價在高檔有回檔壓力，意見分歧。
- 討論量（buzz volume）：無法量化，定性判斷無資料。
- Themes（僅從替代來源歸納）：(1) 車用與利基型記憶體長期需求；(2) 股價高檔的回檔風險；(3) 景氣循環股的獲利高峰是否可持續；(4) 10/29 財報（Investing.com 所列預定日）前的預期。

## Insider activity
Net 6mo：DATA_UNAVAILABLE（yf insider 回傳空陣列，無法確認淨買賣金額與申報人身份）。
- 持股結構參考（yf major_holders，日期未標示）：內部人持股 30.26%，機構持股 24.78%，機構佔流通股 35.54%，機構家數約 200。
- 機構持股趨勢：僅單一時點，無法判定增減方向，ownership shift 為 DATA_UNAVAILABLE。

## 價格背景（供對照，非情緒來源）
- Google Finance：2026/10/07 收 177.00 TWD，52 週高 233.50，本益比 19.53。
- MarketScreener：164.50 TWD，一週 -10.11%，三個月 +74.26%（日期不明）。
- Morningstar：前收 159.50 TWD，標準化本益比 17.61。
- Investing.com UK 頁面顯示 93.50 TWD，明顯過時，已排除。
- 2026/08/07 收 163.50 TWD（-4.39%）。
- 基本面背景：2026/06 單月營收 205.97 億 TWD，創歷史新高；1–6 月累計營收年增 139.2%；Q1 單季毛利率 53.4%（來源為網路報導）。

## Net sentiment score
- 分析師面：偏多（8 buy / 0 sell，且 hold 已由 1 降至 0）。
- 散戶面：無法判定（主要社群來源全部 DATA_UNAVAILABLE）；替代來源呈現短線偏空、長線偏多的分歧。
- 綜合：**偏多（信心：低）**。依據僅有分析師評等，散戶端缺口大，且目標價離散度高，不足以作為高信心結論。

Divergence flag：**無法判定（DATA_UNAVAILABLE）**。由於社群資料缺失，無法確認散戶傾向是否與分析師傾向相反。若日後補上 Reddit、StockTwits 或 PTT 資料，應優先檢查此欄位。

## 資料缺口與可靠度
- Reddit、StockTwits、PTT：皆為 DATA_UNAVAILABLE（網路連線或 DNS 失敗，非 403/429）。
- yf insider：空陣列，原因不明。
- yf 的 cookie/crumb 取得失敗（fc.yahoo.com ConnectionError），可能影響部分 yf 端點的完整性。
- 網路搜尋結果的評等與目標價數字互相衝突，且多數缺乏明確日期，只能作為輔助。
- 本報告僅描述市場情緒，不構成交易建議。

SENTIMENT REPORT COMPLETE
