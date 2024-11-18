import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = 0;

        for(int i=1;i<=10;i++){
            if(i == 3 || i == 5 || i == 10){
                n += sc.nextInt();
            }else{
                int tmp = sc.nextInt();
            }
        }

        System.out.print(n);
    }
}