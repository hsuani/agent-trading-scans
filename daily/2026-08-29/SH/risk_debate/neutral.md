# Neutral risk view — SH

## Points of agreement (both sides)
- 兩邊都算出「price stop 本身的 dollar risk 極小」——aggressive 在 1% NAV 下算出 stop 損失僅 $202（0.02% NAV），conservative 在 0.5% NAV 下算出 $77.5（0.008% NAV）。雙方都同意：notional size 標籤本身不等於風險大小，真正決定風險的是 stop 距離。
- 雙方都同意此倉位本質是「組合保費」而非方向性押注，不應長抱、須錨定 9/16 FOMC 重新評估。
- 雙方對 call spread 這類 convex overlay 沒有異議（aggressive 主動提出，conservative 未反對）。

## Aggressive overreach
- Where：size 拉高到 1.0-1.5% NAV。
- Why：忽略了 conservative 提出的 gap risk——FOMC 鴿派驚喜可能使 SH 跳空跌破 stop 直接見 $31.20-31.40，此時損失是 stop 距離 × 股數，而非掛定 stop 價。放大 notional 同時放大了這個未被計入的滑價曝險，與「dollar risk 極小」的論證自相矛盾。另外，"1-4 週衰減僅 0.1-0.3%" 這句話是對投資計畫自身 bear 案例（4-6 週純衰減達 5.5-6%）的過度樂觀簡化，屬於反射性駁斥而非重新驗證數字。

## Conservative overreach
- Where：等三角突破收盤站上 $32.60 或等 9/9 CPI 後才進場；2 週天期止損。
- Why：現價已貼近本輪辯論唯一可證偽事件（9/16 FOMC）的進場窗口起點，等突破確認等於放棄「保費在保護尚未定價時買最便宜」這個 setup 的核心優勢，且可能追高進場。2 週天期止損（約落在 9/12 前後）會在 FOMC（9/15-16）前就強制出場，等於斬斷了整個交易論點賴以驗證的唯一事件，時間點缺乏依據。

## Balanced adjustment proposal
- Size：維持 0.5% NAV 現貨（conservative 的紀律有理，gap risk 下不應放大 notional）；不採用 aggressive 的 1-1.5% NAV 放大現貨曝險。
- Stop：採 aggressive 的 $31.55（避開 $31.83 下方 stop-hunt 集中區，ATR 倍數合理），同時疊加 conservative 的 %-based 停損：部位淨值跌 4% 即出場，但時間視窗延長至涵蓋 9/16 FOMC（而非武斷的 2 週），並在 9/9 CPI 設一個 interim check（若無確認訊號則減碼至半倉，而非直接全出）。
- Entry：維持現價進場（aggressive/交易員原判斷），不等突破確認，因窗口短且定位為保費非動能交易。
- Hedge：以小額 SH call spread（$33/$35，到期 9/18）作為額外 convex overlay，另立 risk budget，不取代現貨小倉位。
- Time horizon：不變，錨定 9/16 FOMC，另加 9/9 CPI 為中繼檢查點。

## Net $ risk if stop hits
以 illustrative NAV $1,000,000、0.5% NAV（155 股，entry $32.20）計：正常觸價 $31.55 → $0.65 × 155 ≈ **$101**（0.010% NAV）；若 FOMC 鴿派驚喜跳空滑價至 $31.30，實際損失可能達 ≈ **$140-170**（0.014-0.017% NAV）。

## Net $ upside at T1 / T2
T1 $33.96：$1.76 × 155 ≈ **$273**；T2 $34.09：$1.89 × 155 ≈ **$293**。

NEUTRAL VIEW COMPLETE
