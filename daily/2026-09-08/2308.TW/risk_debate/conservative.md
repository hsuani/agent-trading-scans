# Conservative risk view — 2308.TW

## Where trader is too aggressive

- **部位上限偏高**：提案建議 1.0–1.5% NAV，但在 PRICE_DATA_UNAVAILABLE 的條件下根本無法定義 ATR，止損區間「NTD 1,750」純為估算，不可作為精確風控依據。無實際成交價就設定部位，等同在黑暗中瞄準。
- **止損幅度過寬**：以參考進場價 NTD 2,000 計算，止損距離 NTD 250（12.5%），遠超一般波動度允許的緊止損標準。對一支 Forward P/E 42x 的高估值股票，12.5% 的空間在任何一個壞消息下都可能一次性跳空穿越。
- **估值無安全邊際**：Forward P/E 42x 意味每一分 EPS 下修都將引發「分子與倍數雙殺（Double Kill）」。投資計畫本身已引用熊方基本情境 -47%，但部位規模並未充分反映此一尾部風險。
- **Capex 700 億元尚未兌現**：全年資本支出佔估計營收 17–18%，短期 FCF 承壓已確定；若需求邊際放緩，FCF 轉負將直接衝擊倍數重估速度。

## Tail scenarios

- **Scenario A（機率 ~20%）：超大規模雲端業者凍結 AI 資料中心採購**。Microsoft / Google 任一宣布 2027 年 Capex 暫緩，市場即刻重估台達電 2027 EPS 共識 65.1 元。若倍數壓縮至 25x，目標價約 NTD 1,600，較 NTD 2,000 下行 -20%。1.5% NAV 部位虧損達 0.3% NAV（未含跳空擴大風險）。
- **Scenario B（機率 ~15%）：Fed 升息預期重燃 / 台灣地緣衝突升溫**。高 Beta 電子股在流動性緊縮週期遭外資集中拋售。外資持股 62.16%，一旦贖回潮啟動，市場承接深度不足，NTD 1,750 止損不一定能成交，滑價風險顯著。實際損失可能比估算多 30–50%。
- **Scenario C（機率 ~10%）：光寶科奪得 HVDC 重大訂單**。市占敘事瓦解，分析師目標價群體性下修，21 BUY / 0 SELL 的極端樂觀共識快速反轉，造成踩踏。

## Recommended adjustments

- **Size：1.0–1.5% NAV → 0.5% NAV**（理由：PRICE_DATA_UNAVAILABLE 無法計算精確 ATR，Capex 重押 + Forward P/E 42x 雙重風險需額外降倉緩衝）
- **Stop：NTD 1,750（估算）→ 等待開盤實際價格後，以真實前低重新計算，勿以估算值下單**
- **Entry：分批進場，第一批 0.3% NAV 等待開盤 30 分鐘確認支撐；第二批 0.2% NAV 等 Q3 月報 EPS ≥ 2.5 元確認後再加**
- **Consider：以 TAIEX 指數 Put 或 SOX ETF Put 對沖 AI 板塊系統性風險，降低組合 Beta 暴露**

## Position-level $ risk

以 0.5% NAV 計（假設 NAV = NTD 10,000,000，部位 NTD 50,000）：止損幅度 12.5% → 若止損如期成交，損失 NTD 6,250（= 0.0625% NAV）。**可接受**。但若跳空至 NTD 1,600（Scenario A），損失擴大至 NTD 20,000（= 0.2% NAV），此時 0.5% 部位上限即為關鍵防線；若按原提案 1.5% NAV 進場，同一跳空情境損失達 0.6% NAV，對單一個股而言不可接受。

## What I'd push for

在 PRICE_DATA_UNAVAILABLE 解除、開盤實際成交價確認前，**一律不進場**。正式開盤後，首筆建倉限 0.3% NAV，以真實前低（非估算 NTD 1,750）設定止損，當日外資淨賣超超過 500 張即暫停執行。待 2026 年 10 月 Q3 月報 EPS ≥ 2.5 元確認後，才允許加碼至 0.5% NAV 上限。Forward P/E 42x 在沒有更低進場點或更緊止損的前提下，任何超過 0.5% NAV 的部位規模都是以希望代替風控。

CONSERVATIVE VIEW COMPLETE
