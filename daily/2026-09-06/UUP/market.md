# Technical — UUP as of 2026-09-06

## Status
**PRICE_DATA_UNAVAILABLE**

Data retrieval failed due to proxy connectivity restrictions to Yahoo Finance. Unable to retrieve:
- Current price
- Moving averages (MA50, MA200)
- RSI14, MACD, and other technical indicators
- DXY levels and support/resistance data
- 52-week range information

## Signal Evaluation
- **RSI14**: Data unavailable
- **Price vs MA50**: Data unavailable
- **Signal Condition (RSI<72 AND price>MA50)**: **UNABLE TO ASSESS**

## Technical Analysis
Cannot proceed with standard technical analysis without market price data. The ta.py and yf.py tools encountered egress proxy denials connecting to query2.finance.yahoo.com, guce.yahoo.com, and fc.yahoo.com.

## Indicators table
| Indicator | Value | Reading |
|---|---|---|
| Current Price | N/A | Data unavailable |
| RSI14 | N/A | Data unavailable |
| MACD hist | N/A | Data unavailable |
| MA50 | N/A | Data unavailable |
| MA200 | N/A | Data unavailable |
| DXY Levels | N/A | Data unavailable |
| 52w High | N/A | Data unavailable |
| 52w Low | N/A | Data unavailable |

---

**Status**: Data unavailable — proxy access restrictions prevent market data retrieval.

MARKET COMPLETE