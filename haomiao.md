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


### 2024.08.23
uniswap 学习
uniswap 最开始是部署在 Ethereum 上的去中心化交易所，可以交易任何币种对。
和传统的交易所不同，传统交易所主要用的是订单簿的撮合方式，比如有人 1000 元想买ETH，有人 1000 元想卖 ETH，这笔交易才能成交。
但由于链上的交易量不大，挂单人数较少，挂单需要 gas 费用等原因，订单簿的方式会造成长期无法有效成交的问题。

uniswap 创新性的提出了自动做市商的概念，用流动性池来代替订单簿，流动性提供者把一对代币对存入池子，就可以创建一个市场。而每一个在这个池子里交易的人，都需要交一定的手续费给流动性提供者（也就是所谓的做市商），这样可以吸引更多的人把钱存入池子。

那么代币的价格如何决定呢？主要是通过 k = x * y 的公式来确定。
x 和 y 是池子里面两种代币的数量，k是一个常数。

下面用个简单的例子来说明：
假如我把 1000 usdt 和 1 个 eth 添加到池子
那么 x * y = 1000 * 1 = 1000

eth 的价格 = 池子里usdt的数量 / eth的数量 = 1000 / 1 = 1000

假设现在有用户想用100 usdt 买 eth
用户将 100 usdt 放入池子，池子里的usdt 是 1100 个
根据 k = x * y，k必须恒定为1000，所以新 eth的数量得是 1000 / 1100 = 0.909
那么用户可以获得的 eth 是 1 - 0.909 = 0.091
用户购买的 eth 价格是 100 / 0.091 = 1099

交易后池子里有 1100 usdt，0.909 个 eth，新的eth价格是 1100 / 0.909 = 1210
因此随着购买和卖出行为，池子里的 eth 价格在不停变化

可以看到，由于池子较小，eth 的价格变动非常剧烈，这可能会成为一个问题。


### 2024.08.24
uniswap 中的无常损失
理论上来说，由于uniswap只需要添加流动性池子就可以收取手续费，应该能吸引非常多的人来加池子
但由于无常损失的存在，吓退了不少人
不过，无常损失实际上并不能算做是亏损，因为它表达的更多像是机会成本的概念

还是用一个例子来说明
假如在 ETH/USDT 的池子中提供流动性

我存入了 1 ETH和 1000 USDT，ETH的价格是1000 USDT
假设ETH的价格涨到了 2000 USDT，那么池子中的 ETH 会减少， USDT 的数量会增加
新的池子状态可能是0.707 ETH和1414.21 USDT
如果你在这个时候撤回流动性，你会得到0.707 ETH和1414.21 USDT。
那么按照这时候的总价值计算，你获得了 0.707 * 2000 + 1414.21 = 2828.21 USDT

如果你没有提供流动性，你手上会有1000 USDT 和 1 ETH(价值 2000 USDT)，也就是一共 3000 usdt
所以无常损失是：3000 - 2828.21 = 171.79 USDT

当然，如果 ETH 的价格重新回到 1000 USDT 的价格，你手上还是 1 个 ETH 和 1000 USDT
这时候无常损失就等于0，并且你还能赚到这段时间的其他交易者给你支付的手续费。

所以无常损失并非你实际损失的金钱，更像是你添加流动性池子 vs 你持有原有 token 相比，少赚了的钱
根据 “少赚就是亏” 原理，所以才会认为无常损失是可怕的。
不过实际上这只是机会成本而已。

减少无常损失还有一些策略：
1，选择一些低波动的资产，比如（usdc/usdt, dai/usdt），因为波动小，且会回归均值（1），所以只要不退出池子，或者在合适的时候退出池子，就不会造成无常损失
2，uniswap v3 加入了集中流动性功能，允许LP在一个固定的价格区间内提供流动性，可以提高资本效率，降低无常损失
3，通过自动化工具和机器人来动态调整流动性，根据市场变化自动调整价格区间和流动性分布

### 2024.08.25
AAVE 的借贷机制

Aave 是一个去中心化金融（DeFi）平台，允许用户在无需中介的情况下进行加密货币借贷。Aave 通过智能合约自动执行借贷操作，提供了一个安全、透明和高效的借贷环境。

1. 流动性池
Aave 采用了流动性池的模型，用户可以将自己的加密资产存入流动性池中，成为流动性提供者（LP）。这些资产可以被其他用户借出，流动性提供者则可以赚取利息。

