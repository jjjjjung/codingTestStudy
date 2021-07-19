def solution(board, moves):
    arr = []
    cnt = 0
           
    for i in range(len(moves)): 
        row = moves[i] - 1
        
        if board[len(board)-1][row] == 0: # 해당 행의 제일 아래값이 0이면 아무런 일도 일어나지 않음
            continue
                
        for j in range(len(board)):
            if board[j][row] == 0: # 해당 행을 차례로 검사하는데 0이면 한칸 밑으로 이동
                continue
            else: 
                arr.append(board[j][row]) # 값을 arr에 넣음
                board[j][row] = 0
                break
        
        if len(arr) > 1: # 길이가 최소 2가 되어야 검사
            if arr[-1] == arr[-2]: # 앞, 뒤의 값이 같으면 둘다 없애줌
                cnt += 2
                arr.pop(-1)
                arr.pop(-1)  

    return cnt