import java.util.*;

public class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int n = sc.nextInt();
       String result = "";

       if(n >= 3000){
        result = "book";
       }else if(n >= 1000){
        result = "mask";
       }else{
        result = "no";
       }

       System.out.print(result);
    }
}