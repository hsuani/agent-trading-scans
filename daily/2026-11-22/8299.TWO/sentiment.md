# Sentiment — 8299.TWO (群聯 Phison Electronics) as of 2026-11-22

## 資料來源狀態
- yf 工具: `ratings` 與 `holders` 不是有效子指令,實際使用 `recommendations`/`rec_summary`/`major_holders`/`inst_holders`。`insider` 與 `inst_holders` 回傳空陣列 (Yahoo cookie/crumb 連線失敗),快取檔中同樣為空,視為 DATA_UNAVAILABLE。
- Reddit (r/wallstreetbets、r/stocks): WebFetch 無法連線,DATA_UNAVAILABLE。
- StockTwits: 網域無法解析 (api.stocktwits.com),DATA_UNAVAILABLE。需在 session 網路設定允許該網域後才可重試。
- wantrich.chinatimes.com 無法解析,本次未能直接開啟該文,相關數字改以搜尋摘要為準。
- PTT / Dcard: 搜尋未找到可用討論串,DATA_UNAVAILABLE。

## Analyst consensus
Yahoo rec_summary (0m): 13 家 — 4 strong buy / 7 buy / 0 hold / 2 sell / 0 strong sell。買進評等占 11/13 (約 85%)。
- 歷史趨勢 (Yahoo 無日期欄位,以期別表示): -1m / -2m / -3m 皆為 4 SB / 7 B / 1 hold / 1 sell。
- 推論: 0m 相較 -1m,一家 hold 轉為 sell,與下列新聞中的「減碼」降評相符 (此為推論,非直接資料)。
- 新聞 (WebSearch 摘要,來源為 wantrich.chinatimes.com 與 statementdog,未能直接驗證):
  - 外資 (未具名於摘要) 由「優於大盤」降為「減碼」,目標價由 NT$2,588 降至 NT$1,357 (約 -48%),理由是 Q3 毛利率低於預期、傳統模組毛利率承壓,並承認先前估值模型有計算錯誤。
  - 本土投顧多數下修目標價。一家由買進降為中立 (理由: PC 市場疲軟)。另一家維持買進但目標價由 NT$2,998 降至 NT$2,070 (-31%)。凱基維持增加持股,目標價由 NT$2,900 降至 NT$2,700。
- 矛盾來源: 另一組搜尋結果列出 CLSA 目標價 NT$3,000 (11/05/2026 維持) 與 Macquarie 目標價 NT$3,000 (10/21/2026 維持),Investing.com 共識平均約 NT$2,697 至 NT$2,977。這些數字與「外資減碼 NT$1,357」並不一致,可能是不同券商或過時快照,無法確認。
- 價格來源亦有矛盾: 一處顯示 11/9 漲停至 NT$1,650;Investing.com 快照顯示 NT$1,500 但前收 NT$564 (明顯資料錯誤)。目前股價 DATA_UNAVAILABLE (未能取得可信即時價)。

## Retail social
- Reddit: DATA_UNAVAILABLE (連線失敗)。
- StockTwits / X: StockTwits DATA_UNAVAILABLE。X 未有可用結果。
- 替代來源 (新聞與研究報告,非散戶原始貼文): 媒體聚焦於毛利率是否回落、AI 與企業級 SSD 需求、庫藏股與估值分歧,未見明確散戶情緒量化資料。
- 聲量 (buzz volume): DATA_UNAVAILABLE,無法與平常基準比較。
- 散戶傾向: DATA_UNAVAILABLE (無法判定偏多、偏空或分歧)。一篇部落格提到 4 月散戶融資增加、大戶持股比例下滑,可信度低,未採計。

