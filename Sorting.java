import java.util.Scanner;
/*
СОРТИРОВКИ
ВВОД: первое число - кол-во элтов в массиве, далее - числа в массиве через пробел
 */
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] list = new int[n];
        for (int i = 0; i < n; i++) {
            list[i] = scanner.nextInt();
        }
        heapSort(list);
        StringBuilder out = new StringBuilder();
        for (int i =0; i < n; i++) {
            out.append(list[i]);
            out.append(" ");
        }
        System.out.println(out);
    }

    public static void selectionSort(int[] list) {
        for (int i = 0 ; i < list.length - 1; i++) {
            int indexOfMin = i;
            for (int j = i + 1; j < list.length; j++) {
                if (list[j] < list[indexOfMin]) {
                    indexOfMin = j;
                }
            }
            int temp = list[i];
            list[i] = list[indexOfMin];
            list[indexOfMin] = temp;
        }
    }

    public static void insertSort(int[] list) {
        for (int i = 1; i < list.length; i++) {
            int j = i;
            while (j > 0 && list[j] < list[j - 1]) {
                int temp = list[j];
                list[j] = list[j - 1];
                list[j - 1] = temp;
                j -= 1;
            }
        }
    }

    public static void bubbleSort(int[] list) {
        for (int i = list.length - 1; i > 0; i--) {
            int j = 0;
            while (j < i) {
                if (list[j] > list[j + 1]) {
                        int temp = list[j];
                        list[j] = list[j + 1];
                        list[j + 1] = temp;
                }
                j += 1;
            }
        }
    }

    public static int[] merge(int[] a, int[] b) {
        int i = 0;
        int j = 0;
        int k = 0;
        int[] res = new int[a.length + b.length];
        while (i < a.length && j < b.length) {
            if (a[i] <= b[j]) {
                res[k] = a[i];
                i += 1;
            } else {
                res[k] = b[j];
                j += 1;
            }
            k += 1;
        }
        if (i < a.length) {
            while (i < a.length) {
                res[k] = a[i];
                i +=1;
            }
        } else {
            while (j < b.length) {
            res[k] = b[j];
            j += 1;
            }
        }
        return res;
    }

    public static int[] mergeSort(int[]list) {
        if (list.length <= 1) {
            return list;
        }
        int m = list.length / 2;
        int[] list1 = new int[m];
        int[] list2 = new int[list.length - m];
        for (int i= 0; i < list.length; i++){
            if (i < m) {
                list1[i] = list[i];
            } else {
                list2[i - m] = list[i];
            }
        }
        return merge(mergeSort(list1), mergeSort(list2));
    }


    public static int partition(int[] list, int l, int r) {
        int j = l;
        for (int i = l + 1; i <= r; i++) {
            if (list[i] <= list[l]) {
                j += 1;
                int temp = list[j];
                list[j] = list[i];
                list[i] = temp;
            }
        }
        int temp = list[j];
        list[j] = list[l];
        list[l] = temp;
        return j;
    }

    public static void quickSort(int[] list, int l, int r) {
        if (l >= r) {
            return;
        }
        int m = partition(list, l, r);
        quickSort(list, l, m - 1);
        quickSort(list, m + 1, r);
    }

    public static void quickSort(int[] list) {
        quickSort(list, 0, list.length - 1);
    }

    public static void siftDownMaxHeap(int[] list, int index, int size) {
        int nowIndex = index;
        while (nowIndex < size && (nowIndex * 2) <= size) {
            int targetIndex = nowIndex * 2;
            if ((nowIndex * 2) + 1 <= size &&
                    list[(nowIndex * 2) - 1] < list[((nowIndex * 2) + 1) - 1]) {
                targetIndex = (nowIndex * 2) + 1;
            }
            if (list[nowIndex - 1] > list[targetIndex - 1]) {
                break;
            }
            int temp = list[nowIndex - 1];
            list[nowIndex - 1] = list[targetIndex - 1];
            list[targetIndex - 1] = temp;
            nowIndex = targetIndex;
        }
    }

    public static void buildMaxHeap(int[] list) {
        for (int i = (list.length / 2); i > 0; i--) {
            siftDownMaxHeap(list, i, list.length);
        }
    }

    public static void heapSort(int[] list) {
        buildMaxHeap(list);
        int size = list.length;
        for (int i = list.length; i > 0; i--) {
            int temp = list[size - 1];
            list[size - 1] = list[0];
            list[0] = temp;
            size -= 1;
            siftDownMaxHeap(list, 1, size);
        }
    }
}
