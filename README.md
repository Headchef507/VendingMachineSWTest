
## the Software Testing Project

### to run all tests do:
$ python -m unittest


## This is/was the original java code the class is based on:
```Java
class VendingMachine {
    private final int capacity = 10;
    private int stock = 0;
    private boolean coinInserted = false;
    VendingMachine() { /∗ Create with no bottles in stock ∗/ };
    VendingMachine(int x) throws CapacityExceededException, NegativeOrZeroParameterException { /∗ Create with x bottles ∗/ };
    void refill(int x) throws CapacityExceededException,CurrentlyCoinInsertedException,NegativeOrZeroParameterException { };
    void insertCoin() throws MoreThanOneCoinInsertedException, EmptyStockException { };
    Bottle requestBottle() throws NoCoinInsertedException { };
}
```
 - I will change it so that every time we add a number to stock, we will have to add a list of bottles to the system
    - will then also return the lenght of the list as number of bottles in stock