import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] n = new int[N];

        for(int i=0;i<n.length;i++){
            n[i] = sc.nextInt();
        }

        for(int j=0;j<n.length;j++){
            if(n[j] % 2 == 1 && n[j] % 3 == 0){
                System.out.println(n[j]);
            }
        }
    }
}