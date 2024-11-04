import java.util.Scanner;
public class Two
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        double n=sc.nextDouble();
        double m=sc.nextDouble();
        double avg = (n+m)/2;
        System.out.printf("%.4f",avg);
    }
}