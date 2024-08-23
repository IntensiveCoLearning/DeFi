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
1. 算法型稳定币 & 稳定资产
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
<!-- Content_END -->
