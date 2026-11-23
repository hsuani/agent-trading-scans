# RGTI (Rigetti Computing) 新聞分析

- 日期：2026-11-24
- 角色：news-analyst（TradingAgents pipeline）
- 資料窗口：約 2026-10-25 至 2026-11-23（搜尋工具僅能取得至今日 2026-11-23 之前的資料）
- 方法：WebSearch 多輪查詢；未使用 WebFetch。部分來源彼此矛盾，已於各節標註。

## 淨情緒判斷

**偏空（Bearish / 中度偏空）**

主要理由：
1. Q3 2026 營收 $1.4M，年減約 27-28%，遠低於市場預期；FY2026 約 $20M 指引依賴 Q4 由 C-DAC 客戶驗收，需要約 $9M 的單季營收，達成風險高。
2. 股價接近 52 週低點（約 $7.08），近一年跌幅約 70%；Jefferies 將目標價由 $18 下調至 $12。
3. 內部人士近期減持（CFO 約 $31K，COO 約 $72K，2026-11-20 前後）。
4. 估值（P/S 約 1,000 倍以上，依 Motley Fool 2026-11-10 收盤資料）與營收基本面脫節。

正面因素（部分抵銷）：
- 108-qubit Cepheus-1-108Q 達成 99.5% median two-qubit gate fidelity，符合既定里程碑。
- 美國商務部 CHIPS R&D 最高 $100M 協議（2026-09 簽署），並取得政府少數非控股股權。
- 現金及可供出售投資約 $497.1M（2026-09-30），無債務負擔（依公司披露），短期無立即流動性壓力。

## 1. 公司基本面與財報（近 30 天）

| 日期 | 事件 | 重點 | 情緒 |
|---|---|---|---|
| 2026-11-10 (盤後) / 11-11 報導 | Q3 2026 財報 | 營收 $1.4M（去年同期 $1.95M）；9M 營收 $10.9M（去年同期 $5.2M）；營業虧損 $33.2M；現金及投資 $497.1M；FY26 指引約 $20M，依賴 C-DAC 驗收 | 負面 |
| 2026-11-10/11 | 分析師動作 | Jefferies 目標價 $18 → $12；TipRanks 指出 FY26 營收指引 $20M，低於共識 $22.9M | 負面 |
| 2026-11-20 ~ 11-21 | 內部人士減持 | CFO Jeffrey Bertelsen 約 $31K；COO Rivas 約 $72K | 偏負面（金額小，但方向一致） |
| 2026-11 初 | 應用合作 | Rigetti 硬體支援 FirstQFM 量子儲備計算（reservoir computing）金融預測系統 | 中性偏正 |

**注意**：各來源對 Q3 營收「未達預期」的幅度說法不一（有來源稱 $1.41M 對比 $3.67M 預期；另有來源稱約比 $4M 估計低約 60%）。請以 8-K 或新聞稿原文為準。

## 2. 政府 / 國防 / 合約

| 日期 | 事件 | 狀態 | 情緒 |
|---|---|---|---|
| 2026-09-08 | 美國商務部 CHIPS R&D 最高 $100M 最終協議（LOI 已於 2026-05-21 簽署） | 已簽署定案；政府取得少數非控股股權 | 正面（但有稀釋/股權讓渡含義） |
| 日期不明 | AFRL（美國空軍研究實驗室）3 年期 $5.8M 合約，與 QphoX 合作超導量子網路 | 來源未顯示日期，需確認 | 正面（規模小） |
| 日期不明（疑為舊聞） | DARPA ONISQ 相關最高 $8.6M（與 NASA Quantum AI 合作）；DARPA 量子應用基準測試合約 | 日期無法確認，可能為舊聞，**非 2026 新增 DARPA 合約** | 中性 |

## 3. 技術里程碑與路線圖

