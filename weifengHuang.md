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

# {Breeze}

1. I'm Breeze, a software development engineer specializing in front-end and script development. I'm continuously exploring Web3 technologies, with a particular interest in DeFi, which is one of the most prominent application areas in the Web3 space. I'm eager to deepen my understanding of DeFi through this learning experience.
2. 你认为你会完成本次残酷学习吗？  
of course

## Notes

<!-- Content_START -->

### 2024.08.20
study the https://banklessdao.substack.com/p/the-stablecoin-edition-defi-download

1. Why the World Needs Stablecoins:

- Frictionless Cryptocurrency Trading: Stablecoins eliminate the need to convert cryptocurrency to fiat currency when trading, reducing reliance on traditional banking systems and their associated fees and delays.
- Faster and Cheaper International Remittances: Compared to traditional wire transfers, stablecoins offer significantly lower fees and near-instantaneous transaction speeds, making them ideal for international payments and remittances.
- Enhanced Security and Transparency: Stablecoins leverage blockchain technology, providing greater security against fraud and arbitrary seizures compared to traditional banking systems. Transactions are transparent, cryptographically secured, and require personal accountability, minimizing risks associated with intermediaries.


todo:
- Why did the Luna algorithmic stablecoin collapse?

### 2024.08.21

continue study

Types of Stablecoins

- Fiat-collateralized Stablecoins (USDT, USDC, BUSD, etc.)
- Crypto-backed Stablecoins (DAI, USDP, etc.)
- Commodity-backed Stablecoins (USDC.io, etc.)
- Algorithmic Stablecoins (UST, etc.)


The collapse of the Luna algorithmic stablecoin was due to several interconnected factors:

1. Flawed Design: The Luna/UST system relied on an algorithmic mechanism to maintain UST's peg to the US dollar. This mechanism was based on the ability to swap 1 UST for $1 worth of Luna, which was supposed to create arbitrage opportunities to keep UST at $1. However, this design was vulnerable to extreme market conditions.

2. Bank Run: When large amounts of UST were sold off rapidly, it triggered a "death spiral." As UST's price fell below $1, more people tried to redeem UST for Luna, causing Luna's price to plummet. This further eroded confidence in UST, leading to more sell-offs.

3. Lack of Sufficient Backing: Unlike traditional stablecoins backed by real assets, UST was primarily backed by Luna tokens and some Bitcoin reserves. When the system was stressed, these reserves proved insufficient to maintain the peg.

4. Market Volatility: The crypto market was experiencing a downturn, which added pressure to the already strained system.

5. Loss of Confidence: As the mechanism failed to maintain the peg, users lost confidence in the system, accelerating the collapse.

6. Complexity and Lack of Understanding: Many users may not have fully understood the risks associated with algorithmic stablecoins, leading to panic when the system showed signs of stress.

The Luna collapse highlighted the risks associated with algorithmic stablecoins and the importance of robust backing and risk management in stablecoin designs.

![Stablecoin Types](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fff01519d-c60c-4177-88f7-deb355389319_653x457.png)

[image]()
### 2024.08.22
- read the chapter “future of defi” and complete the the-stablecoin-edition-defi-download 
- read the https://nigdaemon.gitbook.io/how-to-defi-advanced-zhogn-wen-b/di-6-zhang-qu-zhong-xin-hua-de-wen-ding-bi-he-wen-ding-zi-chan
### 2024.08.23

