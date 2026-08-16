# Neutral risk view — S (SentinelOne)

## Points of agreement（雙方共識）
- 2026-08-27 Q3 FY2026 財報是近期唯一有效的方向確認錨點；四項觸發條件（ARR 年增率 ≥ 25%、淨新增 ARR > $55M、指引維持上限 $1.020B、Purple AI 採納率 > 40%）雙方均認可
- Call spread 結構優於裸股跨財報——用權利金天然封頂最大損失，在 PRICE_DATA_UNAVAILABLE 環境下解決傳統止損無法設定的問題；雙方都提到此工具
- MEDIUM 信念 + 財報前擁擠倉位 → 財報前倉位應小於標準配置，財報後依結果決定是否擴倉

## Aggressive overreach
- **訊號誤讀：** Call:Put 23:1 被單向詮釋為「知情資金建多頭」，屬反射性樂觀偏誤。此比率同樣可解釋為零售追漲造成的擁擠，兩種情境歷史均有案可查，無法單向定性。
- **倉位過重、時機論點誇大：** 在 MEDIUM 信念、報價缺失、gamma 風險三項同時成立下，立即建 1.5-2.0% NAV 過激。「等財報就失去全部 alpha」忽略了 1-3 個月時間框架下財報後進場仍有充足騎乘空間。

## Conservative overreach
- **零倉位等於放棄工具：** 若以 call spread 進場，最大損失已等於權利金，「無止損 = 無限暴露」的前提不再成立；「財報前完全不建倉」是用倉位放棄解決本可用結構解決的風險。
- **CEO 賣股訊號過重：** 稅務預扣性出售在缺乏主動賣出意圖佐證的情況下，被定性為強力空頭訊號，結論力度超過證據所支持的程度。

## Balanced adjustment proposal
- **Size：** 0.5% NAV，全部以 bull call spread 表達（到期 2026-09-19），財報前不持裸股；財報後若任意三條觸發條件達標，加碼至 1.0-1.5% NAV（含股票現貨）；若觸發條件均未達標，不展期、不加碼
- **Stop：** call spread 權利金即最大損失上限，無需傳統止損價格；無 PRICE_DATA_UNAVAILABLE 之限制
- **Entry：** 財報前建立 0.5% NAV call spread（行使價待即時報價恢復後確認，PRICE_DATA_UNAVAILABLE 下不填推測數字）；財報後第 48 小時 gamma 賣壓充分釋放後再決定加碼
- **Hedge：** call spread 結構本身即上行參與 + 下行封頂；IV > 60% 環境下另加 put 對沖成本過高，不建議疊加
- **Time horizon：** 1-3 個月（以季度為單位）

## Net $ risk if stop hits
以 $1M NAV 為例：0.5% NAV call spread 權利金 = **$5,000 最大損失**（= NAV 0.5%）

## Net $ upside at T1 / T2
財報超預期情境（ARR 重新加速至 25%+、Purple AI 商業化確認）：
- **T1**（call spread 全額兌現）：**$15,000-$25,000**（= 1.5-2.5% NAV；R:R 約 3:1-5:1）
- **T2**（擴倉後持有至 FY2027 指引確認）：加碼至 1.5% NAV 後上行 20% 情境 → **額外 $30,000**（= 3.0% NAV）

NEUTRAL VIEW COMPLETE
