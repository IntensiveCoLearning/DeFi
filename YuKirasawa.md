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

# YuKirasawa

1. 自我介绍

   YuKirasawa，希望学习一些 DeFi 的技术。

2. 你认为你会完成本次残酷学习吗？

   会

## Notes

<!-- Content_START -->

### 2024.08.20

大体了解了各类稳定币。

1. 法币抵押稳定币：通过法定货币资产储备保证与法定货币价格的锚定。现在常用的 USDT、USDC 都属于此类。其风险主要在于资产储备的真实性。
2. 加密货币抵押稳定币：通过加密货币资产储备保证其价格的稳定。由于抵押资产具有价格波动，需要超额 (比如 150%) 的资产抵押。链上资产抵押的透明度较高，但即使存在超额抵押，仍有抵押物价格剧烈波动产生黑天鹅事件的可能。
3. 算法稳定币：通过算法调整供应量，从而试图稳定其价格。不需要抵押资产，从而缺少“硬通货”提供的信心，容易从抛售行为演变为崩盘 (死亡螺旋)。

### 2024.08.21

MakerDAO 的稳定币 DAI 是一种使用多种链上资产抵押的稳定币。Maker Vault 是存储抵押资产的智能合约，用户可以通过将资产存入 Maker Vault 来生成 DAI. 存入抵押品获得 DAI 的过程可以看成通过抵押向 Maker Vault 借出 DAI. 还回 DAI 时需要支付稳定费 (Stability Fee)

Maker Vault 接受的担保品资产由 MKR 持有者投票纳入，并确定其清算率。清算率决定了抵押资产会在多少的超额抵押率下被清算。

Maker Vault 的拍卖机制：在进行清算时，Maker 协议会使用基于市场的拍卖机制将担保物卖出，这被称为担保品拍卖 (Collateral Auction)。拍卖得到的 DAI 会偿还从 Maker Vault 的借款。

Dai Savings Rate (DSR) 允许 Dai 用户获得储蓄收益 ，只需用户将他们的 DAI 锁入 Maker 协议的 DSR 合约即可，该合约可以通过 Oasis 的存款平台或其他接入 Maker 协议的平台访问。DSR 合约不对用户设置最低存款要求，用户可以随时从 DSR 合约中取出部分或全部 Dai。

DSR 是一个系统全局参数，决定了 Dai 持有者可基于其存款获得的收益。当 Dai 的市场价格由于市场变化而偏离目标价格时，MKR 持有者可以通过投票更改 DSR 来维护价格的稳定性。

当 DAI 低于挂钩价时：系统会提高稳定费，激励用户偿还债务、取回抵押品，或者提高 DAI 储蓄率，增加 DAI 的需求。

当 DAI 高于挂钩价时：系统会降低稳定费，激励用户抵押资产借出 DAI，或是降低 DAI 储蓄率，降低 DAI 的需求。

Ref: https://makerdao.com/zh-CN/whitepaper/

<!-- Content_END -->
