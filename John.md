---
timezone: timezone: Asia/Shanghai
---

# John

1. 长期从事于web开发工作，希望更深入理解defi领域知识的人。
2. 我会坚持下来并完成此次共学任务。
3. 联系方式：joancaster@outlook.com

## Notes

<!-- Content_START -->

### 2024.08.20

稳定币：
    概念：价值相对稳定的加密货币，99%的稳定币是相对于美元的汇率稳定，类似于金本位，稳定币的稳定大多是依靠资产的抵押保证其价值稳定，主流的稳定币包括USDT、USDC、BUSD、DAI等。
    意义：稳定币提供了一个相对安全的加密货币币种，给追求价值稳定的资金一个除了法币以外的选择，使得用户不用担心自己的加密货币一夜间缩水，也不用在每次停止交易后把货币提现。
    运行模式：主流的稳定币如USDT、Dai等是通过质押资产的方式保证其价值稳定，大致流程为用户抵押价值资产给运营方，运营方根据抵押物的价值给用户铸造等价或超额的稳定币，供用户自由交易；用户可以将稳定币交还给运营方，运营方将销毁归还的币，并返还等价的法币。
    USDT与Dai区别:USDT由Tether公司运营，主要抵押物是美元，体量大流动性强，受监管程度高，Dai由MakerDAO运营，主要抵押物是加密货币，体量较小，透明度高。

### 2024.08.21

稳定币的其他运作模式：
    除了以资产抵押为背书的稳定币，还有其他价值稳定模式，如弹性供应模式、铸造销毁模式、自动套利模式以及他们的组合模式。
    弹性供应模式：
    由算法调控，当价格高于目标时系统会增加所有用户钱包中的代币数量，当价格低于目标时系统会减少所有钱包中的代币数量，但变化后在总供应中的比例不变，由于它复杂性更高和价格波动较大，尚未获得广泛采用，代表币种-AMPL
    铸造销毁模式：
    代表币种-UST，用户可以以1:1的比例用Terra发行的LUNA兑换UST，反过来也可以，UST曾经是市值第三大的稳定币，由于设计缺陷导致了22年发生灾难性的崩溃，这种做法已不再被信任，这里的设计缺陷主要指系统运作依赖Anchor协议提供的20%高收益维持，不可持续。
    自动套利模式：
    价值由抵押资产和算法两部分控制，当币价高于1美元时套利者被激励代币，当币价低于1美元时套利者被激励赎回现金，铸币和赎回均是美元与代币1:1的，有一定市场认可，相比USDT来说小众。
    超额抵押模式：
    用户存入ETH获得低于抵押品的稳定币，超额抵押能提供价格波动的缓冲，如Dai

### 2024.08.22
借贷：
    专有名词：
        APR：年利率
        APY：年复利率，将产生的利息加入到本金中能产生的总利率
        流动性池：存在合约中的储备资金，用于借贷和兑换
        AMM：自动市场，主要包括Uniswap、Curve、Balancer等类型
        费率：在一次兑换交易中资金提供者收取的手续费比例
        抵押率：抵押1美元等价物获得的加密货币市值，加密货币价值低于抵押品时有被清算的风险。

### 2024.8.23
借贷：
    专有名词：
        浮动利率：流动性池利用率和利率呈折线图，拐点以前利率处于低点，鼓励用户借贷，拐点以后利率急剧上升，抑制继续借贷，减少金融风险。
        固定利率：相对固定的利率，通常高于浮动利率，可能会整体调控。
        清算：当存入的抵押物价值低于抵押物最低水平，系统会强制以3%的折扣出售借款人的抵押物用于偿还债务，偿还之后剩余的款项会还给债权人。
        强制平仓：贷款价格下降额度接近本金时会强制抛售本金偿还贷款，并且收取一定的罚款，意味着当贷款价格跌幅未达到本金时就会被清算。
        LTV：可以借入的最大金额占抵押品价值的百分比，抵押率的倒数
    AAVE:
        贡献者可以把钱存入流动性池，赚取利息
        借款人可以把币抵押给合约来换取其他币种，通常是超额抵押
        提供浮动利率和固定利率两种模式
    Alchemix:
        和AAVE类似，区别是如果抵押率低于设定值时系统会限制借款人继续借贷，直到抵押率上升回预设，不会发生强制清算；即便已经严重资不抵债，系统也只会建议借款人投入更多抵押资产，然后用现有的抵押资产产生的利息慢慢偿还债务。

### 2024.8.25
去中心化交易所：
    Uniswap：它是以太坊上最流行的去中心化交易所之一，通过自动做市商机制来提供流动性和交易服务，主要有三个版本，V1版只支持ETH和ERC20之间的交易，V2版允许任意合约的ERC20代币之间的交易，并引入了闪电贷功能、价格预言机功能以稳定交易价格，V3引入了集中流动性概念，允许做市商在特定价格范围内提供流动性，引入了多重费率等级,为不同的交易对提供更灵活的费率选择，改进了价格预言机,提供更精确和防操纵的价格数据，使用NFT来代表流动性头寸。

