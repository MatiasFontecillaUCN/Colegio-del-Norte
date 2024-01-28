<script>
  import { validateRUT } from 'validar-rut';
  import Header from '../Header.svelte';
  import Footer from '../Footer.svelte';

  let professors = [];
  let name = '';
  let lastname = '';
  let rut = '';
  let phone_number = '';
  let email = '';
  let subject = '';
  let isOpen = false;
  let isOpen1 = false;
  let isOpen2 = false;
  let isOpen3 = false;
  let isOpen4 = false;
  let isOpen5 = false;
  let isOpen6 = false;
  let message = '';
  let api = true;
  let rowCount = 0;
  let showButton = false;

  let selectedProfessor = null;

  let nameError1 = true;
  let lastnameError1 = true;
  let isValidRut1 = false;
  let isValidEmail1 = true;
  let phoneError1 = true;
  let subjectError1 = true;

  let rutDelete = '';
  let nameDelete = '';
  let lastnameDelete = '';

  function modal() {
    isOpen = !isOpen;
    name = '';
    lastname = '';
    rut = '';
    phone_number = '';
    email = '';
    subject = '';
    nameError1 = true;
    lastnameError1 = true;
    isValidRut1 = false;
    isValidEmail1 = true;
    phoneError1 = true;
    subjectError1 = true;
  }

  function modal1(rut, name, lastname) {
    isOpen1 = !isOpen1;
    rutDelete = rut;
    nameDelete = name;
    lastnameDelete = lastname;
  }

  async function createProfessor() {
    const data = {
      name,
      lastname,
      rut,
      phone_number,
      email,
      subject,
    };

    const response = await fetch(`${import.meta.env.VITE_BASE_API_URL}/professors`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      const newProfessor = await response.json();
      const createdProfessor = newProfessor.professor;
      if (newProfessor.created) {
        professors = [...professors, createdProfessor];
        isOpen4 = !isOpen4;
        setTimeout(() => {
          isOpen4 = !isOpen4;
        }, 1500);
        modal();
        window.location.reload();
      } else {
        console.log('Error al crear al profesor');
      }
    } else {
      console.log('Error en la solicitud al servidor');
      modal();
      isOpen3 = !isOpen3;
      setTimeout(() => {
        isOpen3 = !isOpen3;
      }, 1500);
    }
  }

     function closeModalEdit() {
       isOpen5 = !isOpen5;
     }

  function modalEdit(rut) {
    selectedProfessor = professors.find((professor) => professor.rut === rut);
    nameError1 = false;
    lastnameError1 = false;
    isValidRut1 = true;
    isValidEmail1 = false;
    phoneError1 = false;
    subjectError1 = false;
    isOpen5 = !isOpen5;
  }

  async function editProfessor(
    name,
    lastname,
    rut,
    phone_number,
    email,
    subject,
  ) {
    console.log(name, lastname, rut, phone_number, email, subject);
    const data = {
      name,
      lastname,
      rut,
      phone_number,
      email,
      subject,
    };
    console.log(data);
    const response = await fetch(`${import.meta.env.VITE_BASE_API_URL}/professors`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    if (response.ok) {
      isOpen5 = !isOpen5;
      isOpen6 = !isOpen6;
      setTimeout(() => {
        isOpen6 = !isOpen6;
      }, 1500);
      window.location.reload();
    } else {
      throw new Error('Error al editar el recurso');
    }
  }

  async function deleteProfessor(rut) {
    isOpen1 = !isOpen1;
    isOpen2 = !isOpen2;
    setTimeout(() => {
      isOpen2 = !isOpen2;
    }, 1500);
    try {
      const response = await fetch(`${import.meta.env.VITE_BASE_API_URL}/professors`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ rut }),
      });

      if (response.ok) {
        const updatedProfessors = await getProffesorsUpdate();
        professors = updatedProfessors;
      } else {
        message = `Error al eliminar al profesor: ${response.statusText}`;
      }
    } catch (error) {
      message = `Error al eliminar al profesor: ${error.message}`;
    }
  }
  async function getProffesorsUpdate() {
    const response = await fetch(`${import.meta.env.VITE_BASE_API_URL}/professors`);
    if (response.ok) {
      return await response.json();
    }
    return [];
  }

  async function fetchProfessors() {
    try {
      const response = await fetch(`${import.meta.env.VITE_BASE_API_URL}/professors`, {
        method: 'GET',
      });

      if (response.ok) {
        professors = await response.json();
        rowCount = professors.length;
        if (rowCount === 5) {
          showButton = true;
        }
        console.log(professors);
        updatePagination();
      } else {
        console.error('Error al cargar datos de profesores desde la API');
      }
    } catch (err) {
      api = false;
      console.error('Error al realizar la solicitud a la API:', err);
    }
  }

  fetchProfessors();

  let name1 = '';
  let lastName1 = '';
  let rut1 = '';
  let email1 = '';
  let phone1 = '';
  let subject1 = '';

  function handleChangeName(e) {
    if (e.key === ' ') {
      e.preventDefault();
    }
    name1 = e.target.value;
    if (name1.length > 2 && !/\d/.test(name1)) {
      nameError1 = false;
    } else {
      nameError1 = true;
    }
  }

  function handleChangeLastname(e) {
    if (e.key === ' ') {
      e.preventDefault();
    }
    lastName1 = e.target.value;
    if (lastName1.length > 2 && !/\d/.test(lastName1)) {
      lastnameError1 = false;
    } else {
      lastnameError1 = true;
    }
  }

  function validateRut(rut) {
    const cleanRUT = String(rut).replace(/[.-]/g, '');

    if (cleanRUT.length < 7 || cleanRUT.length > 12) {
      return false;
    }
    const isValid = validateRUT(cleanRUT);
    return isValid;
  }

  function handleChangeRut(e) {
    rut1 = e.target.value;
    isValidRut1 = validateRut(rut1);
  }

  function handleChangePhone(e) {
    if (e.key === ' ') {
      e.preventDefault();
    }
    const inputText = e.target.value;
    const numericOnly = inputText.replace(/[^0-9]/g, '');
    phone1 = numericOnly;
    if (phone1.length > 8 && !/[a-zA-Z]/.test(inputText)) {
      phoneError1 = false;
    } else {
      phoneError1 = true;
    }
  }

  function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const cleanEmail = email.trim();

    if (
      cleanEmail.length < 4
      || cleanEmail.length > 255
      || !emailRegex.test(cleanEmail)
    ) {
      return true;
    }

    return false;
  }

  function handleChangeEmail(e) {
    if (e.key === ' ') {
      e.preventDefault();
    }

    email1 = e.target.value;
    isValidEmail1 = validateEmail(email1);
  }

  function handleChangeSubject(e) {
    if (e.key === ' ') {
      e.preventDefault();
    }
    subject1 = e.target.value;
    if (subject1.length > 2 && !/\d/.test(subject1)) {
      subjectError1 = false;
    } else {
      subjectError1 = true;
    }
  }

  let currentPage = 1;
  const itemsPerPage = 5;
  let totalPages = 0;

  function updatePagination() {
    const totalItems = professors.length;
    const totalPages = Math.ceil(totalItems / itemsPerPage);
    if (currentPage > totalPages) {
      currentPage = totalPages;
    }
  }

  function showPage(page) {
    currentPage = page;
  }

  function nextPage() {
    totalPages = Math.ceil(professors.length / itemsPerPage);
    if (currentPage < totalPages) {
      currentPage++;
    }
  }

  function previousPage() {
    if (currentPage > 1) {
      currentPage--;
    }
  }
