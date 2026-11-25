# Sentiment — 1815.TWO (富喬工業 Fulltech Fiber Glass) as of 2026-11-26

> 資料狀態：**資料不足（data-limited）**。Yahoo 資料源連線失敗、Reddit 與 StockTwits 無法存取，本報告僅有少量網路搜尋結果，多數欄位無法填寫。以下結論信心低，不應作為交易依據。

## Analyst consensus
yf 工具回傳 rec_summary 與 recommendations 全為 0（period 0m），伴隨 Yahoo cookie/crumb 取得失敗，**無法判定** 買進 / 持有 / 賣出分布。這些 0 值應視為資料缺漏，不是「無券商覆蓋」。

搜尋結果中僅找到一則未標註日期的技術面文章提到目標價 128 TWD（TradingView 頁面，單一目標價，無區間），以及 Investing.com 以均線判讀為 Buy，但兩者皆無日期，無法當作 2026-11 的最新共識。近期評等調整：**無法確認**。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：**無法存取**（WebFetch 被拒）。無法取樣討論串，無法判定 tilt。
- StockTwits：**無法存取**（api.stocktwits.com DNS 解析失敗，需於 session 網路設定允許該網域）。
- X / 新聞搜尋：搜尋結果以股價與基本面頁面為主，未找到 2026-11 前後的意見類文章。網路搜尋的股價描述彼此矛盾（一則寫近一週跌約 10%，另一則寫近一週漲約 9%），且多數快照未標日期，不可採用。
- 聲量（buzz volume）：**無法量化**，無相對於歷史的基準。
- Themes（僅依未標日期的基本面頁面，屬弱證據）：
  - 估值偏高：Simply Wall St 顯示本益比約 92–103x，估值與成長面分數低，反映偏保守的市場觀點。
  - 技術面：一則 AI 生成的技術分析頁面給予均線 Buy 判讀，參考價值有限。
- Tilt：**無法判定**（僅有弱證據，無社群樣本）。

## Insider activity
yf insider 工具回傳空陣列，**無法判定** 6 個月內董監或大股東的淨買賣金額。搜尋「董監 申報 持股 轉讓 2026」未找到本股的個別申報資料；僅有金管會按月彙整的董監持股異動公告（不含個別公司細節）。

Notable：無。

## Ownership shifts
yf major_holders（資料可能不完整，但數值可讀）：
- 內部人持股比例（insidersPercentHeld）：約 23.9%
- 機構持股比例（institutionsPercentHeld）：約 10.4%
- 機構浮通股持股比例（institutionsFloatPercentHeld）：約 13.6%
- 機構家數：23 家

單一時點快照，**無歷史序列**，無法判斷機構集中度的趨勢（增加或減少）。內部人持股比例偏高，代表籌碼集中度高，流通股數相對有限，但這只是結構性描述，不構成方向性訊號。

## Net sentiment score
Composite：**neutral（信心：低）**。

依據僅為：分析師端無可用資料、零社群樣本、內部人交易無資料、機構持股無趨勢。唯一有方向性的弱訊號是估值偏高的基本面描述，但來源未標日期，權重低。

Divergence flag：**無法判定（no）**。因為分析師端與散戶端皆無可用的方向性資料，無法比較兩者 tilt 是否相反。

## 資料缺口與後續補查建議
1. Yahoo 資料源（cookie/crumb）恢復後重跑 `pipeline/tools/yf 1815.TWO rec_summary`、`recommendations`、`insider`。
2. 於 session 網路設定允許 `api.stocktwits.com` 與 `www.reddit.com`，之後重試社群樣本。
3. 公開資訊觀測站（mops.twse.com.tw）查詢董事、監察人持股轉讓申報，或 Goodinfo / Yahoo 股市「法人評等」頁面取得 2026-11 前後的券商評等與目標價。
4. 搜尋時請以正確名稱「富喬」或代號 1815 查詢。本次初始查詢曾誤用「富旭」，部分結果因此混入無關公司（如富世達 6805）。

SENTIMENT REPORT COMPLETE
