---
timezone: Asia/Shanghai
---

> 请在上边的 timezone 添加你的当地时区，这会有助于你的打卡状态的自动化更新，如果没有添加，默认为北京时间 UTC+8 时区
> 时区请参考以下列表，请移除 # 以后的内容

timezone: Pacific/Honolulu # 夏威夷-阿留申标准时间 (UTC-10)

timezone: America/Anchorage # 阿拉斯加标准时间 (UTC-9)

timezone: America/Los_Angeles # 太平洋标准时间 (UTC-8)

timezone: America/Denver # 山地标准时间 (UTC-7)

timezone: America/Chicago # 中部标准时间 (UTC-6)

timezone: America/New_York # 东部标准时间 (UTC-5)

timezone: America/Halifax # 大西洋标准时间 (UTC-4)

timezone: America/St_Johns # 纽芬兰标准时间 (UTC-3:30)

timezone: America/Sao_Paulo # 巴西利亚时间 (UTC-3)

timezone: Atlantic/Azores # 亚速尔群岛时间 (UTC-1)

timezone: Europe/London # 格林威治标准时间 (UTC+0)

timezone: Europe/Berlin # 中欧标准时间 (UTC+1)

timezone: Europe/Helsinki # 东欧标准时间 (UTC+2)

timezone: Europe/Moscow # 莫斯科标准时间 (UTC+3)

timezone: Asia/Dubai # 海湾标准时间 (UTC+4)

timezone: Asia/Kolkata # 印度标准时间 (UTC+5:30)

timezone: Asia/Dhaka # 孟加拉国标准时间 (UTC+6)

timezone: Asia/Bangkok # 中南半岛时间 (UTC+7)

timezone: Asia/Shanghai # 中国标准时间 (UTC+8)

timezone: Asia/Tokyo # 日本标准时间 (UTC+9)

timezone: Australia/Sydney # 澳大利亚东部标准时间 (UTC+10)

timezone: Pacific/Auckland # 新西兰标准时间 (UTC+12)

---

# haomiao

1. 自我介绍
目前在公司内部创业做端侧 AI 模型推理，对 Web3 有兴趣，想了解 DeFi。
代码写的很杂，常用语言或多或少都写过，主要是 Golang, C, Python, Java, Typescript, Javascript

2. 你认为你会完成本次残酷学习吗？
是的

## Notes

<!-- Content_START -->

### 2024.08.19

今天阅读的文章
https://nigdaemon.gitbook.io/how-to-defi-advanced-zhogn-wen-b/di-6-zhang-qu-zhong-xin-hua-de-wen-ding-bi-he-wen-ding-zi-chan
https://www.binance.com/zh-CN/square/post/43195

为什么要有稳定币?
因为加密货币的价格不够稳定，人们的意识中也没有形成所谓的 “币本位” 的计价方式。而日常的使用中，能稳定对各种资产进行计价是一个刚需。
因此引起了稳定币的需求。

稳定币有哪些？
稳定币分为中心化的稳定币和去中心化的稳定币
中心化的比如 USDT 和 USDC，USDT是由 Tether 公司发行的，USDC是由 Center 管理，Center是Circle创建的联盟，联盟包括 Coinbase和Bitmain等。
二者都是合法的公司，纳入监管，但由于中心化，有一定的风险。
去中心化的稳定币有 DAI，是去中心化组织 MakerDAO 发行，没有中心化的风险，但由于超额抵押会导致其他问题。
此外，还有一些去中心化的算法稳定币，依赖具体的算法来维持币价稳定

稳定币的用途？
1. 链上金融的退出流动性，比如你买了一个 ETH，赚了钱想退出，卖出 ETH 后可以获得链上稳定币，不用反复在银行转账中耗费时间
2. 跨国转账，传统金融系统的跨国转账和结算是非常耗时且手续费高昂的，但基于链上稳定币的转账则方便且便宜（不过这个优势主要是区块链的，而不是稳定币的）
总之，稳定币在当前2024年的语境下，基本等于“链上美元”。基本就是链上的支付，储值等活动的基础

稳定币的风险
1. 中心化的稳定币有被封禁的可能，比如 Tether 公司可以对某些 USDT 进行标记后封禁。
2. 脱锚风险，去中心化的稳定币一般存在抵押物，由于抵押物价格大幅波动，会导致稳定币实际上并不稳定，导致脱锚
3. 资金效率低下，一般来说，基于抵押物的稳定币，要求超额抵押；也就是为了铸造出 1 美元的稳定币，要花费市价 1.5-1.8 美元的 eth，这极大的降低了资金利用的效率

DAI 的价值是如何保持稳定的
简单的说，通过调节利率来实现；