</script>

<body>
  <Header />
  <main>
    <div class="div-main">
      <p class="title-info">Listado de profesores</p>
      {#if !api}
        <h2
          class="title-info"
          style="color: black; font-size: 20px; font-weight: 300"
        >
          No hay Profesores registrados.
        </h2>
      {:else}
        <div class="button-create" style="text-align: end;">
          <button
            on:click={modal}
            type="button"
            class="button-icon col bi bi-plus-lg"
            style="background-color: #18cf5e; margin-bottom: 10px;"
            data-toggle="tooltip"
            data-placement="bottom"
            title="Agregar"
          />
        </div>
        <div class="text-center table-responsive">
          <table class="table table-striped border table-bordered align-middle">
            <thead class="align-middle">
              <tr>
                <th class="col-2">Nombre</th>
                <th class="col-2">Rut</th>
                <th class="col-2">Teléfono</th>
                <th class="col-2">Correo</th>
                <th class="col-2">Asignatura</th>
                <th class="col-2">Acciones</th>
              </tr>
            </thead>
            <tbody>
              {#each professors.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage) as item}
                <tr>
                  <td>{item.name} {item.lastname}</td>
                  <td>{item.rut}</td>
                  <td>+{item.phone_number}</td>
                  <td>{item.email}</td>
                  <td>{item.subject}</td>
                  <td>
                    <div
                      class="button-container display-flex justify-content-center align-items-center;"
                    >
                      <button
                        on:click={() => modalEdit(item.rut)}
                        type="button"
                        class="button-icon col bi bi-pencil-fill"
                        style=" background-color: #FBD24E; margin-right: 10px"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        title="Editar"
                      />
                      <button
                        on:click={() => modal1(item.rut, item.name, item.lastname)}
                        type="button"
                        class="button-icon col bi bi-trash-fill"
                        style="background-color: red;"
                        data-toggle="tooltip"
                        data-placement="bottom"
                        title="Eliminar"
                      />
                    </div>
                  </td>
                </tr>
              {/each}
            </tbody>
          </table>
        </div>
        <div class="pagination-container">
          <nav aria-label="Page navigation example">
            <ul class="pagination justify-content-center">
              <li class="page-item">
                <a
                  class="page-link"
                  href="#"
                  aria-label="Previous"
                  on:click={previousPage}
                >
                  <span aria-hidden="true">&laquo;</span>
                </a>
              </li>
              <li class="page-item">
                <a
                  class="page-link"
                  href="#"
                  aria-label="Next"
                  on:click={nextPage}
                >
                  <span aria-hidden="true">&raquo;</span>
                </a>
              </li>
            </ul>
          </nav>
        </div>
      {/if}
    </div>

    {#if isOpen}
      <div class="modal-overlay">
        <div class="modal-software w-50">
          <div style="text-align:right">
            <button class="close-button" on:click={modal}>&times;</button>
          </div>
          <div class="container-modal">
            <form on:submit|preventDefault={createProfessor}>
              <h3>Agregar profesor</h3>
              <div class="label-input">
                <label for="nameClient" class="form-label">Nombre *</label>
                <input
                  type="text"
                  class="form-control input-edit"
                  on:input={handleChangeName}
                  bind:value={name}
                  placeholder="Nombre"
                  required
                />
                {#if nameError1}
                  <p style="color: red; margin:5px 0 0">
                    El nombre no es válido.
                  </p>
                {:else}
                  <p style="color: green; margin:5px 0 0">
                    El nombre es válido.
                  </p>
                {/if}
              </div>
              <div class="label-input">
                <label for="lastNameClient" class="form-label">Apellido *</label
                >
                <input
                  type="text"
                  class="form-control input-edit"
                  on:input={handleChangeLastname}
                  bind:value={lastname}
                  placeholder="Apellido"
                  required
                />
                {#if lastnameError1}
                  <p style="color: red; margin:5px 0 0">
                    El apellido no es válido.
                  </p>
                {:else}
                  <p style="color: green; margin:5px 0 0">
                    El apellido es válido.
                  </p>
                {/if}
              </div>
              <div class="label-input">
                <label for="rutClient" class="form-label">Rut *</label>
                <input
                  type="text"
                  class="form-control input-edit"
                  on:input={handleChangeRut}
                  bind:value={rut}
                  placeholder="RUT"
                  required
                />
                {#if isValidRut1}
                  <p style="color: green; margin:5px 0 0">El RUT es válido.</p>
                {:else}
                  <p style="color: red; margin:5px 0 0">El RUT no es válido.</p>
                {/if}
              </div>
              <div class="label-input">
                <label for="rutClient" class="form-label">Teléfono *</label>
                <input
                  type="text"
                  class="form-control input-edit"
                  on:input={handleChangePhone}
                  bind:value={phone_number}
                  placeholder="Número de teléfono"
                  required
                />
                {#if phoneError1}
                  <p style="color: red; margin:5px 0 0">
                    El teléfono no es válido.
                  </p>
                {:else}
                  <p style="color: green; margin:5px 0 0">
                    El teléfono es válido.
                  </p>
                {/if}
              </div>
              <div class="label-input">
                <label for="rutClient" class="form-label">Email *</label>
                <input
                  type="text"
                  class="form-control input-edit"
                  on:input={handleChangeEmail}
                  bind:value={email}
                  placeholder="Correo electrónico"
                  required
                />
                {#if isValidEmail1}
                  <p style="color: red; margin:5px 0 0">
                    El email no es válido.
                  </p>
                {:else}
                  <p style="color: green; margin:5px 0 0">
                    El email es válido.
                  </p>
                {/if}
              </div>
              <div class="label-input">
                <label for="rutClient" class="form-label">Materia *</label>
                <input
                  type="text"
                  class="form-control input-edit"
                  on:input={handleChangeSubject}
                  bind:value={subject}
                  placeholder="Materia"
                  required
                />
                {#if subjectError1}
                  <p style="color: red; margin:5px 0 0">
                    La materia no es válido.
                  </p>
                {:else}
                  <p style="color: green; margin:5px 0 0">
                    La materia es válido.
                  </p>
                {/if}
              </div>
              <div class="modal-button">
                <button
                  type="submit"
                  class="button-confirm"
                  disabled={nameError1
                    || lastnameError1
                    || !isValidRut1
                    || isValidEmail1
                    || phoneError1
                    || subjectError1}>Crear</button
                >
                <button class="button-confirm button-cancel" on:click={modal}
                  >Cancelar</button
                >
              </div>
            </form>
          </div>
        </div>
      </div>
    {/if}

    {#if isOpen1}
      <div class="modal-overlay">
        <div class="modal-software w-50">
          <div style="text-align:right">
            <button class="close-button" on:click={modal1}>&times;</button>
          </div>
          <div class="container-modal">
            <h2>
              ¿Estas seguro de eliminar al profesor(a) {nameDelete}
              {lastnameDelete}?
            </h2>
            <div class="modal-button">
              <button
                class="button-confirm"
                on:click={() => deleteProfessor(rutDelete)}>Confirmar</button
              >
              <button class="button-confirm button-cancel" on:click={modal1}
                >Cancelar</button
              >
            </div>
          </div>
        </div>
      </div>
    {/if}

    {#if isOpen2}
      <div class="modal-overlay">
        <div class="modal-software w-50">
          <h5>Profesor eliminado con éxito.</h5>
        </div>
      </div>
    {/if}

    {#if isOpen3}
      <div class="modal-overlay">
        <div class="modal-software w-50">
          <h5>Error al crear el profesor.</h5>
        </div>
      </div>
    {/if}

    {#if isOpen4}
      <div class="modal-overlay">
        <div class="modal-software w-50">
          <h5>Profesor creado con éxito.</h5>
        </div>
      </div>
    {/if}

    {#if isOpen5}
      <div class="modal-overlay">
        <div class="modal-software w-50">
          <div class="container-modal">
            <form
              on:submit|preventDefault={() => editProfessor(
                selectedProfessor.name,
                selectedProfessor.lastname,
                selectedProfessor.rut,
                selectedProfessor.phone_number,
                selectedProfessor.email,
                selectedProfessor.subject,
              )}
            >
              <h3>Editar profesor</h3>

              <div class="label-input">
                <label for="nameClient" class="form-label">Nombre *</label>
                <input
                  type="text"
                  class="form-control input-edit"
                  on:input={handleChangeName}
                  bind:value={selectedProfessor.name}
                  required
                />
                {#if nameError1}
                  <p style="color: red; margin:5px 0 0">
                    El nombre no es válido.
                  </p>
                {:else}
                  <p style="color: green; margin:5px 0 0">
                    El nombre es válido.
                  </p>
                {/if}
              </div>

              <div class="label-input">
                <label for="lastNameClient" class="form-label">Apellido *</label
                >
                <input
                  type="text"
                  class="form-control input-edit"
                  on:input={handleChangeLastname}
                  bind:value={selectedProfessor.lastname}
                  required
                />
                {#if lastnameError1}
                  <p style="color: red; margin:5px 0 0">
                    El apellido no es válido.
                  </p>
                {:else}
                  <p style="color: green; margin:5px 0 0">
                    El apellido es válido.
                  </p>
                {/if}
              </div>
              <div class="label-input">
                <label for="rutClient" class="form-label">Rut *</label>
                <input
                  type="text"
                  class="form-control input-edit"
                  on:input={handleChangeRut}
                  bind:value={selectedProfessor.rut}
                  readonly
                  disabled
                />
                {#if isValidRut1}
                  <p style="color: green; margin:5px 0 0">El RUT es válido.</p>
                {:else}
                  <p style="color: red; margin:5px 0 0">El RUT no es válido.</p>
                {/if}
              </div>
              <div class="label-input">
                <label for="rutClient" class="form-label">Teléfono *</label>
                <input
                  type="text"
                  class="form-control input-edit"
                  on:input={handleChangePhone}
                  bind:value={selectedProfessor.phone_number}
                  required
                />
                {#if phoneError1}
                  <p style="color: red; margin:5px 0 0">
                    El teléfono no es válido.
                  </p>
                {:else}
                  <p style="color: green; margin:5px 0 0">
                    El teléfono es válido.
                  </p>
                {/if}
              </div>
              <div class="label-input">
                <label for="rutClient" class="form-label">Email *</label>
                <input
                  type="text"
                  class="form-control input-edit"
                  on:input={handleChangeEmail}
                  bind:value={selectedProfessor.email}
                  required
                />
                {#if isValidEmail1}
                  <p style="color: red; margin:5px 0 0">
                    El email no es válido.
                  </p>
                {:else}
                  <p style="color: green; margin:5px 0 0">
                    El email es válido.
                  </p>
                {/if}
              </div>
              <div class="label-input">
                <label for="rutClient" class="form-label">Materia *</label>
                <input
                  type="text"
                  class="form-control input-edit"
                  on:input={handleChangeSubject}
                  bind:value={selectedProfessor.subject}
                  required
                />
                {#if subjectError1}
                  <p style="color: red; margin:5px 0 0">
                    La materia no es válido.
                  </p>
                {:else}
                  <p style="color: green; margin:5px 0 0">
                    La materia es válido.
                  </p>
                {/if}
              </div>
              <div class="modal-button">
                <button
                  type="submit"
                  class="button-confirm"
                  disabled={nameError1
                    || lastnameError1
                    || !isValidRut1
                    || isValidEmail1
                    || phoneError1
                    || subjectError1}>Editar</button
                >
                <button
                  class="button-confirm button-cancel"
                  on:click={closeModalEdit}>Cancelar</button
                >
              </div>
            </form>
          </div>
        </div>
      </div>
    {/if}
    {#if isOpen6}
      <div class="modal-overlay">
        <div class="modal-software w-50">
          <h5>Profesor editado con éxito.</h5>
        </div>
      </div>
    {/if}
  </main>
  <Footer />
</body>
