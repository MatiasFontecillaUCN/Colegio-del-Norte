<script>
  import { auth } from "../stores/Auth";
  import { onMount } from "svelte";
  let roles;
  let rut;
  const token = sessionStorage.getItem('jwtToken');

  onMount(() => {
    roles = getTokenByRol(token);
    rut = getTokenByRut(token);
    console.log(roles);
    console.log(rut)

    /*if (!roles || !roles.includes('user')) {
      navigate('/', { replace: true });
    }*/
  });


  function isLoggedIn() {
    if (token) {
      return true;
    } else {
      return false;
    }
  }
  
  function getTokenByRol(token) {
    if (!token) {
      return null;
    }

    const decodedToken = decodeToken(token);

    if (!decodedToken || !decodedToken.roles) {
      return null;
    }
    return decodedToken.roles;
  }
  function getTokenByRut(token) {
    if (!token) {
      return null;
    }

    const decodedToken = decodeToken(token);

    if (!decodedToken || !decodedToken.roles) {
      return null;
    }
    return decodedToken.sub.replace(/[.-]/g, "");
  }

  function decodeToken(token) {
    if (!token) {
        return null; 
    }
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}

  const handleLogout = () => {
    auth.clearToken();
    isLoggedIn() == false;
    const homeURL = "/";
    window.history.replaceState({}, document.title, homeURL);
    window.location.href = homeURL;
  };

  let isOpen = false
  function modal () {
    isOpen = !isOpen
  }

</script>

<div>
  <div class="div-main container">
    <p class="title-svelte">Colegio del Norte</p>
    <div class="row">
        <a href="/" class="button-options col">Inicio</a>
        <a href="/about-us" class="button-options col">Quienes somos</a>
        <a href="/contact" class="button-options col">Contacto</a>
        <a href="/registration" class="button-options col">Matrícula</a>

        {#if roles && roles.includes('temporal')}
        <a href="/view-request-client" class="button-options col" data-rut={rut}>Mis Matrículas</a>
        {/if}

        {#if roles && roles.includes('admin')}
        <a href="/view-request-admin" class="button-options col">Ver Matrículas</a>
        <a href="/view-professor-admin" class="button-options col">Ver profesores</a>
        {/if}

        {#if roles && roles.includes('user')}
        <a href="/view-request-client" class="button-options col">Mis Matrículas</a>
        <a href="/view-student-client" class="button-options col">Mis alumnos</a>
        <a href="/view-professor-client" class="button-options col">Ver profesores</a>
        {/if}

        <p class="col"></p>
        {#if isLoggedIn() == false}
        <a href="/login" class="button-options col" style="margin-left: auto">Iniciar sesión</a>
        {/if}
        {#if isLoggedIn() == true}
        <button class="button-options col" style="margin-left: auto" on:click={modal} >Cerrar sesión</button>
        {/if}
      </div>
      {#if isOpen}
            <div class='modal-overlay'>
                <div class='modal-software w-50'>
                    <div style='text-align:right'>
                        <button class='close-button' on:click={modal}>&times;</button>
                    </div>
                    <div class='container-modal'>
                        <h2>¿Estas seguro que deseas cerrar sesión?</h2>
                        <div class='modal-button'>
                            <button class='button-confirm' on:click={handleLogout}>Confirmar</button>
                            <button class='button-confirm button-cancel' on:click={modal}>Cancelar</button>
                        </div>
                    </div>
                </div>
            </div>
            {/if}
  </div>
</div>
