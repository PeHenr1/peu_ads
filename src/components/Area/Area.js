import React from "react";
import "./Area.css";
import Professor from "../Professor/Professor";

const Area = (props) => {
  // Criando uma variável css com um objeto json que encapsula
  // a definição do estilo (no caso, só a definição de cor):
  const corDeFundo = { backgroundColor: props.corSecundaria };
  const corSublinhado = { borderColor: props.corPrimaria };
  return (
    (props.professores.length > 0) ? <section className="area" style={corDeFundo}>
      <h3 style={corSublinhado}>{props.nome}</h3>
      <div className="professores">
        {props.professores.map((prof) => (
          <Professor
            key={prof.name}
            nome={prof.nome}
            titulo={prof.titulo}
            imagem={prof.imagem}
          />
        ))}
      </div>
    </section>
    : ''
  );
};
export default Area;
