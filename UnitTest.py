# coding:utf-8

from ApiClient import ApiClient
from model.Symbol import Symbol

if __name__ == "__main__":
    print "hello world"

    client = ApiClient()

    symbol = Symbol(Symbol.BTC, Symbol.USDT).get_symbol()

    print symbol

    # 行情API测试
    # market = client.get_kline(symbol, "1min", "150")
    # ticks = market.ticks
    # for tick in ticks:
        # print "1min内 %s 最低价:%s,最高价:%s" % (symbol,tick.low, tick.high)


    # 聚合行情测试
    # merge = client.get_merged_tickers(symbol)
    # tick = merge.tick
    # print tick


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
    # client.cancel_order("812362689")

    # 订单详情
    # order = client.get_order_detail("812362689")
    # print order

    #历史订单条件查询
    # orders = client.get_all_orders(symbol,"canceled",start_date="2018-01-18",end_date="2018-01-19")
    # for order in orders:
    #     print "time:%s,symbol:%s,type:%s,price:%s,amount:%s,field_amount:%s,field_cash_amount:%s,status:%s" % (
    #         order.created_at, order.symbol, order.type, order.price, order.amount, order.field_amount,
    #         order.field_cash_amount,
    #         order.state)

    #从交易账户转移到借贷账户
    # client.transfer_balance_from_spot_to_loan(symbol,Symbol.USDT,"1")

    #从借贷账户转移到交易账户
    # client.tratransfer_balance_from_loan_to_spot(symbol,Symbol.USDT,"1")

    #借贷
    # order = client.apply_for_loan(symbol,Symbol.EOS,"30")
    # print "loan id:",order.id

    #偿还借贷
    # client.repay_loan("211790","30")

    #借贷订单
    # orders = client.get_loan_orders(symbol,Symbol.EOS)
    # for order in orders:
    #     print order