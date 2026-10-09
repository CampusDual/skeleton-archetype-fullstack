package com.campusdual.stockrestaurante;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Punto de entrada principal de la aplicacion.
 */
@SpringBootApplication
public class StockRestauranteApplication {

    /**
     * Arranca el contexto de Spring Boot.
     *
     * @param args argumentos de linea de comandos
     */
    public static void main(String[] args) {
        SpringApplication.run(StockRestauranteApplication.class, args);
    }
}
