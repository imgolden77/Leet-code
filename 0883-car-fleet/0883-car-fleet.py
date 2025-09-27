class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. (Position, Time) 쌍을 만들고 Position 기준 내림차순 정렬 (타겟에 가까운 차 순)
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        
        fleet_count = 0
        max_time = 0.0 # 현재까지 확인된 플릿 중 가장 늦게 도착하는 시간
        
        for pos, spd in cars:
            # 2. 각 차의 타겟 도착 시간 계산
            time_to_target = (target - pos) / spd
            
            # 3. 새로운 플릿 형성 조건 확인
            if time_to_target > max_time:
                # 현재 차가 기존 플릿의 리더보다 늦게 도착하면, 새로운 플릿을 형성
                fleet_count += 1
                max_time = time_to_target # 이 차가 새로운 플릿의 blocking time이 됨
            # else: time_to_target <= max_time 이면, 현재 차는 앞선 플릿에 합류하므로 무시
            
        return fleet_count