import java.util.*;

public class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int n = sc.nextInt();
       int result = n * n;

       System.out.println(result);

       if(n < 5){
        System.out.print("tiny");
       } 
    }
}