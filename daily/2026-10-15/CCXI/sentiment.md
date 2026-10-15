# Sentiment — CCXI as of 2026-10-15

CCXI 為 Churchill Capital Corp XI，一家 SPAC（空白支票公司），尚未完成併購，無營收與獲利。下列各項判讀都應以此為前提。

## 分析師共識

**DATA_UNAVAILABLE（結構性無覆蓋）**

- `yf CCXI rec_summary` 與 `yf CCXI recommendations` 皆回傳空陣列，無買進/持有/賣出計數，也無評級變動或目標價紀錄。
- SPAC 通常沒有 sell-side 覆蓋，因此「無評級」本身就是正常狀態，不代表資料故障。
- 前一日報告（2026-10-05）引用的 $53.04 目標價，本次無法核實，不予採用。

## 零售社群

- **Reddit（r/wallstreetbets、r/stocks）**：WebFetch 遭站點封鎖（Claude Code 無法連線 www.reddit.com），無法取得帖文樣本。WebSearch 也未找到相關 Reddit 討論。
- **StockTwits**：api.stocktwits.com DNS 解析失敗（ENOTFOUND），無資料。
- **X / 新聞聊天**：WebSearch 找不到 2026 年 10 月的任何 CCXI 相關輿論或新聞。搜尋結果多為 2026 年 4 月至 7 月的自動生成股價頁，內容重複且品質低。
- **提及量**：無法量化，定性判斷為低。以 SPAC 的特性，零售投機性部位通常很少。
- **主題**（從 2026 年中的新聞推得，非零售原文）：
  - 與 Agility Robotics（人形機器人公司）的併購案，估值 $2.5B 盤前權益價值，合併後預計以 AGLT 代號掛牌。
  - 併購資金約 $620M 總額（假設無贖回），含信託 $420M 與 Foxconn 領投的約 $200M PIPE（每股 $10）。
  - 主要不確定性為贖回率。
- 整體零售語氣無可靠樣本，無法判定多空傾向。

## 內部人交易

**Net 6mo：$0 買入 / $0 賣出（快取資料中 6 個月窗口內無任何交易）**

- 快取中最新一筆交易為 2022-08-16（CFO Susan M. Kanaya 賣出與選擇權行使），距今超過 4 年。
- 2021–2022 年紀錄包含 CEO Thomas J. Schall（2022-08-04 賣出約 $6.5M）、CFO Kanaya、董事 James L. Tyree 等，成交價多在 $33–$70。此價位與 2026 年 CCXI 約 $11 的交易區間明顯不符。
- **資料完整性警示**：這組內部人紀錄可能屬於其他發行人或歷史 CIK 對應錯誤，不應直接用於本 SPAC 的內部人情緒判讀。建議核對 SEC Form 3/4/5 申報。
- 無 2026 年內部人買賣紀錄可用。

## 股東結構

- 內部人持股：6.33%
- 機構持股：68.79%（流通股口徑 73.44%），機構數量 78 家
- 股權集中度中等偏分散，但 SPAC 股東結構常受贖回與 PIPE 認購影響，機構占比在併購完成前後可能大幅變動。

## 價格與事件背景（僅作脈絡）

- 近期收盤：2026-10-12 $10.78、10-13 $11.16、10-14 $10.83，當週區間約 $10.64–$11.35。
- 價格略高於 $10 信託價值，溢價約 8%，反映市場對併購的部分預期，但幅度有限。
- 時程說明有分歧：
  - Unite.ai 單一來源指出 S-4 於 2026-10-13 生效，股東大會定於 2026-11-02。
  - Humanoid.guide 引述文件指出，若 2026-12-31 前未完成交易，任一方可終止。
  - 前一日報告所稱 2026-09-17 股東大會，與上述時程不一致，本次不採用。
- 以上時程皆需以 SEC EDGAR 原始申報核實。

## 淨情緒評分

**Composite：中性（neutral），信心：低**

依據與限制：
- 分析師面：無覆蓋，無法納入評分。
- 零售面：Reddit、StockTwits 皆無資料，WebSearch 無 2026 年 10 月的相關輿論。
- 內部人面：6 個月內無交易，屬中性。快取紀錄有明顯錯置風險，不納入評分。
- 事件面：併購進行中，S-4 生效與股東大會為近期催化劑，但贖回率與 PIPE 條件未知，方向不明。

**Divergence flag：否（無法判定）**。因分析師面無資料，無法比較零售與分析師傾向是否相反。

## 資料缺口與建議

1. 核實 SEC EDGAR 上 CCXI 的 S-4、併購時程與 Form 4 申報。
2. 修正或確認 insider 快取是否為本發行人資料。
3. 下次可在 Reddit 或 StockTwits 可連線的環境重試零售樣本。

Sources:
- [Agility Robotics 併購公告（Robotics247）](https://www.robotics247.com/article/agility-robotics-goes-public-merges-with-churchill-capital-corp-xi-at-2.5-billion-valuation)
- [併購條款與 Nov 2 股東大會、S-4 生效（Unite.ai）](https://www.unite.ai/?p=485205)
- [Dec 31 終止條款（Humanoid.guide）](https://humanoid.guide/?p=14145)
- [CCXI 股價與 52 週區間（Stock Analysis）](https://stockanalysis.com/stocks/ccxi/)
- 本地資料：pipeline/tools/yf CCXI insider、major_holders、rec_summary、recommendations；prices/CCXI.csv

SENTIMENT REPORT COMPLETE
