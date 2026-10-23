# Sentiment — 6217.TWO (中探針科技) as of 2026-10-24

資料品質總註: 本次資料大多不可用或時點不一致。yfinance 因 Yahoo cookie/crumb 取得失敗,recommendations、rec_summary、insider 三項回傳空陣列,視為 DATA_UNAVAILABLE。Reddit 與 StockTwits 直接抓取失敗(Reddit 連線被拒、StockTwits DNS 解析失敗),屬 soft-fail。WebSearch 結果多為 2026 年 1 月至 8 月的快取頁面,沒有找到 10 月的討論或新聞。以下判斷信心偏低。

## Analyst consensus
DATA_UNAVAILABLE. yfinance rec_summary 與 recommendations 皆回傳空值,無法取得買進/持有/賣出家數、評等變動或目標價變動。台股小型櫃買股通常覆蓋券商家數少,實際覆蓋情況需另行確認。

## Retail social
- Reddit: DATA_UNAVAILABLE。r/stocks 與 r/wallstreetbets 搜尋 6217 的請求無法連線,也預期英文散戶討論極少(台股小型櫃買股在英文社群幾乎沒有聲量)。
- StockTwits / X: DATA_UNAVAILABLE。StockTwits 無法解析,且此股在英文平台幾乎無 cashtag 討論。X 上未找到可用的近期英文貼文。
- 中文論壇 (CMoney 股市爆料同學等): 一則 CMoney 討論頁(未標註日期)描述討論偏負面,包含下市疑慮、公司高層持股減少的說法,也有少數人認為若研發與成本控制有成效仍有長期獲利空間。這是唯一的中文散戶語料,時點不明,僅供參考。
- 聲量 (相對一般水準): 無法量化。英文渠道可視為接近零,中文渠道未找到 2026 年 10 月的討論量資料。
- 主要主題 (依可見語料歸納):
  1. 虧損與獲利能力: 近四季 EPS 為負(來源記載約 -0.37 元),市場關注何時轉虧為盈。
  2. 估值: 股淨比約 6.5 至 6.9 倍,被視為偏高。
  3. 股價大幅回檔: 自 5 月高點(約 324.5 元)大幅下跌,被視為高本益比股的修正。
  4. 外資與法人賣超: 4 月起外資與三大法人多次賣超。
  5. 交易所注意股處置: 因周轉率過高被列為注意股。
- 散戶傾向: 偏空 (低信心,僅依中文論壇單一來源與新聞標題推論)。

## Insider activity
Net 6mo: DATA_UNAVAILABLE。yfinance insider 回傳空值。網路搜尋未取得董監事持股申報明細,僅知某論壇討論提及高層賣出,但無金額、日期、人員等可驗證資訊。
- 可核對的官方管道: 公開資訊觀測站 (MOPS) 的「內部人持股變動申報」,依公司代號 6217 查詢。
- 參考: yfinance major_holders 顯示內部人持股比例約 17.2%,但未提供時間序列,無法判斷增減。

## Ownership shifts
- yfinance major_holders (時點不明): insidersPercentHeld 約 17.2%;institutionsPercentHeld 約 1.86%;institutionsFloatPercentHeld 約 2.24%;institutionsCount 為 7。
- 注意: 機構持股 1.86% 明顯偏低,且與法人資料的常見口徑不一致(台股通常以外資持股比例呈現),此數字可能只計美股式 13F 機構,不宜直接解讀。
- 中文來源: 玩股網籌碼頁顯示 2026 年 7 月 24 日外資持股比例約 21.47%,投信持股為 0。這與 yfinance 的口徑不同,不可直接比較。
- 趨勢: 無法判斷。缺少連續多期的持股比例資料,也找不到 10 月的更新。

## Price context (供判讀情緒用,非本報告的核心訊號)
- 2026 年 4 月初約 200 元;5 月 14 日約 324.5 元(高點);之後急速回落。
- 7 月下旬約 166 至 181 元;7 月 30 日約 101.5 元(來源不一)。
- 8 月 4 日收 134.00 元(來源 MONEY LINK,單一來源)。
- 10 月 2 日約 177.50 元(玩股網本益比頁,當日 +1.72%)。
- 10 月 8 日收 168 元(-2.89%,StatementDog 頁面)。
- 以上價格來自不同快取頁面,互相之間有跳動,彼此不能直接串接成完整走勢。10 月 24 日的最新價格未取得。
- 財務基本面 (來源記載): 股淨比約 6.9 倍;一則頁面列出 4 項風險與 2 項亮點,且財務體質項目未通過排除地雷股檢查。

## Net sentiment score
Composite: bearish (低信心)。

依據:
- 可用的中文散戶語料 (CMoney 論壇) 偏負面,但時點不明、來源單一。
- 新聞與籌碼標題顯示 4 至 5 月的外資與法人賣超、注意股處置、虧損與高估值。這些多為 2026 年中期的資訊,未必反映 10 月。
- 分析師共識、英文社群、StockTwits 皆無資料,故無法做跨來源交叉驗證。

Divergence flag: DATA_UNAVAILABLE。因缺少分析師評等,無法判斷散戶與分析師傾向是否背離。

## 指標表

| 指標 | 數值 | 備註 |
|---|---|---|
| 整體情緒傾向 | 偏空 (bearish) | 低信心;單一中文論壇與新聞標題推論 |
| 分析師買進比例 | DATA_UNAVAILABLE | yfinance rec_summary 空值 |
| 分析師共識分數 | DATA_UNAVAILABLE | 無評等資料,無法計算 |
| 分析師目標價變動 | DATA_UNAVAILABLE | 無資料 |
| 散戶聲量 (Reddit/StockTwits) | DATA_UNAVAILABLE | 英文渠道幾乎無討論,且抓取失敗 |
| 中文論壇傾向 | 偏空 | 時點不明,單一來源 |
| 6 個月內部人淨買賣 | DATA_UNAVAILABLE | yfinance insider 空值,無 MOPS 明細 |
| 內部人持股比例 | 約 17.2% | yfinance major_holders,時點不明 |
| 機構持股比例 | 約 1.86% | yfinance 口徑,疑似僅計部分機構,不可直接比較 |
| 機構家數 | 7 | yfinance major_holders |
| 外資持股比例 | 約 21.47% (2026-07-24) | 玩股網,與 yfinance 口徑不同 |

## 後續待補 (非本次可取得)
1. 以 MOPS 查詢 6217 近 6 個月董監事與大股東持股變動申報,補上淨買賣金額。
2. 以可連線的券商研究來源或 TEJ 等資料庫補上分析師評等與目標價。
3. 以 PTT 股板、Dcard 或財經媒體補抓 10 月的中文討論量與語氣。
4. 外資與投信買賣超的連續資料,以確認 10 月走勢。

SENTIMENT REPORT COMPLETE
