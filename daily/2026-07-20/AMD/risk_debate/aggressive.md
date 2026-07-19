# Aggressive risk view — AMD

## Where trader is too cautious

- **完全空手 = 主動放棄不對稱報酬**：保守方以 EV/EBITDA 101.21x 及共識上行僅 +11% 為由拒絕建倉，但此框架是以「股票直接持有」衡量風險報酬，完全忽略 options 結構可將最大損失壓縮至 premium 本身的特性。在二元催化劑前一至兩個交易日持有 call spread，風險結構根本不同於持有正股。

- **等待 7/22 結果才入場 = 吃不到預期升溫的 momentum**：市場在大型發表活動前通常會逐步計入樂觀預期，若 Venice 確如宣稱達成 2nm 製程 1.7x 效能提升，重倉機構在事件前就會推高隱含波動率與股價。空手等到基準測試公開，期權 premium 已膨脹、正股也已反映，補追的入場成本必然更高。

- **止損邏輯的盲點**：保守方以「ATR 不可計算」為由迴避止損設定，但 call spread 本身即是預設上限損失的工具，無需依賴 ATR。以 PRICE_DATA_UNAVAILABLE 封殺 options 入場的論述缺乏邏輯一致性。

- **高管拋售作為唯一反向信號被過度放大**：$982.3M 拋售中相當比例源自 10b5-1 計劃（設定時機早於六月高位），用作「管理層認為估值見頂」的直接證據說服力不足。FCF +180% YoY、毛利率 53.1% 歷史新高、Rackspace 30 MW 落地協議，這些具體數字是拋售論述所刻意迴避的。

---

## Recommended adjustments

- **Size：0% → 1%（透過 call spread，以 premium 定義最大虧損）**
  理由：Venice 是本季最高優先催化劑，若基準測試使 ROCm 工作負載相容性出現突破，機構重新定價幅度可能遠超 +11% 共識上行。以 1% 組合規模買入 call spread，在最壞情況下（Venice 令人失望、正股下跌）損失上限即為 premium，不存在無限損失風險。

- **Entry：7/22 前 1–2 個交易日入場，而非等待事件後**
  理由：事件後若為正面結果，隱含波動率回落（vol crush）將大幅侵蝕 options 的 delta 收益；事件前建立 call spread 能在 IV 擴張期間鎖定較低購入成本。

- **Stop：call spread 最大損失 = 支付 premium 的 100%（組合 ~0.5–1%）**
  無需另設動態止損，結構本身即為風險邊界。

- **考慮：call spread（OTM，跨越 Venice + 8/4 財報雙催化劑）**
  到期日建議覆蓋 8/4 Q2 財報後（如 8 月第三週到期），捕捉兩組催化劑，避免僅押注 7/22 單一事件的 binary risk。具體行使價待 PRICE_DATA_UNAVAILABLE 解除後，依實際股價與 $640 Goldman 目標之距離設定 call spread 區間。

---

## Asymmetry argument

最壞情況最大虧損：組合約 **0.5–1%**（call spread premium 全損）。

現實上行情境：若 Venice Zen 6 基準測試大幅超越 NVIDIA 同級產品，並於 8/4 財報數據中心指引高於預期，AMD 股價從當前水準向 Goldman 目標 $640 靠攏，call spread 可產生 **3x–5x premium 回報**（視行使價結構而定）。

**R:R 估算：上行 ~$3–5 / 下行 ~$1（即 3:1 至 5:1）**

保守方引用的 +11% 對 -22% ~ -47% 不對稱，是正股持有者的風險框架；options call spread 持有者的 R:R 結構完全不同，最大損失已被 premium 封頂，而正股持有者的下行空間依然無上限。

---

## What I'd push for

在 7/22 前 1–2 個交易日，以 **組合 1% 資金買入涵蓋 8/4 財報的 OTM call spread**（到期日選 8 月第三週）。最大損失鎖定於 premium（約組合 0.5–1%），換取對 Venice 超預期 + 財報雙催化劑的非線性上行暴露。保守方的「等待確認再入場」邏輯看似穩健，實質上是在 R:R 最差的時機（vol crush 後、正股已反映）才允許入場，這是風險管理的倒置。以 call spread 的有限損失特性介入 7/22 前，才是本次催化劑窗口中正確的風險框架。

---

RISK-AGGRESSIVE COMPLETE
