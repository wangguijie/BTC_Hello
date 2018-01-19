# coding:utf-8

from ApiClient import ApiClient
from model.Symbol import Symbol

if __name__ == "__main__":
    print "hello world"

    client = ApiClient()

    symbol = Symbol(Symbol.EOS, Symbol.USDT).get_symbol()

    print symbol

    # 行情API测试
    # market = client.get_kline(symbol, "1min", "150")
    # ticks = market.ticks
    # for tick in ticks:
    #     print "1min内 %s 最低价:%s,最高价:%s" % (symbol,tick.low, tick.high)


    # 聚合行情测试
    # merge = client.get_merged_tickers(symbol)
    # tick = merge.tick
    # print "%s 24小时成交数量为:%s,开盘价:%s,收盘价:%s"%(symbol,tick.amount,tick.open,tick.close)


    # 深度图信息
    # depth = client.get_depth(symbol,"step1")
    # print "%s 当前买单数据:%s"%(symbol,depth.tick.bids)
    # print "%s 当前卖单数据:%s"%(symbol,depth.tick.asks)


    # 交易详情
    # trade = client.get_trade_detail(symbol)
    # trade_data = trade.tick.data[0]
    # print "%s at %s %s %s ,price is: %s"%(symbol,trade_data.ts,trade_data.direction,trade_data.amount,trade_data.price)


    # 账户
    # accounts = client.get_all_accounts()
    # print "total has %s account:"%len(accounts)
    # for account in accounts:
    #     print " id:%s,status:%s,type:%s,subtype:%s"%(account.id,account.state,account.type,account.subtype)

    # 余额 1527480
    # balances = client.get_balance("1527480")
    # for balance in balances:
    #     print "balnce is:%s,type:%s"%(balance.balance,balance.type)


    # 下单
    # order = client.send_order("0.1", symbol, "buy-limit","10.00")
    # if order is not None:
    #     print order.id
    # else:
    #     print "None"
    # 撤单
    # client.cancel_order(order.id)

    # 订单详情
    # order = client.get_order_detail("811025068")
    # print "time:%s,symbol:%s,type:%s,price:%s,amount:%s,field_amount:%s,field_cash_amount:%s,status:%s" % (
    # order.created_at, order.symbol, order.type, order.price, order.amount, order.field_amount, order.field_cash_amount,
    # order.state)

    #历史订单条件查询
    # orders = client.get_all_orders(symbol,"canceled",start_date="2018-01-18",end_date="2018-01-19")
    # for order in orders:
    #     print "time:%s,symbol:%s,type:%s,price:%s,amount:%s,field_amount:%s,field_cash_amount:%s,status:%s" % (
    #         order.created_at, order.symbol, order.type, order.price, order.amount, order.field_amount,
    #         order.field_cash_amount,
    #         order.state)


