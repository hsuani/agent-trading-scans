# Sentiment — CRWV as of 2026-11-23

資料來源狀態: Reddit (r/wallstreetbets、r/stocks) 直接存取被拒絕; api.stocktwits.com 在本工作階段無法解析 (需於網路設定允許該網域)。散戶部分僅能依 WebSearch 次級新聞推估, 信心低。yf 工具的 Yahoo cookie/crumb 取得失敗但仍回傳資料, 數值可用。analyst 評級計數與 11-16 報告完全相同, 疑為快取值, 未必反映 11-23 當日最新狀態。持股資料為 9/30 13F 申報, 距 as-of 日有時間差。

## Analyst consensus

| 評級 | 家數 (最新, period 0m) | 一個月前 (-1m) | 三個月前 (-3m) | 三個月變化 |
|---|---|---|---|---|
| Strong Buy | 7 | 8 | 5 | +2 |
| Buy | 24 | 24 | 21 | +3 |
| Hold | 7 | 7 | 10 | -3 |
| Sell | 2 | 2 | 1 | +1 |
| Strong Sell | 1 | 1 | 1 | 0 |
| 合計 | 41 | 42 | 38 | |

目前 41 家中 31 家為 Buy 系 (約 76%), 7 家 Hold (約 17%), 3 家 Sell 系 (約 7%)。三個月內 Buy 系比例由約 68% 升至約 76%, Hold 由 10 家減為 7 家。近一個月 Buy 系由 32 家微降至 31 家, Strong Buy 由 8 家降為 7 家, 方向上屬小幅降溫。

最近動作 (WebSearch 次級報導, 未逐一核對原始研報, 僅供參考):
- 財報後 (11 月中) 多家券商調整目標價, 報導以目標價下修為主: Wells Fargo 目標價降至 $115 但維持 Overweight。
- Deutsche Bank 報導為升評至 Buy, 目標價 $140。
- Citi 在 Q3 超預期後上調目標, 報導標題指 "over 200% upside", 偏多。
- 整體報導描述 sell-side 在財報後 "largely sees pt cuts", 認為是整個 AI 雲端族群去評價 (de-rating) 的延續。
- 與 11-16 報告引用的 Stifel 目標價由 $120 降至 $60 並維持 Hold 的報導, 本次搜尋未再出現, 無法確認是否為新事件。

## Retail social

- Reddit: 無法取得 (WebFetch 遭拒絕)。r/wallstreetbets 與 r/stocks 的 CRWV 搜尋均未能讀取, 無法列出代表性貼文或計算多空比例。
- StockTwits: 無法取得 (api.stocktwits.com 無法解析, 本次未重試)。次級報導 (StockTwits 新聞文章) 指出, 財報後 CRWV 單日大漲約 25% (報導價 $60.77), 週漲幅約 31%, 散戶情緒指標由 "bearish" 轉為 "extremely bullish"。此為媒體轉述, 無法核對原始留言量與多空標記比例。
- X / 新聞: WebSearch 可見的次級來源多為財經媒體與券商評論, 未見具體 X 貼文量化資料。
- 聲量 (buzz volume): 無法量化相對於平時的倍數。定性判斷為財報週前後明顯升溫, 但非財報期間的日常水準無資料。
- 散戶取向: 次級來源顯示財報後偏多 (反彈、目標價上修聲音), 但同時存在債務與資本支出疑慮的偏空敘述。目前標示為 "偏多但信心低", 未經 Reddit 或 StockTwits 直接驗證。
- 主要議題 (依次級報導彙整):
  - 反彈與估值: 財報超預期後股價單週大漲, 市場討論 "是否能再翻倍" 與 "債務疑慮是否被低估"。
  - 債務與資本支出: 2026 年資本支出指引上修至 $37B–$39B, 是偏空論點的核心。
  - 稀釋與內部人賣出: 內部人大量賣出被視為偏空訊號, 媒體常引用。
  - 同業與 NVIDIA: NVIDIA 為第二大持股人 (約 10%), 相關持股變動常被拿來當成信心指標。
  - 價格資料不一致: 不同來源報導的盤中價差異大, 散戶討論可能因此混亂, 需以即時報價為準。

## Insider activity

資料區間: yf insider 回傳 150 筆, 日期範圍 2026-06-22 至 2026-11-10。6 個月窗口 (2026-05-23 起) 的前段未被完整涵蓋, 以下為 "回傳期間內的合計"。金額為 USD。

Net 6mo (可見期間): 公開市場買入 $0 (無 open-market purchase)。賣出合計約 $1.23B (USD B), 共 79 筆賣出交易。

