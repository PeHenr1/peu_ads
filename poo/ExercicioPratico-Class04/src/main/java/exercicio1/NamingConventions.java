package exercicio1;

public class NamingConventions {
    public enum Convention {VARIABLE, CONSTANT, CLASS, METHOD}

    public static boolean isFollowingConvention(String element, Convention convention){
        return switch (convention) {
            case VARIABLE, METHOD -> element.matches("^[a-z][a-zA-Z0-9]*$");
            case CONSTANT -> element.matches("^[A-Z][A-Z0-9_]*$");
            case CLASS -> element.matches("^[A-Z][a-zA-Z0-9]*$");
        };
    }

    public static String fromConstToVariable(String constantName) {
        String[] parts = constantName.split("_");
        StringBuilder variableName = new StringBuilder(parts[0].toLowerCase());
        for (int i = 1; i < parts.length; i++) {
            variableName.append(parts[i].substring(0, 1).toUpperCase()).append(parts[i].substring(1).toLowerCase());
        }
        return variableName.toString();
    }

    public static String fromVariableToConst(String variableName) {
        StringBuilder constantName = new StringBuilder();
        for (char c : variableName.toCharArray()) {
            if (Character.isUpperCase(c)) {
                constantName.append('_').append(c);
            } else {
                constantName.append(Character.toUpperCase(c));
            }
        }
        return constantName.toString();
    }

    public static boolean isValidJavaIdentifier(String identifier) {
        if (identifier == null || identifier.isEmpty() || !Character.isJavaIdentifierStart(identifier.charAt(0))) {
            return false;
        }
        for (int i = 1; i < identifier.length(); i++) {
            if (!Character.isJavaIdentifierPart(identifier.charAt(i))) {
                return false;
            }
        }
        return true;
    }
}