### 2024.08.24
- study the MakerDAO, and The Maker Protocol Smart Contract Modules System is complicated
![alt text](https://docs.makerdao.com/~gitbook/image?url=https%3A%2F%2F4167714931-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-LtJ1VeNJVW-jiKH0xoL%252Fuploads%252Fuu2gnwI8XK0MXMGImPgD%252FMCD%2520System%25202.1.png%3Falt%3Dmedia%26token%3Da7898b0e-71a3-460b-a6e9-6b95b40d66f6&width=768&dpr=4&quality=100&sign=ca447c47&sv=1)
- https://drive.google.com/file/d/1VtGV8Ct2iBO8WjWsjFYLg5DnwlGmetSp/view?pli=1 
    - Vat - The single source of truth for the Maker Protocol.
    - Cat - Public interface for confiscating unsafe urns (Vaults) and processing seized collateral
    - Spotter - Allows external actors to update the price feed in Vat for a given Ilk 
- smart contract https://github.com/makerdao/dss.git；

### 2024.08.25
the maker protocol Design Considerations

1. Token Agnostic
- System is indifferent to implementation of external tokens
- The Join adapters abstract away the differences between ERC 20s, Non Fungible Tokens
(NFTs), invoice tokens, etc

2. Verifiable
○ Designed from bottom up to be well suited for formal verification; every Vat state defined
and proved
○ The Vat makes no external calls, as functions in external contracts are subject to change
○ The Vat contains no precision loss; it only adds, subtracts, and multiplies
3. Modular and Upgradable
○ Implementations of e.g. auctions, liquidation, Vault risk conditions, and new collateral types, to
be altered on a live system through Maker Governance
 Vault States within the Vat
<img width="977" alt="image" src="https://github.com/user-attachments/assets/fef56fb1-4dd4-4f19-bbbe-77619505147e">

### 2024.08.26
read the https://web3caff.com/zh/archives/80903  and [Centrifuge](https://mp.weixin.qq.com/s?__biz=MzIyNzIzODcyMQ==&mid=2678429163&idx=1&sn=ddf9712d5363e2371da050acaa7556d9&chksm=f23503c5c5428ad34513e0abf64e6984e7aacbe3c0ddb5cecc29f85806192144e40e2a2de2c7&scene=21#wechat_redirect)

- RWA: Real World Asset Tokenization

- some project such as Monetalis Clydesdal, use the On-chain governance of MakerDAO + off-chain governance of the foundation system

### 2024.08.27
read the https://mp.weixin.qq.com/s/gzr9q9kM3j-R0ec7sCb3NQ


<img width="733" alt="image" src="https://github.com/user-attachments/assets/3e970a6b-3350-498b-bed8-29365715ab55">

- paypal publish the pyUsd
- visa 

<img width="730" alt="image" src="https://github.com/user-attachments/assets/89fdfaaa-696b-4eef-b339-768feb9a59ca">

todo：
1. We can use ETH to borrow DAI, then purchase US Treasury RWA (Real World Asset), which generally yields an annual return of about 5%. This is higher than the return from staking ETH on Lido. If we adopt this approach, what are the associated risks?
2. https://debank.com/profile/0x3e8734ec146c981e3ed1f6b582d447dde701d90c/history 

### 2024.08.30
reading the https://banklessdao.substack.com/p/the-lending-edition-defi-download  and learn defi lending basic
![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8e574287-1db9-4703-a2c0-97eaed9de53f_606x526.png)

### 2024.08.31
Flash Loans
- DeFi lending has enabled the rise of "Flash Loans". Flash loans allow users to borrow assets without providing collateral for a very limited amount of time (within the same block). These loans are typically used for arbitrage opportunities between different DeFi protocols.

Use cases:
1. Creating a fully leveraged position
2. Collateral or debt asset swaps
3. Closing a position
4. Creating a liquidity mining position

smart contract：
- https://github.com/aave/protocol-v2
- https://github.com/compound-finance/compound-protocol

### 2024.09.01
lending project
- Maker
- Compound
- Alchemix
    - No Automatic Liquidations:

        Alchemix utilizes a same-asset lending model, meaning you borrow synthetic assets pegged to your collateral.
        For example, deposit ETH, borrow alETH (a synthetic asset mirroring ETH's price).
        If ETH drops in price, the value of your borrowed alETH falls proportionally.
        This mechanism ensures your Loan-to-Value (LTV) ratio remains stable, preventing liquidations.
    - Self-Repaying Loans:
        Alchemix puts your deposited collateral to work, earning yield.
        This yield is used to gradually pay down your loan balance automatically.
        Essentially, you borrow against the future yield generated by your crypto assets.
- Notional
    ![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4dc25879-deaf-487a-a12d-7476bf30ea4b_1600x1079.png)

## DeFi Lending Platforms: Features & Comparison

This table summarizes the key features and differences between the DeFi lending platforms discussed in the text:

| Feature/Functionality | Maker | Compound | Aave | Alchemix | Rari Fuse | Voltz | Euler Finance | Notional |
|---|---|---|---|---|---|---|---|---|
| **Main Function** | Over-collateralized loans, DAI stablecoin | Lending & borrowing | Lending, borrowing, flash loans | Self-repaying loans | User-created lending pools | Interest rate swaps | Lending, borrowing, flash loans | Fixed-rate lending |
| **Collateral Types** | Various governance tokens (e.g., ETH) | Various ERC-20 tokens | Various ERC-20 tokens (some ineligible) | DAI, ETH, wstETH, rETH, USDC, USDT | Any ERC-20 token |  | Various ERC-20 tokens (risk-tiered) | Stablecoins, ETH, BTC |
| **Loan Types** | DAI stablecoin | cTokens (interest-bearing) | aTokens (1:1 redeemable) | Synthetic assets pegged to collateral (e.g., alETH) | Based on pool settings |  |  | fCash (fixed-rate tokens) |
| **Interest Rate Type** | Stability Fee (similar to interest) | Variable | Variable or stable | Auto-repaid via collateral yield | Based on pool settings | Market-determined |  | Fixed |
| **Liquidation Mechanism** | Yes, triggered below collateralization ratio | Yes, triggered below collateralization ratio | Yes, triggered below collateralization ratio, AAVE token as backstop | No automatic liquidations | Based on pool settings |  |  | Yes |
| **Unique Features** | First DeFi project, DAI stablecoin | cTokens track earnings | Stable rate option, flash loans, AAVE token backstop | No liquidations, automatic repayment | Highly customizable, risk isolated | DeFi Interest Rate Swaps |  Supports various assets, risk tiering, multiple functionalities | Fixed-rate loans, fCash tokens |
| **Advantages** | High security, long history, stable | Easy to use, good UX | Feature-rich, flexible | Reduced liquidation risk, no manual repayment | Meets diverse needs, manageable risk | Offers fixed-rate products, enables new trading strategies | Wide range of assets, robust risk management | Fixed rates, predictability |
| **Disadvantages** | Potentially higher interest rates | Variable interest rates | Stable rates not perfectly stable | Yield uncertainty, limited use cases | Users must assess risk themselves | Market immaturity | Potentially complex to use | Platform risk, liquidity risk | 



### 2024.09.02
reading 
- https://nigdaemon.gitbook.io/how-to-defi-advanced-zhogn-wen-b/di-5-zhang-qu-zhong-xin-hua-de-jie-dai
- https://www.notion.so/lxdao/DeFi-642bdcdbc2304e0bbb7da998cc084299

### 2024.09.03
Attempting to connect to the testnet using Aave, obtain test tokens, and go through the lending process. However, I'm currently unable to proceed on Aave as it keeps prompting to use the mainnet. Still trying to figure it out.

- Oracle Price Contract: https://etherscan.io/address/0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419#code

### 2024.09.04
turned on the testnet switch in the top right corner of the Aave system, and tried using the supply and borrow functions. Details can be found at https://sepolia.etherscan.io/address/0x54e5e5D90eB14e642d4c880c74ffd42D3762b1bb

aave flash loan: https://docs.aave.com/developers/guides/flash-loans

### 2024.09.07
reading https://banklessdao.substack.com/p/the-amm-edition-part-i-defi-download】

AMM: Automated Market Maker

price mechanism: A * B = k 

- The mechanism would be a smart contract that holds A tokens of type T1, and B tokens of type T2, and maintains the invariant that A * B = k for some constant k (in the version where people can invest, k can change, but only during investment/withdrawal transactions, NOT trades).

project
- uniswap
- balancer
- curve

### 2024.09.08
reading 
    - https://banklessdao.substack.com/p/the-amm-edition-part-ii-defi-download
    - https://nigdaemon.gitbook.io/how-to-defi-advanced-zhogn-wen-b/di-7-zhang-de-xue-jie-de-jie-dai
    - https://nigdaemon.gitbook.io/how-to-defi-advanced-zhogn-wen-b/di-4-zhang-dex-ju-he-qi
    
DEX Aggregators
 - In the future, there won't be a single aggregated website, but rather DEX aggregation functionality will be built into wallets or products directly.
 - MEV
    - Arbitrage
    - Liquidations
    - Front and Back Running    
    - Sandwich Trading
 - 1inch

TODO:
    - use uniswap and 1inch to swap token
<!-- Content_END -->    

