emmoozii | 2020-06-29 13:45:40 UTC | #1

What do you think or know about games with cryptocurrency?
Some games use diamonds, old ones used "cash"(?), today I discovered a game called Cryptokitties that uses Ethereum to you continue the game, u buy, sell and trade ethereum kitties, I know that games like that sound very "games focused on microtransactions", but what if an online game allowed that, but it was optional, as we see in MMO games that are not focused on Pay-To-Win but provide microtransactions only for skin, etc?
Is there a module or sdk that we could study to perhaps include in our games using Urho3D?

-------------------------

tarzeron | 2020-06-29 18:07:37 UTC | #2

if you just want to accept payments look for a specific service that can process them, it will have its own SDK or RPC API

If you want to do something like cryptokitties, you need to decide for which crypto currency you will do it.

For the Ethereum very useful js and python SDK, for urho3d try watch "ethereum/aleth". In addition to sdk, you will need public full node to which you can make requests, for Ethereum this [https://infura.io](https://infura.io/). Also there you will need to write a smart contract,using solidity. 

Depending on the tasks, I would suggest making a midleware server, which will handle the state in the blockchain, and if necessary, sign the transaction on the client side in urho3d application, try using https://github.com/trustwallet/wallet-core

-------------------------

