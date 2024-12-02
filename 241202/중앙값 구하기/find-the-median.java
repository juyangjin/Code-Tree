import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] a = sc.nextLine().split(" ");
        int[] b = new int[a.length];

        for(int i=0;i<b.length;i++){
            b[i] = Integer.parseInt(a[i]);
        }

        Arrays.sort(b);

        System.out.print(b[1]);
    }
}