## Serf gossip protocol

It is based on "SWIM: Scalable Weakly-consistent Infection-style Process Group Membership Protocol"

A node can join either an existing cluster or create a new cluster. 
If a new cluster is created then when new members arrival is waited for. If a node joins an existing cluster, then it is given the address of at least one existing member of the node. The new node does a full state sync with the existing member over tcp and then begins gossiping its existence to the cluster.

Gossip is done over UDP at fixed intervals(???Why is gossip done over UDP?). Full state sync is done over TCP also at fixed interval which is much larger than gossip interval(??? Why is full state sync required. It is required as it increases the likelyhood of convergence to same state faster than only gossiping). 

Failure detection is done by periodic random probing, if the probe does not ack(within some multiple of rtt), then an indirect probe is done which means a random set of members are asked to probe the same node(Reduces chance of own network failure causing issues). If the indirect probes also fail, this information is gossiped and the node is marked as suspicious. If the node marked as suspicious does not say it is alive in a configurable amount of time, the node is marked dead and removed from membership list and this information is again gossiped to randomly selected peers.

## Peer selection

Gossip peer selection is generally random, it can also be based on the some criteria(??get examples for this criteria)

## Spreading gossip
1. Push - Infected nodes are the ones sending/infecting susceptible nodes. Works well where there are a few updates.
2. Pull - All nodes are actively pulling for updates. (A node can’t know in advance new updates, so it has to pull all continuously).
Works well when there are frequent updates.
4. Push-Pull -Self explanatory
