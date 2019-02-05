package towerofbabel.problemscomplex;

import java.util.Arrays;
import java.util.stream.IntStream;

public class Main {

    public static void main(String[] args) {
        int[] a = fibonacci_series(7);
        System.out.println(Arrays.toString(a));
    }

    public static int fibonacci_nth(int n) {
        if(n == 0) return 0;
        if(n == 1) return 1;
        else return fibonacci_nth(n-2) + fibonacci_nth(n-1);
    }

    public static int[] fibonacci_series(int n) {
        return IntStream.range(0, n+1).map(i->fibonacci_nth(i)).toArray();
    }
}