注意: Magnetar 2026-08-14 有兩筆完全相同的賣出申報 (307,131 股、$33.4M), 疑似重複計算, 去重後賣出約 $1.20B。

| 人員 | 身分 | 賣出金額 (USD B) | 備註 |
|---|---|---|---|
| Magnetar Financial | 10% 以上持股人 | 0.51 | 8 月集中出售, 8/12 單日最高約 $0.23B |
| Michael N. Intrator | CEO | 0.42 | 每週約 307,692 股的週期性出售, 疑似預定計畫 (10b5-1 未經核實) |
| Brannin McBee | Officer | 0.23 | 6–8 月多次出售, 單筆最大約 $0.02B |
| Kristen J. McVeety | General Counsel | 0.02 | 含選擇權行使後賣出 |
| Brian M. Venturo | Officer & Director | 0.02 | 6 月與 7 月出售, 9/18 另有股票贈與 |
| Nitin Agrawal | CFO | 0.02 | 7–9 月多筆出售 |
| 其他 (Goldberg, Jones, Jain, Baker) | Officer / COO | 0.01 | 小額 |

近期動態: 11/09 COO Sachin Jain 以 $46.23 賣出 13,611 股 (約 $0.63M), 為近期最低價格的一筆賣出, 顯示股價在 11 月初已跌至約 $46 區間。10/13 Officer Jonathan Jones 以 $77–80 賣出約 $2.9M。

其他非市場交易: 董事 (Hutchins, Whitman, Boone) 有股票授予 (grant) 與少量交易, 金額極小, 屬例行薪酬性質, 不列為看多訊號。CFO Agrawal 與 CEO Intrator 在 11 月無新增賣出紀錄 (回傳資料截至 11/10)。

價格脈絡: 6 月至 10 月內部人賣出價格區間約 $66–$111。11 月初股價跌至 $46 後, 次級報導指財報後反彈至約 $57–61。

## Ownership shifts

- 內部人持股 (insidersPercentHeld): 約 18.4%。
- 機構持股 (institutionsPercentHeld): 約 74.9%; 持股機構家數 1,386 家。
- 機構占流通股比例 (institutionsFloatPercentHeld): 約 91.8%。
- 前十大持股 (9/30 13F 申報):
  - Magnetar Financial: 10.24%, 持股 47.7M 股, 較前期減少約 8.4%。
  - Nvidia: 10.13%, 持股 47.2M 股, 持平。
  - BlackRock: 6.38%, 較前期增持約 23%。
  - Vanguard (兩個實體合計): 約 7.6%, 雙雙增持 (約 +5% 與 +10%)。
  - Invesco: 2.72%, 增持約 2%。
  - Value Aligned Research Advisors: 2.50%, 增持約 7%。
  - Aspex Management (HK): 2.21%, 增持約 30%。
  - Proficio Capital Partners: 1.99%, 持股翻倍 (+100%)。
  - Two Sigma Investments: 1.82%, 大幅增持 (+147%)。
- 趨勢判讀: 前十大機構多為增持, 尤其 Two Sigma、Proficio、Aspex 等量化或中小型策略基金明顯加碼。唯一明顯減持者為 Magnetar, 與其 8 月 Form 4 大額賣出方向一致。Nvidia 持股維持不變。機構集中度高 (前十大合計約 45%), 大型被動基金與策略持股者為主。

## Net sentiment score

- 分析師: 偏多 (Buy 系約 76%, 三個月內比例上升), 但近期目標價以下修為主, 估值分歧明顯。一個月內 Strong Buy 小幅減少。信心: 中高。
- 內部人: 偏空 (可見期間約 $1.20–1.23B 賣出、零公開市場買入; 主要賣方為 10% 持股人、CEO 與多位高階主管)。部分賣出疑似預定計畫, 不必然代表對前景的判斷。信心: 高 (交易記錄可直接查證)。
- 機構: 中性偏多 (前十大多為增持, 僅 Magnetar 減持)。信心: 中。
- 散戶: 無法直接判定。次級來源呈現財報後偏多、債務與稀釋疑慮偏空的混合敘述。信心: 低。
- 綜合: 中性 (信心低)。分析師與機構偏多, 內部人大額賣出偏空, 散戶資料缺口使整體判斷受限。

Divergence flag: 是。分析師與機構持股偏多, 與內部人大額賣出方向相反。散戶與分析師之間的分歧無法可靠判定, 因 Reddit 與 StockTwits 皆無法取得直接資料。

注意: 本報告為情緒盤點, 不含交易建議。

SENTIMENT REPORT COMPLETE
