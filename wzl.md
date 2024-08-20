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

# {wzl}

1. 自我介绍：区块链硕士，defi研究者，web3学习者
2. 你认为你会完成本次残酷学习吗？会的

## Notes

<!-- Content_START -->

### 2024.08.20
## MarkerDAO学习笔记
### 概念

MakerDAO 是一个基于以太坊的去中心化超额抵押稳定币协议，其核心产品是 DAI，一种与美元挂钩的稳定币。MakerDAO 的目标是通过超额抵押机制来维持 DAI 与美元的 1:1 锚定，并提供一个去中心化、透明和安全的金融系统。

### DAI 的运行逻辑

1. **抵押:** 用户将支持的资产（例如 ETH、USDC 等）存入 MakerDAO 的 Vault（保险库）中，并按照一定比例获得 DAI。
2. **借出:** 用户可以将 DAI 借出，并支付稳定费 (Stability Fee) 作为利息。
3. **偿还:** 用户需要偿还借出的 DAI 和稳定费，才能取回抵押资产。
4. **清算:** 如果抵押资产的价值低于债务和稳定费，Vault 会被清算，抵押资产会被拍卖，拍卖所得用于偿还债务。

### 价格稳定机制

MakerDAO 通过以下机制来维持 DAI 的价格稳定：

1. **稳定费调整:** 当 DAI 价格高于 1 美元时，降低稳定费，鼓励用户创建 Vault 生成 DAI；当 DAI 价格低于 1 美元时，提高稳定费，刺激用户关闭 Vault 销毁 DAI。
2. **DAI 存款利率 (DSR) 调整:** 用户可以将 DAI 锁定在 MakerDAO 的 DSR 合约中获得储蓄收益。当 DAI 价格高于 1 美元时，降低 DSR，减少 DAI 的需求；当 DAI 价格低于 1 美元时，提高 DSR，增加 DAI 的需求。
3. **紧急关停:** 在紧急情况下，MakerDAO 可以触发紧急关停机制，暂停 Vault 的创建和操作，并冻结喂价机制，以保护 DAI 持有者的利益。

### PSM 模块

PSM (Peg Stabilization Module) 是 MakerDAO 推出的锚定稳定模块，旨在为 DAI 的价格提供双边缓冲保护。用户可以将支持的稳定币资产（例如 USDC）存入 PSM，按照 1:1 的固定汇率铸造 DAI，并支付 0.1% 的交易费用。

### 清算和拍卖机制

当 Vault 的抵押资产价值低于债务和稳定费时，会触发清算机制。清算过程包括：

1. **清算拍卖:** 抵押资产会被拍卖，拍卖所得用于偿还债务。
2. **债务拍卖:** 如果拍卖所得不足以偿还债务，会进行债务拍卖，用户可以用 DAI 支付债务，并获得一定数量的 MKR 作为奖励。

### 生态

MakerDAO 的生态系统不断发展，包括：

- **DAI:** 稳定币
- **Vault:** 保险库
- **PSM:** 锚定稳定模块
- **Spark Protocol:** 借贷协议
- **Endgame Plan:** 去中心化计划

### 竞争对手

MakerDAO 的主要竞争对手包括：

- **Aave:** 去中心化借贷协议
- **Frax Finance:** 混合型稳定币协议
- **Curve Finance:** 稳定币交易平台

### 总结

MakerDAO 作为去中心化超额抵押稳定币协议的先驱，其 DAI 稳定币已经成为 DeFi 生态系统的重要组成部分。MakerDAO 正在不断发展和创新，并积极探索新的应用场景，以实现其去中心化和金融普惠的目标。

### 2024.08.19
了解稳定币的概念以及分类，笔记如下：
## 稳定币学习笔记

**1. 稳定币概述**

* 稳定币是加密货币生态系统的重要组成部分，旨在提供稳定的价值存储和交易媒介。
* 稳定币通常与法定货币挂钩，例如美元，以降低价格波动性。
* 稳定币可以分为中心化稳定币和去中心化稳定币。

**2. 中心化稳定币**

* 例如 Tether (USDT)，由中心化实体发行并由法币储备支持。
* 优点：价格稳定，易于使用。
* 缺点：缺乏透明度，依赖中心化实体，存在系统性风险。

**3. 去中心化稳定币**

* 例如 MakerDAO 的 Dai (DAI)，通过抵押加密货币来维持价格稳定。
* 优点：去中心化，透明度高，抗审查。
* 缺点：资本效率低下，抵押品风险，价格波动性。

**4. 算法稳定币**

* 利用算法来控制稳定币的市场结构和经济基础，旨在实现去中心化和价格稳定。
* 例如 Ampleforth (AMPL) 的弹性模式和 Empty Set Dollar (ESD) 的铸币税模式。
* 优点：去中心化，价格稳定性。
* 缺点：复杂性高，风险较高，需要强大的社区支持。

**5. 新一代算法稳定币**

* 例如 Fei Protocol、Reflexer 和 Float Protocol，在抵押机制、交易者激励措施和紧急救市措施等方面有所创新。
* 优点：更高的资本效率，更强的价格稳定性。
* 缺点：仍处于实验阶段，需要时间和实践来验证其可行性。

**6. 稳定币的未来**

* 稳定币市场将继续增长，机构采用将加速发展。
* 监管环境将更加完善，稳定币将更加安全可靠。
* 稳定币将在日常生活中得到更广泛的应用，例如支付、跨境汇款和工资支付等。

**7. 总结**

稳定币是 DeFi 生态系统的重要组成部分，为加密货币市场提供了稳定性。算法稳定币是稳定币发展的重要方向。未来，稳定币将更加安全可靠，并在日常生活中得到更广泛的应用。

<!-- Content_END -->
