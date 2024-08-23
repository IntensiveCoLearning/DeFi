---
timezone: Asia/Shanghai
---

---

# {evilgenius}

1. 自我介绍
   java后端, 通过朋友入行, 平时主要跟油管博主自学
   restaking, 做lp, 合伙开赌场, meme, 现货合约什么都看一点 ...
   热爱技术 但是觉得在web3世界里面主要还是看庄家怎么叙事, 有资金才有庞氏
   希望和大家共同探索defi世界~
2. 你认为你会完成本次残酷学习吗？
   会尽量跟上 .. 不过8月28结婚, 确实有点忙...

## Notes

<!-- Content_START -->

### 2024.07.11

笔记内容

### 2024.07.12

### 2024.08.19

稳定币: btc等主流币波动大, 稳定币购买的时候波动不会太大

稳定币: USDC USDT DAI

锚定币: WBTC  renBTC  sETH  stETH

稳定币类型:

1. 基于存款准备金 (usdc, usdt, 谁知道这些吊毛公司真正储备了多少呢)
2. 基于抵押
3. 基于算法

how to work:   MakerDAO

1. ETH存到开放的CDP, 150%的抵押物可以铸造100%借款   **<超额质押>**
2. 提取DAI
3. 偿还DAI 解锁ETH

会收取铸币税

Synthetix 铸造衍生品资产

1. SNX存款铸造衍生品, 600%抵押物铸造100%衍生品
2. 提取衍生品  eg: sTSLA share
3. 归还sTSLA 解锁SNX

通过价格预言机, 向区块链报告外部价格

算稳 ampleforth AMPL, 比较早期已经不用

1. 通胀, 1AMPL > 1USD, 供应增加
2. 收缩, 1AMPL < 1USD, 供应减少
3. 平衡, 不需采取措施

极大依赖于预言机进行价格锚定

#### luna崩盘

Terra 生态系统（区块链）：

LUNA（Terra 区块链的原生代币，类似于 ETH）

 UST （Terra 区块链的原生稳定币）

最近一次也是规模最大的算法稳定币崩盘发生在 5 月 9 日的 UST，当时公开市场的大规模抛售将其价格推至 0.70 美元。如上所述，低于 1 美元的脱钩将触发套利者销毁 1 UST 来铸造价值 1 美元的 LUNA，从而减少 UST 供应，将其价格推回至 1 美元。然而，Terra 利益相关者开始对 UST 重新获得锚定汇率失去信心，因为铸币税的数额将开始导致 LUNA 的供应量过度膨胀。这导致了如下所示的负反馈循环。

银行挤兑，死亡螺旋

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/3e0406c3-f112-4454-9c45-bff874491deb/05943366-c1e6-44d2-b304-95d93270b202/image.png)

seigniorage 铸币税

UST的价格跌至<0.04美元，LUNA的价格跌至不到一美分（<0.01美元）

就 UST 而言，Terraform Labs 类似于美联储，但没有维持与信仰货币挂钩所需的几乎无限量的资本。

算稳优势：

1. 无需信任
2. 资本效率, 没有抵押品

劣势：

未经测试且高风险

### 2024.08.20

#### How to DeFi 阅读摘要

算法稳定币可以进一步细分为不同的类别--主要的子类别是：rebase（弹性）和seigniorage（铸币税）模式。

##### **弹性模式（rebase）**

弹性模式通过改变稳定币的全部供应量来控制价格。根据稳定币的价格是高于还是低于预定的挂钩价格，协议将在一个固定的时期内自动增加或减少每个持有人钱包中代币的供应量。

这样做的理由是，通过强行控制供应，稳定币的价格可以根据简单的通货膨胀/通货紧缩的经济理论来影响价格。

这种模式的开创性协议是Ampleforth（AMPL），最早可以追溯到2019年。

**Ampleforth**

https://nigdaemon.gitbook.io/~gitbook/image?url=https%3A%2F%2Ftva1.sinaimg.cn%2Flarge%2F008i3skNgy1gseai1iqd6j30qq070gmp.jpg&width=300&dpr=4&quality=100&sign=425e5612&sv=1

