def gradient_descent(x_start, learning_rate, num_iterations):
    x = x_start  # 初始值
    history = [x]  # 用於記錄每一步的 x 值

    # 定義你的函數和導數（梯度）
    def func(x):
        return x**2  # 這裡我們使用 x^2 作為示例，你可以替換為你自己的函數

    def gradient(x):
        return 2*x  # x^2 的導數是 2x

    # 進行梯度下降
    for i in range(num_iterations):
        x = x - learning_rate * gradient(x)  # 更新 x
        history.append(x)  # 將新的 x 值添加到歷史記錄中

    return history

# 使用梯度下降算法找到函數的最小值
history = gradient_descent(x_start=5, learning_rate=0.1, num_iterations=100)

# 打印最後的 x 值（應該接近 0，因為我們的函數是 x^2）
print(history[-1])