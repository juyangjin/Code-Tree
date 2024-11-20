import java.util.*;

public class Main {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       Map<String, Integer> arr = new HashMap<>();

       arr.put("book", 3000);
       arr.put("mask", 1000);

       int n = sc.nextInt();
       int i = 0;

       for (Map.Entry<String, String> entry : arr.entrySet()) {
        if(arr.getValue > n) arr.remove(arr.getValue());
        }

        Integer result = Collections.max(arr.keySet());

        System.out.print(result);
    }
}