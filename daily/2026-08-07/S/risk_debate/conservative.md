# Conservative risk view — S (SentinelOne)

## Where trader is too aggressive

- **部位規模在黑暗中設定**：PRICE_DATA_UNAVAILABLE 狀態下 ATR、年化波動率均無法取得，0.5% NAV 的「Small」標籤毫無 vol-adjusted 依據。S 屬高 beta 成長股，歷史日波動率可達 3–5%，實際風險暴露可能等同正常環境下 1–2% 的倉位。
- **財報前試水邏輯矛盾**：proposal 允許「財報前以 half-size 試水」，但 Q3 FY2026 ARR 若跌破 20% 即為多方論點崩解事件，這屬於純二元尾部風險。conviction LOW 卻主動吃財報風險，邏輯不一致。
- **52 週高點入場動能脆弱**：news.md 記載股價觸及 52 週高點 $20.05，情緒已高度樂觀，任何數據未達預期將在無技術止損錨點的情況下暴露完全開放式下行。
- **整合風險被低估**：Observo AI $225M 現金加股票收購、三筆 12 個月內收購，協同效益零量化。新任 CFO Sonalee Parekh 上任首季即面臨財報，機構對管理層執行力共識尚未建立。

## Tail scenarios

- **Scenario A（~25%）**：Q3 ARR 年增降至 20–22%，低於市場共識 → EV/Revenue 從 ~6–7× 壓縮至 ~5×，Goldman Sachs 目標 $15.50（investment_plan 引用）成為短期錨點，自 $20.05 跌幅約 **-23%**。
- **Scenario B（~15%）**：Observo AI 整合延誤，毛利率壓縮 >200 bps，現金消耗加速 + BTIG 持續負面現場調查 → 分析師下調，股價測試 **$13–14**，跌幅 **-30% 至 -35%**。
- **Scenario C（~10%）**：Fed 緊縮意外回頭（通膨黏性）→ 高 EV/Revenue 估值多重殺傷，GAAP 虧損公司首當其衝；參考 2022 年 SaaS 殺估值波，跌幅 40–50% 非不可能。

## Recommended adjustments

- **Size**：Small (0.5% NAV) → **0.25% NAV**；若不確定能獲得財報前價格資料，建議**完全待機**至財報後。
- **Stop**：技術止損無法設定（PRICE_DATA_UNAVAILABLE）。僅保留**基本面止損**：ARR 年增 <20% 即無條件全數離場，不設緩衝。
- **Entry**：**取消財報前試水建倉**。等待 Q3 FY2026 財報公布、價格資料恢復，確認 ATR 與 S/R 位置後方可建倉。
- **Consider**：若堅持財報前持有，以 OTM put（行使價約 $17，待價格資料恢復後計算 delta）對沖 Scenario A 尾部。

## Position-level $ risk

即時價格不可用，以文件中可查驗數字估算：入場代理價 $20.05（52 週高點，news.md），下行錨點 $15.50（Goldman 目標，investment_plan.md），每股潛在損失 **$4.55**。以 $1M NAV 為例：0.5% 部位 ($5,000) 觸及 $15.50 → 損失 **$1,137（1.14% NAV）**，且此跌幅可在財報後單日實現。0.25% 部位將損失壓縮至 **~$568（0.57% NAV）**，屬可接受範圍。Scenario B 下損失倍增，不可接受。

## What I'd push for

多方結構性方向（ARR $1B、自治 SOC 差異化、合規需求底撐）具有可查驗基礎，不反對長期邏輯。但「PRICE_DATA_UNAVAILABLE + conviction LOW + 財報二元事件」三者同時成立時，建倉條件根本未成熟。**執行建議**：現階段維持 100% 現金；等待 Q3 FY2026 財報公布，若 ARR 年增 ≥24% 且自治 SOC 有量化 ARPU 披露，財報後以 0.5% NAV 建倉並設基於 ATR 的技術止損；若 ARR <22%，放棄本次機會，不追跌。耐心等待數據確認比在高點承擔二元風險更符合 conviction LOW 的風險紀律。

CONSERVATIVE VIEW COMPLETE
