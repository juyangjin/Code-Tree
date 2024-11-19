import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String num = sc.nextLine();
        char[] arr = num.toCharArray();
        
        for(int i=0;i<3;i++){
           System.out.print(arr[i]);
        }

        for(int i=8;i<13;i++){
           System.out.print(arr[i]);
        }

        for(int i=3;i<8;i++){
           System.out.print(arr[i]);
        }
    }
}