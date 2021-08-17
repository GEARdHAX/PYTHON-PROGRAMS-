package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here


        Scanner sc = new Scanner(System.in);
        System.out.println("  ENTER 1st NO.  ");
        int num1 = sc.nextInt();
        System.out.println("  ENTER 2nd NO.  ");
        int num2 = sc.nextInt();
        int sum = num1 + num2;
        int sub = num1-num2;
        int mult = num1*num2;
        float div = (num1/num2);
        System.out.println("  ENTER BOOLEAN  ");
        boolean b1 = sc.hasNextInt();
        System.out.println("  ANSWER OF SUM IS:  ");  
        System.out.println(sum);
        System.out.println("  ANSWER OF SUB IS:  ");
        System.out.println(sub);
        System.out.println("  ANSWER OF MULT IS:  ");
        System.out.println(mult);
        System.out.println("  ANSWER OF DIV IS:  ");
        System.out.println(div);
        System.out.println(" ANSWER OF BOOLEAN: ");
        System.out.println(b1);

        
        

    }
}
