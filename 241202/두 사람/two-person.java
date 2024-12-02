import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = 0;

        String one = sc.nextLine();
        String two = sc.nextLine();

        String[] str_one = one.split(" ");
        String[] str_two = one.split(" ");
        int tmp = 0;

        if(one.contains("M")){
            tmp = Integer.parseInt(str_one[0]);
            if(tmp > 19) answer = 1;
        }
        tmp = 0;
        if(two.contains("M")){
            tmp = Integer.parseInt(str_two[0]);
            if(tmp > 19) answer = 1;
        }

        System.out.print(answer);
    }
}