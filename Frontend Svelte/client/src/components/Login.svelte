<script>
    import Header from './Header.svelte';
    import Footer from './Footer.svelte';
    //import { user } from '../stores/User';
    import { auth } from '../stores/Auth';

    const username = '';
    let rut = '';
    let password = '';
    const isLoggedIn = false;
    let rutError = true;
    let passwordError = true;
    const isInputEmpty = true;
    let isOpen = false;

    function handleChangeRut(e) {
      if (e.key === ' ') {
        e.preventDefault();
      } else {
        rut = e.target.value;
        rutError = rut.trim() === '';
      }
    }
    function handleChangePassword(e) {
      if (e.key === ' ') {
        e.preventDefault();
      } else {
        password = e.target.value;
        passwordError = password.trim() === '';
      }
    }
   
    function modal() {
      isOpen = !isOpen;
    }
    const login = async (e) => {
      e.preventDefault();
      let rut = e.target.rut.value;
      let password = e.target.password.value;

        if (!rut.trim() || !password.trim()) {
            console.log('Campos vacíos');
            return;
        }
        try {
          const formData = new FormData();
          formData.append('rut', rut);
          formData.append('password', password);

            const response = await fetch(`${import.meta.env.VITE_BASE_API_URL}/login`, {
                method: 'POST',
                body: formData,
                
            });
            //console.log('rut: ', rut, 'contraseña: ', password);
            //console.log(response);

            if (response.ok) {
                const token = await response.text();
                auth.setToken(token);
                const decodedToken = decodeToken(token);
                
                //console.log('Usuario:', decodedToken);
                
                
                const homeURL = '/';
                window.history.replaceState({}, document.title, homeURL);
                window.location.href = homeURL;

            
            } else {
                console.log('Credenciales incorrectas');
            }
        } catch (error) {
            console.error('Error al procesar el formulario:', error);
        }
    }

    // Función para decodificar un token JWT (ejemplo, puedes usar una biblioteca como `jsonwebtoken`)
function decodeToken(token) {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}

</script>

<body>
    <Header />
    {#if isLoggedIn}
        <div>
            <p class="title-info">Bienvenido, {username}</p>
        </div>
    {:else}
        <div>
            <div class="div-main">
                <p class="title-info">Inicio de sesión</p>
                <div class="container-login">
                    <div class="login w-50">
                        <form class="form-login" on:submit={login}>
                            <div class="label-input w-75">
                                <p id="username-required" style="color: red; margin-top:10px">* Campo requerido</p>
                                <label for="username">Rut *</label>
                                <input class="input-login" on:input={handleChangeRut} type="text" id="rut" placeholder="123456789" />
                                {#if rutError}
                                <div>
                                    <p class='message-empty-text'>Rellena este campo</p>
                                </div>
                                {/if}
                            </div>
                            <div class="label-input w-75">
                                <label for="password">Contraseña *</label>
                                <input class="input-login" on:input={handleChangePassword} type="password" id="password" placeholder="*********" />
                                {#if passwordError}
                                <div>
                                    <p class='message-empty-text'>Rellena este campo</p>
                                </div>
                                {/if}
                            </div>
                            <button class="button-confirm" type="submit" disabled={rutError || passwordError}>Iniciar sesión</button>
                        </form>
                    </div>
                </div>
                {#if isOpen}
                <div class='modal-overlay'>
                    <div class='modal-software w-50'>
                        <div style='text-align:right'>
                            <button class='close-button' on:click={modal}>&times;</button>
                        </div>
                        <div class='container-modal'>
                            <h2>El rut y/o la contraseña están incorrectas</h2>
                        </div>
                    </div>
                </div>
                {/if}
            </div>
        </div>
    {/if}
    <Footer />
</body>
