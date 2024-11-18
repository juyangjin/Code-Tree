import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] n = new int[10]; 
        int num = 0;
        double num2 = 0;
        int len = 0;

        for(int i=0;i<10;i++){
            n[i] = sc.nextInt();
        }

        for(int i=0;i<10;i++){
            if((i + 1) % 2 == 0){
                num += n[i];
            }
            if((i + 1) % 3 == 0){
                num2 += n[i];
                len++;
            }
        }

        System.out.print(num + " ");
        num2 = (double) num2 / len;

        System.out.printf("%.1f", num2);
    }
}