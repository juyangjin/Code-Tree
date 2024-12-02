import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int b = sc.nextInt();
        int a = sc.nextInt();

        for(int i=b;i>=a;i--){
            if(i % 2 == 1){
                System.out.print(i + " ");
            }
        }
    }
}