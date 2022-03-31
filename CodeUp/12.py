# 클래스 
class Wizard:
    # 클래스의 메소드들 , self는 객체를 의미함.
    def stats(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print('파이어볼')
# x에 클래스 지정    
x = Wizard()
# Wizard클래스의 stat에 값보내줌
x.stats(health = 545, mana = 210, armor = 10)
print(x.health, x.mana, x.armor)
x.attack()
