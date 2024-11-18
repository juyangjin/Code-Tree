import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = 0;
        double n2 = 0;
        int len = 0;

        for(int i=1;i<=10;i++){
            if(i % 2 == 0) n += sc.nextInt();
            else if(i % 3 == 0){
                n2 += sc.nextDouble();
                len++;
            } 
            else sc.nextInt();
        }

        System.out.print(n + " ");
        double tmp = Math.round(n2 /= len);
        System.out.print(tmp);
    }
}