每隔24小时，Ampleforth（AMPL）的全部流通供应量都会按比例增加或减少，以确保价格保持在1美元。如果AMPL的价格比1美元的目标价高出5%或更多，每日的rebase将扩大钱包中AMPL的数量。如果AMPL的价格比1美元的目标价格低5%或更多，每日的rebase将减少钱包中持有的AMPL数量。

每个钱包持有人都将受到影响，但他们将保留与以前相同的市场份额。rebase，无论是正数还是负数，都是非稀释性的，因为它们按比例影响所有的AMPL余额。

由于rebase是以固定的时间间隔进行的，因此用户可以在rebase之前及时购买或出售AMPL，以增加他们持有的价值。

##### **铸币税模式（Seigniorage Model）**

铸币税模式通过引入一个动态影响市场的奖励系统来控制价格。如果价格高于挂钩，新的代币就会被铸造出来，并分配给提供流动性或有代币抵押的参与者。

如果价格低于挂钩，代币将停止铸造，并引入机制以减少供应。用户可以购买燃烧相关代币的优惠券，将其从供应中销毁。这些优惠券在未来可以被兑换成更多的代币，但只有当价格回到或超过预定的挂钩时才可以。

这种模式有三个基本迭代：

**Empty Set Dollar**

https://nigdaemon.gitbook.io/~gitbook/image?url=https%3A%2F%2Ftva1.sinaimg.cn%2Flarge%2F008i3skNgy1gseaprf466j30qj051my9.jpg&width=300&dpr=4&quality=100&sign=75cfaccd&sv=1

ESD是一种单币抵押模式。正如其名字所暗示的，这种模式中只有一个代币。用户通过协议的原生代币在去中心化自治组织（DAO）中提供流动性或股权--ESD代币有效地充当了稳定币和治理代币。

在每个纪元的开始，系统将测量时间加权平均价格（TWAP）。如果TWAP高于1美元，该协议将进入通货膨胀阶段，并铸造代币作为对DAO抵押者和流动性提供者的奖励。相反，如果价格低于1美元，该协议将进入收缩阶段，用户将停止收到任何奖励。

在收缩阶段，如果协议再次进入扩张阶段，用户可以通过燃烧ESD来购买优惠券，以获得高达45%的溢价。然而，优惠券只能持续30天，这意味着如果系统保持在收缩阶段超过30天，优惠券购买者有可能一无所获。ESD中的纪元持续时间为8小时。

**Basis Cash**

https://nigdaemon.gitbook.io/~gitbook/image?url=https%3A%2F%2Ftva1.sinaimg.cn%2Flarge%2F008i3skNgy1gsehwsnacxj31dg0ca75f.jpg&width=300&dpr=4&quality=100&sign=d307162e&sv=1

Basis Cash是一种双代币征税模式。正如项目名字所暗示的那样，除算法稳定币外，项目还有一种被称为股份代币的额外代币。Basis Cash的稳定币是Basis Cash（BAC），而其股份代币是Basis Share（BAS）。

与ESD一样，Basis Cash依赖于一种TWAP机制，它将根据BAC的价格是高于还是低于1美元来铸造或停止铸造BAC。当BAC高于1美元时，协议进入一个扩张阶段，用户可以通过押注BAS从Boardroom DAO获得新铸造的BAC。

当BAC低于1美元时，协议进入收缩阶段，没有新的BAC将被铸造给Boardroom的BAS抵押者。基准债券（类似于ESD优惠券）可供购买，价格为（BAC）^2。当协议再次进入扩张阶段时，基础债券的购买者将得到赎回BAC的机会。

Basis现金纪元持续24小时，与ESD优惠券不同，Basis Bonds没有过期日期。

**Frax Finance**

https://nigdaemon.gitbook.io/~gitbook/image?url=https%3A%2F%2Ftva1.sinaimg.cn%2Flarge%2F008i3skNgy1gsei0te1xoj312e078whh.jpg&width=300&dpr=4&quality=100&sign=a0f10420&sv=1

