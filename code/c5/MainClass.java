public class MainClass {
    public static void main(String[] args) {
        MainClass main = new MainClass();
        String output = main.getGreeting();
        System.out.println(output);
    }

    public static String getGreeting() {
        return "Hello, Jenkins!";
    }
}