2. 存款和借款
存款
存款操作：用户将资产（如ETH、USDC、DAI等）存入Aave的流动性池，存款后会收到相应的aToken（如aETH、aUSDC等）作为存款凭证。
利息收益：存款用户通过持有aToken赚取利息，利息来源于借款用户支付的借款利率。
借款
抵押借款：用户需要提供一定数量的加密资产作为抵押品，才能进行借款。抵押品的价值必须高于借款金额，以确保借款的安全性。
借款操作：用户选择要借的资产和数量，系统会根据抵押品的价值和借款利率计算可借金额。
利息支付：借款用户需要按时支付利息，利息率根据市场供需情况动态调整。

3. 利率模型
Aave 采用动态利率模型，根据市场供需情况自动调整存款利率和借款利率。
存款利率：当流动性池中的借款需求增加时，存款利率会上升，以吸引更多用户存款。
借款利率：当流动性池中的可用资金减少时，借款利率会上升，以抑制借款需求。

4. 抵押品和清算
抵押率
抵押率：每种资产都有特定的抵押率，表示用户可以借款的最大比例。例如，如果ETH的抵押率是75%，用户可以用价值1000美元的ETH作为抵押，借款最多750美元的其他资产。
清算
清算条件：如果抵押品的价值下降，导致借款超过抵押率，系统会自动触发清算机制。
清算操作：清算人可以偿还部分借款，获得相应比例的抵押品作为奖励，从而确保系统的安全性和稳定性。

5. 利息的支付
对于借款人，在归还本金的时候支付利息
对于存款人，可以随时提取存款和累积的利息。
累积的利息是根据实时的年化利率，每个区块进行累积的，对于ETH来说，就是大约15s一次累积利息.

6. aToken 是如何赎回原始的ETH
存款用户通过持有aToken自动赚取利息。利息的来源是借款用户支付的借款利率。
假设年化存款利率为5%。如果你持有10 aETH，随着时间的推移，这10 aETH的价值会增加。例如，一年后，你的10 aETH可能代表10.5 ETH的价值。
当你决定赎回你的存款时，你可以将aToken兑换回基础资产，并获得累积的利息。

### 2024.08.26
AAVE 的清算机制
AAVE 的清算机制通过健康因子来管理借款人的风险，以下是一个简单的例子来说明这一过程。
假设你在 Aave 平台上抵押了价值 2000 美元的 2 个 ETH（当时的市场价），并借出了价值 1000 美元的 USDC。Aave 平台允许你借款的最大抵押率（Loan-to-Value, LTV）是 80%，这意味着你最多可以借出价值 1600 美元的 USDC。
此时健康因子 = 2000 * 0.8 / 1000 = 1.6
大于1，是健康的，没问题的

市场波动
假设市场发生波动，ETH 的价格下跌。现在，你的抵押品价值变成了 1500 美元。
抵押品：1500 美元的 ETH
借款：1000 美元的 USDC
健康因子 = 1500 * 0.8 / 1000 = 1.2
健康因子大于1 所以无事发生

假设市场发生波动，ETH 的价格下跌到了 1000 美元
抵押品：1000 美元的 ETH
借款：1000 美元的 USDC
健康因子 = 1000 * 0.8 / 1000 = 0.8
在这个例子中，健康因子小于1，要触发清算

清算过程
清算人可以选择清算你的头寸，清算人需要偿还你的借款（1000 USDT），并以折扣价格获得她的抵押品（如 2 ETH）。
清算人通过调用 AAVE 的清算智能合约执行这一操作，并会获得一定的清算奖励。
所谓的清算奖励，指的是可以以10%的折扣获得你的2个ETH

清算人只需支付 1800 USDT (2 ETH * 90% 折扣 * 1000 USDT/ETH) 就可以获得价值 2000 USDT 的 2 ETH。
清算人获得的 2 ETH 可以立即在市场上出售,或继续持有以期价格上涨。
清算人获得的利润为 2000 USDT - 1800 USDT = 200 USDT。这相当于借款人的 1000 USDT 债务中有 200 USDT 被清算人获得作为奖励。
剩余的 800 USDT 抵押品价值将返还给借款人。

