FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — AMD as of 2026-11-02

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
REJECT

## 持倉狀態
AMD 不在 `pipeline/tools/held_tickers.txt`，屬新倉評估。問題是「該不該進」，答案是：財報前不進。

## Dealbreaker
Q3 財報在 11/3（下一個交易日）公布，選擇權隱含波動約 ±7%，而 10/30 已出現 -10.9%、2 倍均量的異常下跌且原因未明。這代表實際跳動可能超過隱含值，且事件勝率無法從現有資料估出。本流程要求 R:R 可計算、Stop 可定義；財報跳空可直接穿越任何價格停損，兩個前提都不成立。這不是看空，是「資訊將在 24–48 小時內落地，等它出來的期望值較高」。

不採用 aggressive 的 $520/$560 call spread：其 B/A ≈ 3–4x 沒有實際 IV 與 skew 報價佐證，而財報前 IV 偏高，IV crush 會吃掉大部分理論 payoff。基本面證據較紮實不等於二元事件勝率較高，兩者不能混用。

## Risk debate adjudication
- Aggressive's strongest point：等「收盤站回 MA50 $548」才轉多，會放掉 $504.8 到 $548 這段 8.5% 的 alpha。這點成立，但代價是用未知勝率換取已知上檔，不划算。
- Conservative's strongest point：forward EPS 15.94 與 TIKR NTM EPS 約 11 的落差，意味市場已預先消化大量未證實的 MI450 貢獻。若 Q4 指引不夠具體，估值重定價是跳空式的，$492.21 這條線保護不了。
- Net：我偏向 **neutral**。Neutral 正確指出 aggressive 把論點強度與事件風險混為一談，也正確指出 conservative 的 1 ATR 停損在 67% 年化波動的個股上會被雜訊打掉。財報後若重啟，停損採 1.5 ATR、縮小股數控風險，是合理的中間值。

## 論點支柱（供財報後重啟用）
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 資料中心成長動能 | Q3 營收 ≥$13.3B（指引上緣）、Data Center 分部維持高雙位數 YoY | Q2'26 營收 +50.1% YoY，Q3 指引約 $13.0B，待 11/3 驗證 | 觀察中 |
| MI450/Helios 開始貢獻營收 | Q4 指引明確量化 MI450 營收，支撐 forward EPS 15.94 | Meta 1B 為非約束性承諾，無實際錢包份額資料 | 觀察中 |
| 毛利率結構改善 | 非 GAAP 毛利率 ≥56% | Q2'26 為 53.8%（+14.0pt），Q3 指引約 56% | 觀察中 |
| 長期趨勢未破壞 | MA20>MA50>MA200 排列維持，收盤守住 $492.21 | 排列未破，但 10/6 起 lower highs/lows，MACD hist -5.02 擴大 | 觀察中 |

四根支柱全部處於觀察中，沒有一根已被財報驗證，這本身就是不建倉的理由。

## 論點失效條件
與 Stop 分開；以下是論點紀律，財報後觸發即不重啟多方評估。
- 若 Q3 營收低於 $12.8B 或非 GAAP 毛利率低於 55%，「成長動能」與「毛利率」支柱失效 → 不進多單，改評估偏空。
- 若 Q4 指引未給出 MI450/Helios 量化貢獻，或管理層提及 CoWoS/HBM 供應限制導致時程延後，「MI450」支柱失效 → 不進多單，forward P/E 31.7x 失去基礎。
- 若 10/30 下跌被證實為個股事件（訂單取消、客戶轉單、指引外流），「趨勢」支柱失效 → 轉 SHORT_OR_AVOID 評估。
- 若連續兩季 Data Center 分部營收 YoY 低於 30%，整個 forward EPS 翻倍的敘事失效 → 長期觀察名單移除。

## Monitoring trigger
財報後 2–3 個交易日內重新評估，不追早盤跳空：
- 轉 LONG（MEDIUM）：上述四根支柱至少三根轉為成立，且收盤站回 MA50 $548。初始半倉，Stop 1.5 ATR（約 $44），單筆 NAV 風險壓在 1–2%，T2 看 $600。
- 轉 SHORT_OR_AVOID：收盤跌破 $492.21，下看 $470 再看 $440.50。小倉位，不追空到 MA200。
- 若財報延後公布，本 REJECT 持續有效。

## Catalyst calendar
- 2026-11-03 — Q3 財報與 Q4 指引（核心事件）
- 2026-11-17–18 — NVDA 財報（同業情緒檢查點）
- 2026-12-09 — FOMC（宏觀情緒檢查點）

FINAL DECISION COMPLETE
