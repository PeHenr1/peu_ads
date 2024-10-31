package org.example;

import java.util.Objects;

public class Employee implements Comparable<Employee> {
    private final String id;
    private final String name;
    private final String occupation;

    public Employee(String id, String name, String occupation){
        this.id = id;
        this.name = name;
        this.occupation = occupation;
    }

    public String getOccupation() {
        return occupation;
    }
    public String getName() {
        return name;
    }
    public String getId() {
        return id;
    }

    @Override
    public int compareTo(Employee other) {
        return id.compareTo(other.id);
    }
}
