class Star:
    name = 'star' # 클래스 변수
    x = 100 # 클래스 변수

    def change():
        x = 200
        print('x is ',x)



print('x is ',Star.x) # 클래스 변수 액세스
Star.change() # 클래스 함수

star = Star() # 생성자 없이 생성
print(type(star))
print(star.x) # 비록 객체 변수로 액세스 했으나 같은 이름의 클래스 변수가 없음

star.change()