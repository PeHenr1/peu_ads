package org.example;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringJoiner;

public class Tests {

    void main() {
    /*List<Employee> employees = new ArrayList<>();
    var ada = new Employee("01", "Ada Lovelace", "Computer Programmer");
    employees.add(ada);
    employees.add(new Employee("03", "Edsger Dijkstra", "Computer Scientist"));
    employees.add(1, new Employee("02", "David Huffman", "Computer Scientist"));
    for (Employee employee : employees)
        System.out.println(employee.getName());
    System.out.println("employees.size() = " + employees.size());
    employees.remove(ada);
    System.out.println("employees.contains(ada) = " + employees.contains(ada));
    System.out.println("employees.size() = " + employees.size());
     */

        List<String> legendsNames = new ArrayList<>(List.of("Ada", "Hopper", "von Neumann", "Turing"));
        Collections.sort(legendsNames);
        final String output = String.join(", ", legendsNames);
        System.out.println(output);

        List<Employee> legends = new ArrayList<>();
        legends.add(new Employee("03", "Edsger Dijkstra", "Computer Scientist"));
        legends.add(new Employee("01", "Ada Lovelace", "Computer Programmer"));
        legends.add(new Employee("02", "David Huffman", "Computer Scientist"));

        //Collections.sort(legends); // use Collections.reverse(legends) to sort in reverse order
        StringJoiner joiner = new StringJoiner("\n");
        for (Employee legend : legends) {
            joiner.add(legend.toString());
        }
        System.out.println(joiner);
    }
}
