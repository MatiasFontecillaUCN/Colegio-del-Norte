<script>
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

  let mission = localStorage.getItem("mission") || "La misión de nuestro colegio es proporcionar una educación integral y de alta calidad que promueva el desarrollo intelectual, moral, social y emocional de nuestros estudiantes. Nos comprometemos a fomentar la excelencia académica, el respeto a los valores y la diversidad cultural, y a preparar a nuestros alumnos para ser ciudadanos responsables y competentes en un mundo en constante cambio.";
  let vision = localStorage.getItem("vision") || "Nuestra visión es ser reconocidos como un referente en la educación chilena, destacándonos por nuestra excelencia académica y nuestro compromiso con los valores, la inclusión y la innovación educativa. Buscamos formar individuos autónomos, solidarios y creativos, capaces de afrontar los desafíos del siglo XXI. A través de la colaboración con padres, estudiantes y comunidad, aspiramos a crear un ambiente de aprendizaje inspirador que prepare a nuestros alumnos para el éxito académico y personal, contribuyendo al progreso de la sociedad chilena.";
  let academic1 = localStorage.getItem("academic1") || "Mayra Oyanedel";
  let academic2 = localStorage.getItem("academic2") || "Enzo Fernandez";
  let academic3 = localStorage.getItem("academic3") || "Daniela Barrales";
  let academic4 = localStorage.getItem("academic4") || "Karen Gutierrez";
  let position1 = localStorage.getItem("position1") || "Rectora";
  let position2 =
    localStorage.getItem("position2") || "Director Académico enseñanza básica";
  let position3 =
    localStorage.getItem("position3") || "Director Académico enseñanza media";
  let position4 = localStorage.getItem("position4") || "Inspectora general";

  let cont = 0;
  let admin = 0;
  let missionError = false;
  let visionError = false;
  let academic1Error = false;
  let academic2Error = false;
  let academic3Error = false;
  let academic4Error = false;
  let position1Error = false;
  let position2Error = false;
  let position3Error = false;
  let position4Error = false;
  let isOpen = false;

  if (roles == "admin") {
    admin = 1;
  }
  console.log(admin);

  function handleChangeMission(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      mission = e.target.value;
      missionError = mission.trim() === "";
    }
  }
  function handleChangeVision(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      vision = e.target.value;
      visionError = vision.trim() === "";
    }
  }
  function handleChangeAcademic1(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      academic1 = e.target.value;
      academic1Error = academic1.trim() === "";
    }
  }
  function handleChangeAcademic2(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      academic2 = e.target.value;
      academic2Error = academic2.trim() === "";
    }
  }
  function handleChangeAcademic3(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      academic3 = e.target.value;
      academic3Error = academic3.trim() === "";
    }
  }
  function handleChangeAcademic4(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      academic4 = e.target.value;
      academic4Error = academic4.trim() === "";
    }
  }
  function handleChangePosition1(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      position1 = e.target.value;
      position1Error = position1.trim() === "";
    }
  }
  function handleChangePosition2(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      position2 = e.target.value;
      position2Error = position2.trim() === "";
    }
  }
  function handleChangePosition3(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      position3 = e.target.value;
      position3Error = position3.trim() === "";
    }
  }
  function handleChangePosition4(e) {
    if (e.key === " ") {
      e.preventDefault();
    } else {
      position4 = e.target.value;
      position4Error = position4.trim() === "";
    }
  }
  function editInfo() {
    if (mission.trim() === "") {
      missionError = true;
    }
    if (vision.trim() === "") {
      visionError = true;
    }
    if (academic1.trim() === "") {
      academic1Error = true;
    }
    if (academic2.trim() === "") {
      academic2Error = true;
    }
    if (academic3.trim() === "") {
      academic3Error = true;
    }
    if (academic4.trim() === "") {
      academic4Error = true;
    }
    if (position1.trim() === "") {
      academic1Error = true;
    }
    if (position2.trim() === "") {
      academic2Error = true;
    }
    if (position3.trim() === "") {
      academic3Error = true;
    }
    if (position4.trim() === "") {
      academic4Error = true;
    }
    cont = 1 - cont;
  }
  function saveInfo() {
    cont = 0;
    localStorage.setItem("mission", mission);
    localStorage.setItem("vision", vision);
    localStorage.setItem("academic1", academic1);
    localStorage.setItem("academic2", academic2);
    localStorage.setItem("academic3", academic3);
    localStorage.setItem("academic4", academic4);
    localStorage.setItem("position1", position1);
    localStorage.setItem("position2", position2);
    localStorage.setItem("position3", position3);
    localStorage.setItem("position4", position4);
    closeModal();
  }
  function openModal() {
    isOpen = true;
  }
  function closeModal() {
    isOpen = false;
  }
</script>

