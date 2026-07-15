# Neutral risk view — AAOI

## Points of agreement (both sides)
- 財報前（8/6）不應新增裸多方向現貨曝險：conservative 明確主張不加倉；aggressive 雖想進場，但也承認應改用 defined-risk 的 options（非現貨）承接方向性賭注，兩者實質上都否定了「現在買現貨」。
- $110-113 現行停損有問題：兩方都同意這個距離（0.81x ATR14）在 124% 年化波動下容易被雜訊或財報跳空掃損，只是解法方向相反。
- $78.58 不是有效的日常風控工具：aggressive 把它當「呼吸空間」，conservative 直接否定其可執行性，但雙方其實都承認它代表的是「已大幅虧損後的結構性參考點」，而非能主動保護資金的停損。

## Aggressive overreach
- Where：建議既有現貨部位停損放寬至 $78.58（現價下方 37%）。
- Why：ATR 邏輯只能解釋日內/週內雜訊，不能用來合理化財報這種離散跳空風險；把 $78.58 當作可執行停損，等於在高波動理由的包裝下事實上取消了風控，這正是 conservative 指出的「已腰斬才認賠」情境，aggressive 對此未提出反駁。

## Conservative overreach
- Where：既有部位進一步降至 1/4 倉，且新進場需連續 3 日站穩 MA20 + MACD 轉正 + 量能 1.5 倍確認。
- Why：trade_proposal 與 investment_plan 的轉多觸發條件僅要求「站回 MA20 且 MACD 轉正」，並未要求連續 3 日確認，conservative 疊加額外門檻缺乏研究memo依據，容易導致訊號確立後仍觀望、錯過財報後第一波反應；其 tail scenario 機率加總達 70%，權重明顯偏空，屬立場強化而非中性估計。

## Balanced adjustment proposal
- Size：既有現貨降至 1/4 倉（NAV 2.5%，較 conservative 的極端保守與 trade_proposal 的半倉之間取中，但更接近 conservative，因為 ATR 論證支持縮小曝險而非放大停損距離）；不新增現貨部位。
- Stop：現貨收緊至 $118（採 conservative 版本，較貼近近期支撐且未依賴大幅放寬掩蓋風險）；$78.58 僅作結構性參考，不視為可執行停損。
- Entry：不新增現貨；可用 NAV 1-2% 配置財報後到期的 $140/$180 call spread 作衛星倉位，最大虧損鎖定在權利金（採 aggressive 的工具，但縮小規模）。
- Hedge：若既有現貨部位持有過財報，優先以 protective put 對沖跳空缺口，而非單純依賴停損單（回應 conservative 的「停損可能失效」疑慮）。
- Time horizon：持有至 8/6 財報，之後依 MA20 站穩 + MACD 轉正單一組合訊號（不需額外 3 日確認）重新評估標準倉位。

## Net $ risk if stop hits
以 NAV $100,000 為例：現貨 1/4 倉（約 20 股）於 $118 停損，損失 ≈ $150（0.15% NAV）；call spread 衛星倉位權利金最大虧損 $1,000-2,000（1-2% NAV）。若停損正常執行，合計風險 ≈ $1,150-2,150（1.15-2.15% NAV）。若財報跳空至 $90（停損失效情境），現貨損失擴大至 ≈ $709（0.71% NAV），加計權利金損失，合計最大曝險 ≈ $2,700（2.7% NAV）。

## Net $ upside at T1 / T2
T1（分析師共識 $151.30）：現貨 1/4 倉獲利 ≈ $517，call spread 部分價內化增值 ≈ $500-1,000，合計 ≈ $1,000-1,500。
T2（高看目標 $220）：現貨 1/4 倉獲利 ≈ $1,891，call spread 接近最大payout（權利金 3-5 倍，約 $4,500-7,500），合計 ≈ $6,400-9,400。

NEUTRAL VIEW COMPLETE
