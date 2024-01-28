<script>
    import { validateRUT } from "validar-rut";
    import Header from "./Header.svelte";
    import Footer from "./Footer.svelte";

    const token = sessionStorage.getItem("jwtToken");

    let roles = getTokenByRol(token);
    let rutLog = getTokenByRut(token);
    console.log(roles);
    console.log(rutLog);

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
                    return (
                        "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2)
                    );
                })
                .join("")
        );

        return JSON.parse(jsonPayload);
    }

    let titleSchool = localStorage.getItem("titleRegistration") || "";
    let infoSchool = localStorage.getItem("infoRegistration") || "";

    let cont = 0;
    let admin = 0;
    const next = 0;
    const admiError = false;
    let isInputEmpty = true;

    let titleSchoolError = false;
    let infoSchoolError = false;
    let isOpen = false;

    if (roles == "admin") {
        admin = 1;
    }
    console.log(admin);

    let nameClient = "";
    let lastNameClient = "";
    let rutClient = "";
    let emailClient = "";
    let phoneClient = "";
    let nameError = true;
    let lastnameError = true;
    let fileError = true;
    let phoneError = true;
    let admin1 = false;
    let admin2 = false;
    let nameStudent = "";
    let lastNameStudent = "";
    let rutStudent = "";
    let emailStudent = "";
    let phoneStudent = "";
    let nameStudentError = true;
    let lastnameStudentError = true;
    let fileStudentError = true;
    let phoneStudentError = true;
    let isValidRutClient = false;
    let isValidRutStudent = false;
    let isValidEmailClient = true;
    let isValidEmailStudent = true;

    function handleChangeTitleSchool(e) {
        if (e.key === " ") {
            e.preventDefault();
        } else {
            titleSchool = e.target.value;
            titleSchoolError = titleSchool.trim() === "";
            updateInputEmpty();
        }
    }
    function handleChangeInfoSchool(e) {
        if (e.key === " ") {
            e.preventDefault();
        } else {
            infoSchool = e.target.value;
            infoSchoolError = infoSchool.trim() === "";
            updateInputEmpty();
        }
    }
    function editInfo() {
        if (infoSchool.trim() === "") {
            infoSchoolError = true;
        }
        if (titleSchool.trim() === "") {
            titleSchoolError = true;
        }
        cont = 1 - cont;
        updateInputEmpty();
    }
    function saveInfo() {
        cont = 0;
        localStorage.setItem("titleRegistration", titleSchool);
        localStorage.setItem("infoRegistration", infoSchool);
        updateInputEmpty();
        modal();
    }
    function updateInputEmpty() {
        isInputEmpty = titleSchool.trim() === "" || infoSchool.trim() === "";
    }
    function modal() {
        isOpen = !isOpen;
    }

    function handleChangeNameClient(e) {
        if (e.key === " ") {
            e.preventDefault();
        }
        nameClient = e.target.value;
        if (nameClient.length > 2 && !/\d/.test(nameClient)) {
            nameError = false;
        } else {
            nameError = true;
        }
    }
    function handleChangeLastnameClient(e) {
        if (e.key === " ") {
            e.preventDefault();
        }
        lastNameClient = e.target.value;
        if (lastNameClient.length > 2 && !/\d/.test(lastNameClient)) {
            lastnameError = false;
        } else {
            lastnameError = true;
        }
    }
    function validateRut(rut) {
        const cleanRUT = String(rut).replace(/[.-]/g, "");

        if (cleanRUT.length < 7 || cleanRUT.length > 12) {
            return false;
        }
        const isValid = validateRUT(cleanRUT);
        return isValid;
    }
    function handleChangeRutClient(e) {
        rutClient = e.target.value;
        isValidRutClient = validateRut(rutClient);
    }
    function handleChangeFileClient(e) {
        const file = e.target.files[0];
        fileError = !file;
    }

    function validateEmail(email) {
        const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        const cleanEmail = email.trim();

        if (
            cleanEmail.length < 4 ||
            cleanEmail.length > 255 ||
            !emailRegex.test(cleanEmail)
        ) {
            return true;
        }

        return false;
    }

    function handleChangeEmailClient(e) {
        if (e.key === " ") {
            e.preventDefault();
        }

        emailClient = e.target.value;
        isValidEmailClient = validateEmail(emailClient);
    }

    function handleChangePhoneClient(e) {
        if (e.key === " ") {
            e.preventDefault();
        }
        const inputText = e.target.value;
        const numericOnly = inputText.replace(/[^0-9]/g, "");
        phoneClient = numericOnly;
        if (phoneClient.length > 8 && !/[a-zA-Z]/.test(inputText)) {
            phoneError = false;
        } else {
            phoneError = true;
        }
    }
    function handleChangeNameStudent(e) {
        if (e.key === " ") {
            e.preventDefault();
        }
        nameStudent = e.target.value;
        if (nameStudent.length > 2 && !/\d/.test(nameStudent)) {
            nameStudentError = false;
        } else {
            nameStudentError = true;
        }
    }
    function handleChangeLastnameStudent(e) {
        if (e.key === " ") {
            e.preventDefault();
        }
        lastNameStudent = e.target.value;
        if (lastNameStudent.length > 2 && !/\d/.test(lastNameStudent)) {
            lastnameStudentError = false;
        } else {
            lastnameStudentError = true;
        }
    }
    function handleChangeRutStudent(e) {
        const rutStudent = e.target.value;
        isValidRutStudent = validateRut(rutStudent);
    }

    function handleChangeEmailStudent(e) {
        if (e.key === " ") {
            e.preventDefault();
        }

        emailStudent = e.target.value;
        isValidEmailStudent = validateEmail(emailStudent);
    }

    function handleChangePhoneStudent(e) {
        if (e.key === " ") {
            e.preventDefault();
        }
        const inputText = e.target.value;
        const numericOnly = inputText.replace(/[^0-9]/g, "");
        phoneStudent = numericOnly;
        if (phoneStudent.length > 8 && !/[a-zA-Z]/.test(inputText)) {
            phoneStudentError = false;
        } else {
            phoneStudentError = true;
        }
    }
    function handleChangeFileStudent(e) {
        const file = e.target.files[0];
        fileStudentError = !file;
    }

    let isOpen1 = false;
    function modal1() {
        isOpen1 = !isOpen1;
    }
    function handleRegistration() {
        modal1();
        const homeURL = "/registration";
        window.history.replaceState({}, document.title, homeURL);
        window.location.href = homeURL;
    }

    let selectedCourse = "0";
    let courseError = true;

    function handleCourseSelect(e) {
        selectedCourse = e.target.value;
        console.log(selectedCourse);
        getParallel(selectedCourse);
        if (selectedCourse === "0") {
            courseError = true;
        } else {
            courseError = false;
        }
    }

    let isOpen2 = false;
    let name = "";
    let lastname = "";
    let rut = "";
    let phone_number = "";
    let emailclient = "";
    let data_enrollment = [];

    async function createUser() {
        try {
            const response = await fetch(
                `${
                    import.meta.env.VITE_BASE_API_URL
                }/user/${rutClient}/${name}/{lastname}/{emailClient}/{phoneClient}`,
                {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                    },
                }
            );

            if (response.ok) {
                const responseData = await response.json();
                if (
                    responseData.message == "Datos incorrectos" ||
                    responseData.message == "Existe un usuario con esos datos"
                ) {
                    console.log("ya existe", responseData.message);
                    isOpen2 = !isOpen2;
                    setTimeout(() => {
                        isOpen2 = !isOpen2;
                    }, 1500);
                } else {
                    console.log("no exite", responseData);
                    data_enrollment.push(
                        rutClient.replace(/[.-]/g, ""),
                        name.replace(/^\w/, (c) => c.toUpperCase()),
                        lastname.replace(/^\w/, (c) => c.toUpperCase()),
                        phoneClient,
                        emailClient
                    );
                    console.log(data_enrollment);
                    admin1 = true;
                }
            } else {
                console.error("Error", response.statusText);
            }
        } catch (error) {
            console.error("Error en la solicitud:", error);
        }
    }

    let isOpen3 = false;
    let phoneStudent1 = "";
    let emailStudent1 = "";
    async function createStudent() {
        try {
            const response = await fetch(
                `${import.meta.env.VITE_BASE_API_URL}/student/${rutStudent}`,
                {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                    },
                }
            );

            if (response.ok) {
                const responseData = await response.json();
                if (responseData.exists) {
                    console.log("Existe ese estudiante", responseData.message);
                    isOpen3 = !isOpen3;
                    setTimeout(() => {
                        isOpen3 = !isOpen3;
                    }, 1500);
                } else {
                    console.log("no exite", responseData);
                    (rutStudent = rutStudent),
                        (nameStudent = nameStudent),
                        (lastNameStudent = lastNameStudent),
                        (phoneStudent1 = phoneStudent),
                        (emailStudent1 = emailStudent),
                        data_enrollment.push(
                            rutStudent.replace(/[.-]/g, ""),
                            nameStudent.replace(/^\w/, (c) => c.toUpperCase()),
                            lastNameStudent.replace(/^\w/, (c) =>
                                c.toUpperCase()
                            )
                        );
                    console.log(data_enrollment);
                    admin2 = true;
                }
            } else {
                console.error("Error", response.statusText);
            }
        } catch (error) {
            console.error("Error en la solicitud:", error);
        }
    }

    let parallels = [];
    let course = "";
    let cupos = 0;
    let letter = "";
    async function getParallel(selectedCourse) {
        course = selectedCourse;
        try {
            const response = await fetch(
                `${
                    import.meta.env.VITE_BASE_API_URL
                }/student-year-spots/${course}`,
                {
                    method: "GET",
                }
            );

            if (response.ok) {
                parallels = await response.json();
                cupos = parallels.cupos;
                letter = parallels.parallel;
                console.log(parallels);
            } else {
                console.error(
                    "Error al cargar datos de profesores desde la API"
                );
            }
        } catch (err) {
            console.error("Error al realizar la solicitud a la API:", err);
        }
    }

    async function createEnrollment() {
        data_enrollment.push(
            course,
            letter,
            emailStudent1,
            phoneStudent1,
            "99596562"
        );
        console.log("data_enrollment", data_enrollment);
        const keys = [
            "user_rut",
            "user_name",
            "user_lastname",
            "user_phone_number",
            "user_email",
            "student_rut",
            "student_name",
            "student_lastname",
            "student_school_year",
            "student_parallel",
            "student_email",
            "student_phone_number",
            "administrator_rut",
        ];
        const requestData = data_enrollment.reduce((acc, value, index) => {
            acc[keys[index]] = value;
            return acc;
        }, {});
        console.log("request", requestData);
        try {
            const response = await fetch(
                `${import.meta.env.VITE_BASE_API_URL}/enrollment`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(requestData),
                }
            );

            if (response.ok) {
                const responseData = await response.json();
                console.log(
                    "Matricula creada exitosamente:",
                    responseData.message
                );
                modal1();
            } else {
                console.error(
                    "Error al crear la matricula:",
                    response.statusText
                );
            }
        } catch (error) {
            console.error("Error en la matricula:", error);
        }
    }
