<script>
  import { Router, Route } from 'svelte-routing';
  import { auth } from './stores/Auth';
  import Home from './components/Home.svelte';
  import AboutUs from './components/AboutUs.svelte';
  import Contact from './components/Contact.svelte';
  import Registration from './components/Registration.svelte';
  import Login from './components/Login.svelte';
  import ViewRequest from './components/temporaryClient/ViewRequest.svelte';
  import ViewStudent from './components/client/ViewStudent.svelte';
  import ViewProfessor from './components/client/ViewProfessor.svelte';
  import ViewRequestAdmin from './components/admin/ViewRequestAdmin.svelte';
  import ViewProfessorAdmin from './components/admin/ViewProfessorAdmin.svelte';
  import { onMount } from 'svelte';
  //import { afterUpdate, setContext } from "svelte";

  const token = sessionStorage.getItem('jwtToken');
  let roles;

  onMount(async() => {
    roles = getTokenByRol(token);
  });
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
  
</script>


<Router>
  <Route path="/" component={Home} />
  <Route path="/about-us" component={AboutUs} />
  <Route path="/contact" component={Contact} />
  <Route path="/registration" component={Registration} />
  <Route path="/login" component={Login} />
  {#if roles && roles.includes('temporal')}
  <Route path="/view-request-client" component={ViewRequest} />
  {/if}
  {#if roles && roles.includes('user')}
  <Route path="/view-request-client" component={ViewRequest} />
  <Route path="/view-student-client" component={ViewStudent} />
  <Route path="/view-professor-client" component={ViewProfessor} />
  {/if}
  {#if roles && roles.includes('admin')}
  <Route path="/view-request-admin" component={ViewRequestAdmin} />
  <Route path="/view-professor-admin" component={ViewProfessorAdmin} />
  {/if}
</Router>
