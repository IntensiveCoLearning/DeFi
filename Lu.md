---
timezone: Asia/Bangkok
---

# Lu Zhiyuan

1. 自我介绍
   参与过L2的空投，也做过L2的项目方。现在想补补基础，有更好的web3 native，所以报名共学活动。个人说明书见 https://p1i72gf0sn.feishu.cn/wiki/WdSMwvDOeiULi5kyhO9cXT5onGc
2. 你认为你会完成本次残酷学习吗？
   会。我都要完成zk了。
   
## Notes

<!-- Content_START -->

### 2024.08.20

笔记内容。先看一下能不能打卡成功。昨天打卡出问题了。

### 2024.08.22
去中心化的稳定币 & 稳定资产
=============
1. 稳定币总市值（total market capitalization）上升的原因：稳定（non-volatile assets）。    

2. 中心化稳定币（Centralized Stablecoin）USDT VS 去中心化稳定币（Decentralized Stablecoin）DAI。   
      
USDT是2015年在Bitfinex交易上市。它具有先发优势（first-mover advantage），于2021年占40b的总市值（market capitalization），这约是66%的市场份额（market share）。 
       
   Tether maintains its $1 peg (挂钩） through a 1:1 collateral system (1:1的抵押品系统).       
    
   Tether的缺点也来自于它是中心化的、不透明的（non-transparent issuance process）。2019年，它们修改条款，把loans（贷款）to affiliate companies as part of its 
   collateral reserve（抵押品存储），人们怀疑它并不具备所说的有那么多的现金储备（reserves）。  
          
*   好困惑，为什么loan比起现金更没有价值？因为钱不一定追得回来，还是说因为贷款可能是虚高？    
      
   DAI作为借贷协议（lending protocol），是作为借贷需求（borrowing demand）的副产品被发行的。通常是当抵押品（collateral）（通常是ETH）被存入Maker金库（vaults）时。
*   这句话也没有太明白    

   金库（vaults）是超额抵押的（overcollateralized），有助于防止黑天鹅事件(black swan events)，即抵押资产（the collateral assets）的价值大幅下降。
*   超额抵押我能理解，类似于我存入100刀ETH，只能借出来60刀的DAI。
    
DAI的问题在于它的发行方式（over-collateralization）限制了资本效率（limits capital efficiency），很难使得DAI扩大规模（scale with demand）。
*   什么叫做capital efficiency？

人们试图通过Peg Stability Module solution等方法解决DAI遇到的问题，但是DAI的需求是受杠杆需求（leverage）而扩大的，而非是对对更分散的交易媒介（medium of transaction）。      
     
3. 所有稳定币需要解决的问题。   
     
   ethos of decentralization VS  creating a currency that can reliably maintain its peg
   去中心化精神 和 资产稳定
       
4. 算法型稳定币（algorithmic stablecoins）和稳定资产（Stableassets）。   
### 2024.08.23
昨天学习了作为中心化稳定币USDT和去中心化稳定币DAI的各自发行机制以及其弊端，今天要了解其他的稳定币类型，即算法型稳定币。   
稳定币的不可能三角是去中心化（decentralization）, 币价稳定（price stability）, 资本效率（capital efficiency）     
  
   算法型稳定币 & 稳定资产
   =============
      
1.1 是何？   
   
算法型稳定币就是用算法来调节币价。   
算法型稳定资产的特点是浮动挂钩（a floating peg），可作为抵押品（Collateral）。 
       
1.2 分类？    
   
algorithmic stablecoins 可分为两类 
      
   1） 没有抵押品      
   2） 部分或全部（partially/fully）由原生代币抵押     
依靠自身发行的资产（natively issued assets）作为抵押品会产生递归的价值（recursive value），需要算法功能来调节价格（regulate the price）。
      
还可以分类成   
   
   1）rebase（弹性）    
   
特点：改变供应量（changing the entire supply）   
理由：通货膨胀/通货紧缩的经济理论（inflationary/ deflationary economic theory）    
应用例子：Ampleforth     
   
   2）seigniorage（铸币税）模式   
   
特点：a reward system   
三种模式迭代（three basic iterations）：Empty Set Dollar -> Basis Cash -> Frax Finance   
     
Empty Set Dollar是单币抵押模式（a single-token seigniorage model）   
Basis Cash是双代币征税模式（a dual-token seigniorage model）   
Frax Finance是由两种类型的抵押品支持，法币(Fiat）稳定币USDT和原生代币FXS，且是零散的抵押方式。Frax稳定币（FRAX）可以被铸造，并允许从协议中赎回1美元的价值。    
* 这里Frax看不太明白原理。还有为什么偏偏是1美元的价值？   
     
1.3 发展情况？

   1.4 为什么Frax能成功？

   1.5 算法型稳定币 & 稳定资产的未来
### 2024.08.24 
关键词：overcollateralization、CDP、Maker Yield Pool、Governance Polls、Executive Voting
 =============
学习方式：MakerDAO案例学习    
学习材料：https://www.binance.com/en/square/post/43195  
预期学习收获：看看MakerDAO如何在以波动性强的货币作为抵押品的情况下，仍然保持与美元1:1挂钩的      
      
1. What：MakerDao是何     
Rune Christensen https://twitter.com/RuneKek 发起的一个DAO组织      
ETH项目      
用户通过Oasis DApp访问MakerDAO，申请抵押贷款      

2. What：DAI是何      
     DAI是MakerDAO的稳定币，与美元挂钩     
     MakerDAO使用加密货币抵押品来维持DAI挂钩比率
     凭什么能用加密货币（不稳定）作为抵押物？——超额抵押。
   
4. How: DAI的用例（Use cases）     
        杠杠（Leverage）和 DAI储蓄率（Savings Rate）
        前者例如，预见到ETH会上涨，就用ETH抵押借出一部分DAI，再用这部分DAI去购买更多的ETH。
   
5. How：（加密货币）抵押品如何运作？     
     实物（Physical）抵押品，如当铺支持珠宝 -> 法币抵押品（Fiat Collateral），如BUSD支持法币 -> 加密货币抵押品，如DAI支持加密货币

     What：超额抵押是什么？    
     是面对加密货币作为抵押品的价格波动大、贷方有更大风险时的一种解决方案，如要付出500美元的ETH才能借到300美元的DAI。
     
     What：抵押债务头寸（CDP）是什么？     
     CDP = Collateralized Debt Position     
     是个position，由智能合约（smart contract）、抵押品（collateral）、已发行的抵押品支持的稳定币 三个特征构成     
     功能是设置强制平仓比率（a forced liquidation ratio）     
     * “头寸” 是用来描述投资者或交易者持有的资产或负债的一个术语          
      
6. What：Maker收益池（Maker Yield Pool）是什么？      
      users place collateral and generate DAI
* Yield是指协议产生的收益——用户需要支付stability fee，而不是直接归属于用户的回报           
     
7. Why：DAI的价值能保持稳定（remain stable）？     
the CDP mechanism + 调整 stability fee + 调整 the DAI savings rate     
* stability fee 相当于贷款利率，费用增加时，借款成本变高，这会减少借款者的需求     
* DAI savings rate相当于存款利率。当 DAI 储蓄率增加时，持有 DAI可以获得更多的利息，吸引更多人持有 DAI，从而减少 DAI 的流通量，维持 DAI 的稳定价值。
       
9. How: participate in MakerDAO’s governance system      
持有governance token, MKR      
两种参与方式      
Governance Polls 更倾向于非技术性治理决策      
Executive Voting 涉及技术性的变更，尤其是与智能合约代码相关的调整
### 2024.08.25 
关键词：RWA - Real World Assets、SPV - Special Purpose Entity、Legal Wrapper
 =============
学习材料：https://web3caff.com/zh/archives/80903      
预期收获：从MakerDAO RWA 看链下资产的治理体系与交易架构    
关联待看：从Centrifuge看链下资产上链的路径      
      
      1. why：为什么需要捕获链下资产？            
      链下资产可以补充现有抵押物的不足
      * 2021年的DeFi Summer都出现了哪些不可持续的DeFi收益率产品？为什么会在那个夏天涌现，有什么利好的消息使得当时大家都做DeFi吗？这样的情况有可能再次上演吗？
      
      2. How：如何捕获链下资产？            
      最简单的方式是购买第三方发型的代币化美债，如Solv Protocol推出的两只RWA基金是由Red Cedar Digital. Ltd. 提供的代币化美债。      
      ———这样做的弊端是如果第三方跑路就完蛋。      
      最好的方式是构建适合链上协议或DAO组织的治理体系和法律架构。      
      
      2.1 Why：为什么需要法律包装（Legal Wrapper）      
      交易对手风险（对方拿钱跑路）；主体资格认证（不然没法购买链下资产）；破产清算资格（同二，没有主体资格，对手跑路了就没办法追责）     
   
      2.2 How：如何进行法律包装
      “下设” 对应的法人实体，使得DAO或者链上协议在相关司法辖区下有公认的法律地位。
      Foundation + SPV or Trust
      
      3. How：MakerDAO 的 RWA 实践案例
      * 这部分内容略过，难度系数略大，就看了一遍留个印象
      3.1 New Silver Restructuring（信贷资产 RWA）
      Foundation + SPV 的交易架构
      3.2 BlockTower Credit（信贷资产 RWA）
      3.3 BlockTower Andremeda（美债 RWA）
      3.4 Monetalis Clydesdale（美债 RWA）
      3.5 Centrifuge——RWA Roadmap（美债 RWA）
      * 为什么有「美债 RWA 5% 的无风险收益」？无风险的收益是怎么做到的？
      * 什么叫做把「基金代币化」？自己发币，1:1的那种，类似于买了个链上支票吗？
      
      4. 目前发展的弊端以及未来？
      弊端：不是任何RWA平台将资产上链后，所有用户就可以参加。
      目前大多数RWA项目只针对单一/限定资金方，或合格投资者，无法做到散户都能参与。
      RWA 和 DeFi 结合，可以无需许可（为什么？）
      * 关注RWA和DeFi结合的项目是怎么做到无需许可，同时散户参与的理由是什么？

### 2024.08.26
Stablecoin
=============
学习材料：[banklessdao-defi-download-stablecoin](https://banklessdao.substack.com/p/the-stablecoin-edition-defi-download)
预期收获：stablecoin的相关知识，之后可以学习代币经济学（tokennomics）、liquidity pools等关联信息。
 

<!-- Content_END -->
