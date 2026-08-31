class StockSpanner:
    def __init__(self):
        # TODO: Initialize your data structure here.
        self.stk = []
        self.day = -1
        pass

    def next(self, price: int) -> int:
        # TODO: Calculate and return today's span.
        self.day += 1

        while self.stk and self.stk[-1][0] <= price:
            self.stk.pop()
            
        if self.stk:
            span = self.day - self.stk[-1][1]
        else:
            span = self.day+1
        
        self.stk.append((price, self.day))
        
        return span

def run_test(prices: list[int], expected: list[int]) -> None:
    stock_spanner = StockSpanner()
    actual = []

    for price in prices:
        span = stock_spanner.next(price)
        actual.append(span)

    print(f"Prices:   {prices}")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")

    assert actual == expected, (
        f"Test failed!\nExpected: {expected}\nActual:   {actual}"
    )

    print("Test passed!\n")


if __name__ == "__main__":
    # Given example
    run_test(
        prices=[100, 80, 60, 70, 60, 75, 85],
        expected=[1, 1, 1, 2, 1, 4, 6],
    )

    # Increasing prices
    run_test(
        prices=[10, 20, 30, 40],
        expected=[1, 2, 3, 4],
    )

    # Decreasing prices
    run_test(
        prices=[40, 30, 20, 10],
        expected=[1, 1, 1, 1],
    )

    # Equal prices
    run_test(
        prices=[25, 25, 25],
        expected=[1, 2, 3],
    )