import './app.css';
import App from './App.svelte';
import 'bootstrap-icons/font/bootstrap-icons.css';
import { auth } from './stores/Auth';

//auth.clearToken()

const app = new App({
  target: document.getElementById('app'),
});

export default app;
