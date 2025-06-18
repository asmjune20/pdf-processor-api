## T TradeStation®

Mastering Iron Condors and Iron Butterflies: A Guide for Options Traders

Net Chg

High

27.26

Low

Theo Value PAL

28.68

No PAL

Vaive

-0.01

39.83

Delta

-130.01

-90.17

-0.08

-130.06

Max Profit

50.06

15.65

46.18

Max Loss

130.00)

-70.00

Volume

534.370

Theta

6,40

0,53

Beta Wetting

Account

OTM

Gamma

-5.09

52. 99

-1,15

Positions Only

Delta

1.03

Al Actorts

621/2024

Vega

0.17

-0.08

Vol AS

Vega

-1.38

0.20

0.07

017.

Theta

0.70

+ Optor Station Pro

Spend Sage

• 21 Jm 24 056

603

0 ca

Atlas Nuage Sanel

CALLS

RSARX

REGRETS

l Volty- All Opts ( 20, 0.0

Options Strategies

<!-- image -->

## Introduction

Iron condors and iron butterflies are similar options strategies that seek to profit from neutral markets and high-volatility environments. They consist of two credit strategies: the bull put and the bear call spread. We'll cover how they work, when to use them, and how to manage the risks involved.

## What is an iron condor?

To create an iron condor, you simultaneously sell two out-of-the-money credit spreads:

- I The position's profit comes from the premium collected from the sale of these spreads. The goal is for the options to expire worthless, so the premium becomes realized profit. Alternatively, if the iron condor's value drops due to time decay or a decline in volatility before expiration, it can be repurchased at a lower cost if the short options have not been assigned.
- a. One part is a bull put credit spread opened below the current price of the underlying. The short put strike is set where the trader believes the underlying price will not reach before expiration.

<!-- image -->

- b. The other part is a bear call credit spread opened above the underlying price. The short call strike is set above the highest price the underlying is expected to reach before expiration.
- c. Selling the options exposes the trader to the risk of early assignment. For the short put, this would require them to buy shares at the strike price. Assignment of the short call would require the trader to sell underlying shares at the strike price. If they do not already own them, they must buy the underlying shares at the current market price to meet the obligation.
- d. To fulfill assignment obligations on the shorts, the trader could choose to exercise their long option at its strike price. The loss would be limited to the difference between the strikes of the spread leg minus the initial premium collected.
- e. The trade profits if, at expiration, the underlying price falls between the short put and call strikes. The iron condor can also be bought to close at a lower price before expiration. While selling strikes closer to the underlying price will offer a higher premium, it also increases the likelihood of the options finishing in the money.
- 2 · The iron condor is like a short strangle but with limited risk. A short strangle collects a premium from the sale of a call and a put but has large potential risk on the put side and unlimited risk on the call side. Adding the long legs to create two credit spreads reduces the premium collected but also caps the maximum potential loss.

<!-- image -->

## What is an iron butterfly?

An iron butterfly is an options strategy similar to an iron condor, but with the key difference that the short options are at the same strike price, typically at the money. Out-of-the-money puts, and calls are bought to create the two spreads and limit risk.

With an iron butterfly, traders want the underlying to trade right at the short strike at expiration. If so, the maximum potential profit is realized, which is the premium collected from selling the spreads.

To create an iron butterfly, you simultaneously sell an at-the-money bull put spread and bear call spread:

- The two short options (put and call) have the same strike price.
- 2 Profit comes from the net premium collected from the sale of the spreads.
- 3 The goal is for the underlying price to trade as close to or equal to the short strike at expiration, maximizing the premium collected.
- 4 Like iron condors, the value can drop with time decay or lower volatility, allowing a buy-to-close at a lower cost if not assigned.

<!-- image -->

<!-- image -->

## Iron butterfly risks:

- · Both short options expose traders to the risk of early assignment.
- · An assignment on the put requires buying shares of the underlying, and an assignment on the call requires delivering the shares of the underlying. This is also referred to as, put stock to, and stock called away.
- • To mitigate the risk, the trader can exercise their long option.
- · Loss is capped at the difference between the strikes minus the premium collected.

<!-- image -->

- · Maximum profit is realized if the underlying is at the short strike at expiration.
- · Profit varies if the underlying ends up between the breakeven prices. The further it moves from the short strike, the more it diminishes the profit received.

## Iron condor and iron butterfly risk/reward profiles

- a. Reward: The net premium collected.
- b. Breakeven: There are two breakeven points.
- a. Downside: The short put strike minus the premium received.
- b. Upside: The short call strike plus the premium received.
- c. Risk: The difference between the short and long strikes on either side minus the premium collected.

<!-- image -->

<!-- image -->

<!-- image -->

## Quick Reference Guide:

## Iron Condor &amp; Iron Butterfly

| Market outlook               | Neutral and Implied Volatility is expected to decrease                                                                                                                                                                                                                               |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Position net debit or credit | Credit (premium collected)                                                                                                                                                                                                                                                           |
| Margin required              | The difference between one set of short and long strikes, minus the premium collected                                                                                                                                                                                                |
| Number of legs               | Four - one lower strike long put, one higher strike short put, one higher strike short call, and one higher strike long call with the same expiration date                                                                                                                           |
| Location of strikes          | Iron Condor - all strikes are out of the money Iron Butterfly - the short put and call have the same at the money                                                                                                                                                                    |
| Maximum profit               | The net premium collected                                                                                                                                                                                                                                                            |
| Profits from                 | The options expiring with the underlying between the two breakeven points, or from time decay, or volatility dropping                                                                                                                                                                |
| Maximum loss                 | The difference between the strikes minus the premium collected. This occurs if the underlying price rises above the long call strike or drops below the long put strike.                                                                                                             |
| Breakeven                    | Two: the short put strike minus the premium received and the short call strike plus the premium received.                                                                                                                                                                            |
| Risk from                    | The underlying price rising to or above the strike of the long call, dropping to or below the short put strike, or assignment on the short options before expiration. The use of margin is required. Review the Margin Disclosure Statement at www.TradeStation.com/DisclosureMargin |
| Options level required       | Level 3 - Click here for additional information                                                                                                                                                                                                                                      |

## Strategy application - Iron Condor &amp; Iron Butterfly

## Market Conditions

The iron condor and iron butterfly are neutral market strategies that benefit from the underlying price staying within a range. As credit spreads, they benefit when opened when implied volatility is high and expected to decline. Higher implied volatility inflates option premiums and may offer greater potential profits.

<!-- image -->

## Choosing Expirations

Shorter-term options have smaller premiums due to less time value but decay faster. They are also more sensitive to price changes in the underlying, which increases risk. Many traders aim for expirations ranging from 30 to 45 days to establish a balance between profit and time decay. Longer expirations result in higher premiums collected initially but increase volatility and assignment risk.

## Selecting Strikes

## Iron Condors

The maximum profit is realized when the options expire with the underlying between the short strikes. To increase this probability, some traders will:

- Sell an out-of-the-money put and call one standard deviation below and above the current price.

2 Buy a deeper out-of-the-money put and call two standard deviations below and above to complete the position.

Another approach many traders may use is to:

- 1 Sell the put below a support level.

2

Sell the call above a resistance level.

- 3 Choose the long put and call strikes to create the desired risk/ reward profile for the position.

## Considerations:

- · A narrower spread width reduces risk but limits potential reward.
- · Wider spreads have greater profit potential but increased maximum loss.
- · Ensure account size and risk plan allow for maximum potential loss.
- • A stop loss may be attached to mitigate risk exposure.

<!-- image -->

## Iron Butterflies

The maximum profit is realized when the underlying price is at the short strike when the options expire. Traders typically:

Sell an at-the-money put and call for the short strikes.

<!-- image -->

<!-- image -->

2 Can sell slightly out-of-the-money to create a directional bias if desired.

## Like iron condors:

- · Long put and call strikes are selected to create a risk-reward profile that aligns with the trader's risk tolerance and objectives.
- • Narrower spreads reduce both the potential risk and reward.
- • Wider spreads increase potential profit and loss.

## Risk Management

- · Ensure that your account size and risk management strategy can accommodate the maximum potential loss associated with the position.
- · Because short options involve assignment risk, the trader must maintain an account balance large enough to buy the shares they exercise.
- · Margin might be available depending on the account type. Check the requirements under TradeStation's Margin Rates available here: https://www.tradestation.com/pricing/margin-rates/.
- · Consider attaching a stop-loss order to the open position to further manage risk exposure.

<!-- image -->

## Strategy example - Iron Condor

Adobe Inc. (ADBE) is a stock that has been trading in a channel between $460 and $505 for over a month. Implied volatility is above the average, and the implied volatility/historical volatility ratio is above a high percentage.

<!-- image -->

The chosen options have 22 days until expiration. They were selected to take advantage of higher time decay and to have the position expire before the next earnings release for ADBE. Holding the iron condor through an earnings release is undesirable because of possible increased volatility and large price movements, both of which would work against the iron condor's intended profit potential.

<!-- image -->

<!-- image -->

Using OptionStation Pro, build the iron condor by holding the CTRL key on your keyboard and left-click on the bids for the option legs to sell and the asks for the legs to buy. The trade bar will appear and populate with all the option legs selected.

<!-- image -->

Placing this order would attempt to sell the 455/460/505/510 iron condor, which has 22 days until expiration, for the natural price of 1.43. $143 of premium would be collected, and $357 of margin would be required. You can review TradeStation's Options Margin Requirements here: https://www.tradestation.com/ pricing/options-margin-requirements/.

<!-- image -->

<!-- image -->

|                              | ADBE Iron Condor                                                                                                                                                           |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trade cost /margin           | $357 (Difference between strikes - premium X 100)                                                                                                                          |
| Maximum loss                 | $357                                                                                                                                                                       |
| Breakeven price down         | $458.57 (short 460 put - 1.43 premium)                                                                                                                                     |
| Breakeven price up           | $506.43 (short 505 call + 1.43 premium)                                                                                                                                    |
| Maximum profit               | $143                                                                                                                                                                       |
| Rate of return at expiration | 40.1% if ADBE is between 460 and 505                                                                                                                                       |
| Drawbacks/Risks              | 1. Options expiring with the underlying below the short put or above the short call 2. Assignment risk on the short options 3. Maximum risk is greater than maximum reward |
| Features                     | 1. Limited max risk 2. Can profit with little or no price movement 3. High probability of profit with a wide range                                                         |

When the options expire, the iron condor will achieve its maximum profit if ADBE trades between $460 and $505. The maximum loss occurs if ADBE is below $455 or above $510 at expiration. If ADBE moved below $460 or above $505, the position would begin to lose value. Once the breakeven prices are passed, the position begins to lose.

## Strategy example - Iron Butterfly

Box Inc. (BOX) has been trading in a channel around $26 to $27.50 for over a month. The implied volatility is slightly above average, and the implied volatility/ historical volatility ratio is high, suggesting that options premiums may be expensive.

<!-- image -->

Watch the Webinar - "Unlocking the Power of Iron Condors and Iron Butterflies in Your Options Trading Strategy". Discover how to go beyond directional trading and benefit from time and volatility.

<!-- image -->

<!-- image -->

We are selling the 27 put and call, which is the closest strike to the middle of the range and is at the money. We are buying the 25 put and 29 call to limit the risk. This creates a $2-wide spread on both sides.

<!-- image -->

The 25/27/29 iron butterfly has a maximum profit of $130 from the net premium collected and a maximum loss of $70.

<!-- image -->

<!-- image -->

An important detail to note is that at expiration if Box is not trading exactly at $27, one leg of the iron butterfly is likely to be assigned. The position can be closed if none of the short options have been assigned to avoid this. Time decay and a decline in volatility may lower the options premium. The position profits if the cost to close the iron butterfly is lower than the premium collected.

|                              | BOX Iron Butterfly                                                                                                                                                                                                                                                                        |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trade cost /margin           | $70.00 (Difference between strikes - premium X 100)                                                                                                                                                                                                                                       |
| Maximum loss                 | $70.00                                                                                                                                                                                                                                                                                    |
| Breakeven price down         | $25.70 (short 27 put - 1.30 premium)                                                                                                                                                                                                                                                      |
| Breakeven price up           | $28.30 (short 27 call + 1.30 premium)                                                                                                                                                                                                                                                     |
| Maximum profit               | $130                                                                                                                                                                                                                                                                                      |
| Rate of return at expiration | 185.7% if BOX is at $27                                                                                                                                                                                                                                                                   |
| Drawbacks/Risks              | 1. Options expiring with the underlying below the long put or above the long call 2. Assignment risk on the short options 3. If Box is above or below $27 at expiration, the realized profit will be less than the maximum 4. May need to be closed before expiration to avoid assignment |
| Features                     | 1. Limited maximum risk 2. The premium collected is generally higher than a similar iron condor 3. Has a narrower structure than an iron condor with less risk 4. Can profit from time and volatility decay with little or no price movement                                              |

<!-- image -->

## How to place an iron condor or butterfly?

## 1 Select a Stock or Index

- Identify a stock or index expected to stay stable or within a range. Premiums may be higher if the implied volatility is above average and is expected to drop.

## 2 Choose Strike Prices and Expiration

- a. Decide between the iron condor and the iron butterfly.
- I. The iron condor has a wider profit zone that may benefit if the price is expected to move within a range.
- Il. The iron butterfly has a higher maximum profit potential but requires the underlying price to be at the short strike at expiration, which may suit a security expected to remain stable.

b. Iron Condor:Theshort strikesdefinethe rangetheunderlying is expected to remain within until options expiration, and the long strikes define the risk and reward.

- c. Iron Butterfly: The short strikes define the range the underlying is expected to remain within until options expiration, and the long strikes define the risk and reward.
- d. Expiration: All options have the same expiration. Shorter expirations will decay faster, longer expirations carry higher time value.

## 3 Considerations

- a. The strikes of the sold options in an iron condor should be as close to the current price as possible to collect a premium but beyond the price it's expected to be at expiration.
- b. The strikes of the long options define the position's risk The potential maximum loss is the difference between strikes minus the premium collected. The premium paid for the long options reduces the premium collected from the shorts.

<!-- image -->

- c. Time decay benefits the position as it is a credit spread. Options in the spread can be allowed to expire if they are out of the money for the iron condor. With the iron butterfly, one side of the spread may be slightly in the money unless the underlying is at the short strike. To experience more significant time decay, expirations that are less than thirty days out could be chosen. Time decay increases exponentially within the last thirty days before options expiration.
- d. Longer expirations may offer greater premiums but experience slower time decay and increase the possibility of assignment on the short options. Selecting deeper out-ofthe-money options lowers the chance of assignment and the premium received.
- e. The iron butterfly must be closed before expiration to avoid assignment on one side. Automatic assignment occurs automatically at expiration if a short option is in the money by at least $0.01.

## Exiting an iron condor or butterfly

- Traders typically opt to hold iron condors until the options expire. If the options expire out of the money, the total premium collected at entry becomes profit minus commissions and fees.
- 2 An iron butterfly should be closed before expiration to avoid assignment on one side.
- 3 Close the spread by selling the bought options and buying back the sold options. Profit is realized if this is done at a lower value than the premium collected when the spread was opened.
- 4 Since time decay helps the position's profitability, consider using options with approximately 30 days or less before expiration. Closing the spread before options expiry may result in a smaller profit than the maximum.
- 5 The spread can be closed if the underlying stock or index price is above the short call's strike or below the short put's strike and the short option has not been assigned. This may result in a loss that is potentially less than the maximum.

<!-- image -->

- 6 A stop loss can be placed on an open iron condor or iron butterfly. Refer to the Options Education Center's "Placing activation rules on options orders" for more information.

## OptionStation Pro analysis

The price slices in the analysis tab of OptionStation Pro allow you to simulate the theoretical prices and profit or loss of the iron condor and iron butterfly. The prices, volatility, and/or time plots can be adjusted to estimate the effect on the position. This can be helpful in evaluating a trade before entry and determining when and if a position should be exited before expiration. Remember, the results are theoretical and estimates. Actual premiums and pricing may differ.

<!-- image -->

<!-- image -->

<!-- image -->

Explore Strategies - Discover options strategies and empower your trading with the knowledge and skills to navigate dynamic market conditions.

<!-- image -->

## Test before you trade

Access the TradeStation platform in Simulated Trading mode to acquaint yourself with strategy analysis and order entry. Utilize this environment to practice placing bear call spreads without exposing real money, allowing you to gain confidence in executing the strategy.

## Conclusion

The iron condor and iron butterfly strategies offer traders a unique approach to navigating neutral or rangebound markets and managing risk. These strategies combine a bull put spread with a bear call spread, aiming to profit from collecting premiums while benefiting from time and volatility decay. The maximum potential profit is determined by the net premium received when initiating the position, with short options collecting premiums and long options limiting risk at the expense of reduced profit potential.

To successfully incorporate the iron condor and iron butterfly into your trading repertoire, it is essential to develop a comprehensive understanding of their mechanics, risk-reward profile, and the market conditions in which they thrive. As with any options strategy, starting with small positions and gaining practical experience through exposure to various market scenarios is prudent. This handson approach will help you refine your skills and build confidence in executing these strategies effectively.

By dedicating time and effort to mastering the iron condor and iron butterfly, traders can expand their arsenal of tools for tackling neutral markets, managing risk, and pursuing their financial objectives. When employed judiciously and in the right market conditions, these strategies can serve as valuable additions to a trader's toolkit, offering a distinctive approach to capitalizing on market opportunities and optimizing risk-adjusted returns. With practice and perseverance, traders can harness the power of the iron condor and iron butterfly to navigate the complexities of the market and work towards achieving their goals with greater confidence and precision.

<!-- image -->

Review Options Level - Ready to take your options trading to the next level? Learn about your option level and make sure it's right for you. Boost your trading potential!

<!-- image -->

## Important Information and Disclosures

This content is for educational and informational purposes only. Any symbols, financial instruments, or trading strategies discussed are for demonstration purposes only and are not research or recommendations. TradeStation companies do not provide legal, tax, or investment advice.

Past performance, whether actual or indicated by historical tests of strategies, is no guarantee of future performance or success. There is a possibility that you may sustain a loss equal to or greater than your entire investment regardless of which asset class you trade (equities, options or futures); therefore, you should not invest or risk money that you cannot afford to lose. Before trading any asset class, first read the relevant risk disclosure statements on www.TradeStation.com/Important-Information.

Securities and futures trading is offered to self-directed customers by TradeStation Securities, Inc., a brokerdealer registered with the Securities and Exchange Commission and a futures commission merchant licensed with the Commodity Futures Trading Commission. TradeStation Securities is a member of the Financial Industry Regulatory Authority, the National Futures Association, and a number of exchanges.

TradeStation Securities, Inc. and TradeStation Technologies, Inc. are each wholly-owned subsidiaries of TradeStation Group, Inc., both operating, and providing products and services, under the TradeStation brand and trademark. When applying for, or purchasing, accounts, subscriptions, products, and services, it is important that you know which company you will be dealing with. Visit www.TradeStation.com/DisclosureTSCompanies for further important information explaining what this means.

Options trading is not suitable for all investors. Your TradeStation Securities' account application to trade options will be considered and approved or disapproved based on all relevant factors, including your trading experience. See www.TradeStation.com/DisclosureOptions. Visit www.TradeStation.com/Pricing for full details on the costs and fees associated with options.

Margin trading involves risks, and it is important that you fully understand those risks before trading on margin. The Margin Disclosure Statement outlines many of those risks, including that you can lose more funds than you deposit in your margin account; your brokerage firm can force the sale of securities in your account; your brokerage firm can sell your securities without contacting you; and you are not entitled to an extension of time on a margin call. Review the Margin Disclosure Statement at www.TradeStation.com/DisclosureMargin.

Any examples or illustrations provided are hypothetical in nature and do not reflect results actually achieved and do not account for fees, expenses, or other important considerations. These types of examples are provided to illustrate mathematical principles and not meant to predict or project the performance of a specific investment or investment strategy. Accordingly, this information should not be relied upon when making an investment

<!-- image -->