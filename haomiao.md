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

<!-- Content_END -->
