# Neutral risk view — 3008.TW

## Points of agreement (both sides)
- Stop $5,970 相對 entry 中值 $5,700 僅 $270（4.74%），小於 ATR14 約 6.9%，裸空確實容易被單日雜訊掃出，兩方都同意這不是統計上穩健的 stop。
- 裸空結構下 R:R 僅 1.26x（到 T1），兩方都承認偏弱，需要用結構或資金管理處理,而非直接接受。
- 都認為 CPO/FAU 軋空尾部風險需要用對沖工具處理,而不是靠放寬 stop 硬扛。
- 10/27 財報日期在 news.md 與 fundamentals.md 之間的矛盾是真實資訊缺口,應在觸發進場前釐清。

## Aggressive overreach
- Where: 主張把曝險規模「提升至接近研究計畫上限（1/2 部位）」。
- Why: investment_plan.md 的 sizing guidance 本身已寫明「最多四分之一到半個部位」,且前提是 conviction MEDIUM、10/27 數據矛盾未解。用 put spread 把最大損失鎖進權利金,只解決了下檔尾部風險,並未提升論述證據強度或解決數據缺口,以此為由衝到上限是把工具優勢過度延伸為加碼理由。另外主張在 death cross 時就先用「極小試探性 put」卡位,等於繞過 proposal 自己設計的單一收盤確認觸發機制,屬於為求搶跑而犧牲紀律。

## Conservative overreach
- Where: 建議把 stop 進一步收緊至 $5,850,同時又批評原 stop 比 ATR 還窄。
- Why: 這是自我矛盾——若 ATR14 約 6.9%（約 $425/日）已經比 $270 的停損距離更寬,把 stop 收得更緊（$5,970→$5,850,距離縮至 $150）只會放大被雜訊洗出的機率,而非降低。此外「完全不進場、等 FOMC+財報雙重明朗」在觸發式交易（本就只在確認跌破 5,740 後才進場）上近乎多餘的額外延遲,若財報疑義在觸發前已釐清,無需再等 FOMC 結果才行動。

## Balanced adjustment proposal
- Size：以 put spread（Long $5,600 Put / Short $5,360 Put,到期訂在 11 月營收公告後）取代裸空,權利金預算控制在約 0.3–0.35% NAV——介於保守方 0.25% 與激進方「近上限」之間,不因結構封頂損失就衝量。
- Stop：維持裸空論述失效價 $5,970 作為「出場/滾倉」訊號,不收緊也不放寬;但因改用定額損失結構,此 stop 僅作論述檢查點,非強制平倉線。
- Entry：維持單一觸發（收盤確認跌破 $5,740）,不提前卡位、不分批,以維持紀律;但新增前提條件——須先確認 10/27 是否真有財報事件,未釐清前不開倉。
- Hedge：spread 本身即為定額風險工具,不需額外疊加保守方建議的價外 call 或 3406 多單對沖,避免重複付權利金。
- Time horizon：11 月中—下旬(營收驗證期),與 spread 到期對齊;2027 年中 CPO/FAU 事件仍排除在操作視窗外。

## Net $ risk if stop hits
約 NT$60,000–80,000／lot（權利金成本,約 0.3% NAV)——遠低於裸空情境下的 NT$270,000／lot。

## Net $ upside at T1 / T2
約 NT$170,000／lot（T1 與 T2 相同,因 spread 在短腿履約價 $5,360 即封頂,超過此價位無額外獲利——這是定額風險結構的代價,需明確告知)。

RISK DEBATE ROUND COMPLETE
