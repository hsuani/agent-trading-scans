# Neutral risk view — PWR

## Points of agreement (both sides)

- PRICE_DATA_UNAVAILABLE 狀態下，精確 stop 無法定錨，任何倉位決策均須附帶「取得即時報價後方執行」的前置條件——雙方均認可此約束。
- AECOM $337M 固定價格先例構成真實的執行風險黃旗，不得忽略；Q3 財報（約 11 月初）是核心驗證節點，雙方一致。
- 內線 12 個月淨賣出 $17M、買入 $0，屬可查核的結構性負面訊號，需列入持倉監控紅線。
- Investment plan MEDIUM conviction 已排除滿倉（3% NAV），雙方皆不主張以高信念等級入場。

## Aggressive overreach

- **立即全倉 2.5% NAV**：在 PRICE_DATA_UNAVAILABLE 且 conviction 僅 MEDIUM 的條件下，無 stop 定錨即建完整大倉，違反基本風險紀律。MEDIUM conviction 對應投資計畫「半倉至七成倉」指引，2.5% NAV 已超標。
- **PEG 0.58 過度樂觀**：PEG 假設當期高增長率可持續，但 EPS +71% 含有大型合約集中兌現的時點性因素，以此直接論證估值低廉且支持加倉缺乏穩健性。
- **call spread 配置**：核心進場條件（price、stop、ATR）全部缺失時，疊加選擇權策略複雜度只會放大不確定性，並非此時段合理建議。

## Conservative overreach

- **強制等待技術確認才允許任何建倉**：$53B backlog 為已簽約合約數字，非敘事；基本面論點的有效性不依賴技術支撐突破。以 RSI 形態作為入場前置條件，對基本面主導的論點附加了不相干的技術過濾器。
- **R:R < 0.5 論定倒掛**：-30~40% 下行是熊方情境概率加權值，並非確定損失；在無進場價的條件下，以情境損失替代 R:R 計算，誇大了倒掛程度。0.75% NAV 過於保守，與 MEDIUM conviction 等級不匹配。

## Balanced adjustment proposal

| 項目 | 均衡建議 | 理由 |
|------|----------|------|
| Size | **1.0% NAV**（單一批次） | 介於原提案 1.5% 與保守 0.75% 之間；符合 MEDIUM conviction「半倉」指引，PRICE_DATA_UNAVAILABLE 下降低盲目暴露 |
| Stop | 取得報價後設於進場價 **-10%**（hard stop，執行前置條件） | 給予估值波動空間，同時不像 aggressive 的 -12% 過於寬鬆；PRICE_DATA_UNAVAILABLE 解除前禁止建倉 |
| Entry | 取得即時報價後**單筆執行**，不設 Fed 例會自動觸發 | 去除宏觀事件驅動的盲目進場；但不要求 RSI 技術過濾，基本面論點已充分支持入場方向 |
| Hedge | 小規模 PWR OTM put（約倉位名義值 **0.5%**）對沖 AECOM 式執行尾部風險 | 比 XLI put spread 更精準；比 aggressive call spread 更保守且符合當前資訊缺口 |
| Time horizon | **1–3 個月**，核心驗證點為 Q3 財報（約 11 月初） | 雙方一致，不爭議 |

## Net $ risk if stop hits

stop 設 -10%，倉位 1.0% NAV：**損失 = 0.10% NAV**
熊方情境（-35%，機率 15%）：損失 = **0.35% NAV**

## Net $ upside at T1 / T2

- **T1**（分析師均值目標 +14%）：**+0.14% NAV**
- **T2**（Q3 財報驗證後再評價 +22%）：**+0.22% NAV**

> 注意：因 PRICE_DATA_UNAVAILABLE，所有美元金額以 NAV 百分比呈現；取得即時報價後應換算為絕對美元金額驗證。

NEUTRAL RISK COMPLETE
