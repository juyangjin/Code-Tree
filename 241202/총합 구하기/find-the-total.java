import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int answer = 0;

        for(int i=a;i<=b;i++){
            if(i % 6 == 0 && i % 8 != 0){
                answer += i;
            } 
        }
        System.out.print(answer);
    }
}