### 2024.8.26
去中心化交易所：
    流动性池是维持DEX运行的关键，其庞大的资金需求主要由用户提供，uniswap主要是由用户存入资产置换流动性以获取利息，兑换者的交易需要满足恒定积模型，当出现大额交易时可能会出现较大滑点，用户在交易时可以设置能接受的滑点；这种滑点会催生出套利行为：当两个交易所的价格不同时，交易者可以低价买入并在另一个交易所高价卖出，Uniswap官网：https://blog.uniswap.org/uni

### 2024.8.27
UniswapV3:
    集中流动性：用户可以选择特定范围的储量比例时才启用自己的资金，从而自动管控风险；这种设定可以使用户资金少量投入到某个主要价格活动区间，提高资金利用率的同时能有效管理风险。
    多个费用等级：平台根据不同风险等级预设了多个费率等级，在波动性大的兑换中给予高费率
    价格预言机：根据过去9天内交易价格的时间加权平均
    资金转换：当价格区间波动，流动性会逐渐做两种资金的兑换，当价格来到范围之外，资金会全部兑换成价格较低的那一边，对投资者来说相当于失去了价格上涨带来的收益
    用NFT表示价格区间：V3创新性的用NFT保存用户的买入行为，包括流动性曲线的货币种类、费率、价格区间、兑换合约地址等信息，他允许NFT持有者调整流动性、收集费用、或关闭流动性位置，可以创建基于这些 NFT 的衍生品或将其用作其他金融产品的组成部分，允许在钱包和 DeFi 平台上更直观地展示流动性位置，更容易与其他 DeFi 协议集成，NFT 可以保存流动性位置的完整历史记录等。

### 2024.8.28
UniswapV3:
    分级费率：对流动性提供了三个独立的费用等级，在ETH/DAI等非相关货币兑换时承担更高风险，有更高的费率，USDC/DAI等相关货币则相反，低风险低费率
Curve:
    目标：允许用户以低费用低滑点交换加密货币，主要是ETH和Dai等稳定币的兑换，在流动性池平衡时采用低费率，不平衡时采用高费率以促进平衡，v2版本中也支持erc20的交易
    CRV代币：流动性提供者接收CRV代币作为激励，用户可以用他们的CRV质押、投票、提升
    质押：用户质押CRV并获得veCRV，交易费用的50%以LP代币的形式分配给质押者，回报率取决于质押时间
    提升：veCRV持有者可以参与社区内提案投票，并赚取更高的流动性费率(2.5%)作为奖金
    curve wars:为了赚取更多CRV，用户之间展开的激烈竞争被称为curve wars

### 2024.8.30
聚合器：
    作用：在做币种交易时有很多DEX可选择，但是用户无法直观地选出最低的滑点和最低的费率，这种时候就依赖聚合器，它可以帮用户实现最大的交易价值，甚至可以把单笔交易拆分成多次以实现利益最大化，
    常见的聚合器：1inch 第一大聚合器，支持发币和gas退款，支持九大链(Ethereum, Binance Chain, Polygon, Optimism, Arbitrum, Gnosis, Avalanche, Fantom, Klaytn)；Paraswap

### 2024.8.31
跨链桥：
    常见的跨链模式包括：mint&burn、lock&burn、原子交换、中继链、侧链、预言机(CCIP为例)、零知识证明
    原子交换：有点相当于订单薄，以哈希锁为订单媒介，创建链1换链2的订单，在时间范围内有人下订单以链2换等额链1资产则促成交易；
    中继链：使用第三方链做跨链交易的验证器，保证了交易的安全性；
    零知识证明：使用零知识证明生成用户A在链1销毁或锁定了指定资产的证明，将证明发送到链2并铸造相应的资产；

### 2024.9.2
    combo-aggregator：继承了交易所聚合器和跨链桥的功能，能轻松实现低成本转移token及其他跨链功能
    抢跑：交易者可以提高gas费用实现抢先，会导致普通用户的交易失败、高延迟等，增加用户使用成本，可能因为被抢跑产生更大的滑点，或者套利行为被抢跑失去利润，大型交易合作者会选择使用Flashbots--一种交易打包机制来实现直接对矿工发起的打包请求，不进入公开的内存池，从而避免抢跑行为。
    尾随：机器人在检测到大型交易时可能会立刻发起一笔新的交易，企图在前者带来的价格变动中套利，这种行为是无害的。
    sandwich攻击:是抢跑和尾随的组合，例如有一笔大的ETH买Dai订单，攻击者先提高gas大量购入ETH->Dai，导致正常交易出现更大滑点，然后在正常交易打包完毕后将Dai兑换为ETH，此时由于ETH流动性比之前大幅减少的缘故，攻击者能获得比攻击之前更多的ETH，损失由正常用户的高额滑点承担。

