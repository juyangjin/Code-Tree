import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double a = sc.nextDouble();
        String result = "";

        if(1.0 <= a){
            result = "High";
        }else if(0.5 <= a){
            result = "Middle";
        }else{
            result = "Low";
        }
        System.out.print(result);
    }
}