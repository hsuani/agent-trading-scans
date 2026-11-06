# Sentiment — 6510.TWO (中華精測) as of 2026-11-07

## Executive summary

- 分析師評等偏多:yfinance 彙整的 rec_summary 顯示 10 家券商,4 strong buy + 6 buy,0 hold、0 sell。近兩期評等結構幾乎不變,最近一個月淨增 1 家買進評等。
- 散戶情緒無法直接量測:Reddit 無法連線,StockTwits 未納入(依指示不抓取財經網站),WebSearch 也找不到 2026-11 的 PTT 股板實際發言。本報告的散戶判斷只能靠新聞與媒體摘要的間接訊號。
- 內部人訊號缺資料:yfinance insider 回傳空陣列,無法判斷 6 個月內董監事或高階主管買賣方向。
- 籌碼面:insidersPercentHeld 36.8%、institutionsPercentHeld 27.6%,機構 73 家。只有單一快照,無法判斷集中度趨勢。
- 綜合:分析師偏多、散戶端間接訊號為偏多但伴隨估值與波動疑慮,信心度低至中等。本報告不提供交易建議。

## Data availability

| 來源 | 狀態 | 備註 |
|---|---|---|
| yf recommendations | 可用 | 三期快照(0m、-1m、-2m),無目標價欄位 |
| yf rec_summary | 可用 | 與 recommendations 數值相同 |
| yf insider | 空資料 | 回傳 `[]`,可能是真實無申報,也可能是 TWSE/TPEX 覆蓋缺口,無法區分 |
| yf major_holders | 部分可用 | 只有單一快照,無歷史趨勢 |
| Reddit r/stocks 搜尋 | 失敗 | WebFetch 無法連線 www.reddit.com,本次不納入 |
| StockTwits | 未抓取 | 財經網站限制,依指示跳過 |
| WebSearch 散戶討論 | 部分可用 | 找不到 2026-11 的 PTT 或論壇發言,只有新聞摘要 |
| WebSearch 券商目標價 | 部分可用 | 最新可見評等為 2026-04-30 華南投顧報告,之後無確認的目標價調整 |

資料時效與排除:
- 本次未取得 2026-11-07 當日的股價,因此不計算市值或估值倍數的即時數字。
- 搜尋結果中有一則 WebSearch 回傳的是 MPI Corporation(6223,旺矽),與 6510 中華精測不同公司,已排除,不納入任何數字。
- 未借用 daily/ 下其他日期報告的數字。

## Retail / social sentiment read

**聲量**:無法量化。Reddit 失敗,PTT 與 X 在搜尋中沒有可確認的 2026-11 發言。以新聞數量估,2026 年中後段仍有媒體以「注意股」或股價異動作主題,但沒有可比較的散戶提及次數基準。

**間接訊號(新聞與媒體摘要,非散戶原文)**:
- 2026-09-09 nStock 整理的「注意股」報導,指 5 日累漲約 15.84%,代表當時短線人氣與成交集中。
- 2025 年第三季法說會後股價因管理層語氣偏保守而大跌,顯示市場對管理層指引敏感。
- 估值討論:統計狗頁面顯示本益比約 68.5 倍、殖利率約 0.53%(快照日期不明),成長股估值爭論是常見主題。
- 三廠擴產受缺工與材料延誤影響,並提到可轉債籌資可能稀釋股本,這兩點是媒體報導中較常出現的疑慮。

**散戶傾向判斷**:無法直接判定。依間接訊號,基本面敘事偏多(營收與獲利創高),但估值與波動、擴產進度、稀釋疑慮構成空方論點。傾向標示為「混合」,信心低。

**可引用的代表性觀點(來源為媒體,非散戶原文)**:
- 偏多敘事:公司 2026 年營收與毛利率目標被引用為支撐。
- 偏空敘事:「估值偏高、法說語氣保守即重挫」。

## Analyst consensus

**目前分布(yf rec_summary,0m 快照)**:10 家,4 strong buy / 6 buy / 0 hold / 0 sell。

**近期變化(yf recommendations)**:

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 |
|---|---|---|---|---|---|---|
| 0m(目前) | 4 | 6 | 0 | 0 | 0 | 10 |
| -1m | 4 | 5 | 0 | 0 | 0 | 9 |
| -2m | 4 | 5 | 0 | 0 | 0 | 9 |

- 最近一個月淨增 1 家買進評等,無降評紀錄。結構上完全偏多。
- yf 未提供目標價欄位,無法計算平均目標價或其變化。

**個別券商(WebSearch 摘錄,非 yf 數字)**:
- 華南投顧 2026-04-30 訪談報告:買進,目標價 4,300 元,以 2026 年 EPS 53.97 元與 80 倍本益比推算。同報告列 2025-09 區間持有、目標價 1,390 元;2025-04 買進、目標價 600 元。這些是過去的評等,僅供參考。
- 另有一篇無日期的文章推估合理價值區間 4,960 至 5,880 元,屬媒體推算,非正式評等,不納入共識計算。

