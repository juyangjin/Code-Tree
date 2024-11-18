import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        char[] str = new char[10];

        for(int i=0;i<10;i++){
            str[i] = sc.next().charAt(0);
    }

    System.out.print(str[1] + " " + str[4] + " " + str[7]);

    }
}