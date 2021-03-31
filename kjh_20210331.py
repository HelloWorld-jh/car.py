'''파이썬 300제 딕셔너리 84~98'''
temp = {}
print(temp)

ice_cream = {"메로나":1000, "폴라포":1200,"빵빠레":1800}
print(ice_cream)
ice_cream["죠스바"] = 1200
ice_cream["월드콘"] = 1500
print(ice_cream)

ice = {'메로나' : 1000,
'폴라포' : 1200,
'빵빠레' : 1800,
'죠스바' : 1200,
'월드콘' : 1500}
ice["메로나"] = 1300
print(ice)

# 딕셔너리에 없는 키를 사용해서 인덱싱하면 에러가 발생합니다.
inventory = {"메로나":[300,20], "비비빅":[400,3], "죠스바":[250,100]}
print(inventory)
print(inventory["메로나"][0],"원")
inventory = {"메로나": [300,20],
"비비빅":[400,3],
"죠스바":[250,100]}
# 구구단을 gugudan.txt에 출력해보세요.

# f = open('guguan.txt', 'w')
# for dan in range(2,10):
#     dan = input('몇 단?')
#     for i in range(1,10):
#         f.write(f"{dan} x {i} = {int(dan) * i}\n")
# f.close()

# 한글 쓰기

f = open('text.txt','w', encoding='utf-8')
f.write('안녕하세요.반갑습니다.\n')
f.close()

# 전체 내용 한번에 읽기
f= open('text.txt','r',encoding='utf-8')
a = f.read() # 파일에 담긴 모든 내용을 문자열로 반환
f.close()
print(a)

# 한 줄씩 읽기
f = open('guguan.txt','r',encoding='utf=8')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
f.close()
print(a)

print('=' * 80)

for line in a:
    print(line, end='')







