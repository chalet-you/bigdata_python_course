"""
字符串格式化的课后案例
"""

# 定义需要的变量
name = "新东方"
stock_price = 19.99
stock_code = "10234"

# 股票 价格 每日 增长因子
stock_price_daily_growth_factor = 1.2
growth_days = 7

finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days

print(f"公司：{name}，股票代码是{stock_code}，当前股价：{stock_price}")
msg = "每日增长系数：%.1f，经过%d天的增长后，股价达到了%.2f" % (stock_price_daily_growth_factor, growth_days, finally_stock_price)
print(msg)
