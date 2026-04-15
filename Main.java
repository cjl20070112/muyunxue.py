

public class Main{
    public static void main(String[] args) {
        double sum1 = getarea(3.5,2.1);
        double sum2 = getarea(4.2,1.5);
        if(sum1 > sum2){
            System.out.printf("第一个面积更大并且值为：%.2f",sum1);
        }else{
            System.out.printf("第二个面积更大并且值为：%.2f",sum2);
        }
    }
    public static double getarea(double num1,double num2){
        double a = num1 * num2;
        return a;
    }
}