import java.util.Scanner;
public class Temp
{
    public static void main(String args[])
    {
        Scanner sc= new Scanner(System.in);
        int f=sc.nextInt();
        float c=(f-32)*(5/9F);
        System.out.printf("%.2f",c);
    }
}