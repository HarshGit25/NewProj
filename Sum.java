import java.utill.*;
public class Sum{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int num1,num2;
        int sum=0;
        System.out.println("Enter 2 numbers:");
        num1 = scan.nextInt();
        num2 = scan.nextInt();
        sum = num1 + num2;
        System.out.println("Sum of two numbers = "+sum);
    }
}