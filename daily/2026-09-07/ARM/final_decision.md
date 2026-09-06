FINAL TRANSACTION PROPOSAL: **SELL**

# Final decision — ARM as of 2026-09-07

## FINAL TRANSACTION PROPOSAL: **SELL**

## Verdict
MODIFY

## Final trade card (if not REJECT)

> **PRICE_DATA_UNAVAILABLE — Yahoo Finance 遭封鎖 (403)，以下所有價位均來自研究文本與分析師目標，非即時報價。無即時價格，暫不給進出場價位；下表數值為研究參考值，不可直接掛單執行。**

| Field | Value |
|---|---|
| Direction | SHORT（以 defined-risk 結構表達，非裸空現股） |
| Structure | Bear Put Spread：Buy $440P / Sell $300P，到期 2026-12-19 |
| Entry zone | 無即時價格，暫不給進出場價位（研究參考現價 $461，非可執行） |
| Stop | 無即時價格，暫不給進出場價位。結構性停損 = 100% 權利金；論點停損見下方失效條件 |
| Target 1 | $286（研究參考值：39 位分析師共識目標，約 -38%） |
| Target 2 | $212（研究參考值：Morgan Stanley 最保守目標，約 -54%） |
| Size | Small — **0.35% NAV** 起始；催化劑確認後可加至 0.70% NAV |
| Horizon | 3–4 個月（涵蓋 2026-11 業績與 FTC 窗口） |
| Conviction | **MEDIUM** |
| R:R to T1 | 約 4.5:1（依 Neutral 之權利金 $25–$30 推估，須以實際 IV 重算） |

**執行前置條件（強制）**：須先自 broker feed 或 Bloomberg 取得現價與 $440P/$300P 的 IV 報價，確認權利金 ≤ 淨價差寬度的 25%。未取得報價前，部位掛 0，不得憑研究價位下單。

## Risk debate adjudication
- Aggressive's strongest point：三項可查信號（內部人士 90 天 20 筆全數賣出、NVIDIA 完全清倉並轉為競爭者、FTC 已於 2026-05 立案）已同時成立，等到 2026-11 業績才動作等於把最好的 R:R 窗口讓出去；且以 Put Spread 取代裸空，正確地解決了軋空問題。
- Conservative's strongest point：無即時報價即無法驗證 ATR 與停損，SoftBank 持有 86.4%、流通盤稀薄，裸空的尾部損失無界。
- Net：我採納 **neutral** 的權重。保守方的軋空論證針對的是裸空，套用到最大損失已封頂於權利金的 Put Spread 上屬論證錯位；但它對「定價無法驗證」的批評成立，故我保留其精神——不是歸零，而是把「取得報價確認」設為硬性前置條件，並把起始規模壓到 0.35%（低於激進的 0.75%、也低於中立的 0.40%）。

## 為何 MODIFY 而非直接核准交易員提案
交易員提出 HOLD／等待四項觸發之一，等同放棄已成立的信號組合；但激進方的「立即 0.75%」又忽略期權定價無法驗證。我改為：方向採納空方（SELL），工具採 Bear Put Spread，規模減半，並加上報價確認的執行閘門。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 估值無先例 | P/S 顯著高於 NVIDIA 歷史峰值 ~40x | P/S 67x、GAAP P/E 288x，共識目標低 38% | 成立 |
| 內部人士與策略股東用腳投票 | 出現賣出集中 | 90 天 20 筆全數賣出、淨 $26M+、買進為零；NVIDIA 2026-02 清倉 | 成立 |
| 監管尾端風險未定價 | FTC／KFTC 產生實質壓力 | 雙調查並行，尚無裁決 | 觀察中 |
| 資料中心版稅動能將減速 | FY2027 H2 增速滑落至 +30–50% | 目前 +100% YoY，尚未驗證 | 觀察中 |

## 論點失效條件
- 若 FTC 正式結案且公告無任何實質制裁，監管支柱失效 → 出場（平倉 Spread）
- 若 2026-11 Q1 FY2027 資料中心版稅 YoY ≥ +80%，減速支柱失效 → 出場
- 若 CEO 或 CFO 出現任何公開市場買進的 SEC Form 4，內部人士支柱失效 → 減碼一半
- 若股價連續兩個交易日收在 $520 以上（研究參考值），承認動能主導 → 減碼一半，不等權利金歸零

## Monitoring trigger
若 SoftBank 季報揭露減持、或 FTC 發出強制措施／業務剝離通知，於權利金到期前重評並考慮加碼至 0.70% NAV。

## Key risks
Fed 寬鬆使高倍數股再擴張、業績超預期觸發回補、期權以不利 IV 建倉、2026-12-19 到期前論點未兌現導致時間價值全損。

## Catalyst calendar
- 2026-11 — ARM Q1 FY2027 業績（資料中心版稅分部增速）
- 2026-11 — KFTC 初步裁決窗口
- 2026-Q4 持續 — FTC 進展、SoftBank 持股披露、SEC Form 4
- 2026-12-19 — Put Spread 到期

FINAL DECISION COMPLETE