Frax借鉴了铸币税模式的基本原则，并创建了自己独特的模式，其稳定币（FRAX）由两种类型的抵押品支持--由法币支持的集中式稳定币（USDC）和其原生股票代币Frax Share（FXS）。虽然Frax目前采用法币稳定币作为抵押品，但该协议确实最终打算完全过渡到分散的抵押品。

与Basis或ESD不同的是，Frax采取的是零散的抵押方式。Frax有一个可调整的抵押品比率，由PID控制器控制。抵押率根据增长比率进行调整，该比率衡量FXS流动性的多少与FRAX的总体供应量。

Frax稳定币（FRAX）可以被铸造，并允许从协议中赎回1美元的价值。这激励了套利者购买或铸造FRAX，使价格回到其挂钩点。另一方面，FXS会产生费用、税收收入和多余的抵押品价值。值得注意的是，Frax推出了veFXS，它将算法市场操作控制器（AMO）的部分利润给了FXS抵押者，类似于veCRV在曲线金融上获得部分交易费的情况。

当FRAX高于1美元时，PID将抵押率降低一点，而当FRAX低于1美元时，PID将抵押率提高一点。刷新频率和阶梯参数都可以通过FXS治理来调整。

截至2021年5月8日，FRAX有85.25%由USDC支持，14.75%由FXS支持。

##### **为什么FRAX成功了？**

虽然sUSD、UST和FRAX的成功都有各自的原因，但我们将重点关注FRAX，因为它到目前为止拥有最好的挂钩保持率，整个2021年第一季度的平均价格为1.001美元。以下是我们认为它们到目前为止成功的一些原因：

1. FRAX部分由USDC抵押，这使社区对该系统保持挂钩有一定信心。截至2021年5月8日，85.25%的FRAX是由USDC支持的。
2. Frax保持着灵活的抵押率，满足市场对FRAX定价为1美元的要求。
3. 抵押品被重新部署到其他地方以赚取利息。这有助于带来外部收入并支撑协议发展。
4. FRAX的价格波动会转移至FXS，用于对FSX的回购和燃烧。

虽然这些只是简化的原因，但仍然需要不断地重新考虑，特别是在危机时期，当FXS的价格大幅下降，流动性挖矿奖励最终停止时，是否还能依然保持目前的状态。

#### **起底 MakerDAO RWA，看 DeFi 捕获链下资产的治理体系与交易架构
阅读摘要**

https://web3caff.com/zh/archives/80903

rwa叙事: 现实世界token化   real world asset

现实世界token化   real world asset

synthetix  将现实世界的资产token化

1. 可以将大量资源引入到web3
2. 链上可以有真实的业务属性, 减少链上旁氏属性
3. 对于传统世界来说, 可以提供传统行业业务效率,    资金流动率

合法合规  问题很严峻  红线

如何定义链上发行的资产不是非法发行的 (政府, 头部机构去做)

重运营的活儿

**DeFi 如何治理链下法人实体**

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/3e0406c3-f112-4454-9c45-bff874491deb/e414d57f-721e-4293-ba20-739b10c0e409/image.png)

- 基金会作为法人实体对内而言，无需任何注册资本，无需股东/成员角色，使得基金会成为单一目的独立孤儿法人实体；基金会也可类似于信托，指定 MakerDAO 或其成员为受益人（Beneficiary）；同时基金会也能做到破产隔离（Bankruptcy-Remote），即使 MakerDAO 或者基金会 “Go Dark” 也不会影响彼此。
- 基金会作为法人实体对外而言，能够实现（1）与链下实体进行交互，如签约、提供服务等；（2）通过 KYC/AML 合法持有链下资产/IP；（3）保护 DAO 成员的有限责任；（4）根据 DAO 的决议，代表 DAO 执行一系列链下的操作。

感觉就是通过开曼基金会法律包装一下, 学法律的心也挺坏…

个人认为RWA还是各国法律红线, 主要还是看项目怎么运营

先学到这儿 明天学 https://www.binance.com/zh-CN/square/post/43195

### 2024.08.21

币安广场，查漏补缺

## **抵押债务头寸（CDP）是什么？**

