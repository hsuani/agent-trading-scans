# Sentiment — SIVE.ST (Sivers Semiconductors) as of 2026-10-15

## Analyst consensus
目前 **1 buy / 0 hold / 0 sell**（yf rec_summary，0m / -1m / -2m 三期皆相同）。覆蓋家數只有 1 家（推測為 Redeye），樣本過小，不具統計意義。

近期升降評等：近三個月無評等變動（yf recommendations 無 upgrade / downgrade 紀錄）。

目標價：yf 無 1 年期目標價。WebSearch 找到的 Redeye 公允價值區間 SEK 3-22（Base Case 由 SEK 13 上調至 SEK 14），但文件未註明年度，且 Redeye 報告為舊文，無法確認是否為最新版本，僅供參考。Redeye 在 Q2 後的評論指出：2026 年營收與 EBITDA 預估下調，但 2027-2028 年預估大致維持，Base Case 小幅上調。

## Retail social
- Reddit: **DATA_UNAVAILABLE**。r/wallstreetbets 與 r/stocks 的 JSON 端點在本沙箱被擋，且 SIVE 在這兩個社群的討論量本身通常極低，即使可讀也可能無足夠樣本。
- StockTwits / X: **DATA_UNAVAILABLE（StockTwits）**。WebSearch 只找到 OTC 代號 SIVEF 的頁面，缺乏時間戳與情緒分數，不採用。X 端的訊息在 WebSearch 結果中僅有間接提及：一篇德文報導指出股價先前一度大漲，部分漲幅與某 X 帳號的社群推廣有關（來源未能直接核實）。
- Forum（Flashback / Avanza）：WebSearch 未找到相關討論串。
- 聲量（定性）：未能量化，無法與基準比較。WebSearch 結果以新聞轉載與自動化市場新聞頁為主，真正的散戶討論幾乎沒有被索引到。
- Tilt：**無法判定**。不應從新聞標題推論散戶情緒。
- Themes（從新聞與公司公告歸納，非散戶原文）：
  - 第二上市（Nasdaq）計畫：多篇報導把它當作主要題材，時程約為 2026 下半年至 2027 年初。
  - 機會管道（pipeline）成長：管道金額從年初起大幅增加，7 月報告約 12 億美元；AI 資料中心、衛星通訊、車用 LiDAR 為主要題材。
  - 稀釋與持續性疑慮：約 7 億瑞典克朗定向增資，以及審計與持續經營相關的警示。
  - 股價大幅回落：自 6/3 高點 10.23 歐元回落約 6 至 7 成。

## Insider activity
yf insider 回傳空陣列，無法從資料源取得交易明細。以下資料來自 WebSearch 新聞與公司公告，**未能逐筆核實**：

- 7/9 買進（Boerse-Express 報導）：Todd Thomson（董事）以約 42.80 SEK 買 12,500 股；Karin Raj（董事）買 13,264 股；Helena Svancar（董事）買 11,019 股；VD Vickram Vathulya 同日買入（股數未取得）。
- 7/13 公司公告：董事 Bami Bastani、Karin Raj、Helena Svancar、Todd Thomson、Joakim Nideborn 完成年度股東會授權的買股，持有期限 12 個月。
- 金額估算（假設上述 3 人股數皆以 42.80 SEK 成交，屬粗估）：已知董事買入約 1.57M SEK（約 15 萬美元等級）。Vathulya 與 Bastani、Nideborn 的股數未知，無法加總。
- 賣出：WebSearch 找到一則 Affärsvärlden 標題（7/22 前後）提到「董事賣、VD 買」，與公司公告不一致，無法核實。另有一則未經核實的標題，稱大股東可能未申報而賣出。兩者皆**不計入**淨額。
- 淨額 6 個月：**約 +1.57M SEK 以上（僅已知董事買入，估算），未知賣出，淨買方向**。資料完整度低。
- 注意：這些買入發生在 lock-up 到期前後（7/16 到期），且在 7/28 起進入封閉期前完成。買入可能帶有「支撐股價」或履行股東會授權的性質，不宜直接解讀為強烈看多訊號。

## Ownership shifts
- insidersPercentHeld：21.34%
- institutionsPercentHeld：15.09%（institutionsFloatPercentHeld 19.19%）
- institutionsCount：55
- 趨勢：**DATA_UNAVAILABLE**。yf major_holders 只回傳當前快照，無歷史比較。內部人持股 21% 偏高，加上大幅稀釋後的持股結構，流動性與籌碼集中度值得留意。

## 價格與事件背景（僅供脈絡）
- 6/3：年內高點 10.23 歐元。
- 7/15：收盤約 3.55 歐元（較高點低約 65%）。
- 7/16：lock-up 到期。
- 8/27：Q2 2026 報告：淨銷售 SEK 53.8M，年減約 12%；產品/硬體營收年增約 13%；調整後 EBITDA 約 -SEK 35.5M。管理層稱為刻意的轉型期，影響預計於 2026 Q4 顯現。
- 10/6：約 3.16 歐元，當日上漲約 3.7%，無公司特定新聞。
- 10/22：預定召開臨時股東會，提案更換審計機構（Deloitte → Ernst & Young），與美國上市所需的 PCAOB 審計準備有關。本日 (10/15) 尚未發生。
- 11/26：Q3 報告（已排定）。
- 注意：來源之間的價格數字有衝突，例如某來源稱「年初至今上漲 713%」，與 6 月高點後大幅回落的描述不一致，該數字屬於促銷性質來源，未採用。

## Net sentiment score
**Composite：中性（信心：低）**

- 分析師面：偏多（1 buy，覆蓋極薄，權重低）。
- 內部人面：偏多（董事與 CEO 在 lock-up 前後有買入，金額有限，且與股東會授權有關）。
- 散戶面：無法判定（Reddit / StockTwits 不可取得，WebSearch 未索引到有效討論）。
- 基本面與價格動能：偏弱（Q2 營收年減、EBITDA 虧損擴大、股價自高點大幅回落、定向增資稀釋）。
- 綜合：分析師與內部人的正面訊號都很薄弱，且被基本面與稀釋壓過，因此合併為中性，但信心低，主要因為散戶面與部分內部人交易數據不可得。

**Divergence flag：無法判定（no）**
- 由於散戶 tilt 無法取得，無法判斷是否與分析師 tilt 相反。若未來取得 Reddit 或論壇資料，可再檢視。

## Data gaps
- Reddit、StockTwits：沙箱封鎖，SOFT-FAIL。
- yf insider：空陣列，交易明細改由 WebSearch 新聞拼湊，未逐筆核實。
- yf recommendations：僅有期間彙總，無逐筆 upgrade / downgrade 紀錄。
- 機構持股趨勢：無歷史資料。
- 價格來源有衝突，本報告未採用單一來源的絕對價位。

SENTIMENT REPORT COMPLETE
