import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> arr = new ArrayList<>();
        int len = 0;

        while(true){
            int n = sc.nextInt();
            len++;
            if(n != 0 || len <= 4){
                arr.add(n);
            }else{
                arr.add(n);
                break;
            }
        }

        int len2 = arr.size();
        int result = 0;

        Collections.reverse(arr);

        for(int i=0;i<4;i++){
            result += arr.get(i);
        }

        System.out.print(result);
    }
}