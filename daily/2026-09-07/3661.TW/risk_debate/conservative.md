# Conservative risk view — 3661.TW (世芯-KY)

> 所有涉及絕對價格之數字均受 PRICE_DATA_UNAVAILABLE 限制（Yahoo Finance 403 封鎖），僅為估值模型推算值，執行前須以券商即時報價核實。

---

## Where trader is too aggressive

- **基本面資料殘缺，不宜以 0.5% NAV 定錨**：毛利率、FCF、應收帳款週期均為 DATA_UNAVAILABLE。在核心盈利品質數據不可驗證的情況下，任何以 EPS 為基礎的目標價（T1 NTD 4,210、T2 NTD 5,205，均為 PRICE_DATA_UNAVAILABLE）都建立在估計值之上，再加一層定價不確定性。此情境最多只能支持「試探性探路倉」，不支持標準半倉。
- **YoY -18.7% 與 QoQ +82.6% 並存，Lumpiness 風險極高**：季環比暴漲後的下一季極可能是 NRE 費用認列高峰。交易員已承認這是核心爭議，卻仍以 0.5% NAV 入場，等於在「多空最大不確定點」下注，尚無 Q3 數據支撐。
- **Stop 過寬，缺口穿越風險真實**：以入場區間頂部 NTD 3,600（PRICE_DATA_UNAVAILABLE）計算，Stop NTD 2,900（PRICE_DATA_UNAVAILABLE）距入場頂端達 -19.4%。若 Q3 財報公布當晚負面驚訝，台股隔日跳空開低完全可能直接穿越 NTD 2,900，止損無法以市價完整執行，實際損失將更大。
- **Amazon 單一客戶集中度 51%，屬二元事件風險**：任何一則關於 Amazon 擴大 Marvell 份額或 Trainium CapEx 削減的消息，均足以使股價單日下挫超過 stop 幅度，現行倉位無法對沖。

---

## Tail scenarios

| 情境 | 發生機率估計 | 觸發事件 | 可能下跌至（PRICE_DATA_UNAVAILABLE） | 損失（0.5% NAV 倉位，以中位入場 NTD 3,500 計） |
|------|------------|---------|-----------------------------------|--------------------------------------------|
| **A：Q3 財報 NRE 遞減確認** | ~25% | Q3 季環比下滑＋管理層下修全年指引 | NTD 2,400–2,600（20–22x × 下修 EPS ~NTD 110，PRICE_DATA_UNAVAILABLE） | 跌至 stop NTD 2,900 = -17.1%；若跳空穿越至 NTD 2,500 = -28.6%，即 0.143% NAV |
| **B：Amazon 客戶分散化衝擊** | ~15% | Amazon 公告擴大 Marvell 比例或延後 Trainium 3 部署 | NTD 2,200–2,500（反映 51% 營收急速重新定價，PRICE_DATA_UNAVAILABLE） | 穿越 stop，實際損失可達 -37%，約 0.185% NAV |
| **C：台灣地緣政治或 Fed 鷹派衝擊** | ~10% | 美中台緊張升溫 / FOMC 超預期升息 | TWSE 半導體股普跌 20%+，NTD 2,700–2,900（PRICE_DATA_UNAVAILABLE） | 接近或穿越 stop，損失集中在 1-2 個交易日 |
| **D：CoWoS 產能惡化** | ~15% | TSMC 先進封裝缺口擴大至滿足率 <50% | NTD 3,000–3,200（PRICE_DATA_UNAVAILABLE），交期延後壓縮 Q3 收入認列 | 逼近 stop 但未必穿越；損失 0.043–0.064% NAV |

---

## Recommended adjustments

- **Size**：Small（0.5% NAV）→ **XSmall（0.25% NAV）**
  - 理由：基本面 DATA_UNAVAILABLE + Lumpiness 極值 + 缺口穿越風險三重疊加，不支持標準半倉。0.25% 為「確認前的探路票」。
- **Stop**：NTD 2,900（PRICE_DATA_UNAVAILABLE）→ **NTD 3,100（PRICE_DATA_UNAVAILABLE）**
  - 從入場中位 NTD 3,500 計，風險從 600 NTD / 股（-17.1%）收窄至 400 NTD / 股（-11.4%）；此水位仍低於 24x × EPS NTD 130.48 估值支撐，結構上有邏輯依據，但能在 Q3 財報跳空前更快清倉。
- **Entry**：不在 NTD 3,400–3,600（PRICE_DATA_UNAVAILABLE）全額建倉；以 0.25% NAV 建立初始倉位，嚴守等待 Q3 財報確認再決定是否加倉至 0.75–1.0%。
- **Consider**：若倉位建立後，可考慮對沖元件——買入 Philadelphia Semiconductor Index（SOX）近月輕虛值 put，或持有台灣 ETF 反向部位以對沖系統性風險；Amazon（AMZN）大幅下跌亦將同步壓制世芯，可監控 AMZN 期權隱含波動率作為前置警示。

---

## Position-level $ risk

| 情境 | 倉位 | 入場（PRICE_DATA_UNAVAILABLE） | Stop（PRICE_DATA_UNAVAILABLE） | 每股損失 | 組合損失 |
|------|------|------|------|------|------|
| 交易員方案（0.5% NAV，止損執行完整） | 0.5% NAV | NTD 3,500 中位 | NTD 2,900 | NTD 600（-17.1%） | ≈ 0.086% NAV |
| 交易員方案（0.5% NAV，跳空穿越至 NTD 2,500） | 0.5% NAV | NTD 3,500 | NTD 2,500 | NTD 1,000（-28.6%） | ≈ 0.143% NAV |
| **保守方案（0.25% NAV，止損收緊至 NTD 3,100）** | **0.25% NAV** | NTD 3,500 | **NTD 3,100** | NTD 400（-11.4%） | **≈ 0.029% NAV** |

**判斷**：交易員原方案若止損正常執行，0.086% NAV 損失本身尚在合理範圍；但跳空穿越情境下 0.143% NAV 為單筆過重，且本案已明確存在「財報夜跳空」風險。保守方案 0.029% NAV 最大損失，為 Q3 不確定性解除前的適當代價。

---

## What I'd push for

在 Q3 財報（2026 年 10 月中旬）公布前，僅建立 **0.25% NAV 探路倉**，入場於 NTD 3,400–3,500（PRICE_DATA_UNAVAILABLE）區間低端，並將 Stop 設於 NTD 3,100（PRICE_DATA_UNAVAILABLE）而非 NTD 2,900；這使缺口穿越損失上限壓縮至 0.029% NAV，同時維持 R:R to T1 仍約 1.5x（(4,210 − 3,450) ÷ (3,450 − 3,100) ≈ 2.2x，均為 PRICE_DATA_UNAVAILABLE 估算）。若 Q3 財報確認季創新高且毛利率 ≥50%，再加倉至 0.75–1.0% NAV；若財報不及預期或 Amazon 動態惡化，則因初始倉位僅 0.25%，損失可控且心理壓力低，能冷靜執行止損。核心主張：**在毛利率 / FCF 等基本面資料 DATA_UNAVAILABLE 的狀態下，0.5% NAV 是「以估計值為事實」的倉位，0.25% NAV 才是與當前資訊品質相稱的部位規模。**

---

RISK-CONSERVATIVE COMPLETE
