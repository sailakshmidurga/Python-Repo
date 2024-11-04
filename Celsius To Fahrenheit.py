import java.util.Scanner;
public class Temp
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int c=sc.nextInt();
        float f=c*1.8F+32;
        System.out.printf("%.2f",f);
    }
}