</script>

<body>
    <Header />
    <main>
        <div class="div-main">
            <div class="info-school">
                {#if admin > 0}
                    <button
                        class="button-options button-edit"
                        on:click={editInfo}>Editar</button
                    >
                {/if}
                <p class="title-info">{titleSchool}</p>
                {#if cont > 0}
                    <input
                        class="input-edit"
                        style="margin-bottom: 5px;"
                        on:input={handleChangeTitleSchool}
                        value={titleSchool}
                        placeholder="Título"
                    />
                    {#if titleSchoolError}
                        <div>
                            <p style="color: red; margin:5px 0 0">
                                Rellena este campo
                            </p>
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
                            <p style="color: red; margin:5px 0 0">
                                Rellena este campo
                            </p>
                        </div>
                    {/if}
                    <button
                        class="button-options button-edit"
                        on:click={modal}
                        style="margin-left: auto; margin-top: 15px"
                        disabled={isInputEmpty}>Guardar</button
                    >
                {/if}
            </div>

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
                                <button
                                    class="button-confirm"
                                    on:click={saveInfo}>Guardar</button
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

            <div class="admision-school">
                <p class="title-info text-start">
                    Etapa 1: Información del apoderado
                </p>
                <form
                    class="form-registration row"
                    on:submit|preventDefault={createUser}
                >
                    <p id="username-required" style="color: #ec463a">
                        * Campo requerido
                    </p>
                    <div class="label-input col-md-4 col-sm-6">
                        <label for="nameClient" class="form-label"
                            >Nombre *</label
                        >
                        <input
                            type="text"
                            class="form-control input-edit"
                            on:input={handleChangeNameClient}
                            bind:value={name}
                            inputmode="text"
                            pattern="[a-zA-Z]*"
                            id="nameClient"
                            placeholder="Juan"
                        />
                        {#if nameError}
                            <p style="color: red; margin:5px 0 0">
                                El nombre no es válido.
                            </p>
                        {:else}
                            <p style="color: green; margin:5px 0 0">
                                El nombre es válido.
                            </p>
                        {/if}
                    </div>
                    <div class="label-input col-md-4 col-sm-6">
                        <label for="lastNameClient" class="form-label"
                            >Apellido *</label
                        >
                        <input
                            type="text"
                            class="form-control input-edit"
                            on:input={handleChangeLastnameClient}
                            bind:value={lastname}
                            inputmode="text"
                            pattern="[a-zA-Z]*"
                            id="lastNameClient"
                            placeholder="Perez"
                        />
                        {#if lastnameError}
                            <p style="color: red; margin:5px 0 0">
                                El apellido no es válido.
                            </p>
                        {:else}
                            <p style="color: green; margin:5px 0 0">
                                El apellido es válido.
                            </p>
                        {/if}
                    </div>
                    <div class="label-input col-md-4 col-sm-6">
                        <label for="rutClient" class="form-label">Rut *</label>
                        <input
                            type="text"
                            class="form-control input-edit"
                            on:input={handleChangeRutClient}
                            bind:value={rutClient}
                            id="rutClient"
                            placeholder="123456789"
                        />
                        {#if isValidRutClient}
                            <p style="color: green; margin:5px 0 0">
                                El RUT es válido.
                            </p>
                        {:else}
                            <p style="color: red; margin:5px 0 0">
                                El RUT no es válido.
                            </p>
                        {/if}
                    </div>
                    <div class="label-input col-md-4 col-sm-6">
                        <label for="rutClient" class="form-label">Email *</label
                        >
                        <input
                            type="text"
                            class="form-control input-edit"
                            on:input={handleChangeEmailClient}
                            bind:value={emailClient}
                            id="emailClient"
                            placeholder="ejemplo@ejemplo.com"
                        />
                        {#if isValidEmailClient}
                            <p style="color: red; margin:5px 0 0">
                                El email no es válido.
                            </p>
                        {:else}
                            <p style="color: green; margin:5px 0 0">
                                El email es válido.
                            </p>
                        {/if}
                    </div>
                    <div class="label-input col-md-4 col-sm-6">
                        <label for="rutClient" class="form-label"
                            >Teléfono *</label
                        >
                        <input
                            type="text"
                            class="form-control input-edit"
                            on:input={handleChangePhoneClient}
                            bind:value={phoneClient}
                            inputmode="numeric"
                            pattern="[0-9]*"
                            id="telefonoClient"
                            placeholder="569 12345678"
                        />
                        {#if phoneError}
                            <p style="color: red; margin:5px 0 0">
                                El teléfono no es válido.
                            </p>
                        {:else}
                            <p style="color: green; margin:5px 0 0">
                                El teléfono es válido.
                            </p>
                        {/if}
                    </div>
                    <div class="label-input col-md-4 col-sm-6">
                        <label for="file" class="form-label"
                            >Carnet en PDF *</label
                        >
                        <input
                            type="file"
                            class="form-control input-edit"
                            on:change={handleChangeFileClient}
                            id="file"
                            accept=".pdf"
                        />
                        {#if fileError}
                            <p style="color: red; margin:5px 0 0">
                                No ha seleccionado un archivo.
                            </p>
                        {:else}
                            <p style="color: green; margin:5px 0 0">
                                El archivo es válido.
                            </p>
                        {/if}
                    </div>
                    <div>
                        <button
                            class="button-options button-edit"
                            type="submit"
                            id="formClientButton"
                            disabled={nameError ||
                                lastnameError ||
                                !isValidRutClient ||
                                isValidEmailClient ||
                                phoneError ||
                                fileError ||
                                admin1}>Siguiente</button
                        >
                    </div>
                </form>

                {#if admin1}
                    <p class="title-info text-start">
                        Etapa 2: Información del alumno
                    </p>
                    <form
                        class="form-registration row"
                        on:submit|preventDefault={createStudent}
                    >
                        <p id="username-required" style="color: #ec463a">
                            * Campo requerido
                        </p>
                        <div class="label-input col-md-4 col-sm-6">
                            <label for="nameClient" class="form-label"
                                >Nombre *</label
                            >
                            <input
                                type="text"
                                class="form-control input-edit"
                                autofocus
                                on:input={handleChangeNameStudent}
                                bind:value={nameStudent}
                                inputmode="text"
                                pattern="[a-zA-Z]*"
                                id="nameStudent"
                                placeholder="Juan"
                            />
                            {#if nameStudentError}
                                <p style="color: red; margin:5px 0 0">
                                    El nombre no es válido.
                                </p>
                            {:else}
                                <p style="color: green; margin:5px 0 0">
                                    El nombre es válido.
                                </p>
                            {/if}
                        </div>
                        <div class="label-input col-md-4 col-sm-6">
                            <label for="lastNameStudent" class="form-label"
                                >Apellido *</label
                            >
                            <input
                                type="text"
                                class="form-control input-edit"
                                on:input={handleChangeLastnameStudent}
                                bind:value={lastNameStudent}
                                inputmode="text"
                                pattern="[a-zA-Z]*"
                                id="lastNameStudent"
                                placeholder="Perez"
                            />
                            {#if lastnameStudentError}
                                <p style="color: red; margin:5px 0 0">
                                    El apellido no es válido.
                                </p>
                            {:else}
                                <p style="color: green; margin:5px 0 0">
                                    El apellido es válido.
                                </p>
                            {/if}
                        </div>
                        <div class="label-input col-md-4 col-sm-6">
                            <label for="rutStudent" class="form-label"
                                >Rut *</label
                            >
                            <input
                                type="text"
                                class="form-control input-edit"
                                on:input={handleChangeRutStudent}
                                bind:value={rutStudent}
                                id="rutStudent"
                                placeholder="123456789"
                            />
                            {#if isValidRutStudent}
                                <p style="color: green;">El RUT es válido.</p>
                            {:else}
                                <p style="color: red;">El RUT no es válido.</p>
                            {/if}
                        </div>
                        <div class="label-input col-md-4 col-sm-6">
                            <label for="rutClient" class="form-label"
                                >Email *</label
                            >
                            <input
                                type="text"
                                class="form-control input-edit"
                                on:input={handleChangeEmailStudent}
                                bind:value={emailStudent}
                                id="emailClient"
                                placeholder="ejemplo@ejemplo.com"
                            />
                            {#if isValidEmailStudent}
                                <p style="color: red; margin:5px 0 0">
                                    El email no es válido.
                                </p>
                            {:else}
                                <p style="color: green; margin:5px 0 0">
                                    El email es válido.
                                </p>
                            {/if}
                        </div>
                        <div class="label-input col-md-4 col-sm-6">
                            <label for="rutClient" class="form-label"
                                >Teléfono *</label
                            >
                            <input
                                type="text"
                                class="form-control input-edit"
                                on:input={handleChangePhoneStudent}
                                bind:value={phoneStudent}
                                inputmode="numeric"
                                pattern="[0-9]*"
                                id="telefonoClient"
                                placeholder="569 12345678"
                            />
                            {#if phoneStudentError}
                                <p style="color: red; margin:5px 0 0">
                                    El teléfono no es válido.
                                </p>
                            {:else}
                                <p style="color: green; margin:5px 0 0">
                                    El teléfono es válido.
                                </p>
                            {/if}
                        </div>
                        <div class="label-input col-md-4 col-sm-6">
                            <label for="file" class="form-label"
                                >Carnet en PDF *</label
                            >
                            <input
                                type="file"
                                class="form-control input-edit"
                                on:change={handleChangeFileStudent}
                                id="file1"
                                accept=".pdf"
                            />
                            {#if fileStudentError}
                                <p style="color: red; margin:5px 0 0">
                                    No ha seleccionado un archivo.
                                </p>
                            {:else}
                                <p style="color: green; margin:5px 0 0">
                                    El archivo es válido.
                                </p>
                            {/if}
                        </div>
                        <div>
                            <button
                                class="button-options button-edit"
                                type="submit"
                                disabled={nameStudentError ||
                                    lastnameStudentError ||
                                    !isValidRutStudent ||
                                    isValidEmailStudent ||
                                    phoneStudentError ||
                                    fileStudentError ||
                                    admin2}>Siguiente</button
                            >
                        </div>
                    </form>
                {/if}

                {#if admin2}
                    <p class="title-info text-start">
                        Etapa 3: Información del alumno
                    </p>
                    <form
                        class="form-registration row"
                        on:submit|preventDefault={createEnrollment}
                    >
                        <p id="username-required" style="color: #ec463a">
                            * Campo requerido
                        </p>
                        <div class="label-input col-md-4 col-sm-6">
                            <label for="nameClient" class="form-label"
                                >Curso *</label
                            >
                            <select
                                class="form-select input-edit"
                                autofocus
                                aria-label="Default select example"
                                on:change={handleCourseSelect}
                            >
                                <option value="0" selected
                                    >Escoja un curso</option
                                >
                                <option value="1">1° Básico</option>
                                <option value="2">2° Básico</option>
                                <option value="3">3° Básico</option>
                                <option value="4">4° Básico</option>
                                <option value="5">5° Básico</option>
                                <option value="6">6° Básico</option>
                                <option value="7">7° Básico</option>
                                <option value="8">8° Básico</option>
                                <option value="9">I° Medio</option>
                                <option value="10">II° Medio</option>
                                <option value="11">III° Medio</option>
                                <option value="12">IV° Medio</option>
                            </select>
                            {#if courseError}
                                <p style="color: red; margin: 5px 0 0">
                                    No ha seleccionado un curso.
                                </p>
                            {/if}
                        </div>
                        <div class="label-input col-md-4 col-sm-6">
                            <label for="cant" class="form-label"
                                >Cupos disponible</label
                            >
                            <input
                                type="text"
                                class="form-control input-edit"
                                disabled
                                bind:value={cupos}
                                id="cant"
                            />
                        </div>
                        <div class="label-input col-md-4 col-sm-6">
                            <label for="paralelo" class="form-label"
                                >Paralelo</label
                            >
                            <input
                                type="text"
                                class="form-control input-edit"
                                disabled
                                bind:value={letter}
                                id="paralelo"
                            />
                        </div>
                        <div>
                            <button
                                class="button-options button-edit"
                                type="submit"
                                disabled={courseError}>Enviar</button
                            >
                        </div>
                    </form>
                {/if}
            </div>

            {#if isOpen1}
                <div class="modal-overlay">
                    <div class="modal-software w-50">
                        <div style="text-align:right">
                            <button class="close-button" on:click={modal1}
                                >&times;</button
                            >
                        </div>
                        <div class="container-modal">
                            <h2>
                                Al enviar la solicitud, se creará una cuenta
                                temporal en donde podrá revisar el estado de sus
                                solicitudes de matriculas
                            </h2>
                            <h5>
                                * Si todas sus solicitudes son rechazadas, su
                                cuenta temporal se cerrará, en caso contrario,
                                podrá acceder a su cuenta y ver la información
                                de su(s) alumno(s) y profesores.
                            </h5>
                            <h5>
                                * Para iniciar sesión, debe colocar su rut y la
                                contraseña es su mismo rut.
                            </h5>
                            <div class="modal-button">
                                <button
                                    class="button-confirm"
                                    on:click={handleRegistration}>Enviar</button
                                >
                                <button
                                    class="button-confirm button-cancel"
                                    on:click={modal1}>Cancelar</button
                                >
                            </div>
                        </div>
                    </div>
                </div>
            {/if}

            {#if isOpen2}
                <div class="modal-overlay">
                    <div class="modal-software w-50">
                        <h5>Error al ingresar al apoderado.</h5>
                    </div>
                </div>
            {/if}

            {#if isOpen3}
                <div class="modal-overlay">
                    <div class="modal-software w-50">
                        <h5>Error al ingresar al alumno.</h5>
                    </div>
                </div>
            {/if}
        </div>
    </main>
    <Footer />
</body>