假设 DAI 价格低于 1 美元
提高利率（借出利率和储蓄利率）
这会导致
1. 更少的人借入 DAI，并会提前偿还DAI贷款，那么流通的DAI就会减少，供应减少则价格回升
2. 更多的人想持有并借出 DAI，需求增加，导致价格回升。

反之同理。基于这样的原理，则币价可以保持稳定。

不过利率的调整是基于 MakerDAO 的治理投票来实现的，可能会在极端情况下响应不够及时导致问题。


### 2024.08.20
今天主要研究一下 luna 崩盘的前因后果

Luna 是 Terra 区块链的原生代币，在 Terra 上的算法稳定币 UST 和 Luna是挂钩的。
用户可以通过销毁 Luna 来生成 UST，也可以通过销毁 UST 来生成 Luna
是仅次于 USDT 和 USDC 的第三大稳定币（当年）

但是当 UST 的价格跌到 1 美元以下的时候，投资者就会抛售 UST 而持有真正的美元，这会导致 Luna 的量增加
压低 Luna 的价格，形成了所谓的 “死亡螺旋”，也就是进一步导致投资者抛售，加速了价格的下跌。

具体的算法稳定机制如下：
1，Luna 是自由涨跌的一个币（这个币其实可以是任意币种，但项目方选择了Luna）
2，当UST价格大于1美元时（1.01），可以通过销毁价值 1 美元的Luna得到一个 UST，然后卖出UST即可得到 1.01 美元，获利 0.01 美元
3，当UST价格小于1美元时（0.99），可以通过购买 1 UST 后销毁，获得价值1美元的Luna，然后卖出 Luna，获利 0.01 美元

主要的逻辑就是，吸引套利者去套利，从而让 UST 的价格维持在1美元附近。

这个玩法要求 Luna 的市值相对保持稳定，如果市值有较大幅度的波动，可能会导致 UST 的价格巨幅波动，从而脱锚
因此，算法稳定币要求对经济学模型有一定的深入考量，而匆忙推出的稳定币未必真的稳定。

### 2024.08.21
今天学习：https://mp.weixin.qq.com/s/gzr9q9kM3j-R0ec7sCb3NQ

web3 支付

传统的支付，除了现金交易外，一般都需要涉及多个中间方
1，清算：支付指令的传输和对账
2，结算：实际转移资金
类比来说，清算就是开出了一张支票，结算就是实际兑付支票写的钱

而跨国的支付就更加复杂，因为不同的国际组织和银行，利益关系交错，他们采用的结算系统也不完全一样，还需要考虑汇率等问题
而区块链的结算就非常方便，几乎是实时到账，无需许可，公开透明，全球只要连接了互联网都可以快速拥有一个自己的“区块链账号”然后进行收款

以支付为目标的 Paypal 推出的 PAYUSD则是发行在 Solana 上的美元稳定币。
除此之外，传统金融机构也逐渐发现代币化是一个非常好的概念，可以盘活很多沉淀在账上的资金，提高资金利用率
甚至引入更强的金融工具，而近实时的金融工具的使用，进一步激活了市场

这里面更多的涉及到了 RWA 的概念，也就是把现实世界的中心化资产，上链。
这中间不可避免的遇到中心化和信任的问题，比如一个房子在链下需要有明确清晰的产权，这个是由政府来保证的
即使链上的代币化的房屋被区块链确保是唯一的真实的，但还是需要政府这个中心化的机构来保证房子的合法性

### 2024.08.22
- case study
    - ETHer.fi 的 Crypto Payment Card
    - ether.fi 主要是 eth 下的一个 staking 和 restaking 项目，但他们也推出了 Cash 业务。这个业务就是我们常见的充值加密货币的预付费 Visa 卡，通过支付服务商提供法币结算，把 USDt 或者其他稳定币进行支付
    - 特色在于，普通的这种 crypto 支付卡，一般充值的是 USDT 或者 USDC，并没有和 DeFi 结合
    - 而 ether.fi 的优势(或者说特色)在于，可以用 ether.fi 的资产作为抵押，换取 usdc 进行消费，并用 staking 和 liquid 的收益来偿还，这样可以保证本金不动的情况下，让大家花“利息”
        - 这样大家更愿意把钱质押在 ether.fi 上，而被动的， ether.fi 的积分价格和收益，都相应的增长，进入一个增长飞轮。
    - 总结：囤币党的福音，在实际使用上更像是一个链上的余额宝，只需要存钱进去，钱会产生收益，你可以直接用这个收益进行支付
    - 但依然有中心化的问题，依赖法币承兑商，依赖 Cash 预付费的美元稳定币。
    - 感想：支付还有很长的路要走，不管链上 DeFi 多么如火如荼，但依然脱离于线下支付体系之外，线下的支付还是依赖传统的支付渠道。


<!-- Content_END -->
