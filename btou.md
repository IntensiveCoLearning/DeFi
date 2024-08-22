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

# {你的名字}
btou
1. 自我介绍
哈喽共学小组的小伙伴们，我是btou，目前是一名web3行业的从业者，从业时间两年，归来仍是菜鸟。目前对于L1&L2和NFT赛道会相对熟悉一点，希望能和大家多多交流。
2. 你认为你会完成本次残酷学习吗？
100%OK
## Notes

<!-- Content_START -->

### 2024.08.19
Bankless DAO-稳定币的前世今生
稳定币如何保持价格的稳定性：
通过外部资产支持；依靠复杂算法
稳定币：安全，速度，易用

世界为何需要稳定币：
稳定币和其他波动比较大的币配对可以使得加密货币的资产核算简单化；
节省资金流转时间，链上全天候资产流转
打破了国家间资金流转的不便性
摩擦、安全且低费用的全球资金转移

BitUSD、NuBits和Tether的区别：
RealCoin (Tether) 使用法定货币和其他资产（如商业票据、国库券和债券）来抵押其稳定币；BitUSD 使用 Bitshares原生代币和其他加密货币；NuBits是有史以来第一个算法稳定币，基于智能合约中一组复杂的算法创建和销毁。
目前唯一存活的只剩下Tether。

链下抵押稳定币
种类：法定货币抵押稳定币；商品抵押稳定币
法定货币抵押稳定币：
Tether；USDC；BUSD等等
商品抵押稳定币：
由其他类型的可互换资产（如黄金、贵金属、石油和房地产）支持
PAX Gold

风险：
受挂钩资产影响；SEC影响；交易对手风险；价格攻击（？）

加密抵押稳定币：
加密抵押稳定币是去中心化的，这意味着它们是由将加密抵押品存入 DeFi 协议的用户铸造（创建）的。
由于加密资产通常波动较大，因此加密抵押稳定币需要超额抵押，以确保其与美元保持挂钩。例如，要铸造 100 美元的 DAI，您需要存入价值超过 170 美元的 ETH 作为抵押品。这确保了如果 ETH 价格暴跌，仍有足够的资产支持 DAI 的挂钩。
优势和发行货币&商品抵押稳定币相反，弱点在于维持挂钩的困难；

算法稳定币
铸币税算法稳定币：
铸币税是货币面值与生产成本之间的差额。例如，一张 10 美元钞票的铸币税为 10 美元减去生产该钞票的材料和印刷成本。如果生产一张 10 美元钞票的成本为 0.01 美元，则该钞票的铸币税为 9.99 美元。

这一概念已应用于算法稳定币，通过创建一种机制，允许人们以 1 美元的成本铸造或销毁稳定币。当稳定币的价格从 1 美元波动时，铸币税会创造套利机会，一旦付诸行动，稳定币就会回到 1 美元。
实例；luna的UST
弱点：暴雷风险巨大

稳定币的未来：
Defi-高收益
私人稳定币
部分准备金（？）
央行数字货币

### 2024.08.20
去中心化的稳定币和稳定资产
主要内容：tether和DAI的缺点以及其他的稳定币
USDT
截止2021年，占稳定币市场份额的66%
通过1:1的抵押品系统维持其1美元的挂钩
缺点：发行过程非透明

DAI
其他的加密货币抵押品换DAI
超额抵押的（一般是150%以上，稳定币除外），鲁棒性强
缺点：过度抵押限制了资本效率

稳定币解决方案：
平衡DeFi的去中心化精神与创造一种能够可靠地维持其挂钩的货币
重点在维持挂钩
中心化的稳定币还是建立在一个安全假设之上：可以完全承受风险并且获得信任的中央实体

算法稳定币
算法稳定币利用算法来控制稳定币的市场结构和经济基础
对各种去中心化的算法稳定币有两种分类方法：
a) 没有抵押品（ESD、AMPL和BAC）
b) 部分/全部由他们自己的原生代币抵押（FRAX、sUSD和UST）

铸币税模式：参考昨日笔记
rebase（弹性模式）
通过改变稳定币的全部供应量来控制价格
稳定币的价格可以根据简单的通货膨胀/通货紧缩的经济理论来影响价格
eg. AMPL

可深入研究：算法稳定币的失败原因？

FRAX的成功：
USDC抵押，人们的信心共识度高；灵活抵押率；抵押品套娃转利息，支撑协议发展，提升抗风险能力；FRAX的价格波动会转移至FXS

下一代的算法稳定币
eg.
Fei
Fei在2021年第一季度末推出。与Frax非常相似，Fei使用了部分抵押系统，但纯粹由ETH支持。Fei的稳定币（FEI）与1美元挂钩，由创新概念支撑，以维持其挂钩并确保协议的整体金融稳定性。
Reflexer
RAI的预期目的是成为稳定的抵押品，并取代现有的抵押资产，如ETH或BTC
Float的例子略看不懂

稳定币的未来发展
抵押模式的延续；更加严格的奖惩制度；更强的能够增强鲁棒性的救市策略


### 2024.08.21
MakerDAO RWA
Defi：Code is law
引入新定义：RWA，借助MakerDao的角度看待RWA对于defi叙事的助力
MakerDAO和DAI
面临风险：抵押品是加密货币，如果波动太大会导致大量清算。
解决方式：将抵押品从加密货币更换为更加未定的基础层抵押品（RWA）
卡点：现实资产上链，会有荤多问题：架构设计，金融，法律合规，技术风险
代币化美债（？）

### 2024.08.22
今日加班，本周请假第一次
<!-- Content_END -->