- **已達成**：Cepheus-1-108Q 於 Q3 2026 達 99.5% median 2Q gate fidelity；80 qubit sublattice 達 99.6%，50 qubit sublattice 達 99.7%。2026-04 GA 時為 99.1%、約 60 ns 門速。
- **路線圖調整（重要）**：原定 2026-12 達到「>150 qubit、約 99.7% fidelity」的目標已實質被取代，新目標為 **mid-2028 達 300+ qubit、約 99.7% fidelity、sub-60 ns 門速**。這代表短期技術催化劑減少。
- **長期目標**：約三年內達 ~1,000 qubit、99.9% fidelity、<50 ns 門速（公司目標，非保證）。
- **衡量標準**：2026 年下半年的技術進展已部分兌現，但路線圖延後會削弱短線多頭敘事。

## 4. 資本募集 / 稀釋風險

- 已知機制：$350M ATM（at-the-market）計畫（Jefferies 為銷售代理），來源對「是否已全數使用」說法不一：
  - 部分來源（2025-06 / 2025-11）稱已完成 $350M 銷售，公司總現金與投資約 $575M。
  - 2026 年一篇文章稱市場仍對「$350M ATM 稀釋」有疑慮，股價因此下跌約 3.8% 至 $17.31（此數字與目前股價區間明顯不符，可信度低）。
- 未找到 2026 年新的股權募集公告（新 ATM、S-3、登記直售）。
- **建議查核**：SEC EDGAR 近 90 天的 8-K、S-3、424B 文件，以確認是否有新的 ATM 或稀釋工具。
- 政府 CHIPS 協議可能包含股權條款，需檢視是否有稀釋或權證安排。

## 5. 競爭對手動向（IonQ / D-Wave / IBM）

| 日期 | 公司 | 事件 | 對 RGTI 的含義 |
|---|---|---|---|
| 2026-11-05 | IonQ | 財報優於預期；Q3 營收 $173.8M（年增 336%，高於共識 $141.2M）；FY26 指引上調至 $505M-$515M；股價大漲（報導 +23%） | 板塊情緒正面外溢，但 RGTI 未能同步受惠 |
| 2026-11-05 | 板塊 | 半導體（Intel、Nvidia、AMD）拋售連帶波及量子股；RGTI、QBTS 單日跌約 18%，IONQ 跌約 15% | 顯示 RGTI 為高 beta 標的，對科技風險情緒敏感 |
| 2026-11-06 | 板塊 | IonQ 財報後反彈；RGTI 報導約 $12.67（+8%），QBTS 約 $11.33（+6%） | 反彈持續性不足 |
| 2026-11-10 | D-Wave (QBTS) | Q3 營收 $4.51M（年增 21%，高於共識）；Q3 bookings $1.9M（年減 19%）；EPS 虧損大於預期；RPO $38.3M（年增 1,221%）；完成 CHIPS 協議 $100M；股價下跌約 7-9% | 同業 CHIPS 協議落地，但市場對財報反應偏負 |
| 2026-11 | IBM | 與 Oak Ridge National Laboratory 發表量子錯誤修正平台 | 競爭壓力增加（大型企業資源）；RGTI 技術差異化需要持續證明 |

## 6. 板塊與總體情緒

- 量子運算股在 2026-11 上旬呈現大幅波動（急跌後反彈），主要受半導體風險情緒驅動，而非個別公司基本面，**板塊同步性高**。
- 自 2025 年下半年以來，量子股整體經歷大幅回檔；RGTI 近一年跌幅約 70%。
- 估值（P/S）仍遠高於 IonQ（約 172）與 QBTS（約 354），但 RGTI 營收基數極小，估值指標的參考意義有限。
- 搜尋結果中的分析文章有部分為 2025 年舊文，已在判斷中排除或降權。

## 7. 已確認的近期催化劑（含日期）