### 2024.08.27
DEX聚合器
DEX 聚合器（Decentralized Exchange Aggregator，去中心化交易所聚合器）是一种工具或平台，旨在通过整合多个去中心化交易所（DEX）的流动性和交易功能，为用户提供更高效、更具竞争力的交易体验。
DEX 聚合器通过智能合约和算法，将用户的交易请求分散到不同的 DEX 上，以找到最佳的价格和最低的滑点，从而优化交易执行。

顾名思义，聚合的意思就是不用在某一个 DEX 交易，而已通过访问多个DEX，找到最佳的价格
比如Uniswap上ETH的价格是2000，Sushiswap 上eth的价格是1980，那么通过比较二者的价格，dex会自动帮我们路由到 sushiswap，从而获得了更低的购买价格。

同样的，由于之前讲的uniswap等流动池子的机制，我们的交易存在滑点，通过在不同的dex分散下单，可以降低对单个流动性池子的影响，从而降低滑点

dex聚合器的功能一般都是通过智能合约来实现的，也就是说本身就是去中心化的，不用担心资金被第三方托管
可以认为dex 聚合器是更好的 dex

当然这也是站在用户体验的角度讲的，但是实际上dex也有一些缺点
1，复杂性提高，由于dex聚合器本身也是由智能合约来实现的，也可能会引入新的bug，导致用户的资金暴露在更多的风险之中
2，交易费用可能会变高，因为虽然本身买入eth的价格（交易的价格）更低更经济，但由于多执行了一层智能合约，可能会导致交易的gas费用增高
3，交易可能会延迟，因为需要聚合多个dex，所以聚合器需要时间来查询和比较多个 DEX 的报价，这可能导致交易延迟。在市场波动较大的情况下，延迟可能导致价格变化，影响交易结果。

### 2024.08.28
了解 MEV
本质上是由于矿工比普通用户对打包顺序有更高的控制力，所以可以在用户的正常交易前后插入自己的交易进行抢跑。

举个例子来说
假设你正在参与一个去中心化交易所（DEX），比如Uniswap上进行交易。你想用10 ETH买一些代币，并且你发送了交易请求。此时，交易进入了区块链网络等待被矿工打包。

在这个过程中，一个矿工注意到你的交易，并且发现如果在你的交易之前插入买单，然后在你的交易之后立即卖出，可以赚取价差。具体来说，这叫做“抢跑”（front-running）。

因为 ETH 区块链大概是 15s 一个区块，所以矿工可以在【一定程度上】控制他的交易和你的交易的相对顺序。

1. 你的交易（原计划顺序）：
	- 你发送了一个交易：用10 ETH 买 100 ABC 代币。
2. 矿工的操作（实际发生顺序）：
	- 矿工发现了你的交易。
	- 矿工先自己发送一个交易：用5 ETH买 ABC 代币（提高ABC代币的价格）。
	- 矿工再打包你的交易：用10 ETH购买 ABC 代币（你以稍高的价格买了少于100 ABC代币）。
	- 然后矿工立即发送一个交易：卖出刚才买的 ABC 代币（以更高的价格卖出）。

这将直接导致
- 矿工赚取了差价：由于矿工先买后卖，他们在这一系列操作中赚取了差价，这个差价就是矿工通过控制交易顺序而提取的价值，即MEV。
- 你的交易成本增加了：因为矿工在你的交易之前进行了买入操作，导致你购买 ABC 代币的成本增加，获取的代币数量也减少了。

### 2024.08.29
MEV的解决方案

1，使用闪电贷保护：闪电贷可以在一个原子交易中完成借款和还款，减少被夹心攻击（sandwich attack）的可能性。
2，使用去中心化交易所（DEX）聚合器：这些工具可以在多个DEX之间分散交易，从而降低单个交易被重新排序的风险。
3，使用保护隐私的交易技术：一些协议如Tornado Cash可以混淆交易来源，减少被MEV攻击的可能性。
4，延迟交易广播：通过延迟广播交易，可以减少被矿工或验证者提前看到和利用的机会。
5，使用MEV保护工具：一些项目如Flashbots提供了专门的工具和服务来保护交易免受MEV攻击。
6，提高交易费用：虽然这不是最理想的方法，但在某些情况下，支付更高的交易费用可以使你的交易更有可能被迅速包含在区块中，从而减少被重新排序的风险。
7，智能合约优化：开发者可以通过优化智能合约逻辑，减少交易被重新排序的可能性。例如，可以使用条件检查和多步骤交易来减少MEV的风险。
8，社区和协议层面的解决方案：一些区块链社区和协议正在研究和实施更深层次的解决方案，如链下排序、随机排序和其他共识机制改进。

