package exercicio1;

public class Main {
    public static void main(String[] args) {
        String constantName = "MY_CONSTANT";
        String variableName = "MyVariable";
        String variableNameY = "myVariable";

        System.out.println(NamingConventions.isFollowingConvention(constantName, NamingConventions.Convention.CONSTANT)); // true
        System.out.println(NamingConventions.isFollowingConvention(variableName, NamingConventions.Convention.VARIABLE)); // false
        System.out.println(NamingConventions.isFollowingConvention(variableNameY, NamingConventions.Convention.VARIABLE)); // true
        System.out.println(NamingConventions.fromConstToVariable(constantName)); // "myConstant"
        System.out.println(NamingConventions.fromVariableToConst(variableName)); // "MY_VARIABLE"
        System.out.println(NamingConventions.isValidJavaIdentifier("myVariable1")); // true
        System.out.println(NamingConventions.isValidJavaIdentifier("1InvalidVar")); // false
    }
}