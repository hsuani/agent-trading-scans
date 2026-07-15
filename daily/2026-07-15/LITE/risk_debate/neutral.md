# Neutral risk view — LITE

## Points of agreement (both sides)
- 財報前不應新增**股票**方向性曝險，原有 ≤0.5% NAV 小倉位已是合理上限，不應加碼。
- 8/11 財報是唯一能解開牛熊分歧的可觀測驗證點，在此之前貿然放大股票 delta 缺乏依據。
- 用**選擇權結構**（而非現貨）承接財報催化劑曝險，是把「不對稱且偏空的 R:R」轉為可控風險的合理工具——雙方都認同這個方向，只是規模與用途（進攻型 call spread vs 防禦型 put）不同。

## Aggressive overreach
- Where：「現在進場優於等財報後確認」、稱 MACD 直方圖轉正 + 貼近 MA20 為「不對稱進場點」。
- Why：股價仍在 MA20 下方（-0.29%）、MA50 下方（-7.82%），MACD 線仍低於訊號線，尚未黃金交叉；把「空頭動能減緩」直接解讀為「反轉已現」是選擇性強調技術面而忽略趨勢仍偏弱的事實。且財報前 IV 通常已墊高，call spread 淨權利金估算的 14-18x asymmetry 未計入 IV crush 成本，實際 payoff ratio 會被壓縮。

## Conservative overreach
- Where：主張財報前應降至 0～0.25% NAV 或直接平倉；為三個尾部情境分別指定 25%／20-30%／15% 精確機率。
- Why：現有倉位已僅 ≤0.5% NAV，模型化虧損本就極小（0.024% NAV），為此再要求清倉等於為了避開一個本已極小的曝險，放棄牛方確實可驗證的動能訊號（連續 8 季 EPS 超額、OCF 轉正、現金部位翻倍）。三個機率數字缺乏明確模型依據，屬於為強化論述加上的精確度假象（false precision），應視為情境權重的定性排序，而非可加總的機率分佈。

## Balanced adjustment proposal
- Size：股票維持既有 ≤0.5% NAV（若已持倉）、不新增股票倉位；另外撥 0.15-0.2% NAV 權利金額度（低於 aggressive 的 0.3-0.5%，考量 IV crush）建立財報後到期的防禦性 put（行使價 ~$780）取代進攻型 call spread，優先保護既有倉位缺口風險，而非另開一個獨立的方向性賭注。
- Stop：採 conservative 的收盤確認制——連續 2 個交易日收盤跌破 $776.01 才減碼，取代即時觸價（現行距離僅 0.56×ATR14，intraday 雜訊掃出風險確實偏高，此點證據充分）。
- Entry：不追價、不因 MACD 直方圖轉正提前進場；需收盤站穩 $817 之上兩日以上或財報結果明朗，才依 investment_plan 的雙向 trigger 行動。
- Hedge：短天期 $780 附近 protective put，成本以覆蓋跳空缺口為目的，非用於放大上檔投機報酬。
- Time horizon：不變，數週，等待 8/11 財報明朗。

## Net $ risk if stop hits
以 0.5% NAV 股票倉位為基準：正常情境（停損有效成交）≈ 0.024% NAV；財報/關稅跳空情境（conservative Scenario A/B 估算）≈ 0.22%～0.32% NAV，約為正常值 10-13 倍——此為財報前必須用 put 對沖、而非僅靠停損單防守的核心理由。

## Net $ upside at T1 / T2
現貨 0.5% NAV 倉位：T1 $839.88（+3.1%）≈ +0.015% NAV；T2 $960（+17.8%）≈ +0.089% NAV。疊加 0.15-0.2% NAV 的財報後選擇權覆蓋層，可在不放大股票尾部曝險下，額外捕捉 guidance 再超額情境的不對稱上檔。

NEUTRAL VIEW COMPLETE
