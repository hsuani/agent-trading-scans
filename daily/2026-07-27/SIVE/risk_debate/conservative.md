# Conservative risk view — SIVE

## Where trader is too aggressive

交易員並未過度積極——AVOID 0% NAV 是正確的。唯一需要壓力測試的是提案中「若借券可得，最多 Small（< 0.5% NAV）做空」的附帶選項。此選項實際上仍有顯著尾部風險：

- **軋空尾部不對稱**：52 週區間 2.85–110 SEK，年化波動率極高。若 Q2 報告（2026-08-27）意外披露具名 CPO 客戶及訂單金額，股價可在一個交易日內翻倍；< 0.5% NAV 的 SHORT 倉位名義損失上限難以預設。
- **流動性懲罰**：Nasdaq Stockholm 小市值，OTC SIVEF 無機構持倉，買賣價差在壓力情境下可大幅擴張，平倉成本不可控。
- **PRICE_DATA_UNAVAILABLE**：無法計算 ATR、R:R 或正確的 vol-adjusted 倉位規模，在此資訊缺口下任何 SHORT 嘗試本質上屬盲目操作。

## Tail scenarios

- **情境 A（機率 15%）：Q2 報告披露具名 CPO 訂單** → 股價向 52 週高點 SEK 110 靠攏（+233% vs ~33 SEK）；SHORT 倉位在帳戶規則允許下遭強制平倉，損失超過倉位面值。AVOID 狀態損失 = SEK 0。
- **情境 B（機率 50%）：Q2 收入再度年減，無訂單確認** → 股價向分析師平均目標 SEK 6.87 下行（-79%）；AVOID 的機會成本為零，若有 SHORT 則可獲利，但執行障礙前已述。
- **情境 C（機率 20%）：總體市場 Fed 衝擊或全球風險規避** → 小市值高波動股通常跌幅超過大盤，SIVE 作為無獲利、無機構持股標的，流動性將進一步蒸發；AVOID 正確。
- **情境 D（機率 15%）：NVIDIA 直接宣佈採購意向或 design win** → 敘事完全翻轉，現價 ~33 SEK 反成低估；AVOID 的機會成本真實存在，但信心度 60% 不足以承擔反向風險。

## Recommended adjustments

- **Size**：0% NAV — 維持，正確。
- **Stop**：不適用（無倉位）。
- **Entry**：等待 2026-08-27 Q2 報告後重新評估，屆時具備可驗證的訂單數字與更新後的 R:R。
- **Consider**：不建議用 index puts 對沖一個已為零持倉的標的，對沖成本徒增摩擦。

## Position-level $ risk

倉位 = 0 股，止損不適用。$ loss if stop hits = **SEK 0 = 0% NAV**。可接受性：完全可接受——在 PRICE_DATA_UNAVAILABLE、分析師目標較現價折讓 79%、借券條件未確認的三重限制下，0% NAV 是風險管理的正確輸出，而非被動保守。

## What I'd push for

維持 AVOID 0% NAV，拒絕在 Q2 報告前嘗試任何 SHORT。核心理由：PRICE_DATA_UNAVAILABLE 使 vol-adjusted sizing 不可能完成；借券池未確認；60% 信心度低於小市值軋空所需門檻。2026-08-27 Q2 報告是唯一正確的重估節點——若 CPO 訂單確認缺席且收入再度年減，再以確認價格資料計算 R:R 後，才考慮以 < 0.5% NAV 的嚴格上限試探 SHORT。現階段任何倉位行動均屬多餘風險。

CONSERVATIVE RISK COMPLETE
