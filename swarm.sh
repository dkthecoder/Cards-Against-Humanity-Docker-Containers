#for swarm manager
docker swarm init

#note down swarm token
#example token
#docker swarm join --token SWMTKN-1-14601cadnn15hf45gjqql23jta4vk4kxh8uy6zyn8vo0fxzu5z-31kwu4qd6up8ktez4kj62ppvr 192.168.61.1:2357

#If you can’t obtain the join command anymore, run the join-token command below on the Swarm Manager VM:
#docker swarm join-token worker