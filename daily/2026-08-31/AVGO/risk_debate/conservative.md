# Conservative risk view — AVGO

## Where trader is too aggressive

**倉位上限設定仍偏寬鬆。** 交易提案建議財報前 30-50% 目標倉位，但上限 50% 在二元事件前兩天仍屬過高。理由如下：

1. **價格數據全面缺失（PRICE_DATA_UNAVAILABLE）**：無法計算 ATR、設定有意義的 Stop，等同於在未知波動幅度下持倉。倉位大小必須對應已知風險，技術面完全盲區下應壓縮至保守端。
2. **EV/EBITDA 25-30x vs. 同業中位 18x**：估值溢價 40-65% 已預先定價正面情境。若財報任何一項指標令市場失望，估值壓縮空間巨大，高倍數股票在利空事件後的跌幅通常為低倍數股票的 1.5-2 倍。
3. **淨負債 $60-70B 疊加高估值**：去槓桿軌跡依賴 FCF 維持，任何 AI XPU 收入下修或 VMware ARR 衰退都將同時惡化財務槓桿與估值，形成雙重壓力。
4. **90 天內 52 筆內部人交易中 51 筆為賣出，Henry Samueli 近兩年套現約 $999M**：高層對現價保守訊號明確，歷史上大規模內部人賣出後三個月股價跑輸大盤的機率顯著偏高。

---

## Tail scenarios

- **Scenario A（機率 20-25%）**：Q3 FY2026 財報 AI XPU 收入未達 $16B 指引，且法說會管理層就 XPV $370B 或有負債迴避作答 → 估值雙殺，高倍數股票面臨快速重新定價，倉位損失可能達整體部位 20-30%，且因 PRICE_DATA_UNAVAILABLE 無預設 Stop 承接。

- **Scenario B（機率 15-20%）**：Google 在財報或法說會周邊公告進一步削減 AVGO XPU 採購量，轉移至自研第七代 TPU 或 MRVL 平台 → 「70% ASIC 市占率」敘事正式瓦解，客戶集中度（Google 佔 AI XPU 收入 > 50%）使衝擊無法被其他客戶快速替代，股價可能出現結構性折價。

- **Scenario C（機率 10-15%）**：VMware ARR 季度環比下滑超 5%（強制漲價 3-4 倍 + CVE-2026-59310 安全事件疊加），機構客戶遷移至 Nutanix / Red Hat 確認加速 → 雙引擎模型中軟體引擎熄火，FCF 能見度大幅下降，去槓桿計畫受阻，信用市場可能同步反應。

---

## Recommended adjustments

- **Size**：財報前最高 **30% 目標倉位（非 50%）**。PRICE_DATA_UNAVAILABLE 使 ATR-based sizing 完全失效，保守端才符合風控紀律。財報後依兩項入場條件達成情況再加倉至中倉（1.5% NAV）。
- **Stop**：因無價格數據，禁止設定名義停損位。但應設定**事件觸發型 Invalidation Stop**：法說會確認 XPV 信用事件 → 立即清倉；AI XPU 收入低於 $14B → 降至最小倉位。
- **Entry**：財報前勿新建完整倉位，現有小倉位持有至財報觀察即可，不追高。
- **Hedge**：考慮以 SOX index puts 或 MRVL/NVDA 相對強弱配對對沖 AI XPU 敘事失敗風險，降低組合對單一財報的集中暴露。

---

## Position-level $ risk

因 PRICE_DATA_UNAVAILABLE，無法計算公式 `(entry − stop) × shares = $ loss`。此為本倉位最核心的風控缺陷：**在不知道最大可能損失金額的情況下，任何超過 30% 目標倉位的建倉決策均屬風控紀律違反**。財報前缺乏技術支撐，下行幅度完全由基本面事件驅動，潛在單日跌幅可能遠超 ATR 預測區間。

---

## What I'd push for

財報前倉位上限壓至 **30% 目標倉位**，而非提案的 50%。XPV $370B 或有負債、Henry Samueli $999M 售股、Google 雙重身份威脅、以及 PRICE_DATA_UNAVAILABLE 導致的 Stop 缺失，四項因素疊加代表尾部風險密度遠超 MEDIUM 信心的標準配倉。2026-09-02 財報是唯一能同時驗證 AI XPU 成長韌性、XPV 風險邊界與 VMware ARR 黏性的事件視窗，在此之前以最小倉位等待確認訊號是正確的風控選擇。財報後若兩項入場條件均達成，再以 1-2 日分批方式擴充至中倉，避免在尾部事件前過度暴露。

---

CONSERVATIVE RISK COMPLETE
