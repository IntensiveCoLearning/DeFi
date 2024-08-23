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

# Alex

1. buidler | trader | lifelong grower
2. yeah

## Notes

<!-- Content_START -->

### 2024.08.19

作为defi三件套之一，稳定币一直在defi lego中处于极为关键的地位，纵使这几年crypto起起伏伏，稳定币的市场一直在稳步提升；

今天学习了一下稳定币四种类型的概念和优缺点：
> 1. 法币抵押稳定币

法币常常常是美元，链上价值1美元的稳定币链下产生1美元作为抵押物；

优点是稳定抗波动，劣势在于缺乏去中心化；

代表有usdt，usdc等；

> 2. 商品抵押稳定币

用实际的商品代替法币当作抵押物；

优点是具有多样性，通胀对冲，劣势是流动性相对较差，赎回复杂；

代表有PAX等；

> 3. 加密担保稳定币

利用链上代币去做抵押；

原理就是用户像协议合约转入eth，usdt或是lp代币等，然后可以mint出稳定币；

由于链上波动性较高，用户需要转入的代币价值要比能mint出来的稳定币价值高不少；

优点是去中心化，劣势是维持稳定的难度高，且资金利用率低；

代表有DAI等；

> 4. 算法稳定币

最复杂的稳定币类型，没有前三种中的抵押物概念，而是用设计的算法去实现稳定；

最常见的原理是 利用代币价值与mint该代币的cost的差值产生的套利行为来维持稳定；

优点是去中心化且资金利用率高，缺点是算法设计难度高，且在真实市场上很容易遭受意料之外的问题；

代表有UST等；



### 2024.08.20

今天学习了fdv和市值的概念和一些逻辑；

fdv是指完全稀释估值，计算方式是计划发行代币数量乘以当前代币价格；

市值是当前市场流通量乘以当前代币价格；

出于团队激励和稳定价格等原因，项目方往往会将部分代币锁一段时间，同时在后期会回购代币进行burn；

较高的fdv意味着通胀压力大，同时波动往往更高，导致做市商面临的难度更大，可能导致流动性降低；

一般而言，FDV/市值比率超过 3-5 倍可能被视为较高。

在牛市中，市场可能更容忍高 FDV/市值比。
熊市期间，投资者可能更关注这个比率，寻求风险更低的项目。

对于交易所来说，高 FDV/市值比的项目可能在上市初期吸引投机者，带来短期交易量。
但长期可能面临持续的卖压，影响交易活跃度和价格表现。

### 2024.08.21

### 2024.08.22

学习了makerdao，maker protocol；

maker protocal是一个利用加密货币质押来生成稳定币的协议；涉及双币系统：mkr，dai，前者主要用于治理，后者是mint出来的稳定币；

makerdao存在的意义旨在用去中心化的治理方式来管理这一种稳定币相关的细节；

dai价值保持稳定，主要和三点有关系：

1. cdp（抵押债务头寸），降低波动对稳定产生的风险；
2. 由协议设计者设计出来的并被mkr持有者同意的稳定费用；
3. 由协议设计者设计出来的并被mkr持有者同意的储蓄率；

<!-- Content_END -->
