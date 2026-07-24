# Conservative risk view — 2449.TW (京元電子)

## Where trader is too aggressive

- **≤0.5% NAV 財報前仍屬過大**：提案允許在 Q2 財報（2026-07-31）前維持最多 0.5% NAV 殘倉，但財報前 6 個交易日的 R:R 極度不對稱。0.5% NAV 看似微小，但若下行觸發 NT$150 熊市目標（現價約 -59% 估算），殘倉損失仍佔 NAV 約 0.3%，在毫無 Stop 可量化的情況下屬不必要的風險敞口。
- **PRICE_DATA_UNAVAILABLE = Stop 完全失能**：技術層面無法設定基於 ATR 的 Stop，等同於持倉在財報前處於「裸露」狀態，任何跳空缺口都無法防禦。
- **P/E 36–40x 無安全邊際**：OSAT 同業（ASE、Amkor）forward P/E 12–20x，當前溢價 80–120%。多頭論文需三個條件同時成立（AI 需求不中斷 + 新廠準時投產 + 毛利率擴張），任一落差即引發 P/E 向同業收斂的多重壓縮，下行幅度遠超上行空間。
- **分析師共識過度一致放大反轉風險**：12/14 買進、0 賣出，若 Q2 EPS 再次 YoY 大幅負成長，首筆降評將引發連鎖評等下修，機構賣壓邊際效應遠大於升評買盤。

## Tail scenarios

- **Scenario A（機率約 35%）：Q2 毛利率 <30%、EPS YoY 持續大幅負成長** → 多重壓縮觸發，P/E 向 OSAT 同業 15–20x 收斂，股價下行 40–59%；若持倉 0.5% NAV，損失約 0.2–0.3% NAV。
- **Scenario B（機率約 20%）：NVIDIA H2 2026 採購指引下修** → AI 測試訂單能見度惡化，客戶集中度（估計 70–77%）放大衝擊，季營收雙位數下滑，折舊浪潮（NT$50B CapEx）同步壓縮 EPS，股價可測試 NT$150 熊市目標。
- **Scenario C（機率約 15%）：苗栗/楊梅新廠延後至 2027 Q2 以後** → CapEx 效益遞延但折舊已提前認列，EPS 受雙重壓縮（利潤率收縮 × 折舊暴增），FCF 缺口擴大，股息進一步削減風險上升。

## Recommended adjustments

- **Size：≤0.5% NAV → 0% NAV（財報前）**；理由：PRICE_DATA_UNAVAILABLE 致 ATR Stop 失能，Q2 財報黑盒風險不值得承擔任何殘倉。
- **Stop：無法量化**；財報後若重建部位，須等候 2–3 個交易日價格穩定後方可設定 ATR-based Stop（建議 1.5× ATR）。
- **Entry：財報後確認進場**；觸發條件：Q2 毛利率 ≥38% 且 EPS YoY 轉正，外資法說會後淨買超確認，方可建立 ≤1.0% NAV 試探性多頭。
- **避險選項**：考慮以 ASE（3711.TW）或 Amkor（AMKR）作為相對強弱參照；若持有台灣科技股集中部位，可評估 TAIEX 指數型工具對沖系統性風險。

## Position-level $ risk

PRICE_DATA_UNAVAILABLE，無法計算 `(entry − stop) × shares` 的絕對金額。以 NAV 比例估算：若維持 0.5% NAV 且 Scenario A 發生（下行 -45%），實現損失約 **0.225% NAV**。表面可接受，但此為**毫無 Stop 防護、財報前裸露敞口**，等同於在賭局桌上押注而非執行有紀律的交易，不符合風險管理標準。

## What I'd push for

在 Q2 財報（2026-07-31）公布前，應將 2449.TW 部位降至 **0% NAV**，完全迴避財報跳空風險。理由不是看空，而是：PRICE_DATA_UNAVAILABLE 使技術 Stop 失能；Q1 EPS YoY -47% 顯示 NT$50B CapEx 折舊壓力尚未見頂；P/E 36–40x 相對 OSAT 同業高溢價 80–120%，下行非對稱性極大；分析師共識一致性反而放大降評連鎖風險。財報後若毛利率 ≥38%、EPS YoY 轉正，再以 ≤1.0% NAV 建立有 Stop 保護的試探性部位，執行紀律遠優於現在承擔不必要的裸露風險。

CONSERVATIVE VIEW COMPLETE
