# Sentiment — 5455.TWO as of 2026-11-08

> **身分警示**：repo 標示 5455.TWO 為「英特磊」，但本次網路查詢顯示代號 5455 對應 **昇益開發股份有限公司 (Sheng Yi Development Co., Ltd.)**，為上櫃住宅建設與建材批發公司（新竹市）。英特磊的公開資料則一貫對應 **IET-KY (4971)**。`_catalysts.json` 另有一筆事件註記「若本次 yfinance 回傳的公司身分 聖億建設」，顯示 5455.TWO 的公司身分在資料管線中已有混淆。在身分確認前，本報告不歸屬任何公司基本面或市場情緒結論。

## Analyst consensus
資料不可得。`yf recommendations`、`yf rec_summary` 皆回傳空陣列（Yahoo cookie/crumb 取得失敗，live feed 被擋，repo cache 無此代號資料）。
無法列出 buy / hold / sell 分布，也無近期升降評等或目標價變動。

## Retail social
- Reddit (r/wallstreetbets、r/stocks)：未取得。本次 WebSearch 未回傳可用討論串，且 Reddit 直連於本沙箱不可用。
- StockTwits / X：未取得。StockTwits 未嘗試直連（受限於沙箱）；X 相關 WebSearch 無 2026-11 期間結果。
- PTT / Dcard：WebSearch 無 5455 相關討論串，僅回傳 4971 (IET-KY) 的新聞與產業文章。
- 聲量：無法評估（無可靠樣本，不以 4971 的聲量替代）。
- 主題：無可歸屬於 5455.TWO 的主題。

## Insider activity
資料不可得。`yf insider` 回傳空陣列，無法計算 6 個月淨買賣金額，也無法判斷 CEO / CFO 或其他人員的交易。
Ownership 參考：`yf major_holders` 顯示 insidersPercentHeld = 70.3%（內部人持股比例，來源為 cache）；institutionsPercentHeld 與 institutionsCount 皆為 0，代表機構持股資料缺失，**不能**解讀為機構完全不持股。機構持股趨勢無法判斷。

## Net sentiment score
Composite: **neutral（信心：低）**。
理由：分析師評等、內部人交易、零售討論三個主要訊號皆無可歸屬資料，僅有的持股結構數據不足以判斷方向。此分數代表「資料不足下的中性預設」，不代表市場觀點中性。

Divergence flag: **無法判定**。缺少分析師或零售任一側的可靠方向性資料，不應推論兩者是否背離。

## 後續待辦
1. 先確認 5455 的正式公司名稱與產業（櫃買中心或公開資訊觀測站），並修正 `pipeline/tools/render_html.py` 與 `pipeline/tools/universe.py` 中的「英特磊 (5455)」標籤，若確認 5455 非英特磊，英特磊應改對應 4971。
2. 身分確認後，重跑 `yf recommendations`、`rec_summary`、`insider`、`major_holders`（需 live feed 恢復）。
3. 若目標為英特磊，本報告應改以 4971 重新產出（社群與評等資料才有可比對來源）。

SENTIMENT REPORT COMPLETE
