# Portfolio Return Calculator

A basic Python tool I built to calculate daily/total stock returns, portfolio weighted return, and a simple risk indicator.

### Features
- Precise calculations using `decimal.Decimal` (no float rounding errors)
- Input validation (list type, length ≥2, positive prices)
- Weighted portfolio return with length & sum checks
- Basic risk flag (high volatility if any day < -30%)
- Safe error handling with messages

### How to Run
```python
# Example usage (replace with real data later)
prices = [100, 102, 101, 104, 103, 105]
total_ret = cal_total_returns(prices)
print(f"Total return: {float(total_ret * 100):.2f}%")

### What I Learned

Why float is dangerous for money → switched to Decimal
Importance of input validation to prevent crashes/wrong results
Iterative improvement based on feedback

Built with
Python (Udemy Complete Python Bootcamp by Jose Portilla – certificate earned)
