import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
/* Расстояние редактирования
ВВОД: две строки латиницей в нижнем регистре
ВЫВОД: первая строка - расстояние, вторая и третья - детализация редактирования
 */

class EditDist {
    public static void main (String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String firstLine = input.readLine();
        String secondLine = input.readLine();
        int[][] matrix = new int[firstLine.length() + 1][secondLine.length() + 1];
        for (int i = 0; i <= firstLine.length(); i++) {
            for (int j = 0; j <= secondLine.length(); j++) {
                if (i == 0) {
                    matrix[i][j] = j;
                    continue;
                }
                if (j == 0) {
                    matrix[i][j] = i;
                    continue;
                }
                int diff = (firstLine.charAt(i - 1) == secondLine.charAt(j - 1)) ? 0 : 1;
                matrix[i][j] = Math.min(Math.min(matrix[i][j - 1] + 1, matrix[i - 1][j] + 1),
                        matrix[i - 1][j - 1] + diff);
            }
        }
        int n = matrix[firstLine.length()][secondLine.length()];
        System.out.println(n);
        n += Math.max(firstLine.length(), secondLine.length());
        char[] firstWord = new char[n];
        char[] secondWord = new char[n];
        int k = n - 1;
        int i = firstLine.length();
        int j = secondLine.length();
        while (i > 0 && j > 0) {

            int min = Math.min(Math.min(matrix[i - 1][j - 1], matrix[i] [j - 1]), matrix[i - 1][j]);

            if (min == matrix[i - 1][j - 1]) {
                if (firstLine.charAt(i - 1) != secondLine.charAt(j - 1)) {
                    firstWord[k] = Character.toUpperCase(firstLine.charAt(i - 1));
                    secondWord[k] = Character.toUpperCase(secondLine.charAt(j - 1));
                    } else {
                    firstWord[k] = firstLine.charAt(i - 1);
                    secondWord[k] = secondLine.charAt(j - 1);
                }
                i -= 1;
                j -= 1;
                k -= 1;
                continue;
            }
            if (min == matrix[i][j - 1]) {
                firstWord[k] = '-';
                secondWord[k] = secondLine.charAt(j - 1);
                j -= 1;
                k -= 1;
                continue;
            }
            if (min == matrix[i - 1][j]) {
                firstWord[k] = firstLine.charAt(i);
                secondWord[k] = '-';
                i -= 1;
                k -= 1;
            }
        }
        if (i == 0) {
            for (int x = j; x > 0; x--) {
                firstWord[k] = '-';
                secondWord[k] = secondLine.charAt(x - 1);
                k -= 1;
            }
        }
        if (j == 0){
            for (int x = i; x > 0; x--) {
                firstWord[k] = firstLine.charAt(x - 1);
                secondWord[k] = '-';
                k -= 1;
            }
        }
        StringBuilder result = new StringBuilder();
        for (int z = k + 1; z < n; z++) {
            result.append(firstWord[z]);
            result.append(' ');
        }
        result.append('\n');
        for (int z = k + 1; z < n; z++) {
            result.append(secondWord[z]);
            result.append(' ');
        }
        System.out.println(result);
    }
}

