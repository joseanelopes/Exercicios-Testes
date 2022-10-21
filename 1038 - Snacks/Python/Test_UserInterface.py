from pytest import MonkeyPatch
from Order import Order
from Menu import Menu
from MenuRepository import MenuRepository
from UserInterface import UserInterface


def test_get_user_input(monkeypatch: MonkeyPatch):
    #Arrange
    menu_repository = MenuRepository()
    user_interface = UserInterface(menu_repository)
    menu1 = Menu(1, "Test 1", 10)
    

    #Act
    monkeypatch.setattr('builtins.input', lambda _: "1 1")
    menu_repository.set_menu_item(menu1)
    order1= user_interface.get_user_input()

    #Assert
    assert order1.code == 1


def test_get_total_price_user(): 
    #Arrange
    menu_repository = MenuRepository()
    user_interface = UserInterface(menu_repository)
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    order1 = Order(1,10)

    #Act
    menu_repository.set_menu_item(menu1)
    result= user_interface.get_total_price(order1)

    #Assert
    assert result == 100