### 2024.9.3
    MEV:最大可提取价值，指交易机器人发掘不同交易所的汇率差，从中套利的行为，总体来说它有优点也有缺点，优点是可以平衡不同交易所之间的价格，缺点是为了争抢赚取汇率差的机会，套利者可能会提高gas费用引发gas灾难，另一方面就是sandwich攻击。此外，矿工可能放弃打包套利者的交易转变成自己的交易，针对这种操作的办法是(MEV Smoothing)
    Mooniswap在交易后会延迟一段时间(通常是5分钟)才会公布交易并修改产生的影响，这样做能抑制套利行为和sandwich攻击，结果上使得流动性提供者获得更多收益。

### 2024.9.5
    基于订单簿的DEX：可以将订单放在链上或者链下，然后等待用户匹配订单后在链上完成交易，这种方法在以太坊上容易产生高昂gas费，不太现实，可以考虑二层链(如xDai)和高吞吐的新链(Solana、Ton)等，将订单放在链下，只在交易产生时修改链上信息被认为是半去中心化的。
    恒定乘积做市商公式：x * y = k,受流动性池大小的影响，大笔交易容易产生较高滑点
    
### 2024.9.6
    恒定和做市商公式  ：x + y = k,一种很理想的市商公式，可以做到零滑点，可惜只要市场间有差价就会出现套利机会，最直接的影响是套利者会耗尽市场上的流动性池，不利于正常使用者。
    恒定平均值做市商公式：(x^w * y^(1-w))^(1/n) = k，当w=0.5时为恒定积做市商公式，当w接近0或接近1时为恒定和做市商公式，这样在调整w时允许提供不平衡流动性
    稳定交换公式：是恒定积和恒定和公式的混合体，当投资组合相对平衡时交易发生在恒定和曲线上，反之则发生在恒定积曲线上，适合稳定币和包装资产的交易
    流动性挖矿：用户将流动性提供给平台，平台将铸造本土代币返还给用户，是最火的流动性吸引项目

### 2024.9.7
    聚合器将各种平台的代币差价补齐，为真正的用户提供了便利，主流的聚合器包括：1inch Network、Matcha、Paraswap
    1inch有两个原生代币：CHI和INCH，CHI是一种gas代币，可以提供42%的gas折扣，治理代币持有者可以参与自治社区的投标，包括交换费、价格影响和衰减期等多种决策。
    Matcha在交易过程中利用了链上和链下组件的组合，它除了必要的网络费用外不向用户收取交易费。
    Paraswap也有自己的gas代币，名为REDUX，通过优化链上内存空间节省gas，它会向促成的交易收取15%的费用，同时正向滑点也是他的收入来源。
    实际使用聚合器交易时受网络拥堵和流动性池大小、交易规模的影响，用户实际兑换所得可能会和交易所的报价不同。

### 2024.9.8
    借贷为两种人提供了桥梁，一种是有闲置资产希望获利的人，一种是有项目规划需要资金的人，主流的借贷协议包括：compound、maker、aave、creamFinance等。
    compound通过计算资产供需关系的算法得出利率；maker是最道德DeFi借贷协议，通过超额抵押实现借贷，支持实际资产和数字资产作为抵押；aave相比compound能借入和借出的资产多很多，并增加了利率转换、抵押品互换、闪电贷等；现在主流的借贷方式还是超额抵押，资金的利用率并不好，由于区块链的匿名交易，这里有待克服。
    稳定币分成两种：有抵押和无抵押的，无抵押的模式有AMPL通过增减整体资产保持比例不变、铸币模式仅通过控制铸币量和用户折现量来控制币价；
    算法稳定币大多都以失败告终，主流观点是认为算法币的持有者不积极参与社区的治理，特别是在价格下跌时纷纷抛售导致恶性循环。
    SUSD、UST和FRAX是算法币里和美元依旧挂钩的，FRAX成功的主要原因是和USDC挂钩、并且有动态的抵押率、更重要的是它有流动性挖矿奖励

### 2024.9.9
永续合约：
    主要特点：提供杠杆交易；无到期日，交易者可以无限期持有头寸；资金费率机制，头寸需要定期支付管理费；双向交易，可以做空或做多；有止损单和限价单等多种风险管理工具。
    perpetual提供永续合约交易，能提供最高10倍的杠杆寸头，并且资金由用户完全所有，但是资产跌幅低于保证金的6.25%就会被清算，dYdX是一个去中心化交易所，提供借贷、现货、保证金交易和永续合约交易，交易模式采用订单簿，保证金要求不低于本金的7.5%，此外还有Futureswap、MCDEX、Injective等均提供了永续协议
去中心化期权：
    提供了一个交易资产买卖权利的金融商品，用户在买入期权后就有了定时买入或卖出某项资产的权利，例如用户如果买了ETH价格为2000刀的期权，当ETH真的涨到2500时用户可以在期权卖方以2000买入ETH在商场上以2500卖出，并支付100管理费，如果价格没有大的涨幅或直接下跌，用户可以不行使期权，损失仅限于期权管理费。如果大的去中心化期权交易所如Hegic、Opyn。
    Hegic允许用户购买RTH和WBTC的美式看涨看跌期权，到期后费用将自动以购买期权的1%结算
    
<!-- Content_END -->

