<script>
  import Header from "./Header.svelte";
  import Footer from "./Footer.svelte";

  const token = sessionStorage.getItem("jwtToken");

  let roles = getTokenByRol(token);
  let rut = getTokenByRut(token);
  console.log(roles);
  console.log(rut);

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
    const base64Url = token.split(".")[1];
    const base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split("")
        .map(function (c) {
          return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
        })
        .join("")
    );

    return JSON.parse(jsonPayload);
  }

  let phone = localStorage.getItem("phone") || "+ 569 89131290 o 5 22 89232323";
  let email = localStorage.getItem("email") || "colegiodelnorte@cn.com";
  let address = localStorage.getItem("address") || "Angamos #610";
  let social = localStorage.getItem("social") || "colegiodelnorte";

  let cont = 0;
  let admin = 0;
  let phoneError = false;
  let emailError = false;
  let addressError = false;
  let socialError = false;
  let isOpen = false;

  if (roles == "admin") {
    admin = 1;
  }
  console.log(admin);

  function handleChangePhone(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      phone = e.target.value;
      phoneError = phone.trim() === "";
    }
  }
  function handleChangeEmail(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      email = e.target.value;
      emailError = email.trim() === "";
    }
  }
  function handleChangeAddress(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      address = e.target.value;
      addressError = address.trim() === "";
    }
  }
  function handleChangeSocial(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      social = e.target.value;
      socialError = social.trim() === "";
    }
  }
  function editInfo() {
    if (phone.trim() === "") {
      phoneError = true;
    }
    if (email.trim() === "") {
      emailError = true;
    }
    if (address.trim() === "") {
      addressError = true;
    }
    if (social.trim() === "") {
      socialError = true;
    }
    cont = 1 - cont;
  }
  function saveInfo() {
    cont = 0;
    localStorage.setItem("phone", phone);
    localStorage.setItem("email", email);
    localStorage.setItem("address", address);
    localStorage.setItem("social", social);
    modal();
  }
  function modal() {
    isOpen = !isOpen;
  }
</script>

<body>
  <Header />
  <main>
    <div class="div-main">
      <p class="title-info">Contacto</p>
      {#if admin > 0}
        <button class="button-options button-edit" on:click={editInfo}
          >Editar</button
        >
      {/if}
      <div class="container-contact-iframe">
        <div class="row">
          <div class="col-md-6 col-sm-12">
            <iframe
              id="inlineFrameExample"
              title="Inline Frame Example"
              width="100%"
              height="570"
              src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2583.696153162065!2d-70.40860880756273!3d-23.67960036019689!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x96afd5985772b1d7%3A0xbb63cf320439d951!2sUniversidad%20Cat%C3%B3lica%20del%20Norte!5e0!3m2!1ses!2scl!4v1694753615372!5m2!1ses!2scl"
            />
          </div>
          <div class="col-md-6 col-sm-12">
            <p class="title-info" style="color: white">
              Contáctenos a través de nuestros medios oficiales de comunicación.
            </p>

            <p class="info-contact">Teléfono:</p>
            <p class="content-info-contact">{phone}</p>
            {#if cont > 0}
              <input
                class="input-edit"
                on:input={handleChangePhone}
                value={phone}
                placeholder="Teléfono"
              />
              {#if phoneError}
                <div>
                  <p class="message-empty-text">Rellena este campo</p>
                </div>
              {/if}
            {/if}

            <p class="info-contact">Correo electrónico:</p>
            <p class="content-info-contact">{email}</p>
            {#if cont > 0}
              <input
                class="input-edit"
                on:input={handleChangeEmail}
                value={email}
                placeholder="Correo electrónico"
              />
              {#if emailError}
                <div>
                  <p class="message-empty-text">Rellena este campo</p>
                </div>
              {/if}
            {/if}

            <p class="info-contact">Dirección:</p>
            <p class="content-info-contact">{address}</p>
            {#if cont > 0}
              <input
                class="input-edit"
                on:input={handleChangeAddress}
                value={address}
                placeholder="Dirección"
              />
              {#if addressError}
                <div>
                  <p class="message-empty-text">Rellena este campo</p>
                </div>
              {/if}
            {/if}

            <p class="info-contact">Síganos en nuestras redes sociales:</p>
            <p class="content-info-contact">{social}</p>
            <div class="d-flex content-info-contact" style="height:25px">
              <div class="button-icon bi bi-instagram" style="color: white" />
              <div class="button-icon bi bi-facebook" style="color: white" />
              <div class="button-icon bi bi-linkedin" style="color: white" />
            </div>
            {#if cont > 0}
              <input
                class="input-edit"
                type="email"
                on:input={handleChangeSocial}
                value={social}
                placeholder="Redes sociales"
              />
              {#if socialError}
                <div>
                  <p class="message-empty-text">Rellena este campo</p>
                </div>
              {/if}

              <button
                class="button-options button-edit button-edit-contact"
                on:click={modal}
                style="margin-left: auto; margin-top: 15px"
                disabled={phoneError ||
                  emailError ||
                  addressError ||
                  socialError}>Guardar</button
              >
            {/if}
          </div>
        </div>
      </div>

      {#if isOpen}
        <div class="modal-overlay">
          <div class="modal-software w-50">
            <div style="text-align:right">
              <button class="close-button" on:click={modal}>&times;</button>
            </div>
            <div class="container-modal">
              <h2>¿Estas seguro de guardar los cambios?</h2>
              <div class="modal-button">
                <button class="button-confirm" on:click={saveInfo}
                  >Guardar</button
                >
                <button class="button-confirm button-cancel" on:click={modal}
                  >Cancelar</button
                >
              </div>
            </div>
          </div>
        </div>
      {/if}
    </div>
  </main>
  <Footer />
</body>
