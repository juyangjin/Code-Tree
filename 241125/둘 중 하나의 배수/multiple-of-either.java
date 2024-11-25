import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();

        System.out.print(a % 3 == 0 || a % 5 == 0 ? 1 : 0);
    }
}