MEV一定是坏事吗？
MEV其实也并不一定是坏事，总的来说有下面两个好处
1，激励，pos的质押奖励未必足够，mev给矿工提供了更多的收入来源，有助于提高网络激励，保证网络的安全性和稳定性
2，套利等交易是可以促进市场效率的，当市场短时间内存在过高的价格差异，套利等良性MEV是可以促进市场的效率提升，同时提升流动性，这时候mev套利交易更像是做市商的角色。


### 2024.08.30
尝试用代码的方式理解 mev 的原理和流程

```python
from web3 import Web3
import time

# 配置
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
PRIVATE_KEY = 'YOUR_PRIVATE_KEY'
TARGET_ACCOUNT = 'TARGET_ACCOUNT_ADDRESS'
GAS_PRICE = Web3.toWei('50', 'gwei')

# 初始化Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# 验证连接
if not web3.isConnected():
    raise Exception("Unable to connect to Ethereum network")

# 获取账户地址
account = web3.eth.account.privateKeyToAccount(PRIVATE_KEY)
address = account.address

# 监控交易池
def monitor_mempool():
    while True:
        pending_txns = web3.eth.get_block('pending', full_transactions=True).transactions
        for txn in pending_txns:
            if txn['to'] == TARGET_ACCOUNT:
                handle_sandwich_attack(txn)
        time.sleep(1)

# 处理夹心攻击
def handle_sandwich_attack(target_txn):
    nonce = web3.eth.getTransactionCount(address)

    # 前置交易（买入）
    front_run_txn = {
        'nonce': nonce,
        'to': target_txn['to'],
        'value': target_txn['value'],
        'gas': 21000,
        'gasPrice': GAS_PRICE,
        'data': target_txn['data']
    }
    signed_front_run_txn = web3.eth.account.signTransaction(front_run_txn, PRIVATE_KEY)
    web3.eth.sendRawTransaction(signed_front_run_txn.rawTransaction)

    # 等待目标交易上链
    while web3.eth.getTransactionCount(TARGET_ACCOUNT) <= target_txn['nonce']:
        time.sleep(1)

    # 后置交易（卖出）
    back_run_txn = {
        'nonce': nonce + 1,
        'to': target_txn['to'],
        'value': target_txn['value'],
        'gas': 21000,
        'gasPrice': GAS_PRICE,
        'data': target_txn['data']
    }
    signed_back_run_txn = web3.eth.account.signTransaction(back_run_txn, PRIVATE_KEY)
    web3.eth.sendRawTransaction(signed_back_run_txn.rawTransaction)

# 启动监控
monitor_mempool()
```

这里要等到目标交易上链之后，我在下一个 block 卖出
这也未必能保证我的前置交易会在目标交易之前完成，可以通过提高gas费等方式来实现优先
不过由于不是矿工，所以其实无法最大化MEV的收益，因为矿工拥有最高的交易排序权力

另外，通过 http 去轮询的方式，过于低效，很容易错过机会，应该用 websocket 或者其他的方案，保证网络的稳定性和实时性



