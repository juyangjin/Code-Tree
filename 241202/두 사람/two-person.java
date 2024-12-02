import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = 0;

        String[] a = sc.nextLine().split(" ");
        String[] b = sc.nextLine().split(" ");

        int i_a = Integer.parseInt(a[0]);
        int i_b = Integer.parseInt(b[0]);
        
        if((a[1].contains("M") && i_a >= 19) || (b[1].contains("M") && i_b >= 19)){
            answer = 1;
        }
        
        System.out.print(answer);
    }
}