/* Динамический рюкзак снизу вверх
Ввод: первая строка n и w через пробел. n(int) - кол-во элементов, w(int) - вместимость рюкзака.
      Далее n строк: два числа(int) через пробел - вес элемента и стоиместь элемента соответственно.
Вывод: первая строка - общая цена в элементов рюкзаке, втрорая - номера элементов в рюкзаке.
 */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;



class DynamicKnapBU {
    public static void main (String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String[] inputString = input.readLine().split(" ");
        int n = Integer.parseInt(inputString[0]);
        int w = Integer.parseInt(inputString[1]);
        int[][] items = new int[n + 1][2];
        items[0][0] = 0;
        items[0][1] = 0;
        for (int i = 1; i <= n; i++) {
            inputString = input.readLine().split(" ");
            items[i][0] = Integer.parseInt(inputString[0]);
            items[i][1] = Integer.parseInt(inputString[1]);
        }
        int[][] knapsack = new int[n + 1][w + 1];
        for (int i = 0; i <= w; i++) {
            knapsack[0][i] = 0;
        }
        for (int i = 0; i <= n; i++) {
            knapsack[i][0] = 0;
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= w; j++) {
                knapsack[i][j] = knapsack[i - 1][j];
                if (items[i][0] <= j) {
                    knapsack[i][j] = Math.max(knapsack[i][j], knapsack[i - 1][j - items[i][0]] + items[i][1]);
                }
            }
        }
        System.out.println(knapsack[n][w]);
        int i = n;
        int j = w;
        StringBuilder res = new StringBuilder();
        while (knapsack[i][j] >= 0) {
            if (knapsack[i - 1][j] == knapsack[i][j]) {
                i -= 1;
                continue;
            }
            res.insert(0, i);
            res.insert(0, " ");
            j -= items[i][0];
            i -= 1;
            if (knapsack[i][j] == 0) break;
        }
        res.deleteCharAt(0);
        System.out.println(res);
        }
}