### 2024.08.31
尝试用 solidity 实现 token1 和 token2 的swap
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SimpleSwap {
    IERC20 public token1;
    IERC20 public token2;
    uint256 public rate; // 交换比率，假设1 token1 = rate token2

    constructor(address _token1, address _token2, uint256 _rate) {
        token1 = IERC20(_token1);
        token2 = IERC20(_token2);
        rate = _rate;
    }

    // 交换token1为token2
    function swapToken1ForToken2(uint256 amount) external {
        require(token1.transferFrom(msg.sender, address(this), amount), "Transfer of token1 failed");
        uint256 amountToReceive = amount * rate;
        require(token2.transfer(msg.sender, amountToReceive), "Transfer of token2 failed");
    }

    // 交换token2为token1
    function swapToken2ForToken1(uint256 amount) external {
        require(token2.transferFrom(msg.sender, address(this), amount), "Transfer of token2 failed");
        uint256 amountToReceive = amount / rate;
        require(token1.transfer(msg.sender, amountToReceive), "Transfer of token1 failed");
    }

    // 提取合约中的token1
    function withdrawToken1(uint256 amount) external {
        require(token1.transfer(msg.sender, amount), "Withdraw of token1 failed");
    }

    // 提取合约中的token2
    function withdrawToken2(uint256 amount) external {
        require(token2.transfer(msg.sender, amount), "Withdraw of token2 failed");
    }
}
```

不过这里的代码是固定rate的，也就是说token1/token2 的价格是保持不变的
我们可以引入 amm 自动做市商的机制（uniswap）

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SimpleAMM is Ownable {
    IERC20 public token1;
    IERC20 public token2;
    uint256 public reserve1;
    uint256 public reserve2;

    event LiquidityAdded(address indexed provider, uint256 amount1, uint256 amount2);
    event LiquidityRemoved(address indexed provider, uint256 amount1, uint256 amount2);
    event Swapped(address indexed swapper, uint256 amountIn, uint256 amountOut, address indexed tokenIn, address indexed tokenOut);

    constructor(address _token1, address _token2) {
        token1 = IERC20(_token1);
        token2 = IERC20(_token2);
    }

    // 添加流动性
    function addLiquidity(uint256 amount1, uint256 amount2) external onlyOwner {
        token1.transferFrom(msg.sender, address(this), amount1);
        token2.transferFrom(msg.sender, address(this), amount2);
        reserve1 += amount1;
        reserve2 += amount2;
        emit LiquidityAdded(msg.sender, amount1, amount2);
    }

    // 移除流动性
    function removeLiquidity(uint256 amount1, uint256 amount2) external onlyOwner {
        require(reserve1 >= amount1 && reserve2 >= amount2, "Insufficient liquidity");
        token1.transfer(msg.sender, amount1);
        token2.transfer(msg.sender, amount2);
        reserve1 -= amount1;
        reserve2 -= amount2;
        emit LiquidityRemoved(msg.sender, amount1, amount2);
    }

    // 交换token1为token2
    function swapToken1ForToken2(uint256 amountIn) external {
        uint256 amountOut = getAmountOut(amountIn, reserve1, reserve2);
        require(amountOut > 0, "Insufficient output amount");
        token1.transferFrom(msg.sender, address(this), amountIn);
        token2.transfer(msg.sender, amountOut);
        reserve1 += amountIn;
        reserve2 -= amountOut;
        emit Swapped(msg.sender, amountIn, amountOut, address(token1), address(token2));
    }

    // 交换token2为token1
    function swapToken2ForToken1(uint256 amountIn) external {
        uint256 amountOut = getAmountOut(amountIn, reserve2, reserve1);
        require(amountOut > 0, "Insufficient output amount");
        token2.transferFrom(msg.sender, address(this), amountIn);
        token1.transfer(msg.sender, amountOut);
        reserve2 += amountIn;
        reserve1 -= amountOut;
        emit Swapped(msg.sender, amountIn, amountOut, address(token2), address(token1));
    }

    // 计算输出金额
    function getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) public pure returns (uint256) {
        require(amountIn > 0, "Insufficient input amount");
        require(reserveIn > 0 && reserveOut > 0, "Insufficient liquidity");
        // 这里设置了 0.3% 的手续费
        uint256 amountInWithFee = amountIn * 997;
        uint256 numerator = amountInWithFee * reserveOut;
        uint256 denominator = (reserveIn * 1000) + amountInWithFee;
        return numerator / denominator;
    }
}
```

上面的 智能合约存在很多漏洞和简化的地方，但我觉得应该能更好的理解swap的原理

### 2024.09.01
闪电贷

闪电贷（Flash Loan）是一种基于区块链技术的去中心化金融（DeFi）工具，允许用户在无需任何抵押的情况下借入大量加密资产，但要求在同一笔交易中归还。如果无法在同一笔交易中归还贷款，整个交易将被回滚，借款行为也会被取消。

好处
无需抵押：闪电贷最大的优势是无需任何抵押物，这使得它非常灵活和方便。
高效：由于闪电贷在同一笔交易中完成借款和还款，整个过程非常快速。
低成本：因为没有抵押需求，用户不需要锁定大量资产，从而降低了资金成本。
自动化和安全性：如果无法归还贷款，交易会被回滚，这提供了一定的安全保障。

