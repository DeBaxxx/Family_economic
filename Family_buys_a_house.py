class Family:
    surname = 'Common family'
    money = 100000
    have_a_house = False

    def info(self):
        print(
            'Family name: {}\nFamily founds: {}\nHaving a house: {}'.format(
                self.surname, self.money, self.have_a_house
             )
        )

    def earn_money(self, amount):
        self.money += amount
        print('Earned {} money! Current volume: {}'.format(amount, self.money))

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print('House purchased! Current money: {}\n'.format(self.money))
        else:
            print('Not enough money(((\n')


my_family = Family()
my_family.info()
print()
print('Try to by a house.')
my_family.buy_house(1000000)
if not my_family.have_a_house:
    my_family.earn_money(800000)
    print('Try to by a house again.')
    my_family.buy_house(10 ** 6, 10)
my_family.info()