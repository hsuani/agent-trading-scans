# Conservative risk view — ZS

## Where trader is too aggressive

- **Investment plan 倉位語言存在歧義風險**：trade_proposal 明定 Small（0.5% NAV），但 investment_plan 寫「半倉至六成倉位介入」，若被解讀為 NAV 的 50-60%，財報前即承受龐大未量化風險。應明確統一為 trade_proposal 的 0.5% NAV 上限，不得在財報前越線。
- **FCF 邊際壓縮輕描淡寫**：多方論述將 FCF 27% → 23%（-400bps）定性為「戰略性投入週期」，但管理層已預告 FY2027 CapEx 繼續上升，AI 計算成本的吸收能力尚未獲得實證。若 FY2027 FCF 邊際指引跌至 20% 以下，Rule of 40 勉強守線，現行估值倍數的 premium 基礎瓦解。這是結構性惡化情境，不應以「可能是一次性」輕帶過。
- **PRICE_DATA_UNAVAILABLE 下缺乏技術支撐確認**：無法確認 ATR、止損水位、支撐區間，等於在黑暗中建倉。R:R 無從量化，任何財報前進場均是定性博弈，不是風險可控的交易。
- **內部人信號被淡化**：19 筆交易 100% 為賣出，淨賣出 $5.3M，CFO 連續在 $144-149 依計畫出脫。雖為計畫性賣出（10b5-1），但零買進在財報前三週屬明顯訊號，執行層並不認為現價具吸引力。

## Tail scenarios

- **情境 A（概率 25%）**：9月3日財報顯示 FY2027 FCF 邊際指引下修至 20% 以下，市場重新定價 → 高成長 SaaS 倍數壓縮，股價承受 20-30% 下行壓力；PRICE_DATA_UNAVAILABLE 無法估算精確損失金額，但 0.5% NAV 倉位下最大損失仍控制在 NAV 的 0.10-0.15% 以內（假設下行 30%）。
- **情境 B（概率 20%）**：淨新增 ARR 季度環比負成長，市場確認 PANW 搶單論述為真，NDR 跌破 110% → 機構調降評級引發多殺多，短期跌幅可能超過情境 A；若在半倉（50% NAV）下進場，NAV 損失可達 10-15%，不可接受。
- **情境 C（概率 15%）**：Fed 在 2026Q4 重啟升息（通膨反彈或地緣衝突推升能源成本），高 P/S 成長股系統性去槓桿，ZS 此類非 GAAP 獲利、股價以未來現金流折現定價的股票首當其衝，與 ARK 類持倉高度相關，隱性集中風險被忽略。

## Recommended adjustments

- **Size**：維持 Small（0.5% NAV），財報前絕對不得擴倉；investment_plan「半倉」語言應明確廢止，在 9月3日前視同零加碼空間。
- **Stop**：PRICE_DATA_UNAVAILABLE 環境下無法設定精確止損，應以**財報結果**作為事件止損：若任一廢止條件觸發，立即清倉，不得持倉等反彈。
- **Entry**：**不進行財報前加碼**，現有觀察倉（0.5% NAV）維持不動；等待 9月3日財報後技術面確認買點再決策。
- **Consider**：若需財報曝險，以 IV Rank 15% 低波動環境購入小額 call spread 取代直接加碼 delta，將財報損益上限控制在已知保費損失範圍內。

## Position-level $ risk

PRICE_DATA_UNAVAILABLE，無法計算精確 $(entry − stop) × shares。以 NAV 比例估算：0.5% NAV 倉位、財報日股價下行 30% 的極端情境下，損失為 0.15% NAV。此水準可接受。若倉位被放大至 investment_plan 所述「半倉」（即使解讀為全倉之半），財報日 30% 下行的損失將達 15% NAV，絕對不可接受。

## What I'd push for

財報前三週，既無價格數據確認技術支撐，又面對 FCF 邊際壓縮方向未定、PANW 競爭衝擊尚無季度數據，內部人信號全為賣出，此時唯一理性選擇是將部位鎖定在 0.5% NAV 觀察倉，不做任何加碼。investment_plan 中「半倉至六成倉位介入」的語言應立即被 trade_proposal 的 Small 定義覆蓋，並在風控紀錄中明確標注。若願意在財報前保有曝險，以 call spread 替代直接持股，將最大損失鎖定在已知保費。9月3日財報後若 FCF 邊際指引守住 23%+ 且 EU 主權雲端管道金額首度揭露超過 $200M ARR，方可重新評估擴倉至 Medium（1.5% NAV），但彼時仍需等待技術面確認買點，不得追高。

CONSERVATIVE VIEW COMPLETE
