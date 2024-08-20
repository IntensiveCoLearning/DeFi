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

# Ray

1. 自我介绍
一个 Web3 开发者，也是这次 Defi 共学的发起来人之一
2. 你认为你会完成本次残酷学习吗？
必须可以，这是 Web3 从业者的必备技能

## Notes

<!-- Content_START -->

### 2024.08.19
- DeFi：全称是 Decentralized Finance，允许用户在无需依赖中心化实体的情况下，使用借贷和交易等应用的金融服务
- 其中稳定币是 DeFi 的基石，可以被认为是乐高中的最小零件， DeFi 的高楼就是在这个基础上搭建起来的
- 稳定币是一种加密资产，使用各种机制将其价值维持在一个记账单位，比如一美元或者一港币，稳定币获得底层协议的安全性、交易速度和易用性
- 为什么需要稳定币：
    - 需要提供一个稳定的价值锚点，为加密获得交易提供桥梁
    - 无摩擦、安全且低费用的全球资金转移
- 稳定币的分类：
    - 链下抵押稳定币
        - 法定货币抵押稳定币，直接与法定货币挂钩，比如 USDT 和 USDC
        - 商品抵押稳定币，与黄金、石油等实物资产挂钩，比如 PAX Gold
        - 风险：
            - 法定货币价格波动
            - 链下抵押资产的透明度
            - 监管风险
            - 价格攻击
    - 链上原生稳定币
        - 加密货币抵押稳定币，使用加密货币本身去生成稳定币，比如 Dai
            - 优点：
                - 去中心化程度高
                - 合约决定，不需要信任基础
                - perminssionless
                - 不受监管影响
            - 缺点：
                - 挂钩困难，价格波动大
                - 因为需要超额抵押，资本效率低下
        - 算法稳定币，利用维持价格挂钩的算法，通过各种机制调节稳定币的供应来实现稳定币，比如 UST
            - 算法稳定币的主要类型：
                - rebase 模式
                - Seigniorage 模式（铸币税模式），当前主流的选择，UST 就是使用的这种方式
            - 优点：
                - 合约决定，不需要信任基础
                - 资本效率高
            - 缺点：
                - 未经测试，风险高
- 稳定币的未来：
    - 目前稳定币的采用潮流不可阻挡，越来越多人使用
    - 会被当做一个主流的资产类型，在加密市场中的各个地方使用
    - 稳定币其实是对央行的一种模仿，那么对于 CBDC 来说，稳定币或许是一种威胁，央行会放任一个全新的央行来威胁自己吗？这里还是有很大的风险

### 2024-08-20
- USDT 和 USDC 的原理相对简单，链上发行了多少，链下就抵押多少等值的美元资产
- 而 DAI 是由链上的机制来完成 mint 和销毁
- DAI 在链上是一个标准的 ERC 20 合约，精度为 18，目前 mint 的量超过了 30 亿，超过 50 万个地址持有：https://etherscan.io/token/0x6b175474e89094c44da98b954eedeac495271d0f#code
- 整体逻辑：用户抵押该协议支持的资产，从而获得铆钉美元的去中心化稳定币 DAI
    - 涉及行为：存入、取出、借出、偿还，DAI 的发行和赎回过程
    - 未偿还资产：涉及利率调整和清算，也就是 DAI 锚定美元价格的方式
- 目前存在两种抵押方式：
    - 单抵押品 DAI 系统（SCD），只支持 ETH 进行抵押
    - 多抵押品 DAI 系统（MCD），支持 ETH 之外的抵押品类型
- 整体流程：
    - 用户存入资金，创建 Valut 
    - 用户获得 DAI，并且产生一个同等价值的债务
    - 用户偿还借出的 DAI 及稳定费 DAI，还清债务
    - 偿还之后可以取回抵押品
- 价格稳定机制：
    - 稳定利率调整：
        - 用户抵押生成 DAI 要支付的利息，当 DAI 价格高于 1 美元，降低稳定利息鼓励用户生成 DAI，低于一美元，增加稳定利率销毁 DAI
    - DAI 存款利率（DSR）调整
        - 用户将 DAI 锁进 Maker 获得储蓄收益，DSR 决定收益大小，由贷款利息支付。如果 无法弥补 DAI 存款利息支出，那么将增发 MKR 进行弥补
    - 紧急关停：
        - 用户无法创建 Valut，或者操作已经创建的 valut，用来保证 DAI 持有者目标价格可以兑付的最后手段

<!-- Content_END -->
