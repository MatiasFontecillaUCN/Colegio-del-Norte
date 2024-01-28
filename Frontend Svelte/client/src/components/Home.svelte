<script>
  // @ts-nocheck

  import { CldImage } from "svelte-cloudinary";
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

  let title = localStorage.getItem("title") || "Admisión 2024";
  let info =
    localStorage.getItem("info") ||
    '"Colegio del Norte basa su gestión en procesos educativos de calidad, pertinentes, significativos e integrales que desarrollen en sus entidades, competencias y habilidades que les permitan acceder y aportar, según su vocación. "Colegio del Norte, un colegio para vivirlo"';
  let titleSchool =
    localStorage.getItem("titleSchool") || "Bienvenido a Colegio del Norte";
  let infoSchool =
    localStorage.getItem("infoSchool") ||
    "Nos complace darles la más cordial bienvenida a nuestra comunidad educativa. En Colegio del Norte, creemos en la importancia de brindar una educación de calidad que fomente el aprendizaje, el crecimiento personal y el desarrollo de habilidades para el futuro. Nuestro compromiso con la excelencia académica y el bienestar de nuestros estudiantes es nuestra prioridad. En este colegio, encontrarán un equipo de educadores apasionados y dedicados que están comprometidos en proporcionar una experiencia educativa enriquecedora. En Colegio del Norte, valoramos la diversidad y promovemos un ambiente inclusivo en el que cada estudiante se sienta respetado y valorado. Nuestra misión es ayudar a cada uno de ustedes a alcanzar su máximo potencial, tanto en el ámbito académico como en el desarrollo de habilidades sociales y emocionales.";
  let titleImg = localStorage.getItem("titleImg") || "Colegio 2024";
  let infoImg = localStorage.getItem("infoImg") || "Actividad 1";
  let titleImg1 = localStorage.getItem("titleImg1") || "Curso 8°A";
  let infoImg1 = localStorage.getItem("infoImg1") || "Curso 8°A";
  let titleImg2 = localStorage.getItem("titleImg2") || "Simulacro Septiembre";
  let infoImg2 = localStorage.getItem("infoImg2") || "Alumnos en simulacro";

  let cont = 0;
  let admin = 0;
  let titleError = false;
  let infoError = false;
  let titleSchoolError = false;
  let infoSchoolError = false;
  let titleImgError = false;
  let infoImgError = false;
  let titleImgError1 = false;
  let infoImgError1 = false;
  let titleImgError2 = false;
  let infoImgError2 = false;
  let isOpen = false;

  const image1 = "Home/gpfeadgzkbvpahexjzb7";
  const image2 = "Home/omntzizohxvpewugguqs";

  if (roles == 'admin') {
    admin = 1;
  }
  console.log(admin);

  function handleChangeTitle(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      title = e.target.value;
      titleError = title.trim() === "";
    }
  }
  function handleChangeInfo(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      info = e.target.value;
      infoError = info.trim() === "";
    }
  }
  function handleChangeTitleImg(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      titleImg = e.target.value;
      titleImgError = titleImg.trim() === "";
    }
  }
  function handleChangeInfoImg(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      infoImg = e.target.value;
      infoImgError = infoImg.trim() === "";
    }
  }
  function handleChangeTitleImg1(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      titleImg1 = e.target.value;
      titleImgError1 = titleImg1.trim() === "";
    }
  }
  function handleChangeInfoImg1(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      infoImg1 = e.target.value;
      infoImgError1 = infoImg1.trim() === "";
    }
  }
  function handleChangeTitleImg2(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      titleImg2 = e.target.value;
      titleImgError2 = titleImg2.trim() === "";
    }
  }
  function handleChangeInfoImg2(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      infoImg2 = e.target.value;
      infoImgError2 = infoImg2.trim() === "";
    }
  }
  function handleChangeTitleSchool(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      titleSchool = e.target.value;
      titleSchoolError = titleSchool.trim() === "";
    }
  }
  function handleChangeInfoSchool(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      infoSchool = e.target.value;
      infoSchoolError = infoSchool.trim() === "";
    }
  }
  function editInfo() {
    if (info.trim() === "") {
      infoError = true;
    }
    if (title.trim() === "") {
      titleError = true;
    }
    if (infoImg.trim() === "") {
      infoImgError = true;
    }
    if (titleImg.trim() === "") {
      titleImgError = true;
    }
    if (infoImg1.trim() === "") {
      infoImgError1 = true;
    }
    if (titleImg1.trim() === "") {
      titleImgError1 = true;
    }
    if (infoImg2.trim() === "") {
      infoImgError2 = true;
    }
    if (titleImg2.trim() === "") {
      titleImgError2 = true;
    }
    if (infoSchool.trim() === "") {
      infoSchoolError = true;
    }
    if (titleSchool.trim() === "") {
      titleSchoolError = true;
    }
    cont = 1 - cont;
  }
  function saveInfo() {
    cont = 0;
    localStorage.setItem("info", info);
    localStorage.setItem("title", title);
    localStorage.setItem("infoImg", infoImg);
    localStorage.setItem("titleImg", titleImg);
    localStorage.setItem("infoImg1", infoImg1);
    localStorage.setItem("titleImg1", titleImg1);
    localStorage.setItem("infoImg2", infoImg2);
    localStorage.setItem("titleImg2", titleImg2);
    localStorage.setItem("infoSchool", infoSchool);
    localStorage.setItem("titleSchool", titleSchool);

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
      {#if admin > 0}
        <button class="button-options button-edit" on:click={editInfo}
          >Editar</button
        >
      {/if}
      <div>
        <div class="container-image-info row">
          <div class="col-md-8 col-sm-12" style="margin-bottom:10px">
            <div
              class="carousel slide pointer-event"
              id="carouselExampleCaptions"
              data-bs-ride="carousel"
              data-bs-interval="4000"
            >
              <div class="carousel-indicators">
                <button
                  type="button"
                  data-bs-target="#carouselExampleCaptions"
                  data-bs-slide-to="0"
                  class="active"
                  aria-label="Slide 1"
                  aria-current="true"
                />
                <button
                  type="button"
                  data-bs-target="#carouselExampleCaptions"
                  data-bs-slide-to="1"
                  aria-label="Slide 2"
                />
                <button
                  type="button"
                  data-bs-target="#carouselExampleCaptions"
                  data-bs-slide-to="2"
                  aria-label="Slide 3"
                />
              </div>
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <CldImage src={image1} alt="Imagen 1" class="full-image" />
                  <div class="carousel-caption d-none d-md-block text-below">
                    <h5>{titleImg}</h5>
                    {#if cont > 0}
                      <input
                        class="input-edit w-50"
                        on:input={handleChangeTitleImg}
                        value={titleImg}
                        placeholder="Título"
                      />
                      {#if titleImgError}
                        <div>
                          <p class="message-empty-text">Rellena este campo</p>
                        </div>
                      {/if}
                    {/if}
                    <p>{infoImg}</p>
                    {#if cont > 0}
                      <input
                        class="input-edit w-50"
                        on:input={handleChangeInfoImg}
                        value={infoImg}
                        placeholder="Título"
                      />
                      {#if infoImgError}
                        <div>
                          <p class="message-empty-text">Rellena este campo</p>
                        </div>
                      {/if}
                    {/if}
                  </div>
                </div>
                <div class="carousel-item">
                  <CldImage src={image1} alt="Imagen 1" class="full-image" />
                  <div class="carousel-caption d-none d-md-block text-below">
                    <h5>{titleImg1}</h5>
                    {#if cont > 0}
                      <input
                        class="input-edit w-50"
                        on:input={handleChangeTitleImg1}
                        value={titleImg1}
                        placeholder="Título"
                      />
                      {#if titleImgError1}
                        <div>
                          <p class="message-empty-text">Rellena este campo</p>
                        </div>
                      {/if}
                    {/if}
                    <p>{infoImg1}</p>
                    {#if cont > 0}
                      <input
                        class="input-edit w-50"
                        on:input={handleChangeInfoImg1}
                        value={infoImg1}
                        placeholder="Título"
                      />
                      {#if infoImgError1}
                        <div>
                          <p class="message-empty-text">Rellena este campo</p>
                        </div>
                      {/if}
                    {/if}
                  </div>
                </div>
                <div class="carousel-item">
                  <CldImage src={image1} alt="Imagen 1" class="full-image" />
                  <div class="carousel-caption d-none d-md-block text-below">
                    <h5>{titleImg2}</h5>
                    {#if cont > 0}
                      <input
                        class="input-edit w-50"
                        on:input={handleChangeTitleImg2}
                        value={titleImg2}
                        placeholder="Título"
                      />
                      {#if titleImgError2}
                        <div>
                          <p class="message-empty-text">Rellena este campo</p>
                        </div>
                      {/if}
                    {/if}
                    <p>{infoImg2}</p>
                    {#if cont > 0}
                      <input
                        class="input-edit w-50"
                        on:input={handleChangeInfoImg2}
                        value={infoImg2}
                        placeholder="Título"
                      />
                      {#if infoImgError2}
                        <div>
                          <p class="message-empty-text">Rellena este campo</p>
                        </div>
                      {/if}
                    {/if}
                  </div>
                </div>
              </div>
              <button
                class="carousel-control-prev"
                type="button"
                data-bs-target="#carouselExampleCaptions"
                data-bs-slide="prev"
              >
                <span class="carousel-control-prev-icon" aria-hidden="true" />
                <span class="visually-hidden">Previous</span>
              </button>
              <button
                class="carousel-control-next"
                type="button"
                data-bs-target="#carouselExampleCaptions"
                data-bs-slide="next"
              >
                <span class="carousel-control-next-icon" aria-hidden="true" />
                <span class="visually-hidden">Next</span>
              </button>
            </div>
          </div>
          <div class="col-md-4 col-sm-12" style="margin-bottom:10px">
            <div class="info">
              <div class="info-content">
                <p class="title-info" style="color: black">{title}</p>
                {#if cont > 0}
                  <input
                    class="input-edit"
                    on:input={handleChangeTitle}
                    value={title}
                    placeholder="Título"
                  />
                  {#if titleError}
                    <div>
                      <p class="message-empty-text">Rellena este campo</p>
                    </div>
                  {/if}
                {/if}
                <p class="content-info">{@html info}</p>
                {#if cont > 0}
                  <textarea
                    class="input-edit"
                    on:input={handleChangeInfo}
                    value={info}
                    placeholder="Descripción"
                  />
                  {#if infoError}
                    <div>
                      <p class="message-empty-text">Rellena este campo</p>
                    </div>
                  {/if}
                {/if}
                <div class="image-info">
                  <CldImage src={image2} alt="Imagen Kolegio del Norte" />
                </div>
              </div>
            </div>
          </div>
          <div class="info-school">
            <p class="title-info" style="text-align: start">{titleSchool}</p>
            {#if cont > 0}
              <input
                class="input-edit"
                on:input={handleChangeTitleSchool}
                style="margin-bottom: 15px;"
                value={titleSchool}
                placeholder="Título"
              />
              {#if titleSchoolError}
                <div>
                  <p class="message-empty-text">Rellena este campo</p>
                </div>
              {/if}
            {/if}
            <p class="content-info-school">{@html infoSchool}</p>
            {#if cont > 0}
              <textarea
                class="input-edit"
                on:input={handleChangeInfoSchool}
                value={infoSchool}
                placeholder="Descripción"
              />
              {#if infoSchoolError}
                <div>
                  <p class="message-empty-text">Rellena este campo</p>
                </div>
              {/if}
              <button
                class="button-options button-edit"
                on:click={modal}
                style="margin-left: auto; margin-top: 15px"
                disabled={infoError ||
                  titleError ||
                  infoImgError ||
                  titleImgError ||
                  titleImgError1 ||
                  infoImgError1 ||
                  titleImgError2 ||
                  infoImgError2 ||
                  infoSchoolError ||
                  titleSchoolError}>Guardar</button
              >
            {/if}

            {#if isOpen}
              <div class="modal-overlay">
                <div class="modal-software w-50">
                  <div style="text-align:right">
                    <button class="close-button" on:click={modal}
                      >&times;</button
                    >
                  </div>
                  <div class="container-modal">
                    <h2>¿Estas seguro de guardar los cambios?</h2>
                    <div class="modal-button">
                      <button class="button-confirm" on:click={saveInfo}
                        >Guardar</button
                      >
                      <button
                        class="button-confirm button-cancel"
                        on:click={modal}>Cancelar</button
                      >
                    </div>
                  </div>
                </div>
              </div>
            {/if}
          </div>
        </div>
      </div>
    </div>
  </main>
  <Footer />
</body>
