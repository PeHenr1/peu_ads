import React from "react";
import "./Form.css";

import CampoTexto from "../TextField/TextField";

const Formulario = () => {
  return (
    <section className="formulario">
      <form>
        <h2>Dados do professor:</h2>
        <CampoTexto label="Nome" placeholder="Digite seu nome" />
        <CampoTexto label="Título" placeholder="Digite seu título" />
        <CampoTexto label="Imagem" placeholder="Digite o endereço da imagem" />
      </form>
    </section>
  );
};
export default Formulario;
