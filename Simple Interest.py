import java.util.Scanner;
public class Simple
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int p=sc.nextInt();
        int q=sc.nextInt();
        int r=sc.nextInt();
        int si=(p*q*r)/100;
        System.out.println(si);
    }
}