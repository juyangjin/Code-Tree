import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int even = 0;
        int odd = 0;

        for(int i=1;i<=10;i++){
            if(i % 2 == 0) even += sc.nextInt();
            else odd += sc.nextInt();
        }

        if(even > odd) System.out.print(even - odd);
        else System.out.print(odd - even);

    }
}