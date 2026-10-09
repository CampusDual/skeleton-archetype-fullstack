package com.campusdual.stockrestaurante.ws.security;

/**
 * Excepcion de configuracion de seguridad para encapsular errores de inicializacion del filtro.
 */
public class SecurityConfigurationException extends RuntimeException {

    public SecurityConfigurationException(String message, Throwable cause) {
        super(message, cause);
    }
}

