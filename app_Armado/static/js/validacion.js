function validacionesFormulario(){
    
    var correo, rut, nombre,number,usuario,contraseña1,contraseña2
    correo = document.getElementById("correo").value;
    rut = document.getElementById("rut").value;
    nombre = document.getElementById("nombre").value;
    number = document.getElementById("number").value;
    usuario = document.getElementById("usuario").value;
    contraseña1 = document.getElementById("contraseña1").value;
    contraseña2 = document.getElementById("contraseña2").value;
    var espacios = false;
    var cont = 0;
   

    if(correo == "" || rut == ""|| nombre == ""|| number == "" || usuario== ""|| contraseña1 == "" || contraseña2 == "" ){
        alert("Todos los campos son obligatorios ");
        return false;
    } 

    if (isNaN(number)){
        alert("El tipo de dato para telefono debe ser numerico");
        return false;
        
    }

    while (!espacios && (cont < contraseña1.length)) {
      if (contraseña1.charAt(cont) == " ")
        espacios = true;
      cont++;
    }
     
    if (espacios) {
      alert ("La contraseña no puede contener espacios en blanco");
      return false;
    }

    if (contraseña1 != contraseña2) {
        alert("Las Contraseñas deben de coincidir");
        return false;
      } else {
        alert("Todo esta correcto");
        return true; 
    }




}






