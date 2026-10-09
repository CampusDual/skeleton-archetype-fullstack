package com.campusdual.stockrestaurante.model.repository;

import com.campusdual.stockrestaurante.model.entity.UserEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<UserEntity, Long> {

    /**
     * Busca un usuario por su nombre de usuario.
     *
     * @param username nombre de usuario
     * @return usuario encontrado si existe
     */
    Optional<UserEntity> findByUsername(String username);

    /**
     * Comprueba si existe un usuario por su nombre de usuario.
     *
     * @param username nombre de usuario
     * @return true si existe
     */
    boolean existsByUsername(String username);
}

