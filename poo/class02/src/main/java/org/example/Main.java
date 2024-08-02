
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.Scanner;

void main() {
    LocalDate date = LocalDate.now(); // Get the current date
    DayOfWeek dow = date.getDayOfWeek(); // Get the day of week of a date
    if (dow == DayOfWeek.SATURDAY || dow == DayOfWeek.SUNDAY)
        System.out.println("Party time!!! \\o/");
    else
        System.out.println("Working time! =(");


    int i = 10;
    int x = 20;
    if(x==20 && ++i == 11){     // ++i incrementa antes || i++ depois
        System.out.println(i);
    }



    Scanner scanner = new Scanner(System.in);
    System.out.print("How many items do you want? "); // the ‘print’ command does not start a new line
    int items = scanner.nextInt();
    System.out.println("Now you have " + items + (items == 1 ? " item." : " items."));


    // SWITCH CASE STATEMENT
    LocalDate dateS = LocalDate.now();
    switch (dateS.getDayOfWeek()) {
        case MONDAY -> System.out.println("It is Monday. =(");
        case TUESDAY -> System.out.println("It is Tuesday. =(");
        case WEDNESDAY -> System.out.println("It is Wednesday. =|");
        case THURSDAY -> System.out.println("It is Thursday. =)");
        case FRIDAY -> System.out.println("It is Friday! =D");
        case SATURDAY -> System.out.println("It is Saturday!! \\o/");
        case SUNDAY -> System.out.println("It is Sunday. <o/");
    }

    //SWITCH CASE EXPRESS
    LocalDate dateE = LocalDate.now();
    final String dayAsString = switch (dateE.getDayOfWeek()) {
        case MONDAY -> "It is Monday. =´(";
        case TUESDAY -> " It is Tuesday. =(";
        case WEDNESDAY -> " It is Wednesday. =|";
        case THURSDAY -> " It is Thursday. =";
        case FRIDAY -> " It is Friday! =D";
        case SATURDAY -> " It is Saturday!! \\o/";
        case SUNDAY -> " It is Sunday. <o/";
    };
    System.out.println(dayAsString);




    while (true) {
        System.out.print("Enter a positive integer: ");
        Scanner scannerr = new Scanner(System.in);
        int number = scannerr.nextInt();
        if (number < 0) continue; // ignora o restante e volta pro começo do laço
        if (number % 2 == 0) System.out.println(number + " is even.");
        else System.out.println(number + " is odd.");
    }
}
}