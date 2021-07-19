
-----
# codingTestStudy - 3주차
-----

✍ <span style="color:red"> 문자열, 해시, 정렬 </span>

## 210719
- **11654번** - 아스키코드

***- ord***: 문자를 입력받으면 해당 아스키 코드 출력
***- chr***: 아스키코드를 입력받으면 해당 문자 출력

- **11720번** - 숫자의 합
> - 숫자 n은 *int*형으로, string은 *list*로 받아줌
> - string에 저장된 데이터들을 int형으로 변환시켜주며 더해줌
```py
n = int(input())
string = list(input())

sum += int(string[i])
```

구글링하다보니 이렇게 간단한 식도 알게 됨
```py
print(sum(map(int, input())))
```


