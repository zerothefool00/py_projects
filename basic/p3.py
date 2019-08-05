'''
연속데이터(시퀀스타입)
 > 리스트     : []-> js의 배열과 동일,
 순서가 존재, 값중복 ok, 인덱스는 정방향/역방향(-1,-2,....) 존재
'''
#  비워있는 리스트 생성
#  정적생성 : 일반적으로 문제는 없으나, 간혹 추가가 않되는 경우가생김
#             이런 경우 동적 생성으로 대체
#             =자료구조를 직접 맞춰서 데이터를 세팅하는 리스트 내포같은 케이스에 사용
nums = []
print(nums,len(),type(nums) )           
nums = list() #동적생성 =>대량의 작업시 조금 더 안정적
print(nums, len(nums), type(nums))
nums=[1,3,5,7,9]
print(nums,len(nums) ,type(nums))
anis = ['dogs','cat','bird']
print(anis,len(anis),type(anis))
# 리스트의 멤버들의 타입이 다르면 리스트를 구성할 수 없다? x
#파이썬의 모든것을 객체이므로, 멤버들도 모두 객체 => 주소를 가지고 있고 이것이 포함
mix = [1,2,3,'dog','cat']
print(mix,len(mix),type(mix))
#차원을 섞으면? 멤버중에 하나가 리스트였다
multiTypeMatrix = [1,2,3,'dog','cat',['bird',100]]
print(multiTypeMatrix, len(multiTypeMatrix),type(multiTypeMatrix))
##################################################################
# multiTypeMatrix에서 100이란 값을 출력하시오
print(multiTypeMatrix[-1][-1])
################################################################
# 슬라이싱 = > 사본작업
nums = [1,3,5,7,9]
#nums에서 3,5,7만 가진 리스트를 구하시오 : 리스트 -> 리스트(슬라이싱이다 : 차원유지기 때문에)
print( nums[1:-1], '사본출력')
#원본은 유지된다 => 원본변경 방법은
#=> 인덱싱을 활용한 변경
nums[0] = 100
print( nums)
# 3,5,7을 모두 -1로 변경하시오
nums[1:-1] = '-1'
# 같은 시퀀스(연속데이터)타입이면 슬라이싱을 범위를 대체할 수 있다
print(nums)
###########################################################
#멤버삭제
del nums[0]
print(nums)
# 9값을 가진 멤버를 제거
nums.remove(9)
print(nums)
nums = [1,3,2, 3,4, 3,5,7]
# 중복된 데이터 중 정방향에서 가장 먼저 찾은 멤버만 제거
#다제거
nums.clear()
print(nums)
#멤버추가
nums.append(1)
print( nums )
#오직자식으로 추가
tmp = [3,5]
nums.extend(tmp)
#리스트를, 이어 붙였다
print(nums + tmp)
print(nums)
#두개를 이어 붙여서 리턴 => 사본작업
#리스트와 for => for문에서 확인