主要用途
套利交易：用户可以利用闪电贷在不同交易所之间进行价格套利，买低卖高，从中获利。
再融资：用户可以使用闪电贷来在不同的借贷平台之间进行再融资，以获得更低的利率或更好的借贷条件。
清算：在去中心化借贷平台上，用户可以使用闪电贷来清算不良贷款，从中赚取清算奖励。
交易策略：用户可以利用闪电贷执行复杂的交易策略，比如多步骤的借贷、交易和偿还操作。

举例说明闪电贷套利
假设我发现了两个去中心化交易所（DEX）之间存在价格差异：
交易所A上，1 ETH = 3000 USDT
交易所B上，1 ETH = 3100 USDT
我决定利用这个价格差进行套利，通过闪电贷来实现。

借款：你在闪电贷平台上借入100 ETH。
购买USDT：你将100 ETH在交易所 B 上兑换成USDT。根据交易所 B 的价格，你将得到100 ETH * 3100 USDT/ETH = 310,000 USDT。
购买ETH：你将310,000 USDT在交易所 A 上兑换成ETH。根据交易所B的价格，你将得到310,000 USDT / 3000 USDT/ETH = 103.3 ETH。
偿还闪电贷：你需要归还 100 ETH给闪电贷平台。因此，你用 103.3 ETH 中的100 ETH 偿还闪电贷。
利润：在归还闪电贷之后，你剩下的ETH就是你的利润。在这个例子中，你的利润为103.3 ETH - 100 ETH = 3.3 ETH。

当然，这个例子中，没有考虑滑点和手续费，但基本是这样的思路

### 2024.09.02
了解 ERC-4337 账户抽象
直觉上理解，对 Defi的易用性上应该有很大的作用

以太坊账户抽象旨在将协议现有两类账户（即外部拥有账户(EOA)和智能合约账户）的功能合二为一。最终要实现的目标是单一合约账户与代币交易并同时创建合约。这一变化使创新型钱包设计成为可能，如社交恢复、定制和可升级性等。

对于终端用户来说，可以带来一些好处
1，灵活的账户管理，包括多重签名，时间锁，限额，实现复杂的权限控制
2，用户不需要直接和智能合约交互，可以将智能合约的复杂性隐藏在钱包的UI/UX后面
3，可以通过指纹，面容ID等方式恢复账户
4，可以实现一些批量化的操作
5，更安全（主要是权限控制更灵活）
6，无gas
    并不一定真的不收gas，可以由第三方代付，这样可以让新用户快速的用起来，而不像现在一样， 新用户如果没有eth，是没法进行转账等操作的


### 2024.09.03
今天了解一下再质押协议 EigenLayer
用户可以将已经质押在其他 DeFi 协议中的资产（或从质押中获得的收益）再次质押在 EigenLayer 中，以获取更多的收益或流动性。

- 收益最大化：
  EigenLayer 通过智能合约自动将用户的再质押资产分配到收益最高的 DeFi 协议中，帮助用户实现收益最大化。
- 流动性提升：
  用户可以通过 EigenLayer 获取更多的流动性，支持更多的投资和交易活动。

EigenLayer 的运作机制
- 初始质押：
  用户将其资产（如 ETH、DAI 等）质押在某一 DeFi 协议中，如 Aave、Compound 等，获得收益或借贷额度。
- 再质押：
  用户将从初始质押中获得的收益或借贷额度再次质押在 EigenLayer 中。
- 自动分配：
  EigenLayer 的智能合约会自动将再质押的资产分配到收益最高的 DeFi 协议中，以实现收益最大化。
- 收益分配：
  用户可以定期从 EigenLayer 中提取其再质押资产的收益。

但提高资本效率，就会导致杠杆率提升，我们可以举一个例子来看
假设你有100 ETH，并通过以下步骤进行再质押：

初始质押：
质押100 ETH 在 Aave 上，获得50 ETH 的借贷额度。
第一次再质押：
借入50 ETH 并质押在 EigenLayer 上，获得25 ETH 的借贷额度。
第二次再质押：
借入25 ETH 并再次质押在 EigenLayer 上，获得12.5 ETH 的借贷额度。
在这个过程中，你最初的100 ETH 通过多层质押和借贷，最终控制的资产总额为100 + 50 + 25 + 12.5 = 187.5 ETH。你的杠杆率从1:1上升到了1.875:1。

虽然实际情况并非如此，可以多层嵌套套娃质押，但意思大概就是这样的。

