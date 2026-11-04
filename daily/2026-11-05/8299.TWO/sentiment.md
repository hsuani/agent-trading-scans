# Sentiment — 8299.TWO (群聯 Phison Electronics) as of 2026-11-05

> 資料時點註記：執行日為 2026-11-04，報告 as-of 日期為 2026-11-05。本次可取得的券商評等與新聞最新僅到 2026 年 8 月中，2026 年 11 月的評等變動未能查到，標註為 DATA_UNAVAILABLE 處不另行推測。

## Analyst consensus

yfinance `rec_summary`（當期 0m）：

| 評等 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 家數 | 4 | 7 | 1 | 1 | 0 | 13 |

共 11 buy / 1 hold / 1 sell，買進比例約 85%。

- 近三期（0m、-1m、-2m）家數完全相同，yfinance 未顯示期間內的評等升降級。`recommendations` 也只回傳彙總計數，沒有個別券商的升降級明細，因此「升降級事件」為 DATA_UNAVAILABLE。
- 公開網頁彙整（WebSearch，來源時點不一）：
  - 2026-05：統一投顧維持買進，目標價 3200 元；CLSA 買入，目標價 3000 元。
  - 2026-08 中：富邦投顧目標價降至 2730 元；統一投顧降至 2700 元；國泰證期維持買進、目標價 2900 元；國票投顧 3000 元；宏遠投顧 3725 元。多數目標價落在 2700 至 2900 元區間。
  - 多家在 2026-08 下修目標價，主因是股價回檔與公司表示會保留較多現金、股息發放率略低於過往。
- 彙整頁面的平均目標價約 2,921 至 2,977 元 TWD，高點約 4,130 元、低點約 2,240 元。各頁數字略有出入，且時點不一，不宜當作同一時點的共識值。
- 另有一篇來源不明、日期不明的 FactSet 報導提到 EPS 預估 37.62 元、目標價 2000 元；因日期無法確認，本報告不採用。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。`www.reddit.com` 在本沙箱遭封鎖，未重試。
- StockTwits：DATA_UNAVAILABLE。`api.stocktwits.com` 無法解析（DNS 失敗），需於 session 網路設定允許該 host。
- X / 新聞輿情：僅能以 WebSearch 取得新聞層級資料，沒有可量化的社群提及次數。
  - 新聞基調偏中性至正面：營運面被描述為穩健，股價在部分時段逆勢上漲；但 2026-08-14 因上半年獲利創高、同時執行長表示保留更多現金，股價單日重挫約 8.77%，顯示市場對現金配置與股利政策有分歧。
  - 第三方論壇（Simply Wall St 社群敘事）同時出現看多與看空敘述：看多主軸為 AI 儲存、aiDAPTIV、下一代控制器；看空主軸為 NAND 價格下滑、競爭加劇、本益比偏高。
- 聲量（buzz volume）：DATA_UNAVAILABLE，無法與歷史基準比較。
- 散戶傾向（tilt）：DATA_UNAVAILABLE，無法判定。
- 主要主題（僅依新聞與彙整文章歸納，非社群原文）：
  1. AI 儲存與 aiDAPTIV 產品線的成長敘事。
  2. NAND 價格循環與獲利能見度。
  3. 股利政策與現金保留的爭議。
  4. 估值（本益比）是否已反映成長。

## Insider activity

yfinance `insider`：回傳空清單，本次未取得任何內部人交易紀錄。

- Net 6mo：DATA_UNAVAILABLE（工具回空值，不等同於「無交易」，因 TPEx 個股的內部人申報資料在 yfinance 常不完整）。
- 未能辨識 CEO / CFO 等個別人員買賣。
- 建議另以公開資訊觀測站的董監事持股申報核對。

## Ownership shifts

yfinance `major_holders`（單一時點快照）：

| 指標 | 數值 |
|---|---|
| 內部人持股比例 | 15.85% |
| 法人持股比例 | 20.69% |
| 法人持股占流通股比例 | 24.59% |
| 法人家數 | 176 |

- 歷史時序：DATA_UNAVAILABLE，無法判定集中度是上升或下降。
- 內部人持股與法人持股合計約 36%，其餘由一般股東與未申報者持有。

## Net sentiment score

- 分析師面（bullish）：11 buy / 1 hold / 1 sell，目標價多落在 2700 至 2900 元，相對 2026-08 的股價基準仍有上行空間（股價基準本身不一致，見下）。信心：中。
- 散戶面（retail）：DATA_UNAVAILABLE，無法評估。
- 新聞面（mixed）：營運正面，股利與現金配置有負面反應，估值有爭議。
- 內部人面：DATA_UNAVAILABLE。

**Composite：偏多（bullish），信心：低。** 理由：分析師多數偏多且覆蓋面廣，但散戶社群與內部人兩個訊號完全缺失，且最新評等資料已停在 2026-08，距離 as-of 日期約三個月，時效性不足。

**股價基準不一致警示**：各來源報價差異大（約 1,495、1,515、1,650、2,110、2,260 元 TWD），無法確認 2026-11-05 的現價。目標價與現價的比較因此不可靠，須以即時報價重算上行空間。

**Divergence flag：無法判定（DATA_UNAVAILABLE）**。散戶傾向缺失，無法比較散戶與分析師是否方向相反。

## 資料缺口與來源

| 來源 | 狀態 |
|---|---|
| yfinance recommendations / rec_summary | 可用（僅彙總計數） |
| yfinance insider | 回空值 |
| yfinance major_holders | 可用（單點快照） |
| Reddit | DATA_UNAVAILABLE（主機封鎖） |
| StockTwits | DATA_UNAVAILABLE（DNS 失敗） |
| WebSearch 新聞與券商彙整 | 可用，時點至 2026-08 中，部分來源過時 |

SENTIMENT REPORT COMPLETE