| 日期 | 催化劑 | 方向 | 可信度 |
|---|---|---|---|
| 2026-11-10/11 | Q3 2026 財報與營收低於預期 | 負面（已發生） | 高 |
| 2026-11-10/11 | Jefferies 目標價下調至 $12 | 負面（已發生） | 中高（來源單一） |
| 2026-11-20 ~ 21 | 內部人士減持 | 偏負面（已發生） | 高 |
| 2026-09-08 | CHIPS $100M 協議定案 | 正面（已發生，但屬舊聞） | 高 |
| 2026 Q4（約 12 月底前） | C-DAC 客戶驗收與 Q4 營收認列，決定 FY26 約 $20M 指引能否達成 | 關鍵（未來） | 高 |
| 2026-12 | 原定 >150 qubit 里程碑已由 2028 路線取代，不再為短期催化 | 中性（已調整） | 高 |
| 2027 年初 | 2026 年報（10-K）與 Q4 財報 | 關鍵（未來） | 中（日期為推估） |
| 持續 | 半導體板塊情緒、IonQ / QBTS 後續動態 | 雙向 | 中 |

## 8. 資料限制與待查項目

1. 搜尋工具僅能取得至 2026-11-23 的資料，2026-11-24 當日新聞未涵蓋。
2. 各來源對價格（例如 $12.67 與 52 週低點 $7.08 的時點差異）與營收差距說法不一，建議以 SEC 文件與即時報價校正。
3. DARPA 與 AFRL 合約日期未能確認，不應視為 2026 新增催化劑。
4. ATM 狀態未能確認，建議查 EDGAR。
5. 本分析為新聞面判斷，不構成投資建議；需與基本面、技術面與估值報告綜合判斷。

## 來源（主要參考，依搜尋結果）

- Rigetti Q3 2026 財報：https://www.hpcwire.com/off-the-wire/rigetti-releases-q3-2026-financial-results-reports-improved-fidelity-on-108-qubit-system/
- The Quantum Insider（Q3 2026 結果與路線圖）：https://thequantuminsider.com/2026/11/11/rigetti-q3-2026-results-quantum-computing-roadmap/
- 24/7 Wall St（Q3 營收不如預期）：https://247wallst.com/cards/rigetti-computing-q3-2026-earnings-rgti-01m73mz4gbe9skq001603k9n31
- Rigetti 投資人新聞稿（CHIPS 協議）：https://investors.rigetti.com/news-releases/news-release-details/rigetti-signs-definitive-agreement-100m-us-government-accelerate
- The Quantum Insider（CHIPS $100M, 2026-09-08）：https://thequantuminsider.com/2026/09/08/us-department-commerce-awards-rigetti-100m-quantum-computing-rd/
- Gurufocus（Q3 2026 估值與營收）：https://www.gurufocus.com/news/9190639/rigetti-computing-rgti-reports-mixed-q3-2026-revenue-amid-modest-valuation-concerns
- Webull（IonQ 上調指引與板塊反彈）：https://www.webull.com/news/15894851247719424
- Webull（D-Wave Q3 2026 財報反應）：https://www.webull.com/news/15900081118638080
- Quantum Computing Report（D-Wave Q3 2026）：https://quantumcomputingreport.com/d-wave-reports-q3-2026-results-revenue-up-21-yoy-rpo-surges-1221-to-38-3m-and-finalizes-100m-chips-act-agreement/
- TIKR（板塊下跌，2026-11-05 前後）：https://www.tikr.com/blog/d-wave-sinks-8-rigetti-down-8-ionq-down-8-as-quantum-stocks-slide-again
- Motley Fool（D-Wave 2026-11-10 下跌）：https://www.fool.com/investing/2026/11/10/why-d-wave-quantum-stock-crashed-today/
- RTTNews / Nasdaq（ATM $350M 歷史資料）：https://www.nasdaq.com/articles/rigetti-computing-raises-350-million-equity-offering-support-quantum-computing-initiatives
- Investing.com（CFO / COO 減持）：https://investing.com/news/insider-trading-news/rigetti-computing-cfo-jeffrey-bertelsen-sells-30996-in-stock-93CH-5043265
- Yahoo Finance（FirstQFM 應用）：https://finance.yahoo.com/technology/ai/articles/rigetti-computing-rgti-powered-quantum-152322158.html
