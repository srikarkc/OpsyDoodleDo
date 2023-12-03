import org.junit.Assert;
import org.junit.Test;

public class TestClass {
    @Test
    public void testGetGreeting() {
        Assert.assertEquals("Hello, Jenkins!", MainClass.getGreeting());
    }
}
