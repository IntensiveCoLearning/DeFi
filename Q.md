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

# {Q}

1. 我叫Q 也是这次残酷 DeFi 的发起人 
   DeFi 在web3 的世界里 贯穿了所有项目，对于传统 web2 的世界里金融是很重要的一环，web3 重塑了金融的概念，利用数学和智能合约打破了原来的某些界限，如果你闯荡在 web3 的世界，定要学习 DeFi 打败周围99%的传统人。希望大家能学习下去～
2. 我可以完成本次学习

## Notes

<!-- Content_START -->

### 2024.08.19

看了 USDT 的官网，发现tron 的发行数量还是超过了ETH 上发行的数量，看来孙哥当时的USDT 免手续费威力真的很猛，同时也看了usdc 发行量，就没有tron 的发行，大多数都在ETH网络上，而sol 上 usdt+usdc 的发行量也只有3.2b 

今天把测试网的token 进行了claim

https://sepolia.etherscan.io/tx/0xb829df95d25530e91e0c57dce33dd42c9368a75b92b862f1e7d597b81ecbf378

### 2024.08.21
今天学习了 USDC 母公司发表的文章
代币资本充足框架（Token Capital Adequacy Framework, TCAF），这是一种为稳定价值代币（包括稳定币、存款代币和代币化现金）设计的基于风险的资本框架
	1. 鼓励在产品设计、开发周期及日常运营中持续改进风险管理实践；
	2. 通过风险评估过程中的决策和输入，引入对风险责任人的问责制；
	3. 为“持续经营”提供足够的损失吸收能力，以确保业务的持续运作；
	4. 保护监管机构和公共部门免受溢出风险的影响，同时增强对受监管的稳定价值代币的消费者保护和信任。

今天把测试网的token 都进行了claim

https://sepolia.etherscan.io/tx/0x688379c9a45b0af05345c1ae678d97a9af4182d40a8c1d58fcfb0d9d664461f4


### 2024.08.22

今天继续学习了 USDC 母公司发表的文章
他们提出了资本框架我们提出的资本框架模型强调以下五个目标：
1. 提供“持续经营”和“终止经营”情况下的损失吸收能力。
2. 补充对操作风险的监管干预措施。
3. 保持简单的同时，尽可能地反映现实中的复杂尾部风险。
4. 提供跨机构和司法管辖区的可比性。
5. 提供激励措施，以最小化和缓解风险事件带来的负外部性。

今天把测试网的token 进行了 稳定币 mint
https://sepolia.etherscan.io/tx/0x5e067a0bb5d66e69d187da1917f6d386c6bf9f86c01892c38139c1715d0695f4

### 2024.08.23
今天学习了
用于金融风险的资本 (κF) 包括针对市场和信用风险敞口的准备金，我们分别用 κF,M 和 κF,C 表示。我们保守地假设市场和信用风险有100%的相关性，即：

 \kappa_F = \kappa_{F,M} + \kappa_{F,C} 

 通过将极端损失部分与清算价格影响部分结合起来（均以收益表示），我们得出市场风险的总体资本 κF,M：

 \kappa_{F,M} = - (L_{M,min} + \delta_p) e_M 

对于某些加密资产支持的代币或算法稳定币，δp 可能较大。例如，在支持算法稳定币 Terra 的 Luna 代币的情况下，δi 可能接近 -100%，因为 Terra 的赎回需求导致 Luna 实际上失去了所有的价值。

今天在测试网里进行了跨链操作：
https://holesky.etherscan.io/tx/0x2b84676b85c7b436d8af1426ee69a294679032c431c381cfe1a6b90b192f2e6e

### 2024.08.24
今天周末花的时间比较少 主要是在测试网进行了借贷
https://sepolia.etherscan.io/tx/0x9ad187878714605db7445146a67ee6904fa939d8215be0514efec8ea46aedd7d

### 2024.08.25
今天继续学习了
技术、基础设施和运营风险：这个运营风险模型使用了“风险价值”（Value at Risk, VaR）的概念来估算罕见尾部事件中的严重损失。VaR模型通常被风险专业人士和监管机构使用。该模型依赖于对损失严重性（通过‘损失阈值’捕捉）和相应的损失频率的联合拟合。‘损失阈值’是指一种损失值，在高于特定置信水平的概率下，预计损失金额不会超过该值。例如，一个99%置信水平的VaR是指，在99%的概率下，损失事件造成的损失金额不会超过该值。这个置信水平对应于每100年发生一次的事件。

链上今天继续进行了mint 稳定币
https://sepolia.etherscan.io/tx/0x9649043dac44a02a48fa7d037fa1651c6350b8adda05077ec3df3674a42a31b7

### 2024.08.27
稳定币的学习告一段落 之后继续学习。
今天开始学习借贷相关的。主要是看aave 的历史。
Aave 协议 V3 允许已批准的桥接器在源网络上销毁aToken，同时在目标网络上立即铸造它们。然后，基础资产可以在通过桥接器移动后，通过将其传递到池中，以延迟方式在目标网络上提供给 Aave。
aave 已经将协议升级至了 v3 
用户将桥接 tx提交给经过验证的桥接协议（比如 Connext），并且在tx被挖掘后就可以访问目标链上的资金。

幕后桥接协议：

在目标链上铸造无担保的 aTokens到中间合约，然后立即提取和转移基础资产给用户。

批量处理多个桥接交易，并将基础资产实际转移到 L2

稍后，一旦资金在 L2 上可用， L2 上的桥接合约（即具有BRIDGEAave V3 上的权限）就会向 Aave 池提供基础资产和费用，以支持之前铸造的未支持的 aTokens。

今天进行了lend 操作
https://explorer-holesky.morphl2.io/tx/0x707ac8c7ba996e3edd80503b5befc1747ee81b37704cb0552c54af6cfab618cb

### 2024.08.28
今天主要是进行了 借贷操作
https://explorer-holesky.morphl2.io/tx/0x72c131ee19aa5bacda161ea0678b74d30febbf7b37763c11acb11b29e46acce1

### 2024.08.29
今天学习了aave 的代币经济升级，
Aave目前为可能发生的协议坏账提供了准备金，该机制被称为“安全模块”，这部分准备金目前由三部分构成：
质押的Aave，现价值2.75亿美金
质押的Aave原生稳定币GHO，现价值6000万美金
质押的Aave-ETH LP，同时也是Aave链上流动性的主要来源之一，现价值1.24亿美金

他们上线了一个安全模块，类似于cex 的平台保证金

<!-- Content_END -->