就好比当年炒房的人是一样的，他们会用首付买一套房子，然后用房子继续去抵押贷款出来，用贷款买更多的房子。
这样的杠杆会快速放大，导致房价下跌的时候连环杠杆清算。

### 2024.09.04
今天看一下ETH 的 L2协议，都在fud以太坊
Polygon (Plasma & PoS Sidechain):

Polygon使用两种主要技术:
  Plasma: 一种链下扩展框架,创建子链来处理交易,定期将状态提交到以太坊主网。
  Proof of Stake (PoS) Sidechain: 一个独立的区块链,使用PoS共识机制,与以太坊主网并行运行。
技术实现:
  使用检查点系统将交易批量提交到以太坊主网
  验证者节点负责验证交易和生成区块
  使用Heimdall层作为验证者管理层,Bor作为区块生产层

Arbitrum (Optimistic Rollup):
Arbitrum使用Optimistic Rollup技术:
  假设所有交易都是有效的,只在出现争议时执行链上验证
  使用交互式欺诈证明来解决争议
技术实现:
  交易在链下处理,只将交易数据发布到主网
  使用"ArbOS"虚拟机来执行智能合约
  引入"Sequencer"角色来排序交易并提高性能

ZK Rollups (如zkSync, StarkNet):
  ZK Rollups使用零知识证明技术:
  生成加密证明来验证交易的有效性,而不暴露具体交易内容
技术实现:
  使用zk-SNARK或zk-STARK等零知识证明系统
  在链下执行计算,生成证明
  将压缩的交易数据和证明提交到主网
  主网上的智能合约验证证明的有效性

Optimism (Optimistic Rollup):
  与Arbitrum类似,Optimism也使用Optimistic Rollup:
  假设交易有效,允许快速处理
  使用欺诈证明机制来处理无效交易
技术实现:
  使用OVM (Optimistic Virtual Machine) 来执行智能合约
  引入"Sequencer"来排序和执行交易
  使用压缩技术减少提交到主网的数据量

从个人的角度，感觉zk 确实是一个比较不错的方案
optimism 的方案，还是会担心作恶风险，同时 7-30 天的时间太长了，不太能接受
我作为普通用户对 L2 的预期
1，互联，可以从一个L2转移资产到另一个L2或者主网，转账时间和 L1 类似，1s-1min都可以接受
2，流动性互通，我尝试在base上去看一些defi项目，比如 pendle之类的，流动性太差了，而且很多浏览器也不支持，导致我质押获得的 token还以为是一个山寨的token。swap 等服务也有类似的问题，滑点太高了，很多币对都没有

### 2024.09.05
lst和lrt的区别和作用

流动性质押代币（LST）
LST 是通过质押以太坊（ETH）获得的代币，允许用户在质押的同时保持流动性。
用户质押ETH后，会收到相应的LST，能够在去中心化金融（DeFi）平台上进行交易、借贷等操作。
LST的主要目标是解放流动性，使得用户在享受质押收益的同时，不失去对其资产的控制权。

流动性再质押代币（LRT）
LRT 是在LST的基础上进一步发展的代币，允许用户将其流动性质押代币（如LST）再次质押，以获得额外的收益。
通过再质押，用户不仅可以获得ETH的质押奖励，还能通过再质押机制（如EigenLayer）获得额外的节点奖励和其他平台的代币奖励。
LRT的复杂性和动态变化使其能够为用户提供多重收益机会，真正实现“一鱼多吃”的效果。

主要区别
功能:
  LST: 主要用于保持流动性，用户质押ETH后获得LST，可以在DeFi中自由使用。
  LRT: 允许用户将LST再次质押，获取更多收益，增加资产的利用效率。
收益结构:
  LST: 仅提供质押收益。
  LRT: 提供质押收益、再质押奖励及其他平台的代币奖励。
复杂性:
  LST: 简单，主要关注质押和流动性。
  LRT: 复杂，涉及多层次的质押和收益机制。

再质押还有一个风险，就是智能合约的风险
这个风险应该是限制 Dapp复杂性的一个重要因素
因为基于质押协议的再质押，所需要经受的风险，是【质押风险】*【再质押风险】
每加一层，就会多一层的智能合约风险，而这个风险是随着加的层数而乘起来的，会快速变大
这让普通用户无法接受这种情况
越是复杂的金融衍生品和金融逻辑，越需要复杂的智能合约，但也给用户带来了越大的风险
<!-- Content_END -->
