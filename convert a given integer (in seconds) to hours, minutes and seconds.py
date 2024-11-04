import java.util.Scanner;
public class Time
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int hours=n/3600;
        int remsec = n-(hours*3600);
        int min = remsec/60;
        remsec-=min*60;
        int sec=remsec;
        System.out.println("H:M:S-"+hours+":"+min+":"+sec);
    }
}