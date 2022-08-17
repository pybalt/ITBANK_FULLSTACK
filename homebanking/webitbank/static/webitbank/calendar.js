const inputNombre = document.getElementById("nombre");
const inputApellido= document.getElementById("apellido");
const inputTelefono = document.getElementById("telefono");
const inputFecha = document.getElementById("fecha");
const inputHora = document.getElementById("hora");
const inputRazon = document.getElementById("razon");
const formulario = document.getElementById("nueva-cita");
const contenedorTurnos = document.getElementById("turnos");

let editando;

//Classes

class Turnos {
  constructor() {
    this.turnos = [];
  }

  agregarTurno(turno) {
    this.turnos = [...this.turnos, turno];

    console.log(this.turnos);
  }

  eliminarTurno(id) {
    this.turnos = this.turnos.filter((turno) => turno.id !== id);
  }

  editarTurno(turnoEditado){
    this.turnos = this.turnos.map( turno => turno.id === turnoEditado.id ? turnoEditado : turno );
  }
}




class UI {
  imprimirAlerta(mensaje, tipo) {
    //Crear div
    const divMensaje = document.createElement("div");
    divMensaje.classList.add("text-center", "alert", "d-block", "col-12");

    if (tipo === "error") {
      divMensaje.classList.add("alert-danger");
    } else {
      divMensaje.classList.add("alert-success");
    }

    //Mensaje de error
    divMensaje.textContent = mensaje;

    //Agregar al DOM

    document
      .getElementById("contenido")
      .insertBefore(divMensaje, document.querySelector(".agregar-cita"));

    setTimeout(() => {
      divMensaje.remove();
    }, 4000);
  }

  imprimirTurnos({ turnos }) {
    this.limpiarHTML();

    turnos.forEach((turno) => {
      const { nombre, apellido, telefono, fecha, hora, razon, id } =
        turno;

      const divTurno = document.createElement("div");
      divTurno.classList.add("turno", "p-3");
      divTurno.dataset.id = id;

      //Scripting de cada elemento

      const NombreParrafo = document.createElement("h2");
      NombreParrafo.classList.add("card-title", "font-weight-bolder");
      NombreParrafo.textContent = nombre;

      const apellidoParrafo = document.createElement("p");
      apellidoParrafo.innerHTML = `
      <span class="font-weight-bolder"> Apellido: </span> ${apellido}
      `;

      const telefonoParrafo = document.createElement("p");
      telefonoParrafo.innerHTML = `
        <span class="font-weight-bolder"> Teléfono: </span> ${telefono}
      `;

      const fechaParrafo = document.createElement("p");
      fechaParrafo.innerHTML = `
        <span class="font-weight-bolder"> Fecha: </span> ${fecha}
      `;

      const horaParrafo = document.createElement("p");
      horaParrafo.innerHTML = `
        <span class="font-weight-bolder"> Hora: </span> ${hora}
      `;

      const razonParrafo = document.createElement("p");
      razonParrafo.innerHTML = `
        <span class="font-weight-bolder"> Razon: </span> ${razon}
      `;

      //Boton para eliminar el turno

      const botonEliminar = document.createElement("button");
      botonEliminar.classList.add("btn", "btn-danger", "mr-2");
      botonEliminar.innerHTML = "Cancelar turno";

      botonEliminar.onclick = () => eliminarTurno(id);

      //Boton  para editar

      const botonEditar = document.createElement("button");
      botonEditar.classList.add("boton-editar");
      botonEditar.innerHTML = "Editar";
      botonEditar.onclick = () => cargarEdicion(turno);

      divTurno.appendChild(NombreParrafo);
      divTurno.appendChild(apellidoParrafo);
      divTurno.appendChild(telefonoParrafo);
      divTurno.appendChild(fechaParrafo);
      divTurno.appendChild(horaParrafo);
      divTurno.appendChild(razonParrafo);
      divTurno.appendChild(botonEliminar);
      divTurno.appendChild(botonEditar);

      //Agregar al HTML
      contenedorTurnos.appendChild(divTurno);
    });
  }

  limpiarHTML() {
    while (contenedorTurnos.firstChild) {
      contenedorTurnos.removeChild(contenedorTurnos.firstChild);
    }
  }
}

const ui = new UI();
const administrarTurnos = new Turnos();

//Eventos

listener();

function listener() {
  inputNombre.addEventListener("input", datosTurno);
  inputApellido.addEventListener("input", datosTurno);
  inputTelefono.addEventListener("input", datosTurno);
  inputFecha.addEventListener("input", datosTurno);
  inputHora.addEventListener("input", datosTurno);
  inputRazon.addEventListener("input", datosTurno);

  formulario.addEventListener("submit", nuevoTurno);
}

//Objeto donde se guardan todos los datos
const turnoObj = {
  nombre: "",
  apellido: "",
  telefono: "",
  fecha: "",
  hora: "",
  razon: "",
};

//Funciones

function datosTurno(e) {
  turnoObj[e.target.name] = e.target.value;
}

//Valida y agrega los turnos a la clase de turnos

function nuevoTurno(e) {
  e.preventDefault();

  //Extrear informacion del objeto de turnos (simula una base de datos)

  const { nombre, apellido, telefono, fecha, hora, razon } = turnoObj;

  if (
    nombre === "" ||
    apellido === "" ||
    telefono === "" ||
    fecha === "" ||
    hora === "" ||
    razon === ""
  ) {
    ui.imprimirAlerta("Todos los campos son obligatorios", "error");
    return;
  }

  if (editando) {
    console.log('modo edicion');
    ui.imprimirAlerta('Se guardaron los cambios');
 
    //Editar el objeto que contiene los datos
    administrarTurnos.editarTurno({ ...turnoObj });



    formulario.querySelector('button[type="submit"]').textContent = "Agendar turno";

    editando = false;

  } else {
    console.log('modo nuevo turno');
    //ID unico
    turnoObj.id = Date.now();

    //Creando nuevo turno

    administrarTurnos.agregarTurno({ ...turnoObj });

    //Mensaje de agregado correctamente

    ui.imprimirAlerta('Se agrego con éxito');
  }

  //Reiniciar el formulario y el objeto

  formulario.reset();
  reiniciarObjeto();

  //Mostrar html de los turnos

  ui.imprimirTurnos(administrarTurnos);
}

function reiniciarObjeto() {
  turnoObj.nombre = "";
  turnoObj.apellido = "";
  turnoObj.telefono = "";
  turnoObj.fecha = "";
  turnoObj.hora = "";
  turnoObj.razon = "";
}

function eliminarTurno(id) {
  administrarTurnos.eliminarTurno(id);

  ui.imprimirAlerta("Turno cancelado con exito");

  ui.imprimirTurnos(administrarTurnos);
}

//Edicion

function cargarEdicion(turno) {
  const { nombre, apellido, telefono, fecha, hora, razon } = turno;

  //Lenar los inputs

  inputNombre.value = nombre;
  inputApellido.value = apellido;
  inputTelefono.value = telefono;
  inputFecha.value = fecha;
  inputHora.value = hora;
  inputRazon.value = razon;

  //Llenar el objeto

  turnoObj.nombre = nombre;
  turnoObj.apellido = apellido;
  turnoObj.telefono = telefono;
  turnoObj.fecha = fecha;
  turnoObj.hora = hora;
  turnoObj.razon = razon;

  //Cambiar texto de boton

  formulario.querySelector('button[type="submit"]').textContent = "Guardar cambios";

  editando = true;
}