<body>
  <Header />
  <main>
    <div class="div-main">
      <p class="title-info">Quienes somos</p>
      {#if admin > 0}
        <button class="button-options button-edit" on:click={editInfo}
          >Editar</button
        >
      {/if}
      <div>
        <div class="info-school">
          <p class="title-info" style="text-align: start">Misión</p>
          <p class="content-info-aboutus">{mission}</p>
          {#if cont > 0}
            <textarea
              class="input-edit"
              on:input={handleChangeMission}
              value={mission}
              placeholder="Misión"
            />
            {#if missionError}
              <div>
                <p class="message-empty-text">Rellena este campo</p>
              </div>
            {/if}
          {/if}

          <p class="title-info" style="text-align: start">Visión</p>
          <p class="content-info-aboutus">{vision}</p>
          {#if cont > 0}
            <textarea
              class="input-edit"
              on:input={handleChangeVision}
              value={vision}
              placeholder="Visión"
            />
            {#if visionError}
              <div>
                <p class="message-empty-text">Rellena este campo</p>
              </div>
            {/if}
          {/if}
          <div class="container">
            <p class="title-info" style="margin-bottom: 10px;">Académicos</p>
            <div class="image-container row">
              <div class="image-description col-md-3 col-sm-6">
                <CldImage
                  width={284}
                  height={362}
                  src="Teachers/vdxm042vpjs8ffsrmriz"
                  alt="Rectora"
                />
                <h4 style="padding-top:10px">{academic1}</h4>
                {#if cont > 0}
                  <input
                    class="input-edit"
                    on:input={handleChangeAcademic1}
                    value={academic1}
                    placeholder="Académico 1"
                  />
                  {#if academic1Error}
                    <div>
                      <p class="message-empty-text">Rellena este campo</p>
                    </div>
                  {/if}
                {/if}
                <p>{position1}</p>
                {#if cont > 0}
                  <input
                    class="input-edit mb-4"
                    on:input={handleChangePosition1}
                    value={position1}
                    placeholder="Académico 1"
                  />
                  {#if position1Error}
                    <div>
                      <p class="message-empty-text">Rellena este campo</p>
                    </div>
                  {/if}
                {/if}
              </div>
              <div class="image-description col-md-3 col-sm-6">
                <CldImage
                  width={284}
                  height={362}
                  src="Teachers/a8ipvqlidaa9jfztna8l"
                  alt="Director Académico enseñanza básica"
                />
                <h4 style="padding-top:10px">{academic2}</h4>
                {#if cont > 0}
                  <input
                    class="input-edit"
                    on:input={handleChangeAcademic2}
                    value={academic2}
                    placeholder="Académico 2"
                  />
                  {#if academic2Error}
                    <div>
                      <p class="message-empty-text">Rellena este campo</p>
                    </div>
                  {/if}
                {/if}
                <p>{position2}</p>
                {#if cont > 0}
                  <input
                    class="input-edit mb-4"
                    on:input={handleChangePosition2}
                    value={position2}
                    placeholder="Académico 2"
                  />
                  {#if position2Error}
                    <div>
                      <p class="message-empty-text">Rellena este campo</p>
                    </div>
                  {/if}
                {/if}
              </div>
              <div class="image-description col-md-3 col-sm-6">
                <CldImage
                  width={284}
                  height={362}
                  src="Teachers/jn2ib4ksbzskfp3l6o0l"
                  alt="Director Académico enseñanza media"
                />
                <h4 style="padding-top:10px">{academic3}</h4>
                {#if cont > 0}
                  <input
                    class="input-edit"
                    on:input={handleChangeAcademic3}
                    value={academic3}
                    placeholder="Académico 3"
                  />
                  {#if academic3Error}
                    <div>
                      <p class="message-empty-text">Rellena este campo</p>
                    </div>
                  {/if}
                {/if}
                <p>{position3}</p>
                {#if cont > 0}
                  <input
                    class="input-edit mb-4"
                    on:input={handleChangePosition3}
                    value={position3}
                    placeholder="Académico 3"
                  />
                  {#if position3Error}
                    <div>
                      <p class="message-empty-text">Rellena este campo</p>
                    </div>
                  {/if}
                {/if}
              </div>
              <div class="image-description col-md-3 col-sm-6">
                <CldImage
                  width={284}
                  height={362}
                  src="Teachers/w0fu765wgnzvjjtjhfh5"
                  alt="Inspectora general"
                />
                <h4 style="padding-top:10px">{academic4}</h4>
                {#if cont > 0}
                  <input
                    class="input-edit"
                    on:input={handleChangeAcademic4}
                    value={academic4}
                    placeholder="Académico 4"
                  />
                  {#if academic4Error}
                    <div>
                      <p class="message-empty-text">Rellena este campo</p>
                    </div>
                  {/if}
                {/if}
                <p>{position4}</p>
                {#if cont > 0}
                  <input
                    class="input-edit mb-4"
                    on:input={handleChangePosition4}
                    value={position4}
                    placeholder="Académico 4"
                  />
                  {#if position4Error}
                    <div>
                      <p class="message-empty-text">Rellena este campo</p>
                    </div>
                  {/if}
                {/if}
              </div>
            </div>
          </div>
          {#if cont > 0}
            <button
              class="button-options button-edit"
              on:click={openModal}
              style="margin-left: auto; margin-top: 10px; margin-bottom: 50px"
              disabled={missionError ||
                visionError ||
                academic1Error ||
                academic2Error ||
                academic3Error ||
                academic4Error ||
                position1Error ||
                position2Error ||
                position3Error ||
                position4Error}>Guardar</button
            >
          {/if}
        </div>
      </div>
      {#if isOpen}
        <div class="modal-overlay">
          <div class="modal-software w-50">
            <div style="text-align:right">
              <button class="close-button" on:click={closeModal}>&times;</button
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
                  on:click={closeModal}>Cancelar</button
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
