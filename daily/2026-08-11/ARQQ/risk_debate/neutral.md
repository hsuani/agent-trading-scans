# Neutral risk view — ARQQ

## Points of agreement (both sides)
- Q4 融資二元事件是主導性風險，在此明朗前任何方向性押注均缺乏可靠 R:R（雙方共識）
- STOCH 91.88 + 認股權證 $22-25 頂壓構成真實短線阻力，入場時機不佳（雙方共識）
- 現金 $28.9M、燃燒 $66M 年化 → 剩餘 3-4 個月跑道幾乎鎖定 Q4 稀釋性融資（雙方共識）
- P/S ~580× 已定價極樂觀情景，現有安全邊際極薄（雙方共識）
- DoD / Tier-1 電信合約催化劑為真實機會，但 TCV 未披露、時間點不確定（雙方共識）

## Aggressive overreach
- **Where**：宣稱 "worst case ≤0.17% NAV"，將「止損精確執行」設為最壞情境前提
- **Why**：此數字只在止損能執行時成立。融資公告屬美東收盤後隔夜事件——若 SPAC 折價 $15-16，次日開盤直接跳空穿越 $21，止損完全失效。2% NAV equity 倉位在跳空 $16 情境下實際損失為 ~0.60% NAV，跳空 $12 為 ~0.95% NAV，比 Aggressive 宣稱的 0.17% 高出 3-5×。此外，STOCH vs RSI 動能延續論點在技術分析框架內有效，但對於隔夜二元融資事件的預測力接近零——以技術動能為 equity LONG 辯護，論點錯誤地混用了適用條件。

## Conservative overreach
- **Where**：要求「融資公告完成後 RSI <60 且 STOCH <50」方可重新評估
- **Why**：此雙重條件實為「等到最大非線性上行機會已被定價後才允許進場」；融資成功時價格極可能跳升，技術指標冷卻需數週，屆時 R:R 結構已根本不同。更關鍵的是，Conservative 批判 equity LONG 的最強論據（止損是幻象）對 **defined-risk options 結構完全無效**——Aggressive 自己在建議中已提出 Call spread（$23/$28，Nov 2026 到期），保費即硬性最大損失，跳空至 $12 亦不額外虧損。Conservative 以「止損無保護」否決所有進場結構，卻未回應 options 消除此問題的事實，屬論述漏洞。

## Balanced adjustment proposal

裁決：**equity LONG 採納 Conservative（AVOID）；structured options 採納 Aggressive 的工具邏輯，但縮減規模**。

| 項目 | 裁決 | 說明 |
|------|------|------|
| **Size** | Equity → 零；Call spread → ≤0.5% NAV 保費 | equity 跳空尾部不可接受；options 最大損失固定 |
| **Stop** | Equity LONG 無有效止損 | 隔夜跳空無法執行；Call spread 以保費為硬上限，無需 stop |
| **Entry** | 不建立 equity LONG；Call spread 若 options 流動性足夠，於 $22.90 附近執行 $23/$28 spread，Nov 2026 到期 | 捕捉 DoD / NCSC 6-12 週前置催化劑窗口，同時規避融資跳空尾部 |
| **Hedge** | 既有持倉以 QQQ put spread 或 ARKQ put 對沖板塊風險 | ARQQ 自身 options 流動性差（Conservative 已指出），板塊對沖成本更低 |
| **Time horizon** | Call spread Nov 2026 到期；融資公告條件明朗後（≥$40M、稀釋 ≤20%、發行價 ≥$20）重評 equity 倉位 | 不要求 RSI <60，融資條件才是重啟觸發器 |

> **注意**：若確認 ARQQ options 流動性不足以合理執行 Call spread，則回歸完全 AVOID——此為預設立場。

## Net $ risk if stop hits

| 倉位結構 | 情境 | 最大損失佔 NAV |
|---------|------|--------------|
| Equity LONG 2% NAV，止損執行 $21 | 理想 | ~0.17% NAV |
| Equity LONG 2% NAV，跳空 $16 | SPAC 折價融資 | ~0.60% NAV（止損失效）|
| Equity LONG 2% NAV，跳空 $12 | 極端情境 | ~0.95% NAV（止損失效）|
| **Call spread ≤0.5% NAV 保費** | **任何跳空情境** | **≤0.5% NAV（固定）** |

**裁決**：equity LONG 的實際尾部損失比名義止損設計高出 3-5×；Call spread 消除此不對稱性，以可預期保費換取明確上行空間。

## Net $ upside at T1 / T2

以 Call spread $23/$28（假設保費 ~$1.50/spread，≤0.5% NAV 投入）為基準：

- **T1（$28，DoD 採購更新或 NCSC 試點正面結果觸發）**：spread 全值行使 $5.00，獲利 $3.50/spread → 相對保費回報 ~2.3×，換算組合貢獻 ~+0.67% NAV
- **T2（融資成功 ≤20% 稀釋後重建 equity，目標 $35-40）**：Call spread 到期了結後視融資條件重新建立 equity 倉位；$22.90 → $40 對應 +75%，equity 倉位 ≤3% NAV 貢獻 ~+2.25% NAV

若 options 不可行，T1 / T2 上行機會主動放棄，維持 AVOID 至融資公告後重評。

---

NEUTRAL VIEW COMPLETE
