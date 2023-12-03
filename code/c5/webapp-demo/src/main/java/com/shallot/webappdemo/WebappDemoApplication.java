package com.shallot.webappdemo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@SpringBootApplication
public class WebappDemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(WebappDemoApplication.class, args);
	}

}

@Controller
class WelcomeController {

    @GetMapping("/")
    public String welcome(Model model) {
        // Add model attributes if needed
        return "welcome"; // This should match the name of your Thymeleaf template
    }
}
