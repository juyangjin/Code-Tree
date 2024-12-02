import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int answer = 1;

        for(int i=1;i<=b;i++){
            if(i % a == 0){
                answer *= i;
            }
        }
        System.out.print(answer);
    }
}