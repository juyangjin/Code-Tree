import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String result = "";

        if(n >= 100){
            result = "vapor";
        }else if(n < 0){
            result = "ice";
        }else{
            result = "water";
        }

        System.out.print(result);
    }
}