**需注意**:券商目標價與近期股價之間的差距很大。HiStock 頁面更新到 2026-08-05 時股價約 2,800 至 3,000 元,與 4 月報告收盤 3,630 元有明顯落差。這代表目標價資料可能過時,需以最新券商報告確認。

**基本面交叉檢核**:
- 2025 年合併營收約 48.06 億元,每股純益 30.41 元。
- 2026 年 1 月合併營收約 4.54 億元,2026 年第一季合併營收約 13.57 億元,約為 1 月營收乘 3 的結果,數字一致。
- 2026 年第一季 EPS 10.43 元,與 2025 全年 EPS 30.41 元的季度分布合理。

## Institutional / insider signal

**內部人(yf insider)**:
- 6 個月內淨買賣金額:無資料。yf 回傳空陣列。
- 無法判斷 CEO、CFO 或其他董監事是否有買賣。
- 這是資料缺口,不能視為內部人中性或無交易。

**持股結構(yf major_holders,單一快照)**:

| 指標 | 數值 |
|---|---|
| insidersPercentHeld | 36.82% |
| institutionsPercentHeld | 27.63% |
| institutionsFloatPercentHeld | 43.73% |
| institutionsCount | 73 家 |

- 內部人持股占比高,且機構占流通股比重約 44%,代表流通股中機構已有相當比例。
- 無歷史快照,無法判斷機構集中度的增減趨勢,也無法判斷近期是否有機構大幅加碼或減碼。
- 媒體提到的可轉債籌資若轉換,可能稀釋現有股東持股比例,這是需要追蹤的結構性變數。

## Overall sentiment verdict

| 面向 | 傾向 | 信心 |
|---|---|---|
| 分析師共識 | 偏多(10 買進 / 0 持有 / 0 賣出) | 中(樣本僅 10 家,無目標價資料) |
| 散戶(間接) | 混合 | 低(無原文與聲量數據) |
| 內部人 | 無資料 | 無 |
| 機構籌碼 | 無趨勢資料,結構穩定 | 低 |

**綜合情緒**:偏多(中低信心)。分析師評等一致偏多,但這個判斷依賴樣本數少的評等與可能過時的目標價。散戶端無法直接量測,只能看出基本面敘事偏多、估值與波動是主要爭議。

**背離旗標**:無法確認。散戶傾向無法直接判定,因此不能判斷是否與分析師傾向相反。若日後取得 PTT 或 StockTwits 的實際發言,需重新評估。

**待補資料**:
- 6 個月內內部人申報(需確認 yf insider 空資料是否為覆蓋缺口)。
- 2026-11-07 當日股價與近期目標價變化。
- PTT 股板 2026-10 至 2026-11 的實際發言量與傾向。
- 機構持股歷史快照,以判斷集中度趨勢。

## Sources

- yfinance 工具輸出:`pipeline/tools/yf 6510.TWO recommendations`、`rec_summary`、`insider`、`major_holders`(本次執行)
- WebFetch Reddit r/stocks 搜尋:連線失敗
- [中華精測 6510 股票網友與新聞摘要 (nStock 新聞列表)](https://www.nstock.tw/%E7%B2%BE%E6%B8%AC%E5%81%9A%E4%BB%80%E9%BA%BC.html)
- [MONEY LINK 6510 基本資料](https://ww2.money-link.com.tw/TWStock/StockBasic.aspx?SymId=6510)
- [中時新聞網 2026-05-27 股東常會與股利報導](https://wantrich.chinatimes.com/news/20260527900855-420101)
- [聯合報 精測股東會與新廠進度](https://udn.com/news/story/7254/9528248)
- [MoneyWeekly 精測相關報導 (AID=149230)](https://www.moneyweekly.com.tw/_Article?AID=149230)
- [MoneyWeekly 精測相關報導 (AID=234377)](https://www.moneyweekly.com.tw/_Article?AID=234377)
- [華南投顧 精測6510 2026-04-30 報告](https://stock-llm-wiki.pages.dev/data_base/Raw_data/報告/報告_華南投顧_精測6510_20260430_original.pdf)
- [HiStock 6510](https://histock.tw/stock/6510)
- [統計狗 6510 分析](https://statementdog.com/analysis/6510)
- [鉅亨/UAnalyze 中華精測 11 月營收季節性回落報導](https://uanalyze.com.tw/articles/4597642226)
- [中時新聞網 2026-02-03 1 月營收報導](https://wantrich.chinatimes.com/news/20260203900591-420101)
- 排除:WebSearch 回傳的 MPI Corporation 6223(旺矽)相關頁面,與 6510 不同公司

SENTIMENT REPORT COMPLETE
