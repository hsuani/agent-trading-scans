# Neutral risk view — MOD

## Points of agreement (both sides)
- 現股方向性曝險應維持 0%：基本面（FCF 轉負、毛利率下滑、DSO 拉長）與事件面（Samsung 傳聞）兩個 crux 都未明朗，追多追空都是賭傳聞結果而非賭基本面。
- 若要參與，應用「買進型選擇權結構」取代現股，把最大虧損鎖死在權利金，避開 MOD 已出現過 -21.4%／+33.8% 的跳空缺口會讓現股停損單失效的風險。
- 部位規模必須遠低於一般持股（0.3%–0.5% NAV 區間），不應用現股的 1.5–2 倍 ATR 停損邏輯硬套在這種雙峰（binary）事件上。

## Aggressive overreach
- Where：call spread 的成本估算（$8–10／寬度 $40）直接假設，market.md 並無選擇權鏈或 IV 資料佐證，4:1 報酬比是建立在未驗證的權利金數字上，過度自信。
- Why：技術面被描述為「乾淨回測後企穩」，但同一份 market.md 明確指出 11-25 反彈量僅 10 日均量 0.57 倍、反彈高點連續下移、MACD 柱體已連續四日收縮——這是動能轉弱的訊號，aggressive 選擇性引用對自己有利的指標（RSI、MACD 轉正）卻略過量能與高點結構，屬於確認偏誤。

## Conservative overreach
- Where：Tail scenario 的機率分配（35%/20%/20%/15%）缺乏統計基礎，屬主觀拍數字；且「要求收盤放量＋連續兩日站穩 $146.50」這個轉多觸發條件，用於一個本質是「公司公告／否認」式跳空觸發的二元事件並不合邏輯——confirmation 一旦發生就是跳空，不會給出「兩日確認」的時間窗。
- Why：此外，conservative 計算的「現股滑價後實際虧損達 0.55% NAV，是預算的近 2 倍」這段論證其實支持的是「不要用現股」而非「選擇權部位也要更保守」，但其建議的部位上限（0.3% NAV）卻被拿來同時套用在已經是選擇權封頂虧損的結構上，邏輯上有一定程度的重複保守（belt-and-suspenders），對已用 spread 鎖死下檔的倉位再疊加板塊避險（VRT put）屬於邊際效益遞減的多餘保護。

## Balanced adjustment proposal
- Size：0.3% NAV（採 conservative 的保守下限，而非 aggressive 的 0.3–0.5% 區間上緣），因權利金估算未經驗證，寧可先保守。
- Stop：不適用現股邏輯；以權利金全損為最大虧損上限，不另設價格停損。
- Entry：可現在小額布局 call spread（如 $140/$180），不需等待 conservative 的「兩日站穩 $146.50」訊號，因為此訊號對 M&A 跳空事件而言意義有限；但到期日應設在 2027-02-03 FQ3 財報之前，涵蓋兩個 crux 任一明朗化的時間窗。
- Hedge：不需額外疊加 VRT/板塊空頭避險——spread 結構本身已封頂下檔，額外避險只會侵蝕本已很小的上行報酬，屬過度保守。
- Time horizon：數天至約 10 週（到 FQ3 財報前），任一 crux 明朗後立即重新評估，不持有過期後倉位。

## Net $ risk if stop hits
以 NAV = USD 1,000,000、0.3% NAV 配置（約 $3,000 權利金）：最大虧損 = $3,000（0.3% NAV），即權利金全損，無額外滑價風險。

## Net $ upside at T1 / T2
T1（股價反彈至 $160，spread 部分轉為實值）約 $6,000（2x 本金）；T2（Samsung 併購條款證實、股價站上 $180，spread 打滿寬度）約 $12,000（4x 本金）。

NEUTRAL VIEW COMPLETE