## Themes (從新聞與研究報告歸納)
1. 毛利率正常化: Q3 毛利率 59.7%,較 Q2 的 65.3% 下降 5.6 個百分點。執行長於 11/6 法說表示,長期維持六成以上毛利率不合理,五成以上即屬不錯。
2. 低價 NAND 庫存消耗後的獲利高峰是否已過。
3. AI 生態與企業級 SSD 成長 (10 月 AI 生態系占營收約 65%,企業級業務占比過半)。
4. 估值與目標價下修 (EPS 預估上修但目標價下修,市場對獲利高峰看法分歧)。
5. NAND 報價與 2027 下半年供過於求的疑慮。

## Insider activity
- 6 個月內 (2026-05-22 至 2026-11-22) yf insider: 空陣列,DATA_UNAVAILABLE。
- 新聞彙整 (搜尋結果最新只到 2026-08,9–11 月申報未覆蓋):
  - 董事長/CEO 潘健成 (經由承鑠投資) 買進: 6 月 35 張、7 月 40 張,合計 75 張 (約 75,000 股) 在 6 個月窗口內。
  - 另一筆 1 月贈與 102 張給子女 (每人 34 張) 不是賣出,且在窗口外。
  - 未查到 CEO 或其他董監事在窗口內賣出群聯股票的紀錄。CEO 曾公開否認傳出的賣股消息。
  - 6 個月淨金額: 無法精確換算為 億 (金額 DATA_UNAVAILABLE;以 2 月均價約 NT$1,960 粗估,僅供參考,不作為正式數字)。
- 公司層級: 董事會通過買回 2,000 張庫藏股,最高投入 NT$45.6 億。這是公司行為,不屬於個人內部人交易。另外公司處分宇瞻 (5289) 股票 3,800 張,屬於其他上市公司的股票處分,與本檔無關。

## Ownership
- Yahoo major_holders: 內部人持股 15.85%、機構持股 20.75%、機構占流通股 24.66%、機構家數 183。
- 機構持股趨勢 (時間序列): DATA_UNAVAILABLE (inst_holders 為空,且只有單一時點快照)。

## 財務數字 (用於交叉檢核,TWD)
- 2026-10 月營收: NT$315.30 億 (較去年同期 +346.3%,較 9 月 +2.9%)。
- 1–10 月累計營收: NT$2,264.62 億 (年增 297.8%)。
- Q3 稅後淨利: 約 NT$305 億,EPS 約 NT$138 (稅後淨利與 EPS 相除可得約 2.2 億股,與公司股本概念一致)。
- 庫藏股: 最高 NT$45.6 億 (2,000 張)。

## Net sentiment score
- 分析師面 (偏多但有警訊): 評等分布仍以買進為主 (約 85% 買進),但近期出現降評與大幅目標價下修。傾向: 偏多 (中等信心)。
- 內部人面: 窗口內有 CEO 關係人買進 75 張,未見賣出紀錄。傾向: 偏多 (低至中等信心,金額與完整申報 DATA_UNAVAILABLE)。
- 公司行為面: 庫藏股買回 2,000 張。傾向: 偏多 (中等信心)。
- 散戶面: DATA_UNAVAILABLE。
- 綜合: 中性偏多 (neutral-to-bullish),信心低。理由: 基本面數字強勁、內部人與公司買回偏多,但分析師近期降評與目標價大砍,且散戶面完全缺漏。

Divergence flag: 無法判定。散戶面缺漏,無法與分析師傾向比較。分析師內部本身也分歧 (外資減碼 vs CLSA/Macquarie 買進 NT$3,000),需要以原始報告再確認。

## 待補項目
1. 取得 yf insider 與 inst_holders 的有效資料 (Yahoo 連線失敗)。
2. 允許 reddit.com 與 api.stocktwits.com 網域後重試。
3. 向公開資訊觀測站查 9–11 月董監事持股申報。
4. 以原始券商報告確認外資減碼日期與 NT$1,357 目標價,並與 CLSA、Macquarie 的 NT$3,000 目標價區分。
5. 確認 11/22 實際收盤價 (目前來源衝突)。

SENTIMENT REPORT COMPLETE