MakerDAO多年来一直使用超额抵押来维持合理可靠的挂钩比率。由于DAI的生成过程由智能合约控制，它可以高效运作，远离人为干扰。当您想借DAI稳定币时，您的加密货币将锁定在CDP智能合约中。CDP将设置*强制平仓比率*，例如，1.5x，这意味着您需要提供150美元的以太坊，换取100美元的DAI。如果用户愿意，可以添加更多抵押品，降低他们的风险。如果抵押品金额低于150%（1.5x），将面临罚款。最终，如果用户未能以附加利率（*稳定费*）偿还DAI，他们将面临[**强制平仓**](https://academy.binance.com/en/glossary/forced-liquidation)风险。

## **DAI的价值如何保持稳定？**

除了降低MakerDAO作为贷方的风险外，CDP机制有助于将DAI与美元挂钩。MakerDAO还可以投票改变稳定费与DAI储蓄率（在DAi储蓄率智能合约中支付给质押者的利息），以控制DAI的供需。这三大工具共同维持DAI与美元按照1：1的比率挂钩。让我们来看看这究竟是怎么回事：

1.当DAI跌破挂钩比率时，该系统会吸引用户偿还债务、收回抵押品并销毁DAI。这可以通过提高稳定费来实现，让借贷变得更加昂贵。DAO还可以提高DAI储蓄率，扩大代币投资需求。

2.当DAI高于其挂钩比率时，则情况正好相反。如果稳定费降低，DAO将激发DAI的生成。这创造了新的DAI，增加了总供应量，降低了价格。MakerDAO还可以通过降低DAI储蓄率来减少DAI的需求，这意味着投资者会换其他的方式来赚利息。

### 2024.08.22

学习稳定币 usual

usual,   市场认可度不是特别高, 和本末社区有合作

优势: 空投明牌

劣势: 模式设计     usd0++锁四年, 崩盘的时候才会拉

ethena 神矿

usdt 千亿规模

usdc 300亿

稳定币的发行商手里有很大规模的美元储备. 拿来买4~5的美国国债多香啊

usual 把储备资金能创造的价值回馈给用户

ethena的底层资产, 套保的空单, 产生的年化回馈给用户   ..  治理代币..  风险基金

usual 底层资产, rwa资产, 目前支持的也是美国国债, 这部分收益也是可以回馈给用户的

投资背景: 
https://www.rootdata.com/zh/Projects/detail/Usual?k=MTE5NTI=

欧洲团队

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/3e0406c3-f112-4454-9c45-bff874491deb/54458655-a23a-4d1a-a6ce-d4719c49509f/image.png)

协议:

usd0背后是美国国债.  实际: usd0背后是usyc, usyc背后是美国国债

usyc 做美国短期国债的rwa项目, 短期国债, 不会存在挤兑风险

目前可以用usyc去铸造usd0的 (目前只针对白名单的机构用户)

为什么脱裤子放屁?

解决的是RWA资产的流动性问题

很多RWA资产因为法律法规(监管)的问题, 买代币需要kyc, 还有单笔的限额  — 对散户不友好, 流动性比较差

持有usd0, 没有kyc, 没有额度限制, 但是拿不到任何收益

想要分到协议的收入, 需要锁定usd0.  所有人的解锁时间都是一样的, 在周期的第一天和最后一天锁定, 都是周期结束解锁

usd0++没办法提前赎回, 退出只能走dex, 会有一丢丢磨损

可以去分配usual代币, 或者不要币, 要一个base yield (稳定币产生的收益)  二选一

实际会比美债更高一点, 因为不是所有的usd0全都锁定, 比如目前70%的usd0锁定, 可以分100%的usd0的tvl产生的收益, 所以是会比美债高的

问题:

usd0的锁定周期太长了, 无法1:1的兑换, 会不会长期负溢价, 全套住

官方 平价套利权par https://docs.usual.money/usual-products/usd0++-enhanced-tbill/parity-arbitrage-right-par
如果usd0++和usd0严重脱锚的时候, 官方会回购一些提前解锁, 把价格拉回去

积分 pills 药丸


<!-- Content_END -->
