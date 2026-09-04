# Neutral risk view — ZS

## Points of agreement (both sides)
- 9/3 財報是真實二元事件，非可忽略的雜訊；兩方都同意 post-earnings 進場需搭配情境判斷，不能機械化執行。
- Stop 若遇跳空必須用「開盤價評估」取代「掛單等 $173.98 成交」的假設——aggressive 承認 trader 的 $173.98 結構合理，conservative 進一步指出跳空會使其失效，二者不衝突，是互補。
- Sizing 定義必須先講清楚（市值 % vs 風險預算 %），否則實際曝險可能相差 25 倍，這是 conservative 抓到的具體漏洞，aggressive 未反駁。

## Aggressive overreach
- Where：主張財報前即應用 call spread 卡位（甚至暗示財報後 beat 就衝到 Large 2.5-3%）。
- Why：investment_plan 明確判定 NEUTRAL、LOW conviction，雙方 confidence 均僅 6/10，且內部人 6 個月零買入的紅旗尚未證偽。同業 CRWD/OKTA beat 是 peer signal，不是 ZS 自身確認的數據，用它反推「上行不對稱」屬選擇性引用；ZS 自身歷史（5 月 -30% 跳空）才是唯一有公司特定先例的參考，且方向是下跌，不是上漲。低信心事件前建倉（即使是 defined-risk 選擇權）已偏離 research manager 的判斷基礎。

## Conservative overreach
- Where：建議財報後「首日不動作，第二至第三個交易日站穩支撐再進 1/3 部位」。
- Why：trade_proposal 的 LONG entry 區間（$180-191 回檔或站穩 $191.25 追價）本身已內建等待確認的邏輯；再疊加 2-3 天觀察期會進一步推高進場價、壓縮 R:R，卻沒有對應的風險削減效益——這是為了迴避時序風險而過度犧牲報酬結構的反射性保守，而非有數據支持的必要調整。Scenario A 的 25% 機率亦缺乏量化依據，屬主觀賦值。

## Balanced adjustment proposal
- Size：財報前維持 AVOID 為預設（呼應 investment_plan），若要保留上行選擇性，僅允許極小額 defined-risk call spread（premium ≤0.4% NAV，比照 aggressive 估算的 ~$400/口），不做股權曝險。財報後採風險預算法，非市值法：LONG 觸發時以「最大損失 = 1% NAV」反推股數（非 trader 原案的 1.5%），並用 T+1 單日確認（非 conservative 的 2-3 日）分 1/3 起始倉、站穩後補足。
- Stop：維持 $173.98（MA20），但明訂跳空情境改用開盤價評估，跌破 -10% 直接出場不等反彈。
- Entry：沿用 trade_proposal 雙向 triggers，僅將「等待天數」由 0（aggressive）與 2-3 天（conservative）折衷為 T+1 確認。
- Hedge：財報前選擇性小額 call spread 可接受，作為戰術性凸性倉位，非股權部位替代品；若同時持有 CRWD/OKTA/PANW，ZS 曝險併入 sector 風險預算。
- Time horizon：1-3m，維持 trade_proposal 原案。

## Net $ risk if stop hits
以 NAV $100,000、entry $185、stop $173.98（風險/股 $11.02、風險預算 1% NAV）計算：約 90 股，部位市值 ≈$16,650（16.65% NAV），機械式 stop 風險 ≈$1,000（1% NAV）。若重演 5 月式跳空至 ~$135（Scenario A），實際損失 ≈$4,500（4.5% NAV）——此為跳空情境下的尾部風險上限，須以開盤評估規則控管，不可視為機械 stop 已完全覆蓋。

## Net $ upside at T1 / T2
同一 90 股部位：T1 $198.88 → 獲利 ≈$1,249；T2 $211.89-225 → 獲利 ≈$2,420-$3,600。

NEUTRAL VIEW COMPLETE
