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

# Sifotd

1. 自我介绍

   一个普通的在校大学生，web3初学者

2. 你认为你会完成本次残酷学习吗？

   会

## Notes

<!-- Content_START -->

### 2024.07.11

笔记内容

### 2024.07.12

<!-- Content_END -->

### 2024.08.19

#### 一些工具网站

有几个网站可以监测产量耕作和流动性挖矿机会： 

● https://www.coingecko.com/en/yield-farming 

● [https://vfat.tools](https://vfat.tools/) 

● https://zapper.fi/farm

查看自己可领取空投：[https://earni.fi](https://earni.fi/)

#### 一些概念

流动性挖矿是指向协议提供流动性，并以协议的原生代币为回报的过程。

AMM：自动做市商

DEX:去中心化交易所

利率转换：Aave的借款人可以在可变利率和稳定利率之间转换。

抵押品互换：借款人可以将他们的抵押品换成另一种资产。这有助于防止贷款低于最低抵押品比率而面临清算。

闪电贷款：如果借款人在同一笔交易中偿还了贷款和额外的利息和费用，借款人可以允许无抵押的贷款。闪电贷款对套利交易者很有用，因为他们在各种DeFi Dapps之间进行套利交易时具有资本效率。

借贷平台的重要指标之一是其借款量。这个指标很重要，因为借款人为其贷款支付费用，从而为这些协议产生收入。以下是每个协议如何获得收入的说明。

1. compound：借款人支付的一部分利息将进入其储备金，作为保险，由COMP代币持有人控制。每个支持的资产都有一个储备系数，用以决定有多少比例的利息将进入储备。你可以通过点击各自的资产页面来检查每个资产的储备系数。
2. Maker：当借款人偿还贷款时，他们将支付本金以及由稳定费决定的利息费用。每种支持的抵押品都有其不同的稳定费用。
3. Aave：该平台有两类费用：在Aave V1中，贷款金额的0.00001%是在贷款发放时收取的。0.09%的费用从闪电贷中收取--关于闪电贷款的更多信息见第14章。
4. Cream：按比例抽取借款人利息进入Cream的储备协议，并作为奖励分配给CREAM代币持有人

#### 杂

1:站在风口 ：尽管《每一天：前5000天》的拍卖价高达4.5亿，但我真的欣赏不来，所以我只能归结于风口

#### 需要稳定币的原因

1：稳定币可以让币圈的人自由进退

2：稳定币没有高昂的转账费用

3：没有中心化的机构随意扣押资产，用户仅对个人负责

#### 对稳定币的思考：

#### 个人认为与现实资产挂钩的稳定币是较好的

1：对使用者的激励是毋庸置疑的。例如我们都习惯用U，而U与美元挂钩。这样使得我们的收入是清晰可见的，是相对稳定的，我们也可以自由选择兑换，自由进退

2：连接现实与web3。有了现实的资产支撑，web3才能不断发展

弊端明显：一旦背后资产垮台，稳定币不再稳定，所以与强大国家的法币挂钩的稳定币是较好的



<!-- Content_START -->
### 2024.08.20

#### 杂

MakerDAO多年来一直使用超额抵押来维持合理可靠的挂钩比率。由于DAI的生成过程由智能合约控制，它可以高效运作，远离人为干扰。当您想借DAI稳定币时，您的加密货币将锁定在CDP智能合约中。CDP将设置*强制平仓比率*，例如，1.5x，这意味着您需要提供150美元的以太坊，换取100美元的DAI。如果用户愿意，可以添加更多抵押品，降低他们的风险。如果抵押品金额低于150%（1.5x），将面临罚款。最终，如果用户未能以附加利率（*稳定费*）偿还DAI，他们将面临[强制平仓](https://academy.binance.com/en/glossary/forced-liquidation)风险。

Maker收益池是用户放置抵押品并生成DAI的地方。这样一来，您就可以同时使用多种不同的加密货币作为抵押品。只要用户归还DAI，Maker收益池就会将其[销毁](https://www.binance.com/cn/square/post/43360)。流程如下：

1.将支持的加密货币存至Maker协议。

2.存款将开设一个Maker收益池仓位。

3.您可以根据抵押品金额来提取DAI。您还需支付稳定费。

4.想要赎回加密货币抵押品，请偿还您提取的DAI。

您可以生成或归还DAI，并随时添加或赎回抵押品。但是，您必须维持收益池中显示的强制平仓比率。如果低于这个比率，收益池就会强制平仓您的抵押品。

#### 稳定币的核心问题

平衡DeFi的去中心化精神与创造一种能够可靠地维持其挂钩的货币。

#### 算法稳定币

算法稳定币利用算法来控制稳定币的市场结构和经济基础。你可以把算法稳定币想象成一个自动化的美联储，在这里，预编程的代码代替了人为的决定，执行特定的行动来控制和影响价格





<!-- Content_END -->
