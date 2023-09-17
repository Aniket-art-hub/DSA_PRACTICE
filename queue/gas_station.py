class GasStation:
        
    def gas_station(self,gas,cost):
        n = len(gas)
        start=0
        end=0
        total_gas=0
        if gas and cost:
            while start<n:
                if gas[start]>=cost[start]:
                    end = (start+1)%n
                    total_gas = gas[start]-cost[start]
                    while start!=end and (total_gas+gas[end])>=cost[end]:
                        total_gas+=gas[end]-cost[end]
                        end=(end+1)%n

                    if start==end:
                        return start
                    elif end>start:
                        start=end
                    else:
                        return -1
                else:
                    start+=1
        return -1
    
GasStation=GasStation()
gas=[1,2,3,4,5]
cost=[3,4,5,1,2]
print(GasStation.gas_station(gas,cost))