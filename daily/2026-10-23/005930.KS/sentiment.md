# Sentiment — 005930.KS (Samsung Electronics) as of 2026-10-23

## 資料可用性總覽
- yf rec_summary：可用（36 位分析師，月度彙總）
- yf recommendations（歷史評級變動）：實際回傳的是同一組月度彙總，沒有個別升降評事件，視為 DATA_UNAVAILABLE（個別升降級）
- yf insider：回傳空陣列，視為 DATA_UNAVAILABLE
- yf major_holders：可用，但只有單一快照，無時間序列，持股趨勢 DATA_UNAVAILABLE
- Reddit（r/wallstreetbets、r/stocks、r/Samsung）直接搜尋：DATA_UNAVAILABLE（本次依指示改用 WebSearch，未直接取 Reddit JSON；WebSearch 未找到相關 WSB 討論串）
- StockTwits：DATA_UNAVAILABLE（未取得）
- X / 新聞輿情：WebSearch 可用，但多為新聞與 SEO 頁面，時效性混雜

## Analyst consensus
yf rec_summary（當前月）：**36 家**，strongBuy 11 / buy 24 / hold 1 / sell 0 / strongSell 0。
即 **35 buy-side / 1 hold / 0 sell**，買方比例約 97%。

近四個月趨勢（yf 月度彙總）：

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m（當前） | 11 | 24 | 1 | 0 | 0 |
| -1m | 11 | 24 | 1 | 0 | 0 |
| -2m | 11 | 25 | 1 | 0 | 0 |
| -3m | 11 | 25 | 1 | 0 | 0 |

- 近四個月評級結構幾乎不變，buy 家數由 25 略降為 24（-1m 起），未見 sell 或 hold 增加。這個 1 家 buy 的變化可能是一家降為 hold 之外的其他變動，但 yf 彙總無法確認，不宜過度解讀。
- 目標價：WebSearch 轉引的 valueinvesting.io 頁面顯示平均 12 個月目標價約 416,900 韓元、分析師 44 家、Strong Buy 14 / Buy 28 / Hold 2 / Sell 0。此數字與 yf 的 36 家不一致，且頁面價格（343,000 韓元）日期不明，**僅列為低可信度參考**。
- 5 月底券商目標價（二手轉述 tilnote.io）：KB 證券 53 萬、未來資產 55 萬、韓國投資證券 57 萬、SK 證券 61 萬、野村 59 萬韓元。屬於較早期資料，目前是否仍有效無法確認。
- 1 月券商報告：SK 證券目標價 26 萬韓元，但該筆為 1 月舊資料，與 5 月後目標價明顯脫節，應視為已過時。

## Retail social
- Reddit：直接 Reddit 搜尋 DATA_UNAVAILABLE。WebSearch 未檢索到 r/wallstreetbets 的 Samsung 相關討論串，無法評估 tilt 與樣本。
- StockTwits：DATA_UNAVAILABLE。
- X / 新聞輿情（WebSearch）：
  - 2 月 FNNews 報導韓國網路論壇出現大幅獲利的貼文，並有散戶擔心錯過（FOMO），例如一位投資人表示「return is over 100%, so I sold half」。此為 2 月舊資料，不代表 10 月現況。
  - 10 月資料：WebSearch 中文與韓文搜尋均未找到 10 月的散戶情緒文章，無法判斷 10 月的 tilt。
- 聲量（buzz volume）：定量 DATA_UNAVAILABLE，無法與典型水準比較。
- Tilt：**無法判定**（bullish / bearish / mixed 均缺乏 10 月直接證據）。
- 主要主題（依有限資料歸納）：
  1. HBM 技術與 AI 記憶體需求（多篇分析與券商報告共同提及）
  2. 股價波動劇烈、追高與停利爭議（2 月與 7 月報導）
  3. 勞資談判與罷工風險（5 月報導）
  4. 10 月 Q3 初步財測與 10/29 正式財報前的期待（SimianX 報導，見下方價格與數字疑慮）

## Price context（情緒判讀前提，數字互相衝突）
WebSearch 來源對股價的說法不一致，無法確定 10/23 的收盤價：
- SimianX（10/16）：收盤 215,500 韓元，較 6/18 歷史高點 362,500 韓元下跌約 40%。
- TradingKey（7/11）：約 38 萬韓元，盤中高點 374,500 韓元（6/19）。
- valueinvesting.io：343,000 韓元（日期不明）。
- TradingView：181,200 韓元，並列出 2026-02-13 歷史高點 184,400 韓元，與上述 6 月高點矛盾，判定為舊快照。

**結論**：目前無法以單一可靠來源確認 10/23 股價。若 10/16 收盤 215,500 韓元屬實，表示近期有大幅回落，但 ±數十萬韓元的來源分歧使此判斷信心偏低。

**數字疑慮（需下游驗證）**：SimianX 引述 Q3 2026 初步財測營收約 195 兆韓元、營業利益約 107.4 兆韓元。換算為 1,950,000 億韓元與 1,074,000 億韓元，營業利益率約 55%，明顯高於三星過去歷史水準；且 107.4 兆單季數字已超過 1 月券商報告對全年 2026 營業利益的預估（148–180 兆韓元）。這兩者互相衝突，**極可能是來源單位或數字誤植，請勿直接採用**，應以 10/8 官方初步財測原文核對。

## Insider activity
Net 6mo：DATA_UNAVAILABLE（yf insider 回傳空陣列，無法得知 CEO / CFO / 其他高管的買賣金額與方向）。
Notable：DATA_UNAVAILABLE。
注意：空陣列也可能代表資料來源（韓國 DART 內部人申報）未被 yf 覆蓋，不能推論為「無內部人交易」。

## Ownership shifts
- 內部人持股：9.69%
- 機構持股：46.90%（float 內佔 51.93%）
- 機構家數：748
- 趨勢：DATA_UNAVAILABLE（只有單一快照，無法判定集中度變化方向）

## Net sentiment score
- **分析師面：偏多（bullish），信心高**。36 家中 35 家 buy-side、0 家 sell，且近四個月結構穩定。
- **散戶面：無法判定（neutral / unknown），信心低**。缺乏 Reddit、StockTwits 直接資料與 10 月的散戶貼文。
- **內部人面：DATA_UNAVAILABLE**。
- **綜合**：分析師偏多、散戶與內部人無有效資料，整體判定 **neutral 偏多（信心：中低）**。判定依據僅為分析師一側，不能代表市場散戶情緒。

**Divergence flag：無法判定（DATA_UNAVAILABLE）**。若 10 月股價確實較 6 月高點回落約 40%，散戶情緒可能偏空，而分析師仍一致看多，會形成背離，但此前提本身未獲確認，故不設旗標。下次更新應先補 Reddit / StockTwits 直接資料與 10/23 可靠收盤價，再判斷背離。

## 資料缺口與後續建議
1. 取得 Reddit（r/wallstreetbets、r/stocks、r/Samsung）與 StockTwits 直接資料，以量化 buzz 與 tilt。
2. 以 DART 或 yf 其他端點補抓內部人交易（近 6 個月）。
3. 以官方來源確認 10/23 收盤價與 Q3 初步財測數字（10/8 公告）。
4. 追蹤 10/29 正式財報前後的評級變動，補充個別升降級事件。

SENTIMENT REPORT COMPLETE
