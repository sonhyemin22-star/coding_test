def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_truck = [0] * bridge_length
    current_bridge = 0
    while len(truck_weights) > 0:
        time += 1
        current_bridge -= bridge_truck.pop(0)
        if current_bridge + truck_weights[0] <= weight:
            current_bridge += truck_weights[0]
            bridge_truck.append(truck_weights.pop(0))
        else:
            bridge_truck.append(0)
    time += len(bridge_truck)
    return time